% walk, free-speed
id_results_dir = '../ID/results_run';
cmc_results_dir = '../CMC/run/results';

% Right Foot Strike (RFS) times
RFS1 = 0.863;
RFS2 = 1.546;

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

% % ------------------------------------------------------
% % Split data into partial 1st and partial 2nd gait cycle
% idJointMoments_1 = idJointMoments(idJointMoments.percentgaitcycle <= 100,:);
% idJointMoments_2 = idJointMoments(idJointMoments.percentgaitcycle >= 100,:);
% idJointMoments_2.percentgaitcycle = mod(idJointMoments_2.percentgaitcycle,100);
% 
% cmcJointMoments_1 = cmcJointMoments(cmcJointMoments.percentgaitcycle <= 100,:);
% cmcJointMoments_2 = cmcJointMoments(cmcJointMoments.percentgaitcycle >= 100,:);
% cmcJointMoments_2.percentgaitcycle = mod(cmcJointMoments_2.percentgaitcycle,100);

% ------------------------------------------------------
% Compute values of ID and CMC joint moments per 1% gait cycle
idJointMoments_interp = dataset({(0:1:100)', 'percentgaitcycle'});
idJointMoments_interp.hipflex = interp1(idJointMoments.percentgaitcycle, idJointMoments.hipflex, idJointMoments_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_interp.kneeext = interp1(idJointMoments.percentgaitcycle, idJointMoments.kneeext, idJointMoments_interp.percentgaitcycle, 'linear', 'extrap');
idJointMoments_interp.ankleext = interp1(idJointMoments.percentgaitcycle, idJointMoments.ankleext, idJointMoments_interp.percentgaitcycle, 'linear', 'extrap');

cmcJointMoments_interp = dataset({(0:1:100)', 'percentgaitcycle'});
cmcJointMoments_interp.hipflex = interp1(cmcJointMoments.percentgaitcycle, cmcJointMoments.hipflex, cmcJointMoments_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_interp.kneeext = interp1(cmcJointMoments.percentgaitcycle, cmcJointMoments.kneeext, cmcJointMoments_interp.percentgaitcycle, 'linear', 'extrap');
cmcJointMoments_interp.ankleext = interp1(cmcJointMoments.percentgaitcycle, cmcJointMoments.ankleext, cmcJointMoments_interp.percentgaitcycle, 'linear', 'extrap');

% ------------------------------------------------------
% Compute RMS and peak errors between CMC and muscle-generated joint moments
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
plot(idJointMoments_interp.percentgaitcycle, idJointMoments_interp.hipflex, 'b'), hold on

subplot(3,1,2)
plot(idJointMoments_interp.percentgaitcycle, idJointMoments_interp.kneeext, 'b'), hold on

subplot(3,1,3)
plot(idJointMoments_interp.percentgaitcycle, idJointMoments_interp.ankleext, 'b'), hold on

% ------------------------------------------------------
% Plot CMC muscle-generated joint moments
subplot(3,1,1)
plot(cmcJointMoments_interp.percentgaitcycle, cmcJointMoments_interp.hipflex, 'r'), hold on

subplot(3,1,2)
plot(cmcJointMoments_interp.percentgaitcycle, cmcJointMoments_interp.kneeext, 'r'), hold on

subplot(3,1,3)
plot(cmcJointMoments_interp.percentgaitcycle, cmcJointMoments_interp.ankleext, 'r'), hold on

% ------------------------------------------------------
% Label plots
subplot(3,1,1)
ylabel('hip flexion moment')
xlim([0,100])
ylim([-200,150])

subplot(3,1,2)
ylabel('knee extension moment')
xlim([0,100])
ylim([-100,250])

subplot(3,1,3)
ylabel('ankle plantarflexion moment')
xlim([0,100])
ylim([-50,300])

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

