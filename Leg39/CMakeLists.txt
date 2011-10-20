SET(LEG39_FILES leg39.osim 
		leg39_controls.xml 
		leg39_controls_off.xml 
		leg39_InitialStates.sto 
		leg39_muscle_layout.txt
		leg39_Setup_ForwardDynamics.xml
		leg39_Setup_InverseDynamics.xml
		leg39_Setup_InverseKinematics.xml
		leg39_Setup_StaticOptimization.xml
		leg39_ComputedMuscleControl_Tasks.xml
		leg39_ControlConstraints.xml
		leg39_Setup_ComputedMuscleControl.xml
		leg39_swing.trc)
INSTALL_FILES(/examples/Leg39/ FILES ${LEG39_FILES})
INSTALL_FILES(/Models  leg39.osim)

INSTALL(DIRECTORY OutputReference DESTINATION examples/Leg39/ PATTERN ".svn" EXCLUDE)
