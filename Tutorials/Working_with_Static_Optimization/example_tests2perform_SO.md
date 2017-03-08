# tests to perform on SO on....

## CMC and Static Optimization fails with Disabled Muscle
https://simtk.org/forums/viewtopic.php?f=91&t=4603

We have been able to reproduce this bug and will address. The problem seemingly comes from the tools using a getMuscles() method that results in the number of possible states not matching the states being initialized.

As you you have seen, the workaround is to delete the muscle and run.


## Static Optimization and Ligament Object
https://simtk.org/forums/viewtopic.php?f=91&t=4750

Has anybody been able to run Static Optimization with a ligament object in their model? I can run CMC just fine but SO does not run. The fact that CMC runs indicates to me that the ligament is implemented correctly?
