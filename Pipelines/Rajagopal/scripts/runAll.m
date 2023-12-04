% Make walking simulations, and generate
%   (1) muscle-generated vs. inverse dynamics joint moments
%   (2) simulated muscle activity vs. emg
makeSimulation('walk')
validationPlots_emg_walk
validationPlots_id_walk
validation_RRA_CMC_trackingErrors_walk

% Make running simulations, and generate
%   (1) muscle-generated vs. inverse dynamics joint moments
%   (2) simulated muscle activity vs. emg
makeSimulation('run')
validationPlots_emg_run
validationPlots_id_run
validation_RRA_CMC_trackingErrors_run