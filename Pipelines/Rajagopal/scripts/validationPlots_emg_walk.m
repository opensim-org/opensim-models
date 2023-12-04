% Plot simulated muscle activation vs. EMG signal

% Right Foot Strike (RFS) times
RFS1 = 0.248;
RFS2 = 1.3925;

% ------------------------------------------------------
% Import CMC states file
cmc_results_dir = '../CMC/walk/results';
cmc = importCMCStatesFileToDataset([cmc_results_dir,'/cmc_states.sto']);
cmc.percentgaitcycle = 100.*(cmc.time - RFS1)./(RFS2 - RFS1);
clear cmc_results_dir

% Load emg activity
load('emg_walk.mat');
emg.percentgaitcycle = 100.*(emg.time - RFS1)./(RFS2 - RFS1);
emg = emg(emg.time >= min(cmc.time) & emg.time <= max(cmc.time),:);

% ------------------------------------------------------
% Split data into partial 1st and partial 2nd gait cycle
cmc_1 = cmc(cmc.percentgaitcycle >= 25 & cmc.percentgaitcycle <= 100, :);
cmc_2 = cmc(cmc.percentgaitcycle >= 100 & cmc.percentgaitcycle <= 125, :);
cmc_2.percentgaitcycle = mod(cmc_2.percentgaitcycle, 100);

emg_1 = emg(emg.percentgaitcycle >= 25 & emg.percentgaitcycle <= 100, :);
emg_2 = emg(emg.percentgaitcycle >= 100 & emg.percentgaitcycle <= 125, :);
emg_2.percentgaitcycle = mod(emg_2.percentgaitcycle, 100);

% ------------------------------------------------------
% Plot EMG (cyan) vs. CMC (blue) muscle activity
figure
% ---------------------------------
% GMAX
muscleName = 'gmax';

    emgData_1 = emg_1.GMAX;
    emgData_2 = emg_2.GMAX;

    cmcData_1 = mean([cmc_1.glmax1ractivation, cmc_1.glmax2ractivation, cmc_1.glmax3ractivation], 2);
    cmcData_2 = mean([cmc_2.glmax1ractivation, cmc_2.glmax2ractivation, cmc_2.glmax3ractivation], 2);

    subplot(4,2,1)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% GMED
muscleName = 'gmed';
    emgData_1 = emg_1.GMED;
    emgData_2 = emg_2.GMED;

    cmcData_1 = mean([cmc_1.glmed1ractivation, cmc_1.glmed2ractivation, cmc_1.glmed3ractivation], 2);
    cmcData_2 = mean([cmc_2.glmed1ractivation, cmc_2.glmed2ractivation, cmc_2.glmed3ractivation], 2);

    subplot(4,2,2)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
    
% ---------------------------------
% RECFEM
muscleName = 'recfem';
    emgData_1 = emg_1.RF;
    emgData_2 = emg_2.RF;

    cmcData_1 = cmc_1.recfemractivation;
    cmcData_2 = cmc_2.recfemractivation;

    subplot(4,2,3)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% VASLAT
muscleName = 'vaslat';
    emgData_1 = emg_1.VL;
    emgData_2 = emg_2.VL;

    cmcData_1 = cmc_1.vaslatractivation;
    cmcData_2 = cmc_2.vaslatractivation;

    subplot(4,2,4)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
    
% ---------------------------------
% BFLH
muscleName = 'bflh';
    emgData_1 = emg_1.BF;
    emgData_2 = emg_2.BF;

    cmcData_1 = cmc_1.bflhractivation;
    cmcData_2 = cmc_2.bflhractivation;

    subplot(4,2,5)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% GASLAT
muscleName = 'gaslat';
    emgData_1 = emg_1.GAS;
    emgData_2 = emg_2.GAS;

    cmcData_1 = cmc_1.gaslatractivation;
    cmcData_2 = cmc_2.gaslatractivation;

    subplot(4,2,6)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% TIBANT
muscleName = 'tibant';
    emgData_1 = emg_1.TA;
    emgData_2 = emg_2.TA;

    cmcData_1 = cmc_1.tibantractivation;
    cmcData_2 = cmc_2.tibantractivation;

    subplot(4,2,7)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% SOLEUS
muscleName = 'soleus';
    emgData_1 = emg_1.SOL;
    emgData_2 = emg_2.SOL;

    cmcData_1 = cmc_1.soleusractivation;
    cmcData_2 = cmc_2.soleusractivation;

    subplot(4,2,8)
%     plot(emg_1.percentgaitcycle, emgData_1, 'c', emg_2.percentgaitcycle, emgData_2, 'c'), hold on
    plot(emg_1.percentgaitcycle, emgData_1.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c', emg_2.percentgaitcycle, emgData_2.*(max([cmcData_1;cmcData_2])./max([emgData_1;emgData_2])), 'c'), hold on
    plot(cmc_1.percentgaitcycle, cmcData_1, 'b', cmc_2.percentgaitcycle, cmcData_2, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
