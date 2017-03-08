//==============================================================================
//The OpenSim Main header must be included in all files
#include <OpenSim/OpenSim.h>
// Set the namespace to shorten the declarations
// Note: Several classes appear in both namespaces and require using the full name
using namespace OpenSim;
using namespace SimTK;
//______________________________________________________________________________
/**
 * 
 */
int main()
{
	try {
		// Code to the construct the model will go here
		
	// Section: Setup
		// Define key model variables 
		double pelvisWidth = 0.20
		// Create an OpenSim Model
		Model osimModel = Model();
		osimModel.setName("DynamicWalkerModel");
		// Get a reference to the ground object
		OpenSim::Body &ground = osimModel.getGroundBody();
		// Define the acceleration of gravity
		osimModel.setGravity(Vec3(0, -9.80665, 0));
		// Construct the Platform
		
	// Section A: Set the properties of the coordinates that define the joint
		// A pin joint consists of a single coordinate describing a change in orientation about the Z axis
		
		double mass = 1;
		// Location of the Center of Mass from the Body Origin expressed in Body Frame
		Vec3 comLocInBody(0.0, 0.0, 0.0);
		// Inertia of the Body expressed in the Body Frame
		Inertia bodyInertia(1.0, 1.0, 1.0, 0.0, 0.0, 0.0);
		// Create the body
		OpenSim::Body* platform = new OpenSim::Body("Platform", mass, comLocInBody, bodyInertia);
		// Create the Platform Joint
		// Create the joint connection the platform to the ground
		Vec3 locationInParent(0.0, 0.0, 0.0);
		Vec3 orientationInParent(0.0, 0.0, 0.0);
		Vec3 locationInChild(0.0, 0.0, 0.0);
		Vec3 orientationInChild(0.0, 0.0, 0.0);
		PinJoint *platformToGround = new PinJoint("PlatformToGround", ground, locationInParent, orientationInParent, *platform, locationInChild, orientationInChild, false);

		CoordinateSet &platformJoints = platformToGround->upd_CoordinateSet();
		platformJoints[0].setName("platform_rz");
		double rotRangePlatform[2] = { -Pi / 2.0, 0 };
		platformJoints[0].setRange(rotRangePlatform);
		platformJoints[0].setDefaultValue(convertDegreesToRadians(-10.0));
		platformJoints[0].setDefaultLocked(true);
		// Add and scale model for display in GUI
		platform->addDisplayGeometry("box.vtp");
		platform->updDisplayer()->setScaleFactors(Vec3(1, 0.05, 1));
		// Add the platform to the Model
		osimModel.addBody(platform);

/*
	// Section A.1 TODO: Create the Pelvis and set the coordinate properties 
		

	// Section A.2 TODO: Create the LeftThigh, LeftShank, RightThigh and RightShank bodies 
		double thighLength = 0.40, shankLength = 0.435;


	// Section B: Add Contact Geometry
		// Add Contact Mesh for Platform
		// The initial orientation is defined by a normal pointing in the positive x direction
		ContactHalfSpace* platformContact = new ContactHalfSpace(Vec3(0.0, 0.0, 0.0), Vec3(0.0, 0.0, -Pi / 2.0), *platform, "PlatformContact");
		osimModel.addContactGeometry(platformContact);

		// Contact Sphere Properties
		double contactSphereRadius = 0.05;

		// Add Contact Sphere for Right Hip
		Vec3 rightHipLocationInPelvis(0.0, 0.0, pelvisWidth / 2.0);
		ContactSphere* rightHipContact = new ContactSphere(contactSphereRadius, rightHipLocationInPelvis, *pelvis, "RHipContact");
		osimModel.addContactGeometry(rightHipContact);
		
	// Section B.1 TODO: Add ContactSphere to the left hip, the knee, and the foot points
		// ********** BEGIN CODE **********


		// **********  END CODE  **********

	// Section B.2 TODO: Add HuntCrossleyForces
		// Define contact parameters for all the spheres
		double stiffness = 1E7, dissipation = 0.1, staticFriction = 0.6, dynamicFriction = 0.4, viscosity = 0.01;
		// Right Hip Contact Parameters
		OpenSim::HuntCrossleyForce::ContactParameters *rightHipContactParams = new OpenSim::HuntCrossleyForce::ContactParameters(stiffness, dissipation, staticFriction, dynamicFriction, viscosity);
		rightHipContactParams->addGeometry("RHipContact");
		rightHipContactParams->addGeometry("PlatformContact");
		// Right Hip Force
		OpenSim::HuntCrossleyForce* rightHipForce = new OpenSim::HuntCrossleyForce(rightHipContactParams);
		rightHipForce->setName("RightHipForce");
		//Add Force
		osimModel.addForce(rightHipForce);
	
	// Section B.2 TODO: Add HuntCrossleyForces betweeen the remaining ContactSpheres 
		// ********** BEGIN CODE **********


		// **********  END CODE  **********
		

	// Section C.1 TODO: Construct CoordinateLimitForces for the Hip and Knee
		// ********** BEGIN CODE **********


		// **********  END CODE  **********

/**/

		// Save the model to a file
		osimModel.print("DynamicWalkerModel.osim");
	}
    catch (OpenSim::Exception ex)
    {
        std::cout << ex.getMessage() << std::endl;
        return 1;
    }
    catch (SimTK::Exception::Base ex)
    {
        std::cout << ex.getMessage() << std::endl;
        return 1;
    }
    catch (std::exception ex)
    {
        std::cout << ex.what() << std::endl;
        return 1;
    }
    catch (...)
    {
        std::cout << "UNRECOGNIZED EXCEPTION" << std::endl;
        return 1;
    }
    std::cout << "Model Built" << std::endl;
    std::cout << "Press return to continue" << std::endl;
    std::cin.get();
    return 0;
 } 