# --------------------------------------------------------------------------- #
# OpenSim: addAnkleSpring.py                                                  #
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
ankleSpringModel = baseModel.clone()
ankleSpringModel.setName(baseModel.getName()+'_ankle_spring')

# Create the spring we'll add to the model (a CoordinateLimitForce in OpenSim)
ankleSpring = modeling.CoordinateLimitForce()

# Set the coordinate for the spring
ankleSpring.set_coordinate('ankle_angle_r')
ankleSpring.setName('AnkleLimitSpringDamper')

# Add the spring to the model
ankleSpringModel.addForce(ankleSpring)

# Load the model in the GUI
loadModel(ankleSpringModel)

# Set the spring's properties
ankleSpring.setUpperStiffness(10.0)
ankleSpring.setUpperLimit(5.0)
ankleSpring.setLowerStiffness(1.0)
ankleSpring.setLowerLimit(-90.0)
ankleSpring.setDamping(0.01)
ankleSpring.setTransition(2.0)

# Save the model to file
fullPathName = baseModel.getInputFileName()
newName = fullPathName.replace('.osim', '_spring.osim')
ankleSpringModel.print(newName)