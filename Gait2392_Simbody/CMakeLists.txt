SET(GAIT2392_FILES subject01_static.trc subject01_walk1.trc subject01_walk1.mot subject01_walk1_grf.mot gait2392_simbody.osim
gait2392_CMC_Actuators.xml
gait2392_CMC_ControlConstraints.xml
gait2392_CMC_Tasks.xml
gait2392_IK_Tasks.xml
gait2392_RRA_Actuators.xml
gait2392_RRA_ControlConstraints.xml
gait2392_RRA_Tasks.xml
gait2392_Scale_MarkerSet.xml
gait2392_Scale_MeasurementSet.xml
gait2392_Scale_Tasks.xml
subject01_Scale_ScaleSet.xml
subject01_Setup_Analyze.xml
subject01_Setup_CMC.xml
subject01_Setup_Forward.xml
subject01_Setup_IK.xml
subject01_Setup_RRA.xml
subject01_Setup_Scale.xml
subject01_walk1_grf.xml)

INSTALL_FILES(/Models/Gait2392_Simbody/ FILES ${GAIT2392_FILES})
##INSTALL(DIRECTORY OutputReference DESTINATION Models/Gait2392_Simbody/ PATTERN ".svn" EXCLUDE)
