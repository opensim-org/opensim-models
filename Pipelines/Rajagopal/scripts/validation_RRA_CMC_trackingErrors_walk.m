% Track max translational and rotational positional errors 
% from IK -> RRA kinematics, and RRA -> CMC kinematics

% subsets of coordinates
pelvis_trans = {'pelvistx', 'pelvisty', 'pelvistz'};
pelvis_rot = {'pelvistilt', 'pelvislist', 'pelvisrotation'};
lumbar = {'lumbarextension', 'lumbarbending', 'lumbarrotation'};
le = {'hipflexionr', 'hipadductionr', 'hiprotationr', 'kneeangler', 'ankleangler',...
      'hipflexionl', 'hipadductionl', 'hiprotationl', 'kneeanglel', 'ankleanglel'};
ue = {'armflexr', 'armaddr', 'armrotr', 'elbowflexr', 'prosupr', ...
      'armflexl', 'armaddl', 'armrotl', 'elbowflexl', 'prosupl'};

% load ik/rra kinematic errors
rra_results_dir = '../RRA/walk/results_rra_2';
rra_walk_pErr = importPErrStoFile([rra_results_dir, '/rra_walk_2_pErr.sto']);
rra_walk_pErr_pelvisTrans = double(rra_walk_pErr(:,pelvis_trans));
rra_walk_pErr_pelvisRot = double(rra_walk_pErr(:,pelvis_rot));
rra_walk_pErr_lumbarRot = double(rra_walk_pErr(:,lumbar));
rra_walk_pErr_leRot = double(rra_walk_pErr(:,le));
rra_walk_pErr_ueRot = double(rra_walk_pErr(:,ue));

% print to console
disp('walking ik/rra errors')
disp('max rms pelvis error')
disp(['   ', num2str(100*max(rms(rra_walk_pErr_pelvisTrans,1))), ' (trans, cm)'])
disp(['   ', num2str(100*max(rms(rra_walk_pErr_pelvisRot,1))), ' (rot, deg)'])
disp('max rms lumbar error')
disp(['   ', num2str(100*max(rms(rra_walk_pErr_lumbarRot,1))), ' (deg)'])
disp('max rms LE error')
disp(['   ', num2str(100*max(rms(rra_walk_pErr_leRot,1))), ' (deg)'])
disp('max rms UE error')
disp(['   ', num2str(100*max(rms(rra_walk_pErr_ueRot,1))), ' (deg)'])
disp(' ')

disp('max pelvis error')
disp(['   ', num2str(100*max(max(abs(rra_walk_pErr_pelvisTrans)))), ' (trans, cm)'])
disp(['   ', num2str(180/pi*max(max(abs(rra_walk_pErr_pelvisRot)))), ' (rot, deg)'])
disp('max lumbar error')
disp(['   ', num2str(180/pi*max(max(abs(rra_walk_pErr_lumbarRot)))), ' (rot, deg)'])
disp('max LE error')
disp(['   ', num2str(180/pi*max(max(abs(rra_walk_pErr_leRot)))), ' (rot, deg)'])
disp('max UE error')
disp(['   ', num2str(180/pi*max(max(abs(rra_walk_pErr_ueRot)))), ' (rot, deg)'])
disp(' ')

% load rra/cmc kinematic errors
cmc_results_dir = '../CMC/walk/results';
cmc_walk_pErr = importPErrStoFile([cmc_results_dir, '/cmc_pErr.sto']);
cmc_walk_pErr_pelvisTrans = double(cmc_walk_pErr(:,pelvis_trans));
cmc_walk_pErr_pelvisRot = double(cmc_walk_pErr(:,pelvis_rot));
cmc_walk_pErr_lumbarRot = double(cmc_walk_pErr(:,lumbar));
cmc_walk_pErr_leRot = double(cmc_walk_pErr(:,le));
cmc_walk_pErr_ueRot = double(cmc_walk_pErr(:,ue));

% print to console
disp('walking rra/cmc errors')
disp('max rms pelvis error')
disp(['   ', num2str(100*max(rms(cmc_walk_pErr_pelvisTrans,1))), ' (trans, cm)'])
disp(['   ', num2str(100*max(rms(cmc_walk_pErr_pelvisRot,1))), ' (rot, deg)'])
disp('max rms lumbar error')
disp(['   ', num2str(100*max(rms(cmc_walk_pErr_lumbarRot,1))), ' (deg)'])
disp('max rms LE error')
disp(['   ', num2str(100*max(rms(cmc_walk_pErr_leRot,1))), ' (deg)'])
disp('max rms UE error')
disp(['   ', num2str(100*max(rms(cmc_walk_pErr_ueRot,1))), ' (deg)'])
disp(' ')

% print to console
disp('walking rra/cmc errors')
disp('max pelvis error')
disp(['   ', num2str(100*max(max(abs(cmc_walk_pErr_pelvisTrans)))), ' (trans, cm)'])
disp(['   ', num2str(180/pi*max(max(abs(cmc_walk_pErr_pelvisRot)))), ' (rot, deg)'])
disp('max lumbar error')
disp(['   ', num2str(180/pi*max(max(abs(cmc_walk_pErr_lumbarRot)))), ' (rot, deg)'])
disp('max LE error')
disp(['   ', num2str(180/pi*max(max(abs(cmc_walk_pErr_leRot)))), ' (rot, deg)'])
disp('max UE error')
disp(['   ', num2str(180/pi*max(max(abs(cmc_walk_pErr_ueRot)))), ' (rot, deg)'])
disp(' ')