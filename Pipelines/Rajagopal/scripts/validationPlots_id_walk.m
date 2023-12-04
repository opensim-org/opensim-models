% walk, free-speed
id_results_dir = '../ID/results_walk';
cmc_results_dir = '../CMC/walk/results';

% Right Foot Strike (RFS) times
RFS1 = 0.248;
RFS2 = 1.3925;

% ------------------------------------------------------
% Load simulation outputs from file, 
% normalize time to % gait cycle,
% and calculate net muscle-generated joint moments
% ID
id_filename = strcat(id_results_dir, '/inverse_dynamics.sto');
idJointMoments = importIDJointMoments(id_filename);
time = idJointMoments(:,1);
percentgaitcycle = 100.*(time-RFS1)./(RFS2 - RFS1);
hipflex = idJointMoments(:,8);
kneeext = -idJointMoments(:,11);
ankleext = -idJointMoments(:,13);
idJointMoments = dataset(time, percentgaitcycle, hipflex, kneeext, ankleext);
clear id_results_dir id_filename ...
      time percentgaitcycle hipflex kneeext ankleext

% CMC time axis
hipMom_filename = strcat(cmc_results_dir, '/cmc_MuscleAnalysis_Moment_hip_flexion_r.sto');
muscleGenMoment = importCMCMuscleAnalysis_JointMoment(hipMom_filename);
time = muscleGenMoment(:,1);
percentgaitcycle = 100.*(time - RFS1)./(RFS2-RFS1);
cmcJointMoments = dataset(time, percentgaitcycle);

% Hip flexion moment (CMC, Muscle Analysis)
netMuscleGenMoment = sum(muscleGenMoment(:,2:end),2);
cmcJointMoments.hipflex = netMuscleGenMoment;

% Knee *extension* moment (CMC, Muscle Analysis)
kneeMom_filename = strcat(cmc_results_dir, '/cmc_MuscleAnalysis_Moment_knee_angle_r.sto');
muscleGenMoment = importCMCMuscleAnalysis_JointMoment(kneeMom_filename);
netMuscleGenMoment = -sum(muscleGenMoment(:,2:end),2);
cmcJointMoments.kneeext = netMuscleGenMoment;

% Ankle *extension* moment (CMC, Muscle Analysis)
ankleMom_filename = strcat(cmc_results_dir, '/cmc_MuscleAnalysis_Moment_ankle_angle_r.sto');
muscleGenMoment = importCMCMuscleAnalysis_JointMoment(ankleMom_filename);
netMuscleGenMoment = -sum(muscleGenMoment(:,2:end),2);
cmcJointMoments.ankleext = netMuscleGenMoment;

clear cmc_results_dir hipMom_filename kneeMom_filename ankleMom_filename ...
      muscleGenMoment time netMuscleGenMoment percentgaitcycle

% ------------------------------------------------------
% Sometimes numerical time steps in CMC make it look like there 
% are "repeated" time steps (e.g. time(1) = time(2) = 0.4800)
% Process to remove those so we can calculate splines later
[~, uIdx, ~] = unique(idJointMoments.percentgaitcycle);
idJointMoments = idJointMoments(uIdx,:);

[~, uIdx, ~] = unique(cmcJointMoments.percentgaitcycle);
cmcJointMoments = cmcJointMoments(uIdx,:);

clear uIdx

% ------------------------------------------------------
% Split data into partial 1st and partial 2nd gait cycle
idJointMoments_1 = idJointMoments(idJointMoments.percentgaitcycle <= 100,:);
idJointMoments_2 = idJointMoments(idJointMoments.percentgaitcycle >= 100,:);
idJointMoments_2.percentgaitcycle = mod(idJointMoments_2.percentgaitcycle,100);

cmcJointMoments_1 = cmcJointMoments(cmcJointMoments.percentgaitcycle <= 100,:);
cmcJointMoments_2 = cmcJointMoments(cmcJointMoments.percentgaitcycle >= 100,:);
cmcJointMoments_2.percentgaitcycle = mod(cmcJointMoments_2.percentgaitcycle,100);

% ------------------------------------------------------
% Compute values of ID and CMC joint moments per 1% gait cycle
idJointMoments_1_interp = dataset({(25:1:100)', 'percentgaitcycle'});
idJointMoments_1_interp.hipflex = interp1(idJointMoments_1.percentgaitcycle, idJointMoments_1.hipflex, idJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_1_interp.kneeext = interp1(idJointMoments_1.percentgaitcycle, idJointMoments_1.kneeext, idJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_1_interp.ankleext = interp1(idJointMoments_1.percentgaitcycle, idJointMoments_1.ankleext, idJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');

idJointMoments_2_interp = dataset({(0:1:25)', 'percentgaitcycle'});
idJointMoments_2_interp.hipflex = interp1(idJointMoments_2.percentgaitcycle, idJointMoments_2.hipflex, idJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_2_interp.kneeext = interp1(idJointMoments_2.percentgaitcycle, idJointMoments_2.kneeext, idJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_2_interp.ankleext = interp1(idJointMoments_2.percentgaitcycle, idJointMoments_2.ankleext, idJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');

cmcJointMoments_1_interp = dataset({(25:1:100)', 'percentgaitcycle'});
cmcJointMoments_1_interp.hipflex = interp1(cmcJointMoments_1.percentgaitcycle, cmcJointMoments_1.hipflex, cmcJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_1_interp.kneeext = interp1(cmcJointMoments_1.percentgaitcycle, cmcJointMoments_1.kneeext, cmcJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_1_interp.ankleext = interp1(cmcJointMoments_1.percentgaitcycle, cmcJointMoments_1.ankleext, cmcJointMoments_1_interp.percentgaitcycle, 'linear', 'extrap');

cmcJointMoments_2_interp = dataset({(0:1:25)', 'percentgaitcycle'});
cmcJointMoments_2_interp.hipflex = interp1(cmcJointMoments_2.percentgaitcycle, cmcJointMoments_2.hipflex, cmcJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_2_interp.kneeext = interp1(cmcJointMoments_2.percentgaitcycle, cmcJointMoments_2.kneeext, cmcJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_2_interp.ankleext = interp1(cmcJointMoments_2.percentgaitcycle, cmcJointMoments_2.ankleext, cmcJointMoments_2_interp.percentgaitcycle, 'linear', 'extrap');

% ------------------------------------------------------
% Compute RMS and peak errors between CMC and muscle-generated joint moments
idJointMoments_interp  = [idJointMoments_1_interp; idJointMoments_2_interp];
cmcJointMoments_interp = [cmcJointMoments_1_interp; cmcJointMoments_2_interp];

maxID = max(double(idJointMoments_interp(:,2:4)), [], 1);
maxCMC = max(double(cmcJointMoments_interp(:,2:4)), [], 1);

diff_id_cmc = double(idJointMoments_interp(:,2:4)) - double(cmcJointMoments_interp(:,2:4));
rms_id_cmc = rms(diff_id_cmc,1);
peak_id_cmc = max(abs(diff_id_cmc),[],1);
rms_id_cmc_norm = rms_id_cmc./maxID;
peak_id_cmc_norm = peak_id_cmc./maxID;

% ------------------------------------------------------
% Set up plot
figure

% ------------------------------------------------------
% Plot ID joint moments
subplot(3,1,1)
plot(idJointMoments_1_interp.percentgaitcycle, idJointMoments_1_interp.hipflex, 'b'), hold on
plot(idJointMoments_2_interp.percentgaitcycle, idJointMoments_2_interp.hipflex, 'b'), hold on

subplot(3,1,2)
plot(idJointMoments_1_interp.percentgaitcycle, idJointMoments_1_interp.kneeext, 'b'), hold on
plot(idJointMoments_2_interp.percentgaitcycle, idJointMoments_2_interp.kneeext, 'b'), hold on

subplot(3,1,3)
plot(idJointMoments_1_interp.percentgaitcycle, idJointMoments_1_interp.ankleext, 'b'), hold on
plot(idJointMoments_2_interp.percentgaitcycle, idJointMoments_2_interp.ankleext, 'b'), hold on

% ------------------------------------------------------
% Plot CMC muscle-generated joint moments
subplot(3,1,1)
plot(cmcJointMoments_1_interp.percentgaitcycle, cmcJointMoments_1_interp.hipflex, 'r'), hold on
plot(cmcJointMoments_2_interp.percentgaitcycle, cmcJointMoments_2_interp.hipflex, 'r'), hold on

subplot(3,1,2)
plot(cmcJointMoments_1_interp.percentgaitcycle, cmcJointMoments_1_interp.kneeext, 'r'), hold on
plot(cmcJointMoments_2_interp.percentgaitcycle, cmcJointMoments_2_interp.kneeext, 'r'), hold on

subplot(3,1,3)
plot(cmcJointMoments_1_interp.percentgaitcycle, cmcJointMoments_1_interp.ankleext, 'r'), hold on
plot(cmcJointMoments_2_interp.percentgaitcycle, cmcJointMoments_2_interp.ankleext, 'r'), hold on

% ------------------------------------------------------
% Label plots
subplot(3,1,1)
ylabel('hip flexion moment')
xlim([0,100])
ylim([-100,100])

subplot(3,1,2)
ylabel('knee extension moment')
xlim([0,100])
ylim([-100,100])

subplot(3,1,3)
ylabel('ankle plantarflexion moment')
xlim([0,100])
ylim([-50,150])

xlabel('percent gait cycle')

% ------------------------------------------------------
% Print to console
disp('Hip Flexion Moment')
disp(['rmsdiff=',num2str(rms_id_cmc(1))])
disp(['rmsdiff norm to peak ID=', num2str(rms_id_cmc_norm(1))])
disp(['peak diff=' num2str(peak_id_cmc(1))])
disp(['peak diff norm to peak ID=', num2str(peak_id_cmc_norm(1))]);
disp(' ')
disp('Knee Extension Moment')
disp(['rmsdiff=',num2str(rms_id_cmc(2))])
disp(['rmsdiff norm to peak ID=', num2str(rms_id_cmc_norm(2))])
disp(['peak diff=' num2str(peak_id_cmc(2))])
disp(['peak diff norm to peak ID=', num2str(peak_id_cmc_norm(2))]);
disp(' ')
disp('Ankle Extension Moment')
disp(['rmsdiff=',num2str(rms_id_cmc(3))])
disp(['rmsdiff norm to peak ID=', num2str(rms_id_cmc_norm(3))])
disp(['peak diff=' num2str(peak_id_cmc(3))])
disp(['peak diff norm to peak ID=', num2str(peak_id_cmc_norm(3))]);

