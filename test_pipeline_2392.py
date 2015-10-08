""" test to run the gait 2392 pipeline


"""
import os
import unittest

import opensim as osm

path2Model = os.path.join(os.getcwd(), 'models', 'Gait2392_Simbody','gait2392.osim')
path2ScaleSetup = os.path.join(os.getcwd(), 'pipelines', 'Gait2392_Simbody','subject01_Setup_Scale.xml')

def run_scaling(path2Model,path2ScaleSetup):

    # get a handle to the model
    model = osm.Model(path2Model)
    # get a handle to the model state
    myState = model.initSystem()
    # create a scaletool object
    scaletool = osm.ScaleTool(path2ScaleSetup)

    # newMarkers = modeling.MarkerSet(markerSetFile)
    # # 	Replace the markerSet to the model
    # myModel.replaceMarkerSet(myState,newMarkers)
    # #	Re-initialize State
    # myState = myModel.initSystem()
    #
    # ## Scaling Tool
    # # Create the scale tool object from existing xml
    # scaleTool = modeling.ScaleTool(scaleSetup)
    # ## ModelScaler-
    # #Name of OpenSim model file (.osim) to write when done scaling.
    # scaleTool.getModelScaler().setOutputModelFileName(scaledModelName)
    # # Filename to write scale factors that were applied to the unscaled model (optional)
    # scaleTool.getModelScaler().setOutputScaleFileName(appliedscaleSet)
    # # Get the path to the subject
    # path2subject = scaleTool.getPathToSubject()
    # # Run model scaler Tool
    # scaleTool.getModelScaler().processModel(myState,myModel,path2subject,subjectMass);
    #
    # ## Load Scaled model and Initialize states-
    # # Load a model
    # loadModel(scaleModelPath)
    # # Get a handle to the current model
    # myModel = getCurrentModel()
    # #initialize
    # myState = myModel.initSystem()
    #
    # ## ModelPlacer-
    # # Get the path to the subject
    # path2subject = scaleTool.getPathToSubject()
    # # Run Marker Placer
    # scaleTool.getMarkerPlacer().processModel(myState,myModel,path2subject)


    # marker placer.
    return 'something'


def run_IK():

    ## Inverse Kinematics tool
    # Create the IK tool object from existing xml
    # ikTool = modeling.InverseKinematicsTool(ikSetupFile)
    # ikTool.setModel(myModel)
    # ikTool.run()
    # # Load a motion
    # loadMotion(ikMotionFilePath)
    # #initialize
    # myState = myModel.initSystem()


def run_ID():
    ## Inverse Dynamics
    # Create the ID tool object from existing xml
    # idTool = modeling.InverseDynamicsTool(idSetupFile)
    # # Set the model to scaled model from above
    # idTool.setModel(myModel)
    # # Run the tool
    # idTool.run()


run_scaling(path2Model,path2ScaleSetup):

run_IK():

run_ID():
