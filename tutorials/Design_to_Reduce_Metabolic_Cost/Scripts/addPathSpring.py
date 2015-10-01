# Get a handle to the current model and create a new copy 
baseModel = getCurrentModel()
pathSpringModel = baseModel.clone()
pathSpringModel.setName(baseModel.getName()+'_path_spring')

# Create the spring we'll add to the model (a PathSpring in OpenSim)
name = 'BiarticularSpringDamper'
restLength = 0.4
stiffness = 10000.0
dissipation = 0.01
pathSpring = modeling.PathSpring(name,restLength,stiffness,dissipation)

# Set geometry path for the path spring to match the gastrocnemius muscle
gastroc = pathSpringModel.getMuscles().get('gastroc_r')
pathSpring.set_GeometryPath(gastroc.getGeometryPath())

# Add the spring to the model
pathSpringModel.addForce(pathSpring)

# Load the model in the GUI
loadModel(pathSpringModel)

# Save the model to file
fullPathName = baseModel.getInputFileName()
newName = fullPathName.replace('.osim', '_path_spring.osim')
pathSpringModel.print(newName)