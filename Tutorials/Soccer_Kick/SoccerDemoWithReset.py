# ----------------------------------------------------------------------- #
# The OpenSim API is a toolkit for musculoskeletal modeling and           #
# simulation. See http://opensim.stanford.edu and the NOTICE file         #
# for more information. OpenSim is developed at Stanford University       #
# and supported by the US National Institutes of Health (U54 GM072970,    #
# R24 HD065690) and by DARPA through the Warrior Web program.             #
#                                                                         #
# Copyright (c) 2005-2019 Stanford University and the Authors             #
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
# Author(s): Ayman Habib, James Dunne, Jen Hicks
# Stanford University
#
# Create and open a custom window

import java.util.ArrayList as ArrayList
import javax.swing.JButton as JButton
import javax.swing.JTextField as JTextField

# Get the Resource Directory path and specify the soccerkick resources dir
workDir = getResourcesDir()+"/Models/SoccerKick"

m = getCurrentModel()
# Hide simulation toolbar so users run thru the custom GUI only
setSimulationToolBarVisibility(0)

# create window and empty all contents
parametersWindow = createParametersWindow()

# Hamstrings
bifemlh = m.getMuscles().get('bifemlh_r')
maxBifemlhForceProperty = bifemlh.getPropertyByName('max_isometric_force')
maxBifemlhForceOriginal = bifemlh.getMaxIsometricForce()

# Rect Fem
rect_fem = m.getMuscles().get('rect_fem_r')
maxRectfemForceProperty = rect_fem.getPropertyByName('max_isometric_force')
maxRectfemForceOriginal = rect_fem.getMaxIsometricForce()

# soleus_r
soleus = m.getMuscles().get('soleus_r')
maxSoleusForceProperty = soleus.getPropertyByName('max_isometric_force')
maxSoleusForceOriginal = soleus.getMaxIsometricForce()

# tib_ant_r
tib_ant = m.getMuscles().get('tib_ant_r')
maxTibAntForceProperty = tib_ant.getPropertyByName('max_isometric_force')
maxTibAntForceOriginal = tib_ant.getMaxIsometricForce()

ballspeed = JTextField()

def getSpeed(event):
    d = modeling.Storage(workDir+"/kick/leg6dof9musc_knee_stop_Kinematics_u.sto")
    z = modeling.ArrayDouble(d.getSize())
    d.getDataColumn('ball_tx', z)
    j = z.get(1)
    for i in range (z.getSize()):
        h = z.get(i)
	if h>j:
	    j=h
    ballspeed.setText(str(j))
    panel.validate()

def createGUI() :
    parametersWindow.reset()
    # Create slider(s)
    parametersWindow.createKnobForProperty(maxBifemlhForceProperty, "Hamstrings Muscle Force (Newtons)", m, bifemlh, 0., 9000.)
    parametersWindow.createKnobForProperty(maxRectfemForceProperty, "Rec Fem Muscle Force (Newtons)", m, rect_fem, 0., 9000.)
    parametersWindow.createKnobForProperty(maxSoleusForceProperty, "Soleus Muscle Force (Newtons)", m, soleus, 0., 9000.)
    parametersWindow.createKnobForProperty(maxTibAntForceProperty, "Tibialis Anterior Muscle Force (Newtons)", m, tib_ant, 0., 9000.)
    # turn angle
    turn = m.getCoordinateSet().get('turn')
    parametersWindow.createKnobForCoordinate(turn, 'Turn Right and Left')
    # reset view
    cameraParams = [-6.71, 6.47, 14.29, 4.56, 1.72, -1.36, 0.08, 0.97, -0.23, -0.57, 0.24, 0.79, 27.21]
    parametersWindow.setDefaultView(cameraParams)
    parametersWindow.createResetViewButton()
    ## run button
    ## This uses absolute path for setup file, could be done better for portability
    parametersWindow.addToolButton(workDir+"/runFD.xml", "Kick...")
    # Outputs
    # Create panel, with custom buttons added later that could control the contents of the plotWindow
    panelSpeed = parametersWindow.addOutputPanel("MaxSpeed");
    # Add a button and a text field for the speed field.
    btn1 = JButton("Get Max Speed", actionPerformed=getSpeed)
    panelSpeed.add(btn1)
    # ballspeed = JTextField()
    panelSpeed.add(ballspeed)
    parametersWindow.validate()

def resetMuscles(event) :
     modeling.PropertyHelper.setValueDouble(maxBifemlhForceOriginal, maxBifemlhForceProperty)
     modeling.PropertyHelper.setValueDouble(maxRectfemForceOriginal, maxRectfemForceProperty)
     modeling.PropertyHelper.setValueDouble(maxSoleusForceOriginal, maxSoleusForceProperty)
     modeling.PropertyHelper.setValueDouble(maxTibAntForceOriginal, maxTibAntForceProperty)
     createGUI()
     panel = parametersWindow.addOutputPanel("Reset model")
     btn = JButton("Reset Muscles", actionPerformed=resetMuscles)
     panel.add(btn)
     parametersWindow.validate()

createGUI()
panel = parametersWindow.addOutputPanel("Reset model")
btn = JButton("Reset Muscles", actionPerformed=resetMuscles)
panel.add(btn)
parametersWindow.validate()
