SET(GAIT2354_FILES subject01_static.trc subject01_walk1.trc subject01_walk1.mot subject01_walk1_grf.mot gait2354_simbody.osim
gait2354_CMC_Actuators.xml
gait2354_CMC_ControlConstraints.xml
gait2354_CMC_Tasks.xml
gait2354_IK_Tasks.xml
gait2354_RRA_Actuators.xml
gait2354_RRA_ControlConstraints.xml
gait2354_RRA_Tasks.xml
gait2354_Scale_MarkerSet.xml
gait2354_Scale_MeasurementSet.xml
gait2354_Scale_Tasks.xml
subject01_Scale_ScaleSet.xml
subject01_Setup_Analyze.xml
subject01_Setup_CMC.xml
subject01_Setup_Forward.xml
subject01_Setup_IK.xml
subject01_Setup_InverseDynamics.xml
subject01_Setup_RRA.xml
subject01_Setup_Scale.xml)

INSTALL_FILES(/examples/Gait2354_Simbody/ FILES ${GAIT2354_FILES})
INSTALL(DIRECTORY OutputReference DESTINATION examples/Gait2354_Simbody/ PATTERN ".svn" EXCLUDE)
