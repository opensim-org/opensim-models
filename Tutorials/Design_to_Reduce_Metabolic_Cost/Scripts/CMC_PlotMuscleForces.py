# --------------------------------------------------------------------------- #
# OpenSim: CMC_EvaluateResults.py                                             #
# --------------------------------------------------------------------------- #
# OpenSim is a toolkit for musculoskeletal modeling and simulation,           #
# developed as an open source project by a worldwide community. Development   #
# and support is coordinated from Stanford University, with funding from the  #
# U.S. NIH and DARPA. See http://opensim.stanford.edu and the README file     #
# for more information including specific grant numbers.                      #
#                                                                             #
# Copyright (c) 2005-2017 Stanford University and the Authors                 #
# Author(s): Ayman Habib                                                      #
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
# --------------------------------------------------------------------------- #
# OpenSim: addPlotDeviceResults.py                                            #
# --------------------------------------------------------------------------- #
# OpenSim is a toolkit for musculoskeletal modeling and simulation,           #
# developed as an open source project by a worldwide community. Development   #
# and support is coordinated from Stanford University, with funding from the  #
# U.S. NIH and DARPA. See http://opensim.stanford.edu and the README file     #
# for more information including specific grant numbers.                      #
#                                                                             #
# Copyright (c) 2005-2017 Stanford University and the Authors                 #
# Author(s): Ayman Habib                                                      #
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
# Plot the Muscle forces from a CMC simulation

# Utils contains tools to browse for files and folders
import org.opensim.utils as utils
import os

# Obtain Directory containing CMC.
resultsFolderCMC = utils.FileUtils.getInstance().browseForFolder("Select the folder with CMC Results",1);

## Plot Muscle Forces
# Create Plotter panel
ForcePlot = createPlotterPanel("Muscle Force Results from CMC Simulation")
# Load and plot kinematics data from CMC results
src = addDataSource(ForcePlot, resultsFolderCMC+"/Subject01_Actuation_force.sto")
addCurve(ForcePlot, src, "time", "gastroc_r")
addCurve(ForcePlot, src, "time", "soleus_r")
addCurve(ForcePlot, src, "time", "tib_ant_r")
addCurve(ForcePlot, src, "time", "iliopsoas_r")
