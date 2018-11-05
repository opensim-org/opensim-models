""" test models in the distribution

"""
import os
import sys
import unittest
import opensim
#import opensim as opensim
root = os.getcwd()
pattern = "*.osim"

osimpaths = list()
modelNames = list()

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            osimpaths.append(os.path.join(path, name))
            modelNames.append(name)

for i in range(len(osimpaths)):
    print("\n\n\n" + 80 * "=" + "\nLoading model '%s'" % osimpaths[i] + "\n" + 80 * "-")
    # Without this next line, the print above does not necessarily
    # precede OpenSim's output.
    sys.stdout.flush()
    filename = osimpaths[i]
    modelname = modelNames[i]
    try:
        model = opensim.Model(filename)
        s = model.initSystem()
    except Exception as e:
        print("Oops, Model '%s' failed:\n%s" % (modelname, e.message))
        sys.exit(1)

    # Print the 4.0 version to file and then read back into memory
    filename_new = filename.replace('.osim','_new.osim')
    modelName_new = modelName.replace('.osim','_new.osim')
    # Print the 4.0 model to file
    model.print(filename_new)
    # Try and read back in the file
    try:
        model = opensim.Model(filename_new)
        s = model.initSystem()
    except  Exception as e:
        print("Oops, 4.0 written Model '%s' failed:\n%s" % (modelName_new, e.message))
        sys.exit(1)

    # Remove the printed file
    os.remove(filename_new)

print("All models loaded successfully.")
