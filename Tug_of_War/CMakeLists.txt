SET(TUG_OF_WAR_FILES Tug_of_War.osim 
		Tug_of_War_controls.xml 
		Tug_of_War_Setup_Forward.xml)
FILE(GLOB BONE_FILES *.vtp)

INSTALL_FILES(/Geometry FILES ${BONE_FILES})
INSTALL_FILES(/Models/Tug_of_War/ FILES ${TUG_OF_WAR_FILES})
