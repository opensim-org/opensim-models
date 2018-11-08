# --------------------------------------------------------------------------- #
# OpenSim: addPathSpring.py                                                   #
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
pathSpringModel = baseModel.clone()
pathSpringModel.setName(baseModel.getName()+'_path_spring')

# Create the spring we'll add to the model (a PathSpring in OpenSim)
name = 'BiarticularSpringDamper'
restLength = 0.4
stiffness = 10000.0
dissipation = 0.01
pathSpring = modeling.PathSpring(name,restLength,stiffness,dissipation)

# Set geometry path for the path spring to match the gastrocnemius muscle
gastroc = pathSpringModel.getMuscles().get('gastroc_r')
pathSpring.set_GeometryPath(gastroc.getGeometryPath())

# Add the spring to the model
pathSpringModel.addForce(pathSpring)

# Load the model in the GUI
loadModel(pathSpringModel)

# Save the model to file
fullPathName = baseModel.getInputFileName()
newName = fullPathName.replace('.osim', '_path_spring.osim')
pathSpringModel.print(newName)