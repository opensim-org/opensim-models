#-----------------------------------------------------------------------------
# www.simtk.org
# CMake file for building an OpenSim project
# Author: The OpenSim Team
#-----------------------------------------------------------------------------
cmake_minimum_required(VERSION 2.6)
# Create Project (Automatically creates variables DynamicWalker_BINARY_DIR and DynamicWalker_SOURCE_DIR}
PROJECT (DynamicWalker)

#-----------------------------------------------------------------------------
#Setup the variable OPENSIM_INSTALL_DIR to the Environment Variable
SET(OPENSIM_INSTALL_DIR $ENV{OPENSIM_HOME} CACHE PATH "Path to OpenSim Install")
# To add Debug feature add ";Debug" after Release on the line below
SET(CMAKE_CONFIGURATION_TYPES "RelWithDebInfo;Release"
      CACHE STRING "Semicolon separated list of supported configuration types, only supports Release and RelWithDebInfo, anything else will be ignored." FORCE )
#-----------------------------------------------------------------------------
# Setup Targets
SET(TARGET DynamicWalkerBuild CACHE STRING "The Name of the executable")
SET(SOURCE DynamicWalkerBuildModel.cpp CACHE STRING "The name of the source files")
#-----------------------------------------------------------------------------
# Setup Headers to Include
SET(SIMTK_HEADERS_DIR ${OPENSIM_INSTALL_DIR}/sdk/include/SimTK/include)
SET(OPENSIM_HEADERS_DIR ${OPENSIM_INSTALL_DIR}/sdk/include)
INCLUDE_DIRECTORIES(${SIMTK_HEADERS_DIR} ${OPENSIM_HEADERS_DIR})
#-----------------------------------------------------------------------------
# Setup Links
SET(OPENSIM_LIBS_DIR ${OPENSIM_INSTALL_DIR}/sdk/lib ${OPENSIM_INSTALL_DIR}/lib)
SET(OPENSIM_DLLS_DIR ${OPENSIM_INSTALL_DIR}/bin)
LINK_DIRECTORIES(${OPENSIM_LIBS_DIR} ${OPENSIM_DLLS_DIR})
#-----------------------------------------------------------------------------
# Namespace
ADD_EXECUTABLE(${TARGET} ${SOURCE})  
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Namespace
SET(NameSpace "OpenSim_" CACHE STRING "Prefix for simtk lib names, includes trailing '_'. Leave empty to use stock SimTK libraries.")
MARK_AS_ADVANCED(NameSpace)
#-----------------------------------------------------------------------------
# Setup Libraries
TARGET_LINK_LIBRARIES(${TARGET}
    debug osimSimulation_d    optimized osimSimulation
    debug osimActuators_d    optimized osimActuators
    debug osimCommon_d        optimized osimCommon
    debug osimAnalyses_d    optimized osimAnalyses
    debug osimTools_d        optimized osimTools
    debug ${NameSpace}SimTKcommon_d optimized ${NameSpace}SimTKcommon
    debug ${NameSpace}SimTKmath_d optimized  ${NameSpace}SimTKmath
    debug ${NameSpace}SimTKsimbody_d optimized ${NameSpace}SimTKsimbody
    liblapack
    ${PLATFORM_LIBS}
)
#-----------------------------------------------------------------------------
# Opertating System Dependent Settings
IF(WIN32)
    SET(PLATFORM_LIBS  pthreadVC2)
ELSE(WIN32)
  SET(NameSpace "")
  IF(APPLE)
    SET(PLATFORM_LIBS  SimTKAtlas)
  ELSE(APPLE)
    SET(PLATFORM_LIBS SimTKAtlas_Lin_generic)
  ENDIF(APPLE)
ENDIF (WIN32)
#-----------------------------------------------------------------------------
MARK_AS_ADVANCED(CMAKE_INSTALL_PREFIX)


