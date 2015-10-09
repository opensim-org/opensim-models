""" test to run the gait 2392 pipeline


"""
import os
import shutil as sh
import ntpath as nt

import filecmp

import unittest
import opensim as osm

path2Model = os.path.join(os.getcwd(), 'models', 'Gait2392_Simbody','gait2392_simbody.osim')
path2ScaleSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_Scale.xml')
path2IKSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_IK.xml')
path2RRASetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_RRA.xml')
path2CMCSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_CMC.xml')


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
	# Get the output model name and return it.
	scaletool = osm.ScaleTool(path2ScaleSetup)
	# get the output model name.
	scaledModelName = scaletool.getMarkerPlacer().getOutputModelFileName()
	# return the model filename
	return scaledModelName

def run_ik(subjectModel, path2IKSetup):
	# get and handle to the model
	model = osm.Model(subjectModel)
	# make a ikTool object
	ik = osm.InverseKinematicsTool(path2IKSetup)
	# set the model on the object
	ik.setModel(model)
	# run IK
	ik.run()

def run_rra(path2RRASetup):
	# setup the cmd command
	cmd = 'rra -S ' + path2RRASetup
	# run rra using command line
	os.system(cmd)

def run_cmc(path2CMCSetup):
	# setup the cmd command
	cmd = 'cmc -S ' + path2CMCSetup
	# run the cmd command
	os.system(cmd)


# run scaling
scaledModelName = run_scaling(path2Model,path2ScaleSetup)
# set the full path to the model.
subjectModel = os.path.dirname(path2ScaleSetup) + '/' + scaledModelName
# run IK
#run_ik(subjectModel, path2IKSetup)
# run rra
#run_rra(path2RRASetup)
# run cmc
#run_cmc(path2CMCSetup)

ref_Model  = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','OutputReference', 'subject01_simbody.osim')
ref_motion = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','OutputReference', 'subject01_walk1_ik.mot')


def test_scaling(ref_Model, subjectModel):

	filecmp.cmp(ref_Model, subjectModel)

	if false

#def test_ik():

#def test_rra():

#def test_cmc():
