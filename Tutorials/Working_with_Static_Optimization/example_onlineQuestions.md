# Static optimization questions from Forum etc.....



## Running SO through Matlab (https://simtk.org/forums/viewtopic.php?f=91&t=4621)

Q:I am trying to set up and run static optimization from Matlab, but I am having trouble figuring out how to do so: using and editing a static optimization settings file, specifying external loads on the model, running the analysis, etc. I'm assuming this is actually possible, perhaps someone can confirm? It doesn't seem to work in the same way as other analyses, e.g. the



A: To run an analysis you will use the AnalyzeTool(). I have attached a Analyze tool setup file to this reply. You will be able to see the different levels of the tool and how to change the properties of it. You can build the tool doing something like;

staticOpt = AnalyzeTool([path 'staticOpt_setup.xml'])

Along with having a static optimization object attached, MuscleAnalysis() is attached to output the muscle states. Your comments have been helpful and we will try and build some confluence info that will help with this particular tool/analysis.

## Static Optimization Reserve Actuators
**Note to self- Try and answer the below question**
One of the main reasons for static optimization crashing is the lack of model strength. So I have added reserve actuators to the static optimization xml setup file.

<replace_actuator_set>false</replace_actuator_set>
<actuator_set_files>my_staticOpt_Reserve_Actuators.xml</actuator_set_files>

Inside this actuator file, I can only specify the optimal_force value. e.g.

<GeneralizedForce name="hip_flexion_r_reserve">
<coordinate> hip_flexion_r </coordinate>
<optimal_force> 1.0 </optimal_force>
</GeneralizedForce>

Now according to the users guide for RRA and CMC, the allowable range of the reserve actuator is between optimal force*default_min and force*default_max. However the default_min and default_max value is specified in the RRA_Control_Constrains xml file, and is not accessible from static optimization. So I was wondering how we specify the default_min & default_max values for the application of static optimization. If we simply increase the optimal force, then the optimization will be more weighted to include force components in this reserve category (because the optimal force value represents the weighting of the actuator - p202 user guide).

## Muscle Force from Static Optimization vs. Force Reporter

q: I am running some simulations with a model including constraints and using static optimization and I have noticed an issue similar to what Alex reported. In my case the muscle forces from ForceReporter are way larger than in the SO simulations.
I thought a workaround could have been assigning the states resulting from static optimization as input through a storage file in the Analysis panel, but I have noticed that the muscle states from SO are all reported as a default value (muscle length 0.1, activation 0.05, I am using Thelen2003 muscles). In your opinion is there a way of setting ForceReporter so that it will use forces occurring in SO simulations?
Thank you in advance for your help,

a: The problem most likely revolves around SO not generating a true state. Its a state-like object that some people requested, but it has no information on fiber length among other things.
So whatever you put into the Analysis tool from SO is not going to give you a good answer. Really, the Analysis tool shouldn't even take incomplete states. Its a design flaw on our part and we are working to improve it in the next release.

## Static Optimization: Constraint Violation
https://simtk.org/forums/viewtopic.php?f=91&t=2370&amp;sid=9f97bdef64f4f8526a71a1b4c2bf87fa
I just came across this forum post from a while ago which clears up some of the questions I had:
https://simtk.org/forum/message.php?msg_id=2371
So, if I have it right,
F - ma = Constraint Violation (where the 'F' and 'ma' are coordinate specific)
and
sum_{all muscles}(activation^p) = Performance.

So, it doesn't really matter how large or small the 'Performance' value is, but the 'Constraint Violation' number should be as close to 0 as possible for the results to be valid. Is that correct?

## Static optimization: Optimal force and controls
https://simtk.org/forums/viewtopic.php?f=91&t=3337

### q:'m still having some problems with Static Optimization and I think it's because I didn't understand it as I should. So I have some questions One of the "Best Practice and Troubleshooting" tips for static optimization is: "Increase the maximun control value of a residual or reserve actuator, while lowering its maximum force. This allow the optimizer to generate a large force to match acceleration but large control values are penalized more heavily (...)". In the reserve actuator the maximum force is the "optimal force" ? and what does it mean being penalized more heavily? I'm trying to run static optimization with exponent 3 in the activation-based cost function, for a walking task (with other external forces than GRF), with gait2392 model. Using expoent 2 cost function it ran but i had to increase the reserve actuator control range (increase maximun and decrease minimun).

a: Basically the Static Optimization analysis tries to match the accelerations computed by inverse dynamics using muscles and residuals/reserves and the knobs it has (in the built in objective function) are the activations. For reserves and residuals, since these reflect errors/unmodeled behaviors, we'd like the optimizer to use them the least. By making max/optimal force small, we make it more expensive for the optimizer to use these rather than muscles.


### q: I still have some questions on this topic. Now Static optimization is running and I'm trying to evaluate the choice of the residual actuators that I have attached to the model. I chose the minimal value of force for which the model ran and then I changed the values for control in an logical manear. After, I kept the value of control and changed force. I evaluated the results and It seems that for the smallest value of optimal force (1) and one of the largest value of control (10000), muscle forces and activations are less noisy in comparisson with the results produced by a residual actuator with the same force and smaller control values. Another thing I observed was that if I increased the control value again (>10000) - yet, mantaining the same force - values became noisy again. Is there an optimal value of control? And, are values such as 10000 and 100000 for control acceptable (meaningful)? What parameters in my results I should evaluate for best choosing residuals actuators (performance and Constraint violation values?) ?

You may be seeing the effects of bad scaling. Ideally you formulate the problem so that the controls are in the range 0-1 (as the optimizer/solver minimizes sum of squares of controls). If the only solution you can get is obtained by setting large values of controls, then those terms will dominate this computation (sum of squares) and will make muscle activations and forces noisy.
