SET(GAIT10DOF18_FILES gait10dof18musc.osim
subject01.osim
gait10dof_Reserve_Actuators.xml
gait10dof_Kinematics_Tracking_Tasks.xml)

INSTALL_FILES(/Models/Gait10dof18musc/ FILES ${GAIT10DOF18_FILES})
INSTALL(DIRECTORY ExperimentalData DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE)
INSTALL(DIRECTORY IK DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE)
INSTALL(DIRECTORY ID DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE)
INSTALL(DIRECTORY RRA DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE)
INSTALL(DIRECTORY CMC DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE
																PATTERN  "controls_43p_r.xml" EXCLUDE)
INSTALL(DIRECTORY OutputReference DESTINATION Models/Gait10dof18musc/ PATTERN ".svn" EXCLUDE
																			PATTERN  "CMC/ResultsCMC_*" EXCLUDE
																			PATTERN  "CMC/*.osim" EXCLUDE)
