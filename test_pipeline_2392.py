""" test to run the gait 2392 pipeline


"""
import os
import shutil as sh
import ntpath as nt

import unittest
import opensim as osm

path2Model = os.path.join(os.getcwd(), 'models', 'Gait2392_Simbody','gait2392_simbody.osim')
path2ScaleSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_Scale.xml')
path2IKSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_IK_Scale.xml')

def run_scaling(path2Model,path2ScaleSetup):

	newModelPath = os.path.dirname(path2ScaleSetup) + '/' + nt.basename(path2Model)
	# copy the model into the new repo
	sh.copyfile(path2Model, newModelPath)
	# define the input string to the exe
	cmd = 'scale -S ' + path2ScaleSetup
	# run scale
	os.system(cmd)
	# Clean up the directory (delete generic model)
	os.remove(newModelPath)

	## Get the output model name and return it.
	scaletool = osm.ScaleTool(path2ScaleSetup)
	# get the output model name.
	scaledModelName = scaletool.getMarkerPlacer().getOutputModelFileName()
	# return the model filename
	return scaledModelName

def run_IK(path2IKSetup):

	cmd = 'ik -S' + path2IKSetup
	# run IK
	os.system(cmd)

	return 1

# run scaling
scaledModelName = run_scaling(path2Model,path2ScaleSetup)
# run IK
run_IK(path2IKSetup)

#run_ID():
