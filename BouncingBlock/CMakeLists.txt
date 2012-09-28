SET(BOUNCING_BLOCK_FILES bouncing_block.osim
                         bouncing_block_weak_spring.osim	
		         run_forward.xml)
FILE(GLOB BONE_FILES *.vtp)

INSTALL_FILES(/Geometry FILES ${BONE_FILES})
INSTALL_FILES(/Models/BouncingBlock/ FILES ${BOUNCING_BLOCK_FILES})
