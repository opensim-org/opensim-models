# --------------------------------------------------------------------------- #
# OpenSim: addpathActuator.py                                                  #
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
# Get a handle to the current model and create a new copy
baseModel = getCurrentModel()
pathActuatorModel = baseModel.clone()
pathActuatorModel.setName(baseModel.getName()+'_PathActuator')

# Create the PathActuator
pathActuator = modeling.PathActuator()
pathActuator.setName('PlantarFlexAssist')

# Add the path points of the PathActuator
pathActuator.addNewPathPoint ('pfa_r-P1',pathActuatorModel.getBodySet().get('tibia_r'), modeling.Vec3(-0.004,-0.1, 0.01))
pathActuator.addNewPathPoint ('pfa_r-P1',pathActuatorModel.getBodySet().get('calcn_r'), modeling.Vec3(0,0.0318395,-0.00544352))

# Set the PathActuator's properties
pathActuator.setOptimalForce(10)

# Add the PathActuator to the model
pathActuatorModel.addForce(pathActuator)

# Load the model in the GUI
s = pathActuatorModel.initSystem()
loadModel(pathActuatorModel)

# Save the model to file
fullPathName = baseModel.getInputFileName()
newName = fullPathName.replace('.osim', '_PathActuator.osim')
pathActuatorModel.print(newName)
