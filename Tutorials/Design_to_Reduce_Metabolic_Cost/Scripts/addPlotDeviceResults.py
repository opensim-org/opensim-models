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
# Plot the device results for comparison (muscle Rates and metabolic cost)
# Note: plotBaselineResults must be run first.
# Script assumes the prefix walk_subject for the CMC results

# Utils contains tools to browse for files and folders
import org.opensim.utils as utils
import os

# Obtain Directory containing device results
#resultsFolderCMC = getInstallDir() + "/Models/gait10dof18musc/CMC/ResultsCMC"
resultsFolderCMC = utils.FileUtils.getInstance().browseForFolder("Select the folder with device CMC Results",1);

# Obtain the legend name
#legendName = "Device"
legendName = os.path.split(resultsFolderCMC)[1]

# Plot the total metabolic energy
src = addDataSource(totalEnergyPlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(totalEnergyPlot, src, "time", "metabolics_TOTAL")
crv.setLegend(legendName)

# Plot the gastrocnemius muscle Rates
src = addDataSource(GastrocRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(GastrocRatePlot, src, "time", "metabolics_gastroc_r")
crv.setLegend(legendName)

# Plot the soleus muscle Rates
src = addDataSource(SoleusRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(SoleusRatePlot, src, "time", "metabolics_soleus_r")
crv.setLegend(legendName)

# Plot the tibialis anterior muscle Rates
src = addDataSource(TibAntRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(TibAntRatePlot, src, "time", "metabolics_tib_ant_r")
crv.setLegend(legendName)

# Plot the iliopsoas metabolic rate
src = addDataSource(psoasRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(psoasRatePlot, src, "time", "metabolics_iliopsoas_r")
crv.setLegend(legendName)
