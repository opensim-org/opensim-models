# --------------------------------------------------------------------------- #
# OpenSim: computeMomentArm.py                                                #
# --------------------------------------------------------------------------- #
# OpenSim is a toolkit for musculoskeletal modeling and simulation,           #
# developed as an open source project by a worldwide community. Development   #
# and support is coordinated from Stanford University, with funding from the  #
# U.S. NIH and DARPA. See http://opensim.stanford.edu and the README file     #
# for more information including specific grant numbers.                      #
#                                                                             #
# Copyright (c) 2005-2017 Stanford University and the Authors                 #
# Author(s): Ayman Habib, Thomas Uchida, Ajay Seth                            #
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
# Author(s): Ajay Seth, Thomas Uchida, Ayman Habib
# Stanford University
#
# This script computes and plots moment arms for PathSprings, PathActuators, and
# other non-muscle forces that contain GeometryPaths. The user is first prompted
# to load the associated motion (kinematics) file, and must then select one of
# the model coordinates to use in the computation of the moment arms.


# Import required packages.
import org.opensim.utils as utils
from javax.swing import JButton,JComboBox,JFrame,JLabel
from java.awt import BorderLayout


# ------------------------------------------------------------------------------
# Compute and plot moment arms for the coordinate selected by the user.
# ------------------------------------------------------------------------------
def ComputeAndPlotMomentArms(coordIndex):
	coordName = coordList[coordIndex]
	
	col_labels = motionStorage.getColumnLabels()
	ncols = col_labels.getSize()-1
	ncoords = currentModel.getCoordinateSet().getSize()
	nt = motionStorage.getSize()
	inDegrees = motionStorage.isInDegrees()
	if (inDegrees):
		currentModel.getSimbodyEngine().convertDegreesToRadians(motionStorage)
	
	coord_inds = modeling.ArrayInt(ncoords, -1)
	for i in range(0, ncoords):
		coord_inds.set(i, motionStorage.getStateIndex(currentModel.
			getCoordinateSet().get(i).getName()))
	
	# Create a zero-sized array, but pre-allocate the capacity to hold all the
	# results.
	momentArms = modeling.ArrayDouble(0.0, 0, nt)
	times = modeling.ArrayDouble(0.0, 0, nt)
	motionStorage.getTimeColumn(times)
	
	momentArmFunctions = modeling.FunctionSet()
	
	for i in range(0, pathForceNames.getSize()):
		momentArmFunctions.adoptAndAppend(modeling.PiecewiseLinearFunction())
		momentArmFunctions.get(i).setName(pathForceNames.getitem(i) + '.' +
			coordName)
	
	# For each instant in the motion file, update the coordinate values inside
	# the state and compute the moment arms for the path force about the
	# coordinate of interest.
	for i in range(0, nt):
		# Get the "state" data from the storage at this instant.
		stateVec = motionStorage.getStateVector(i)
		time = stateVec.getTime()
		data = stateVec.getData()
		
		# Set the time on the state.
		state.setTime(time)
		
		# Set the coordinate values on the state from the storage data.
		for j in range(0, ncoords):
			coord = currentModel.getCoordinateSet().get(j)
			coord.setValue(state, data.getitem(coord_inds.getitem(j)))
		
		for k in range(0, pathForceNames.getSize()):
			force = modeling.PathSpring.safeDownCast(forces.get(pathForceNames.getitem(k)))
			if (force == None):
				force = modeling.PathActuator.safeDownCast(forces.get(pathForceNames.getitem(k)))
			ma_coord = currentModel.getCoordinateSet().get(coordIndex)
			ma_coord.getName()
			ma = force.computeMomentArm(state, ma_coord)
			modeling.PiecewiseLinearFunction.safeDownCast(momentArmFunctions.
				get(k)).addPoint(time, ma)
	
	# Plot moment arm curves
	momentArmPlot = createPlotterPanel("Moment Arms")
	momentArmPlot.setMinX(times.getitem(0))
	momentArmPlot.setMaxX(times.getitem(nt-1))
	momentArmPlot.setXAxisLabel(coordName + ' (rad)')
	momentArmPlot.setYAxisLabel('Moment Arm (m)')
	
	for k in range(0, pathForceNames.getSize()):
		hasNonZero = False
		idx = 0
		while (not hasNonZero and modeling.PiecewiseLinearFunction.safeDownCast(
			momentArmFunctions.get(k)).getNumberOfPoints() > idx):
			if (modeling.PiecewiseLinearFunction.safeDownCast(
				momentArmFunctions.get(k)).getY(idx) != 0):
				hasNonZero = True
			idx = idx + 1
		
		if (hasNonZero):
			addFunctionCurve(momentArmPlot, momentArmFunctions.get(k))


# ------------------------------------------------------------------------------
# Prompt the user to select the desired coordinate from the specified motion
# (kinematics) file.
# ------------------------------------------------------------------------------
class CoordinateChooser:
	def buttonPressed(self, event):
		# The OK button was pressed; proceed to compute and plot moment arms
		# relative to the selected coordinate.
		coordIndex = self.cb.selectedIndex
		coordName = self.data[coordIndex]
		self.frame.setVisible(False)
		ComputeAndPlotMomentArms(coordIndex)
	
	def __init__(self):
		# Populate and display window for selecting a coordinate from the
		# specified motion (kinematics) file.
		self.frame = JFrame("Coordinate chooser")
		self.frame.setSize(350,100)
		self.frame.setLayout(BorderLayout())
		self.frame.setLocationRelativeTo(None)
		
		self.data = coordList
		self.cb = JComboBox(self.data, preferredSize=(200,25))
		self.frame.add(self.cb, BorderLayout.WEST)
		
		btn = JButton('OK', preferredSize=(75,25),
			actionPerformed=self.buttonPressed)
		self.frame.add(btn, BorderLayout.EAST)
		
		self.label = JLabel('Please select the coordinate to use in the \
			moment arm calculations', preferredSize=(325,50))
		self.frame.add(self.label, BorderLayout.NORTH)
		
		self.frame.setVisible(True)


# ------------------------------------------------------------------------------
# [main] Find all non-muscle forces acting along a path in the current model.
# Prompt the user to select a motion (kinematics) file, then display the
# Coordinate Chooser window. Execution then proceeds in the buttonPressed event
# handler.
# ------------------------------------------------------------------------------
currentModel = getCurrentModel()

# Get a working state so we can update the coordinate values.
state = currentModel.initSystem()

# Get the path forces from the current model's force set.
forces = currentModel.getForceSet()

# List of non-muscle forces acting along a path (i.e., compute the moment arms
# corresponding to these elements).
pathForceNames = modeling.ArrayStr()

for i in range(0, forces.getSize()):
	force = forces.get(i)
	muscle = modeling.Muscle.safeDownCast(force)
	if (muscle == None):
		# The force is not a muscle.
		if (force.hasGeometryPath()):
			pathForceNames.append(force.getName())
			print 'Adding ' + force.getName() + \
				' to list of forces to compute moment arm.'

# Obtain a file containing the motion to use for computing moment arms.
motionFile = utils.FileUtils.getInstance().browseForFilename(".sto",
	"Please select the storage/motion file with kinematics to compute moment \
		arms.", 1);
print motionFile

if (motionFile != None):
	motionStorage = modeling.Storage(motionFile)
	
	# Generate list of coordinates.
	coordList = []
	for i in range(0, currentModel.getCoordinateSet().getSize()):
		coordList.append(currentModel.getCoordinateSet().get(i).getName())
	
	CoordinateChooser()
