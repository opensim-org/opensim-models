# Static Optimization

## Study 1- Differences in SO results between IK and RRA motions.  
## Study 2- Effects of model actuation on muscle activation
## Study 3- Evaluating your Results.


## Introduction



#### What does a SO analysis do?

Static optimization works internally by solving the inverse dynamics problem, then trying to solve the redundancy problem for actuators/muscles using the accelerations from the inverse dynamics solution as a constraint. If a constraint violation is reported, this oculd be a sign that the optimizer couldn't solve for muscle forces while enforcing the inverse dynamics solution.

This likely means that there is noise in the data or there is a sudden jump in accelerations in one frame. In this case, you should examine the inverse dynamics solution to determine the problematic frame, and fix/interpolate the data during this portion of the motion.

Ajay (forum)....
OpenSim's StaticOptimization algorithm solves for muscle forces that generate the desired accelerations directly and doesn't solve for the necessary muscle joint moments as an intermediate step. If the kinematics (accelerations) are identical between inverse dynamics and static optimization then the generalized force (torque) must be equivalent to the net moment produced by muscles and other forces. You could always look at the muscle forces estimated by static optimization and CMC to compute the net joint moment.

Static optimization computes the max muscle force (activation of 1) based on the current state (angles, velocities) of the model and assuming an infinitely stiff tendon to then solve for an activation on (0,1) that scales this max muscle force. Prior to 3.0 this force included passive contributions so the applied muscle force was axfiso(flxfv+pfl)xcos(pennation). Scaling the passive force by a seemed wrong to us, so in 3.0 this was changed to exclude the passive force in the calculation of the instantaneous max muscle force. Now the solution for a uses the max muscle force as simply fiso*fl*fv*cos(pennation) (still assumes no tendon dynamics). In your equation you included additive passive force and neglected pennation. We take advantage of the activation scaling the muscle force in formulating the optimization problem.

#### What components of the model are used in the analysis?

#### How are muscles treated during SO?

## Study 1- Differences in SO results between IK and RRA motions.  

You can use IK or RRA results as input kinematics. If using IK results, you usually need to filter them, either externally or using the OpenSim analyze/static optimization field; if using RRA results, you usually do not have to filter.


### Generating a motion - Scale, IK and RRA

### Comparing Static Optimization from different motions

#### - from IK

#### - from RRA

## Study 2- Effects of model actuation on muscle activation

If the residual actuators or the model's muscles are weak, the optimization will take a long time to converge or will never converge at all.
If the residual actuators are weak, increase the maximum control value of a residual, while lowering its maximum force. This allows the optimizer to generate a large force (if necessary) to match accelerations, but large control values are penalized more heavily. In static optimization, ideal actuator excitations are treated as activations in the cost function.
If the muscles are weak, append Coordinate Actuators to the model at the joints in the model. This will allow you to see how much "reserve" actuation is required at a given joint and then strengthen the muscles in your model accordingly.
If troubleshooting a weak model and optimization is slow each time, try reducing the parameter that defines the maximum number of iterations.



#### Reserves and Residuals

#### Changing the Optimal force
"However, I have noted that the activations I receive in SO output depend to the <optimal_force> parameter.I performed several SO with an optimal force equal to 1000, 10 and another one to 1, and they were all clearly differents. It seems the more <optimal_force> parameter is high, the less some of my muscles's activations are (I attached 2 png files of my curves to illustrate that). So here is my question : how can I know what value this parameter must have to give the "good one" SO ?"

Basically the Static Optimization analysis tries to match the accelerations computed by inverse dynamics using muscles and residuals/reserves and the knobs it has (in the built in objective function) are the activations. For reserves and residuals, since these reflect errors/unmodeled behaviors, we'd like the optimizer to use them the least. By making max/optimal force small, we make it more expensive for the optimizer to use these rather than muscles.



## Study 4- Evaluating your Results (fiber length, activations)

- Are there any large or unexpected residual actuator forces?
- Find EMG or muscle activation data for comparison with your simulated activations. Does the timing of muscle activation/deactivation match? Are the magnitudes and patterns in good agreement?

#### Putting in lower bounds for the muscle activations...


## Study 5- Batch processing SO through API functions.



## FAQ
#### Why are my SO activations so much lower than my CMC activations?
