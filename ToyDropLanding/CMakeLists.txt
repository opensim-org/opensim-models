SET(DROP_LANDING_FILES ToyLandingModel.osim
											ToyLandingModel_AFO.osim	
											ToyLandingModel_AFO_10x_stiff.osim
											ToyLandingModel_AFO_backpack.osim
											setup_forward_tool.xml
											afoCuff.STL
											afoPlate.STL
											backpack0.vtp)

INSTALL_FILES(/Models/ToyDropLanding/ FILES ${DROP_LANDING_FILES})
