# Static Optimization

Contents:

- [Introduction](#Introduction)
- [Study 1: The First Simulation](#Study-1:-SO-with-different-motions)
- [Study 2: SO with different motions](#Study-1:-SO-with-different-motions)
- [Study 3: Effects of model actuation on muscle activation](Study 2:-Effects-of-model-actuation-on-muscle-activation)
- [Study 4: Including passive elements](Study-3:-Including-passive-elements)
- [Study 5: Evaluating your Results](Study-3:-Evaluating-your-Results)

Introduction
------------

*Prerequisites and recommending Reading*


Study 1: SO with different motions
----------------------------------

You need three things to run a SO analysis. (1) A model (2) A motion to Drive the model, and (3) External forces to apply to the model.


You can use IK or RRA results as input kinematics. If using IK results, you usually need to filter them, either externally or using the OpenSim analyze/static optimization field; if using RRA results, you usually do not have to filter.


*Generating a motion - Scale, IK and RRA*

*Comparing Static Optimization from different motions*

*from IK*

*from RRA*

Study 2: Effects of model actuation on SO muscle activation
-----------------------------------------------------------

If the residual actuators or the model's muscles are weak, the optimization will take a long time to converge or will never converge at all.
If the residual actuators are weak, increase the maximum control value of a residual, while lowering its maximum force. This allows the optimizer to generate a large force (if necessary) to match accelerations, but large control values are penalized more heavily. In static optimization, ideal actuator excitations are treated as activations in the cost function.
If the muscles are weak, append Coordinate Actuators to the model at the joints in the model. This will allow you to see how much "reserve" actuation is required at a given joint and then strengthen the muscles in your model accordingly.
If troubleshooting a weak model and optimization is slow each time, try reducing the parameter that defines the maximum number of iterations.

*Net Joint Reactions*


*Changing the Optimal force*
"However, I have noted that the activations I receive in SO output depend to the <optimal_force> parameter.I performed several SO with an optimal force equal to 1000, 10 and another one to 1, and they were all clearly differents. It seems the more <optimal_force> parameter is high, the less some of my muscles's activations are (I attached 2 png files of my curves to illustrate that). So here is my question : how can I know what value this parameter must have to give the "good one" SO ?"

Basically the Static Optimization analysis tries to match the accelerations computed by inverse dynamics using muscles and residuals/reserves and the knobs it has (in the built in objective function) are the activations. For reserves and residuals, since these reflect errors/unmodeled behaviors, we'd like the optimizer to use them the least. By making max/optimal force small, we make it more expensive for the optimizer to use these rather than muscles.


Study 4:
--------



Study 4: Evaluating your Results (fiber length, activations)
------------------------------------------------------------

- Are there any large or unexpected residual actuator forces?
- Find EMG or muscle activation data for comparison with your simulated activations. Does the timing of muscle activation/deactivation match? Are the magnitudes and patterns in good agreement?

*Putting in lower bounds for the muscle activations*

Study 5: Batch processing SO through API functions.
---------------------------------------------------
