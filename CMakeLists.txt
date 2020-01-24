cmake_minimum_required(VERSION 3.1.3)
project(OpenSimModels)

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}-install" CACHE PATH
        "The directory in which to install this project." FORCE)
endif()

install(DIRECTORY Geometry/
       DESTINATION Geometry)
# The only difference here between 3.3 and 4.0 is a README.md that says how
# to fix missing polygons.

install(DIRECTORY Models/Arm26/
        DESTINATION Models/Arm26)
install(DIRECTORY Tutorials/Computed_Muscle_Control/
        DESTINATION Models/Arm26)

install(FILES Models/BouncingBlock/bouncing_block.osim
              Models/BouncingBlock/bouncing_block_weak_spring.osim
        DESTINATION Models/BouncingBlock)
install(FILES Models/BouncingBlock/run_forward_bouncingBlock.xml
        DESTINATION Models/BouncingBlock
        RENAME run_forward.xml) # TODO inconsistent filename; which should we use?

install(FILES Models/Gait10dof18musc/gait10dof18musc.osim
              Models/Gait10dof18musc/subject01.osim
              Models/Gait10dof18musc/subject01_metabolics.osim
              Models/Gait10dof18musc/subject01_metabolics_path_spring.osim
              Models/Gait10dof18musc/subject01_metabolics_path_actuator.osim
              Tutorials/Design_to_Reduce_Metabolic_Cost/ExperimentalData/subject01_static.trc
              Tutorials/Design_to_Reduce_Metabolic_Cost/ExperimentalData/subject01_walk.trc
              Tutorials/Design_to_Reduce_Metabolic_Cost/ExperimentalData/subject01_walk_grf.mot
              Tutorials/Design_to_Reduce_Metabolic_Cost/ExperimentalData/subject01_walk_grf.xml
              Tutorials/Design_to_Reduce_Metabolic_Cost/CMC/walk_Setup_CMC.xml
              Tutorials/Design_to_Reduce_Metabolic_Cost/CMC/walk_Setup_CMC_PathActuator.xml
        DESTINATION Models/Gait10dof18musc)
# TODO subject01_metabolics* files?
install(DIRECTORY Tutorials/Design_to_Reduce_Metabolic_Cost/
        DESTINATION Models/Gait10dof18musc
				PATTERN "CMC/walk_Setup_CMC*" EXCLUDE
				PATTERN "ExperimentalData" EXCLUDE)

install(FILES Models/Gait2354_Simbody/gait2354_simbody.osim
        DESTINATION Models/Gait2354_Simbody)
install(DIRECTORY Pipelines/Gait2354_Simbody/
        DESTINATION Models/Gait2354_Simbody
        PATTERN "forces_grf.xml" EXCLUDE
        PATTERN "subject01_Setup_Analyze_Reactions.xml" EXCLUDE
        PATTERN "subject01_Setup_AnalyzeTest.xml" EXCLUDE
        PATTERN "Pipelines/Gait2354_Simbody/subject01_walk1_ik.mot" EXCLUDE)

install(FILES Models/Gait2392_Simbody/gait2392_thelen2003muscle.osim
        DESTINATION Models/Gait2392_Simbody
        RENAME gait2392_simbody.osim)
install(FILES
        Pipelines/Gait2392_Simbody/gait2392_CMC_Actuators.xml
        Pipelines/Gait2392_Simbody/gait2392_CMC_ControlConstraints.xml
        Pipelines/Gait2392_Simbody/gait2392_CMC_Tasks.xml
        Pipelines/Gait2392_Simbody/gait2392_RRA_Actuators.xml
        Pipelines/Gait2392_Simbody/gait2392_RRA_ControlConstraints.xml
        Pipelines/Gait2392_Simbody/gait2392_RRA_Tasks.xml
        Pipelines/Gait2392_Simbody/gait2392_Scale_MarkerSet.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_Analyze.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_CMC.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_Forward.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_IK.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_RRA.xml
        Pipelines/Gait2392_Simbody/subject01_Setup_Scale.xml
        Pipelines/Gait2392_Simbody/subject01_static.trc
        Pipelines/Gait2392_Simbody/subject01_walk1.trc
        Pipelines/Gait2392_Simbody/subject01_walk1_grf.mot
        Pipelines/Gait2392_Simbody/subject01_walk1_grf.xml
        DESTINATION Models/Gait2392_Simbody)
    # TODO should we copy over the OutputReference folder?
install(DIRECTORY Tutorials/Intro_to_Musculoskeletal_Modeling/
        DESTINATION Models/Gait2392_Simbody/Tutorial1)

install(FILES Models/Leg6Dof9Musc/leg6dof9musc.osim
        DESTINATION Models/Leg6Dof9Musc)
install(DIRECTORY Tutorials/Strength_of_Simulation/
        DESTINATION Models/Leg6Dof9Musc)

install(DIRECTORY Models/ToyLanding/
        DESTINATION Models/ToyDropLanding)
install(DIRECTORY Tutorials/Prevention_of_Ankle_Injury/
        DESTINATION Models/ToyDropLanding)

install(DIRECTORY Models/Tug_of_War/
        DESTINATION Models/Tug_of_War)
install(DIRECTORY Tutorials/Pulling_Out_the_Stops_Tug_of_War/
        DESTINATION Models/Tug_of_War
        PATTERN "addPrescribedMotion.py" EXCLUDE # TODO leave in or not?
        )
install(FILES Models/WristModel/wrist.osim
        DESTINATION Models/WristModel)

install(FILES Models/Leg39/leg39.osim
        DESTINATION Models/Leg39)

install(FILES
        Pipelines/Leg39/leg39_swing.trc
        Pipelines/Leg39/leg39_swing_short.trc
        Pipelines/Leg39/leg39_swing_IK_Setup.xml
        Pipelines/Leg39/leg39_swing_short_IK_Setup.xml
        DESTINATION Models/Leg39)

install(DIRECTORY Models/SoccerKick
        DESTINATION Models/)
install(FILES  
        Tutorials/Soccer_Kick/controls_kick.xml
        Tutorials/Soccer_Kick/runFD.xml
        Tutorials/Soccer_Kick/SoccerDemoWithReset.py
        DESTINATION Models/SoccerKick)

install(DIRECTORY Tutorials/doc/
        DESTINATION doc)
