SET(DROP_LANDING_FILES 
	ToyLandingModel.osim
	ToyLandingModel_AFO.osim
	setup_forward_tool.xml
	ActiveAFO_Controls.xml
	ToyLandingModel_activeAFO.osim
	afoCuff.STL
	afoPlate.STL)

INSTALL_FILES(/Models/ToyDropLanding/ FILES ${DROP_LANDING_FILES})
