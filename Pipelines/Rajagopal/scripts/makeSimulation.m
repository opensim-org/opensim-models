function makeSimulation(trial)
    curDirWithMatlabScripts = fileparts(mfilename('fullpath'));
    cd([curDirWithMatlabScripts,'/..']);
    simulationHomeDir = cd;
    if strcmpi(trial, 'walk')
        makeSimulation_walk(simulationHomeDir);
    elseif strcmpi(trial, 'run')
        makeSimulation_run(simulationHomeDir);
    else
        warning('fx input must be ''walk'' or ''run''; generating running simulation')
        makeSimulation_run(simulationHomeDir);
    end
    cd(curDirWithMatlabScripts);
end

function makeSimulation_walk(simulationHomeDir)
    import org.opensim.modeling.*
    disp('walk')
    
    % Scale
    cd([simulationHomeDir,'/Scale'])
    system('opensim-cmd run-tool scale_setup_walk_scaleOnly.xml');
    system('opensim-cmd run-tool scale_setup_walk.xml');
    
    % IK
    cd([simulationHomeDir,'/IK'])
    system('opensim-cmd run-tool ik_setup_walk.xml');
    
    % RRA
    cd([simulationHomeDir,'/RRA/walk']);
    
    system('opensim-cmd run-tool rra_setup_walk_1.xml');
    outlog = fileread('opensim.log');
    massChange = str2double(outlog(regexpi(outlog, 'total mass change: ', 'end'):regexpi(outlog, 'total mass change: .?[0-9]+[.][0-9]+', 'end')));
    disp(['walk, rra 1, dMass = ', num2str(massChange)])
    dCOM = outlog(regexpi(outlog, 'Mass Center \(COM\) adjustment:', 'end'):regexpi(outlog, 'Mass Center \(COM\) adjustment: .+]', 'end'));
    disp(['walk, rra 1, dCOM = ', dCOM])
    osimModel_rraMassChanges = Model('subject_walk_rra1.osim');
    osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange);
    osimModel_rraMassChanges.print('subject_walk_rra1.osim');
    
    system('opensim-cmd run-tool rra_setup_walk_2.xml');
    outlog = fileread('opensim.log');
    massChange = str2double(outlog(regexpi(outlog, 'total mass change: ', 'end'):regexpi(outlog, 'total mass change: .?[0-9]+[.][0-9]+', 'end')));
    disp(['walk, rra 2, dMass = ', num2str(massChange)])
    dCOM = outlog(regexpi(outlog, 'Mass Center \(COM\) adjustment:', 'end'):regexpi(outlog, 'Mass Center \(COM\) adjustment: .+]', 'end'));
    disp(['walk, rra 2, dCOM = ', dCOM])
    osimModel_rraMassChanges = Model('subject_walk_rra2.osim');
    osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange);
    osimModel_rraMassChanges.print('subject_walk_rra2.osim');
    
    % Scale muscle forces based on final mass, set vmax
    osimModel_postRRA = scaleOptimalForceSubjectSpecific(osimModel_rraMassChanges, osimModel_rraMassChanges, 1.70, 1.83);
    osimModel_postRRA = setMaxContractionVelocityAllMuscles(osimModel_postRRA, 15.0);
    osimModel_postRRA.print([simulationHomeDir,'/CMC/walk/subject_walk_adjusted.osim']);
    
	%  CMC
    cd([simulationHomeDir,'/CMC/walk']);
    system('opensim-cmd run-tool cmc_setup_walk.xml');
    
    % ID
    cd([simulationHomeDir,'/ID']);
    system('opensim-cmd run-tool id_setup_walk.xml');
    
end

function makeSimulation_run(simulationHomeDir)
    import org.opensim.modeling.*
    disp('run')
    
    % Scale
    cd([simulationHomeDir,'/Scale'])
    system('opensim-cmd run-tool scale_setup_run.xml');
    
    % IK
    cd([simulationHomeDir,'/IK'])
    system('opensim-cmd run-tool ik_setup_run.xml');
    
    % RRA
    cd([simulationHomeDir,'/RRA/run']);
    
    system('opensim-cmd run-tool rra_setup_run_1.xml');
    outlog = fileread('opensim.log');
    massChange = str2double(outlog(regexpi(outlog, 'total mass change: ', 'end'):regexpi(outlog, 'total mass change: .?[0-9]+[.][0-9]+', 'end')));
    disp(['run, rra 1, dMass = ', num2str(massChange)])
    dCOM = outlog(regexpi(outlog, 'Mass Center \(COM\) adjustment:', 'end'):regexpi(outlog, 'Mass Center \(COM\) adjustment: .+]', 'end'));
    disp(['run, rra 1, dCOM = ', dCOM])
    osimModel_rraMassChanges = Model('subject_run_rra1.osim');
    osimModel_rraMassChanges.initSystem();
    osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange);
    osimModel_rraMassChanges.print('subject_run_rra1.osim');
    
    system('opensim-cmd run-tool rra_setup_run_2.xml');
    outlog = fileread('opensim.log');
    massChange = str2double(outlog(regexpi(outlog, 'total mass change: ', 'end'):regexpi(outlog, 'total mass change: .?[0-9]+[.][0-9]+', 'end')));
    disp(['run, rra 2, dMass = ', num2str(massChange)])
    dCOM = outlog(regexpi(outlog, 'Mass Center \(COM\) adjustment:', 'end'):regexpi(outlog, 'Mass Center \(COM\) adjustment: .+]', 'end'));
    disp(['run, rra 2, dCOM = ', dCOM])
    osimModel_rraMassChanges = Model('subject_run_rra2.osim');
    osimModel_rraMassChanges.initSystem();
    osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange);
    osimModel_rraMassChanges.print('subject_run_rra2.osim');
    
    system('opensim-cmd run-tool rra_setup_run_3.xml');
    outlog = fileread('opensim.log');
    massChange = str2double(outlog(regexpi(outlog, 'total mass change: ', 'end'):regexpi(outlog, 'total mass change: .?[0-9]+[.][0-9]+', 'end')));
    disp(['run, rra 3, dMass = ', num2str(massChange)])
    dCOM = outlog(regexpi(outlog, 'Mass Center \(COM\) adjustment:', 'end'):regexpi(outlog, 'Mass Center \(COM\) adjustment: .+]', 'end'));
    disp(['run, rra 3, dCOM = ', dCOM])
    osimModel_rraMassChanges = Model('subject_run_rra3.osim');
    osimModel_rraMassChanges.initSystem();
    osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange);
    osimModel_rraMassChanges.print('subject_run_rra3.osim');
    
    % Scale muscle forces based on final mass, set vmax
    osimModel_postRRA = scaleOptimalForceSubjectSpecific(osimModel_rraMassChanges, osimModel_rraMassChanges, 1.70, 1.78);
    osimModel_postRRA = setMaxContractionVelocityAllMuscles(osimModel_postRRA, 15.0);
    osimModel_postRRA.print([simulationHomeDir,'/CMC/run/subject_run_adjusted.osim']);
    
    % CMC
    cd([simulationHomeDir,'/CMC/run']);
    system('opensim-cmd run-tool cmc_setup_run.xml');
    
    % ID
    cd([simulationHomeDir,'/ID']);
    system('opensim-cmd run-tool id_setup_run.xml');
end

function osimModel_scaledForces = scaleOptimalForceSubjectSpecific(osimModel_generic, osimModel_scaled, height_generic, height_scaled)
    mass_generic = getMassOfModel(osimModel_generic);
    mass_scaled = getMassOfModel(osimModel_scaled);
    
    Vtotal_generic = 47.05 * mass_generic * height_generic + 1289.6;
    Vtotal_scaled = 47.05 * mass_scaled * height_scaled + 1289.6;
    
    allMuscles_generic = osimModel_generic.getMuscles();
    allMuscles_scaled = osimModel_scaled.getMuscles();
    
    for i=0:allMuscles_generic.getSize()-1
        currentMuscle_generic = allMuscles_generic.get(i);
        currentMuscle_scaled = allMuscles_scaled.get(i);
        
        lmo_generic = currentMuscle_generic.getOptimalFiberLength();
        lmo_scaled = currentMuscle_scaled.getOptimalFiberLength();
        
        forceScaleFactor = (Vtotal_scaled/Vtotal_generic)/(lmo_scaled/lmo_generic);
        
        currentMuscle_scaled.setMaxIsometricForce( forceScaleFactor * currentMuscle_generic.getMaxIsometricForce() );
    end
    
    osimModel_scaledForces = osimModel_scaled;    
end

function osimModel_scaledForces = scaleOptimalForce_constant(osimModel_generic, osimModel_scaled, scaleFactor)
    allMuscles_generic = osimModel_generic.getMuscles();
    allMuscles_scaled = osimModel_scaled.getMuscles();
    
    for i=0:allMuscles_generic.getSize()-1
        currentMuscle_generic = allMuscles_generic.get(i);
        currentMuscle_scaled = allMuscles_scaled.get(i);
        currentMuscle_scaled.setMaxIsometricForce( scaleFactor * currentMuscle_generic.getMaxIsometricForce() );
    end
    
    osimModel_scaledForces = osimModel_scaled;    
end

function osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel, massChange)
    currTotalMass = getMassOfModel(osimModel);
    suggestedNewTotalMass = currTotalMass + massChange;
    massScaleFactor = suggestedNewTotalMass/currTotalMass;
    
    allBodies = osimModel.getBodySet();
    for i = 0:allBodies.getSize()-1
        currBodyMass = allBodies.get(i).getMass();
        newBodyMass = currBodyMass*massScaleFactor;
        allBodies.get(i).setMass(newBodyMass);
    end
    osimModel_rraMassChanges = osimModel;
end

function totalMass = getMassOfModel(osimModel)
    totalMass = 0;
    allBodies = osimModel.getBodySet();
    for i=0:allBodies.getSize()-1
        curBody = allBodies.get(i);
        totalMass = totalMass + curBody.getMass();
    end
end

function osimModel_vmax = setMaxContractionVelocityAllMuscles(osimModel, maxContractionVelocity)
    Muscles = osimModel.getMuscles();
    numMuscles = Muscles.getSize();
    
    for i = 0:numMuscles-1
        currentMuscle = Muscles.get(i);
        currentMuscle.setMaxContractionVelocity(maxContractionVelocity);
    end
    
    osimModel_vmax = osimModel;
end