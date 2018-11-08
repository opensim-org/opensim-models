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
# Import needed packages

# Utils contains tools to browse for files and folders
import org.opensim.utils as utils

# Obtain Directory containing CMC results
#resultsFolderCMC = getInstallDir() + "/Models/gait10dof18musc/CMC/ResultsCMC"
resultsFolderCMC = utils.FileUtils.getInstance().browseForFolder("Select the folder with CMC Results",1);

####################################
# Plot kinematics errors
# Create Plotter panel
pErrPlot = createPlotterPanel("Kinematics Tracking Errors for CMC")

# Load and plot kinematics data from CMC
src = addDataSource(pErrPlot, resultsFolderCMC+"/walk_subject_pErr.sto")
addCurve(pErrPlot, src, "time", "pelvis_tilt")
addCurve(pErrPlot, src, "time", "hip_flexion_r")
addCurve(pErrPlot, src, "time", "knee_angle_r")
addCurve(pErrPlot, src, "time", "ankle_angle_r")

thresholdErrorGood =  modeling.Constant(0.0349)
thresholdErrorGood.setName('GOOD')
addFunctionCurve(pErrPlot, thresholdErrorGood)
setCurveColor(pErrPlot, 4, 0.0, 1.0, 0.0)

thresholdErrorGoodNeg =  modeling.Constant(-0.0349)
thresholdErrorGoodNeg.setName('GOOD')
addFunctionCurve(pErrPlot, thresholdErrorGoodNeg)
setCurveColor(pErrPlot, 5, 0.0, 1.0, 0.0)

thresholdErrorOK =  modeling.Constant(0.0873)
thresholdErrorOK.setName('OK')
addFunctionCurve(pErrPlot, thresholdErrorOK)
setCurveColor(pErrPlot, 6, 1.0, 0.6, 0.4)

thresholdErrorOKNeg =  modeling.Constant(-0.0873)
thresholdErrorOKNeg.setName('OK')
addFunctionCurve(pErrPlot, thresholdErrorOKNeg)
setCurveColor(pErrPlot, 7, 1.0, 0.6, 0.4)

##############################
# Plot the residual forces and moments
residualForcePlot = createPlotterPanel("Residual Forces and Moments")
src = addDataSource(residualForcePlot, resultsFolderCMC+"/walk_subject_Actuation_force.sto")

# Add data to plots, label plots in legend
addCurve(residualForcePlot, src, "time", "FX")
addCurve(residualForcePlot, src, "time", "FY")
addCurve(residualForcePlot, src, "time", "MZ")

# Plot threshold values
thresholdResidualForceGood =  modeling.Constant(10)
thresholdResidualForceGood.setName('GOOD')
addFunctionCurve(residualForcePlot, thresholdResidualForceGood)
setCurveColor(residualForcePlot, 3, 0.0, 1.0, 0.0)

thresholdResidualForceGoodNeg =  modeling.Constant(-10)
thresholdResidualForceGoodNeg.setName('GOOD')
addFunctionCurve(residualForcePlot, thresholdResidualForceGoodNeg)
setCurveColor(residualForcePlot, 4, 0.0, 1.0, 0.0)

thresholdResidualForceOK =  modeling.Constant(25)
thresholdResidualForceOK.setName('OK')
addFunctionCurve(residualForcePlot, thresholdResidualForceOK)
setCurveColor(residualForcePlot, 5, 1.0, 0.6, 0.4)

thresholdResidualForceOKNeg =  modeling.Constant(-25)
thresholdResidualForceOKNeg.setName('OK')
addFunctionCurve(residualForcePlot, thresholdResidualForceOKNeg)
setCurveColor(residualForcePlot, 6, 1.0, 0.6, 0.4)

##############################
# Plot the reserve actuator forces
reserveForcePlot = createPlotterPanel("Reserve Actuators")
src = addDataSource(reserveForcePlot, resultsFolderCMC+"/walk_subject_Actuation_force.sto")

# Add data to plots, label plots in legend
addCurve(reserveForcePlot, src, "time", "hip_flexion_r_reserve")
addCurve(reserveForcePlot, src, "time", "knee_angle_r_reserve")
addCurve(reserveForcePlot, src, "time", "ankle_angle_r_reserve")
addCurve(reserveForcePlot, src, "time", "lumbar_extension_reserve")

# Plot threshold values
thresholdReserveForceGood =  modeling.Constant(25)
thresholdReserveForceGood.setName('GOOD')
addFunctionCurve(reserveForcePlot, thresholdReserveForceGood)
setCurveColor(reserveForcePlot, 4, 0.0, 1.0, 0.0)

thresholdReserveForceGoodNeg =  modeling.Constant(-25)
thresholdReserveForceGoodNeg.setName('GOOD')
addFunctionCurve(reserveForcePlot, thresholdReserveForceGoodNeg)
setCurveColor(reserveForcePlot, 5, 0.0, 1.0, 0.0)
