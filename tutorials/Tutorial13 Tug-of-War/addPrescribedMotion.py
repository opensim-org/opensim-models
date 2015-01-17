# ----------------------------------------------------------------------- #
# The OpenSim API is a toolkit for musculoskeletal modeling and           #
# simulation. See http://opensim.stanford.edu and the NOTICE file         #
# for more information. OpenSim is developed at Stanford University       #
# and supported by the US National Institutes of Health (U54 GM072970,    #
# R24 HD065690) and by DARPA through the Warrior Web program.             #
#                                                                         #
# Copyright (c) 2005-2012 Stanford University and the Authors             #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License");         #
# you may not use this file except in compliance with the License.        #
# You may obtain a copy of the License at                                 #
# http://www.apache.org/licenses/LICENSE-2.0.                             #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or         #
# implied. See the License for the specific language governing            #
# permissions and limitations under the License.                          #
# ----------------------------------------------------------------------- #
#
# Author: Thomas Uchida
# Stanford University
#
# This script is used in the Tug_of_War example to prescribe a motion for the
# block as a function of time.

# Get handle to current model in GUI.
oldModel = getCurrentModel()
if not oldModel:
    print "ERROR: Need to load a model first!\n"

# Create a fresh copy.
newModel = modeling.Model(oldModel)

# Initialize the copy. If values needed to be set in the state, pass along the
# variable 'newState' returned by initSystem.
newState = newModel.initSystem()

# Name the copy for later display in the GUI.
oldName = oldModel.getName()
newModel.setName(oldName + "_prescribedMotion")

# Create PrescribedFunction.
slope = -0.1
yintercept = 0.05
myFunction = modeling.LinearFunction(slope, yintercept)

# Assign PrescribedFunction to specify the motion of the block.
prismaticJoint = newModel.getJointSet().get('ground_block').getCoordinateSet().get(0)
prismaticJoint.set_prescribed_function(myFunction)
prismaticJoint.set_prescribed(True)

# Save new model.
oldPathName = oldModel.getInputFileName()
newPathName = oldPathName.replace('.osim', '_prescribedMotion.osim')
newModel.print(newPathName)

# Add model to GUI.
loadModel(newPathName)
