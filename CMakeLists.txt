PROJECT(OpenSimModels)

cmake_minimum_required(VERSION 2.6)

SUBDIRS(Gait2354_Simbody Gait2392_Simbody WristModel Arm26 Leg6Dof9Musc Tug_of_War BouncingBlock ToyDropLanding Gait10dof18musc)

FILE(GLOB VTP_FILES "Geometry/*.vtp")
FILE(GLOB STL_FILES "Geometry/*.stl")
FILE(GLOB OBJ_FILES "Geometry/*.obj")
FILE(GLOB PNG_FILES "Geometry/*.PNG")
INSTALL_FILES(/Geometry/ FILES  ${VTP_FILES})
INSTALL_FILES(/Geometry/ FILES  ${STL_FILES})
INSTALL_FILES(/Geometry/ FILES  ${OBJ_FILES})
INSTALL_FILES(/Geometry/ FILES  ${PNG_FILES})
