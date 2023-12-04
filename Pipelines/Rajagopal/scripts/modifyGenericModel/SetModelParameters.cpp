#include <OpenSim/OpenSim.h>
#include <ctime>    // for clock()
#include "SetModelParameters.h"

using namespace OpenSim;
using namespace SimTK;
using namespace std;


int main()
{
    clock_t startTime = clock();

	try {
         /* ----------------------- RUNNING 4 m/s ----------------------- */
        
		/* -------------------------------------------------------------
           Mass adjustments with the RRA tool
           ------------------------------------------------------------- */
        // RUN RRA ROUND 1
        /*
         Model* osimModel = new Model("DOWNLOAD_DIR/RRA/run/subject_run_rra1.osim");
        
        double rraSuggMassChange = 0.49989;
        setMassOfBodiesUsingRRAMassChange(osimModel, rraSuggMassChange);
        osimModel->print("DOWNLOAD_DIR/RRA/run/subject_run_rra1.osim");
        */
        
        // RUN RRA ROUND 2
        /*
        Model* osimModel = new Model("DOWNLOAD_DIR/RRA/run/subject_run_rra2.osim");
        
        double rraSuggMassChange = -0.010818;
        setMassOfBodiesUsingRRAMassChange(osimModel, rraSuggMassChange);
        osimModel->print("DOWNLOAD_DIR/RRA/run/subject_run_rra2.osim");
        */
        
        // RUN RRA ROUND 3
        /*
        Model* osimModel = new Model("DOWNLOAD_DIR/RRA/run/subject_run_rra3.osim");
        
        double rraSuggMassChange = 0.067014;
        setMassOfBodiesUsingRRAMassChange(osimModel, rraSuggMassChange);
        osimModel->print("DOWNLOAD_DIR/RRA/run/subject_run_rra3.osim");
        */
        
        /* -------------------------------------------------------------
           Adjust model forces after RRA completes, use mass-height-volume relationship
           ------------------------------------------------------------- */
        /*
        Model* osimModel = new Model("DOWNLOAD_DIR/RRA/run/subject_run_rra3.osim");
        Model* osimModelUpd = new Model("DOWNLOAD_DIR/RRA/run/subject_run_rra3.osim");
        
        double heightOriginal = 1.70; // m
        double heightNew = 1.78; // m
        scaleOptimalForceSubjectSpecific( osimModel, osimModelUpd, heightOriginal,  heightNew );
        setMaxContractionVelocityAllMuscles(osimModelUpd,15.0);

        osimModelUpd->print("DOWNLOAD_DIR/CMC/run/subject_run_adjusted.osim");
        */
        
        
        /* ---------------------- WALKING FREE SPEED ------------------- */
        
        /* -------------------------------------------------------------
           Mass adjustments with the RRA tool
           ------------------------------------------------------------- */
        // WALK RRA ROUND 1
        /*
         Model* osimModel = new Model("DOWNLOAD_DIR/RRA/walk/subject01_walk_rra1.osim");
         
         double rraSuggMassChange = -0.028293;
         setMassOfBodiesUsingRRAMassChange(osimModel, rraSuggMassChange);
         osimModel->print("DOWNLOAD_DIR/RRA/walk/subject_walk_rra1.osim");
        */
        
        // WALK RRA ROUND 2
        /*
         Model* osimModel = new Model("DOWNLOAD_DIR/RRA/walk/subject_walk_rra2.osim");
         
         double rraSuggMassChange = 0.011891;
         setMassOfBodiesUsingRRAMassChange(osimModel, rraSuggMassChange);
         osimModel->print("DOWNLOAD_DIR/RRA/walk/subject_walk_rra2.osim");
        */
        
        /* -------------------------------------------------------------
         Adjust model forces after RRA completes, use mass-height-volume relationship
         ------------------------------------------------------------- */
        /*
         Model* osimModel = new Model("DOWNLOAD_DIR/RRA/walk/subject_walk_rra2.osim");
         Model* osimModelUpd = new Model("DOWNLOAD_DIR/RRA/walk/subject_walk_rra2.osim");
         
         double heightOriginal = 1.70; // m
         double heightNew = 1.83; // m
         scaleOptimalForceSubjectSpecific( osimModel, osimModelUpd, heightOriginal,  heightNew );
         setMaxContractionVelocityAllMuscles(osimModelUpd,15.0);
         
         osimModelUpd->print("DOWNLOAD_DIR/CMC/walk/subject_walk_adjusted.osim");
        */
        
    }
	catch (const std::exception& ex)
    {
        cerr << ex.what() << endl;
        return 1;
    }
    catch (...)
    {
        cerr << "UNRECOGNIZED EXCEPTION" << endl;
        return 1;
    }

    cout << "main() routine time = " << 1.e3*(clock()-startTime)/CLOCKS_PER_SEC << "ms\n";

    cout << "OpenSim example completed successfully." << endl;

	return 0;
}


