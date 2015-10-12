""" test to run the gait 2392 pipeline


"""
import os
import shutil as sh
import ntpath as nt

import filecmp

import unittest
import opensim as osm

path2RRASetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_RRA.xml')
path2CMCSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_CMC.xml')
path2ScaleSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_Scale.xml')

def run_scaling(path2ScaleSetup):
    # define the input string to the exe
    cmd = 'scale -S ' + path2ScaleSetup
    # run scale
    os.system(cmd)

def run_ik(subjectModel, path2IKSetup):
    # get and handle to the model
    model = osm.Model(subjectModel)
    # make a ikTool object
    ik = osm.InverseKinematicsTool(path2IKSetup)
    # set the model on the object
    ik.setModel(model)
    # run IK
    ik.run()
    # return the output file name
    return ik.getOutputMotionFileName()

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
#scaleModelName = run_scaling(path2ScaleSetup)
# set the full path to the model.
#new_Model = os.path.dirname(path2ScaleSetup) + '/' + scaleModelName
# run IK
#run_ik(subjectModel, path2IKSetup)
# run rra
#run_rra(path2RRASetup)
# run cmc
#run_cmc(path2CMCSetup)

global subject_Model

class TestPipelineGait2392(unittest.TestCase):

    # the models and pipelines are in separate folders. Define the file paths.
    # Then copy the model into the pipeline dir
    testDir = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody')
    path2Model = os.path.join(os.getcwd(), 'models', 'Gait2392_Simbody','gait2392_simbody.osim')
    path2ScaleSetup = os.path.join(testDir,'subject01_Setup_Scale.xml')
    path2IKSetup = os.path.join(testDir,'subject01_Setup_IK.xml')
    # reference files
    ref_Model  = os.path.join(testDir,'OutputReference', 'subject01_simbody.osim')
    ref_motion = os.path.join(testDir,'OutputReference', 'subject01_walk1_ik.mot')

    # get the scaled model name
    scaletool = osm.ScaleTool(path2ScaleSetup)
    subjectModel = scaletool.getMarkerPlacer().getOutputModelFileName()

    def test_scaling(self):
        # copy the model into the new repo
        newModelPath = os.path.dirname(self.path2ScaleSetup) + '/' + nt.basename(self.path2Model)
        sh.copyfile(self.path2Model, newModelPath)
        # run the OpenSim scale tool
        run_scaling(self.path2ScaleSetup)
        # compare the reference model file (xml) with scaled model file.
        self.assertTrue(filecmp.cmp(self.ref_Model,os.path.join(self.testDir, self.subjectModel)))

    def test_ik(self):
        # run ik
        motionName = run_ik(os.path.join(self.testDir,self.subjectModel),self.path2IKSetup )
        # test the ouput motion with the ref motion.
        self.assertTrue(filecmp.cmp(os.path.join(self.testDir,motionName),self.ref_motion))

    def test_fake(self):
        self.assertTrue(filecmp.cmp(self.ref_Model, self.ref_Model))
