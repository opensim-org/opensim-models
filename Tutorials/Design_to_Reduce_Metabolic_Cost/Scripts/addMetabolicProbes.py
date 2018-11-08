# --------------------------------------------------------------------------- #
# OpenSim: addMetabolicProbes.py                                              #
# --------------------------------------------------------------------------- #
# OpenSim is a toolkit for musculoskeletal modeling and simulation,           #
# developed as an open source project by a worldwide community. Development   #
# and support is coordinated from Stanford University, with funding from the  #
# U.S. NIH and DARPA. See http://opensim.stanford.edu and the README file     #
# for more information including specific grant numbers.                      #
#                                                                             #
# Copyright (c) 2005-2017 Stanford University and the Authors                 #
# Author(s): Ayman Habib, Thomas Uchida, Christopher Dembia                   #
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License"); you may     #
# not use this file except in compliance with the License. You may obtain a   #
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0           #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
# --------------------------------------------------------------------------- #

#
# Authors: Christopher Dembia, Thomas Uchida
# Stanford University
#
# This script adds metabolic probes (MuscleMetabolicPowerProbeUmberger2010)
# to the current model loaded in the GUI. The new model is loaded into the
# GUI and saved to a file. The ratio of slow- to fast-twitch fibers in each
# muscle are obtained from a text file; all other probe parameters are
# defined below.


# Get a handle to the current model loaded in the GUI.
oldModel = getCurrentModel()

# Create a fresh copy. Initialize and name the copy.
myModel = modeling.Model(oldModel)
myState = myModel.initSystem()
myModel.setName(oldModel.getName()+"_probed")

# Open the data file containing slow-twitch ratios for common muscles. The
# file must be formatted as follows:
#   - space-delimited
#   - first column is the muscle name (excluding suffixes that distinguish
#     between muscles on the left and right sides of the model)
#   - second column is either the slow-twitch ratio (in the range [0,1]) or
#     "-1" if the slow-twitch ratio is unknown for that muscle
import org.opensim.utils as utils
fn = utils.FileUtils.getInstance().browseForFilename(".txt",
    "Please select the file containing the slow-twitch fiber ratios", True)
f = open(fn, "r")

twitchRatios = dict()
for line in f:
    # The file is space-delimited.
    row = line.split(" ")
    
    # Ensure there are exactly two columns in each row.
    if len(row) != 2:
        raise Exception("There must be 2 columns in each row of the file.")
    
    muscleName = row[0]
    twitchRatio = float(row[1])
    
    # Place this row into the "twitchRatios" map.
    twitchRatios[muscleName] = twitchRatio


# The following booleans are constructor arguments for the Umberger probe.
# These settings are used for all probes.
activationMaintenanceRateOn = True
shorteningRateOn = True
basalRateOn = False
mechanicalWorkRateOn = True
reportTotalMetabolicsOnly = False

# The mass of each muscle will be calculated using data from the model:
# muscleMass = (maxIsometricForce / sigma) * rho * optimalFiberLength
# where sigma = 0.25e6 is the specific tension of mammalian muscle (in
# Pascals) and rho = 1059.7 is the density of mammalian muscle (in kg/m^3).

# The slow-twitch ratio used for muscles that either do not appear in the
# file, or appear but whose proportion of slow-twitch fibers is unknown.
defaultTwitchRatio = 0.5


# Define a whole-body probe that will report the total metabolic energy
# consumption over the simulation.
wholeBodyProbe = modeling.Umberger2010MuscleMetabolicsProbe(
    activationMaintenanceRateOn,
    shorteningRateOn,
    basalRateOn,
    mechanicalWorkRateOn,)
wholeBodyProbe.setOperation("value")
wholeBodyProbe.set_report_total_metabolics_only(reportTotalMetabolicsOnly)

# Add the probe to the model and provide a name.
myModel.addProbe(wholeBodyProbe)
wholeBodyProbe.setName("metabolics")

# Loop through all muscles, adding parameters for each into the whole-body
# probe.
for iMuscle in range(myModel.getMuscles().getSize()):
    thisMuscle = myModel.getMuscles().get(iMuscle)
    
    # Get the slow-twitch ratio from the data we read earlier. Start with
    # the default value.
    slowTwitchRatio = defaultTwitchRatio
    
    # Set the slow-twitch ratio to the physiological value, if it is known.
    for key, val in twitchRatios.items():
        if thisMuscle.getName().startswith(key) and val != -1:
            slowTwitchRatio = val
    
    # Add this muscle to the whole-body probe. The arguments are muscle
    # name, slow-twitch ratio, and muscle mass. Note that the muscle mass
    # is ignored unless we set useProvidedMass to True.
    wholeBodyProbe.addMuscle(thisMuscle.getName(),
                             slowTwitchRatio)

# Save the new model to a file with the suffix "_probed".
oldPathName = oldModel.getInputFileName()
newPathName = oldPathName.replace('.osim', '_probed.osim')
myModel.print(newPathName)

# Add the new model to the GUI.
loadModel(newPathName)

# Display the file name of the new model.
win = swing.JFrame("Complete")
dLabel = swing.JLabel("The probed model has been written to "+newPathName)
win.getContentPane().add(dLabel)
win.pack()
win.show()
win.setSize(1000,100)
