% Plot simulated muscle activation vs. EMG signal

% Right Foot Strike (RFS) times
RFS1 = 0.863;
RFS2 = 1.546;

% ------------------------------------------------------
% Import CMC states file
cmc_results_dir = '../CMC/run/results';
cmc = importCMCStatesFileToDataset([cmc_results_dir,'/cmc_states.sto']);
cmc.percentgaitcycle = 100.*(cmc.time - RFS1)./(RFS2 - RFS1);
clear cmc_results_dir

% Load emg activity
load('emg_run.mat');
emg.percentgaitcycle = 100.*(emg.time - RFS1)./(RFS2 - RFS1);
emg = emg(emg.time >= min(cmc.time) & emg.time <= max(cmc.time),:);

% ------------------------------------------------------
% Plot EMG (cyan) vs. CMC (blue) muscle activity
figure
% ---------------------------------
% GMAX
muscleName = 'gmax';

    emgData = emg.GMAX;
    cmcData = mean([cmc.glmax1ractivation, cmc.glmax2ractivation, cmc.glmax3ractivation], 2);
    
    subplot(4,2,1)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% GMED
muscleName = 'gmed';
    emgData = emg.GMED;
    cmcData = mean([cmc.glmed1ractivation, cmc.glmed2ractivation, cmc.glmed3ractivation], 2);

    subplot(4,2,2)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
    
% ---------------------------------
% RECFEM
muscleName = 'recfem';
    emgData = emg.RF;
    cmcData = cmc.recfemractivation;
    
    subplot(4,2,3)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% VASLAT
muscleName = 'vaslat';
    emgData = emg.VL;
    cmcData = cmc.vaslatractivation;
    
    subplot(4,2,4)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
    
% ---------------------------------
% BFLH
muscleName = 'bflh';
    emgData = emg.BFLH;
    cmcData = cmc.bflhractivation;
    
    subplot(4,2,5)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% GASLAT
muscleName = 'gaslat';
    emgData = emg.GASLAT;
    cmcData = cmc.gaslatractivation;
    
    subplot(4,2,6)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% TIBANT
muscleName = 'tibant';
    emgData = emg.TA;
    cmcData = cmc.tibantractivation;
    
    subplot(4,2,7)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])

% ---------------------------------
% SOLEUS
muscleName = 'soleus';
    emgData = emg.SOL;
    cmcData = cmc.soleusractivation;
    
    subplot(4,2,8)
%     plot(emg.percentgaitcycle, emgData, 'c'), hold on
    plot(emg.percentgaitcycle, emgData.*(max(cmcData)./max(emgData)), 'c'), hold on
    plot(cmc.percentgaitcycle, cmcData, 'b'), hold on
    
    title(muscleName)
    xlim([0,100])
    ylim([0,1])
