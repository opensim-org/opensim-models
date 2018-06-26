# Get a handle to the current model and create a new copy 
baseModel = getCurrentModel()
ankleSpringModel = baseModel.clone()
ankleSpringModel.setName(baseModel.getName()+'_ankle_spring')

# Create the spring we'll add to the model (a CoordinateLimitForce in OpenSim)
ankleSpring = modeling.CoordinateLimitForce()

# Set the coordinate for the spring
ankleSpring.set_coordinate('ankle_angle_r')
ankleSpring.setName('AnkleLimitSpringDamper')

# Add the spring to the model
ankleSpringModel.addForce(ankleSpring)

# Load the model in the GUI
loadModel(ankleSpringModel)

# Set the spring's properties
ankleSpring.setUpperStiffness(30.0)
ankleSpring.setUpperLimit(5.0)
ankleSpring.setLowerStiffness(1.0)
ankleSpring.setLowerLimit(-90.0)
ankleSpring.setDamping(0.01)
ankleSpring.setTransition(2.0)

# Save the model to file
fullPathName = baseModel.getInputFileName()
newName = fullPathName.replace('.osim', '_spring.osim')
ankleSpringModel.print(newName)