/** ---------------------------------------------------------------
  *  Contains a general set of tools to modify a model
  * --------------------------------------------------------------- */

using namespace OpenSim;
using namespace std;
using namespace SimTK;


// INCLUDE
#include <OpenSim/OpenSim.h>


//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *   Sets the following active force-length curve parameters
 *     Minimum normalized active fiber length
 *     Transition normalized fiber length
 *     Maximum normalized active fiber length
 *     Shallow ascending slope
 *     Minimum normalized force
 * Input:  originalModel (.osim model)
 * Output: newModel (.osim model)
 */
void setActiveForceLengthCurveParametersAllMuscles( Model* osimModel, double minNormActiveFiberLength, double transNormFiberLength, double maxNormActiveFiberLength, double shallowAscendingSlope, double minNormForce )
{
    Set<Muscle>& allMuscles = osimModel->updMuscles();
    int numMuscles = allMuscles.getSize();
    cout << "\nNumber of muscles: " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles; i++) {
        //Muscle& currMuscle = allMuscles.get(i);
        Millard2012EquilibriumMuscle* currMuscle = static_cast<Millard2012EquilibriumMuscle*>(&allMuscles.get(i));
        
        ActiveForceLengthCurve currCurve = currMuscle->getActiveForceLengthCurve();
        
        cout << "\nCurrent muscle: " << currMuscle->getName() << endl;
        
        cout << "\t current min norm active fiber length: " << currCurve.get_min_norm_active_fiber_length() << endl;
        currCurve.set_min_norm_active_fiber_length(minNormActiveFiberLength);
        
        cout << "\t current transition norm fiber length: " << currCurve.get_transition_norm_fiber_length() << endl;
        currCurve.set_transition_norm_fiber_length(transNormFiberLength);
        
        cout << "\t current max norm active fiber length:  " << currCurve.get_max_norm_active_fiber_length() << endl;
        currCurve.set_max_norm_active_fiber_length(maxNormActiveFiberLength);
        
        cout << "\t current shallow ascending slope: " << currCurve.get_shallow_ascending_slope() << endl;
        currCurve.set_shallow_ascending_slope(shallowAscendingSlope);
        
        cout << "\t current min norm force: " << currCurve.get_minimum_value() << endl;
        currCurve.set_minimum_value(minNormForce);
    }
}


//______________________________________________________________________________
/**
 * For each left muscle in the original model,
 *   set max isometric force, tendon slack length, optimal fiber length, and
 *   pennation angle at optimal fibe rlength to be the same as that of the right 
 *   muscle
 * ASSUMES THAT FOR THE N MUSCLES IN THE MODEL, MUSCLES INDEXED 0 to N/2-1 ARE THE RIGHT MUSCLES
 * AND MUSCLES INDEXED N/2 to N-1 ARE THE LEFT MUSCLES IN THE SAME ORDER
 * Input:  originalModel (.osim model)
 * Output: newModel (.osim model)
 */
void setPropertiesOfLeftMusclesBasedOnRightMuscles( Model* osimModel )
{
    Set<Muscle>& allMuscles = osimModel->updMuscles();
    int numMuscles = allMuscles.getSize();
    cout << "\nNumber of muscles:  " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles/2; i++) {
        Muscle& rightMuscle = allMuscles.get(i);
        Muscle& leftMuscle = allMuscles.get(i+numMuscles/2);
        leftMuscle.setMaxIsometricForce( rightMuscle.getMaxIsometricForce() );
        leftMuscle.setTendonSlackLength( rightMuscle.getTendonSlackLength() );
        leftMuscle.setOptimalFiberLength( rightMuscle.getOptimalFiberLength() );
        leftMuscle.setPennationAngleAtOptimalFiberLength( rightMuscle.getPennationAngleAtOptimalFiberLength() );
        
        cout << "\n";
        cout << rightMuscle.getName() << "\t" << rightMuscle.getMaxIsometricForce() << "\t" << rightMuscle.getTendonSlackLength() << rightMuscle.getOptimalFiberLength() << "\t" << rightMuscle.getPennationAngleAtOptimalFiberLength() << endl;
        cout <<  leftMuscle.getName() << "\t" <<  leftMuscle.getMaxIsometricForce() << "\t" << leftMuscle.getTendonSlackLength() << leftMuscle.getOptimalFiberLength() << "\t" << leftMuscle.getPennationAngleAtOptimalFiberLength()  << endl;
    }
    
}


//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *   if (tendon slack length) / (optimal fiber length) < rigidTendonRatio
 *   set ignore_tendon_compliance to true for that muscle
 * Input:  originalModel (.osim model)
 * Output: newModel (.osim model)
 */
void setRigidTendonBasedOnLtsToLmoRatio( Model* osimModel, double ratioForRigidTendon )
{
    Set<Muscle>& allMuscles= osimModel->updMuscles();
    int numMuscles = allMuscles.getSize();
    cout << "\nNumber of Muscles:  " << numMuscles << endl;
    
    double lts;
    double lmo;
    double ratio;
    int numRigidTendon = 0;
    
    for (int i = 0; i < numMuscles; i++) {
        Muscle& currentMuscle = allMuscles.get(i);
        lts = currentMuscle.getTendonSlackLength();
        lmo = currentMuscle.getOptimalFiberLength();
        ratio = lts/lmo;
        // cout << "\nMuscle:  " << currentMuscle.getName();
        // cout << "\n\tlts = " << lts;
        // cout << "\n\tlmo = " << lmo;
        // cout << "\n\tratio = " << ratio;
        if (ratio <= ratioForRigidTendon) {
            currentMuscle.set_ignore_tendon_compliance(true);
            cout << "\n RT Muscle:  " << currentMuscle.getName() << endl;
            numRigidTendon++;
        }
        else
        {
            currentMuscle.set_ignore_tendon_compliance(false);
        }
    }
    cout << "\nNumber of rigid tendon muscles:  " << numRigidTendon << endl;
}


//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *   use tag use_fiber_damping to true/false (specified in useFiberDamping)
 */
void setFiberDampingAllMuscles( Model* osimModel, double fiberDamping )
{
    Set<Muscle>& Muscles= osimModel->updMuscles();
    int numMuscles = Muscles.getSize();
    cout << "\nNumber of Muscles:  " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles; i++) {
        Millard2012EquilibriumMuscle& currentMuscle = dynamic_cast<Millard2012EquilibriumMuscle&>(Muscles.get(i));
        currentMuscle.setFiberDamping(fiberDamping);
    }
}

//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *   
 */
void modifyPassiveFLCurveAllMuscles( Model* osimModel, double strainAtZeroForce, double strainAtOneNormForce )
{
    Set<Muscle>& Muscles= osimModel->updMuscles();
    int numMuscles = Muscles.getSize();
    cout << "\nNumber of Muscles:  " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles; i++) {
        Millard2012EquilibriumMuscle& currentMuscle = dynamic_cast<Millard2012EquilibriumMuscle&>(Muscles.get(i));
        currentMuscle.upd_FiberForceLengthCurve().set_strain_at_zero_force(strainAtZeroForce);
        currentMuscle.upd_FiberForceLengthCurve().set_strain_at_one_norm_force(strainAtOneNormForce);
        currentMuscle.upd_FiberForceLengthCurve().ensureCurveUpToDate();
    }
}


//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *
 */
void setDefaultActivationOfAllMuscles( Model* osimModel, double defaultAct )
{
    Set<Muscle>& Muscles= osimModel->updMuscles();
    int numMuscles = Muscles.getSize();
    cout << "\nNumber of Muscles:  " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles; i++) {
        Millard2012EquilibriumMuscle& currentMuscle = dynamic_cast<Millard2012EquilibriumMuscle&>(Muscles.get(i));
        currentMuscle.setDefaultActivation(defaultAct);
    }
}


//______________________________________________________________________________
/**
 * For each muscle in the original model,
 *
 */
void setMaxContractionVelocityAllMuscles( Model* osimModel, double maxContractionVelocity )
{
    Set<Muscle>& Muscles= osimModel->updMuscles();
    int numMuscles = Muscles.getSize();
    cout << "\nNumber of Muscles:  " << numMuscles << endl;
    
    for (int i = 0; i < numMuscles; i++) {
        Millard2012EquilibriumMuscle& currentMuscle = dynamic_cast<Millard2012EquilibriumMuscle&>(Muscles.get(i));
        currentMuscle.setMaxContractionVelocity(maxContractionVelocity);
    }
}


//______________________________________________________________________________
/**
 * Add up masses of all bodies to get total mass of model
 * Standard, unscaled model should have mass of 75.337 kg and height of 170 cm (approx)
 */
double getMassOfModel( Model* osimModel )
{
    const BodySet& allBodies = osimModel->getBodySet();
    double totalMass = 0.0;
    for (int i = 0; i < allBodies.getSize(); i++) {
        totalMass += allBodies.get(i).getMass();
    }

    cout << "sum masses of all bodies in model, total mass = " << totalMass << endl;
    
    return totalMass;
}


//______________________________________________________________________________
/**
 * Add up masses of all bodies to get total mass of model
 * Get mass of a starting model, and the recommended mass change from RRA
 * RRA recommends preserving the mass distribution
 */
void setMassOfBodiesUsingRRAMassChange( Model* osimModel, double massChange )
{
    double currTotalMass = getMassOfModel(osimModel);
    double suggestedNewTotalMass = currTotalMass + massChange;
    double massScaleFactor = suggestedNewTotalMass/currTotalMass;
    double currBodyMass, newBodyMass;
    
    BodySet& allBodies = osimModel->updBodySet();
    for (int i = 0; i < allBodies.getSize(); i++) {
        currBodyMass = allBodies.get(i).getMass();
        newBodyMass = currBodyMass*massScaleFactor;
        allBodies.get(i).setMass(newBodyMass);
        
        cout << allBodies.get(i).getName() << " orig mass = " << currBodyMass << "\t new mass = " << newBodyMass << endl;
    }
    
}



//______________________________________________________________________________
/**
 * Scale optimal force of all muscles by a constant
 * Useful if you want to change the specific tension used to scale all muscles, for example
 */
void scaleOptimalForceByConstant( Model* osimModel, double forceScaleFactor)
{
    Set<Muscle>& allMuscles = osimModel->updMuscles();
    for (int i = 0; i < allMuscles.getSize() ; i++) {
        Muscle& currentMuscle = allMuscles.get(i);
        currentMuscle.setMaxIsometricForce( forceScaleFactor*currentMuscle.getMaxIsometricForce() );
    }
}


//______________________________________________________________________________
/**
 * Scale optimal force of all muscles using subject-specific mass, height:
 *   Vtotal   = 47.05 * m * h + 1289.6  (Blemker 2012)
 *   Vmuscle  = Vtotal * VolumeFraction  (Blemker 2012)
 *   PCSAmuscle = Vmuscle / Lmo
 *   Fmo = PCSAmuscle * specificTension
 *       = ((47.05 * m * h + 1289.6) * VolumeFraction / Lmo) * specificTension
 * INPUT:
 *   heightOriginal (m) and heightNew (m)
 *   originalModel (generic), newModel (post-OpenSim scale)
 * To calculate optimal force for a new model given a generic model
 *   Fmo_new = Fmo_original * ( Vtotal_new / Vtotal_original) / (Lmo_new/Lmo_original)
 */
void scaleOptimalForceSubjectSpecific( Model* originalModel, Model* newModel, double heightOriginal, double heightNew )
{
    double massOriginal = getMassOfModel( originalModel );
    double massNew = getMassOfModel( newModel );
    
    double VtotalOriginal = 47.05 * massOriginal * heightOriginal + 1289.6;
    double VtotalNew = 47.05 * massNew * heightNew + 1289.6;
    
    double lmoOriginal, lmoNew, forceScaleFactor;
    
    const Set<Muscle>& allMusclesOriginal = originalModel->getMuscles();
    Set<Muscle>& allMusclesNew = newModel->updMuscles();
    
    for (int i = 0; i < allMusclesOriginal.getSize(); i++ ) {
        Muscle& currentMuscleOriginal = allMusclesOriginal.get(i);
        Muscle& currentMuscleNew = allMusclesNew.get(i);
        
        lmoOriginal = currentMuscleOriginal.getOptimalFiberLength();
        lmoNew = currentMuscleNew.getOptimalFiberLength();
        
        forceScaleFactor = (VtotalNew/VtotalOriginal)/(lmoNew/lmoOriginal);
        
        currentMuscleNew.setMaxIsometricForce( forceScaleFactor * currentMuscleOriginal.getMaxIsometricForce() );
        
        cout << endl << currentMuscleNew.getName() << endl;
        cout << "max isometric force: " << currentMuscleNew.getMaxIsometricForce() << endl;
        cout << "force scaled by: " << forceScaleFactor << endl;
    }
}


//______________________________________________________________________________
/**
 * Print out tab-delimited text file with muscle properties
 *   Muscle name (abbreviation in model)
 *   PCSA (cm^2)
 *   Muscle volume (cm^3)
 *   Peak force (N)
 *   Optimal fiber length (cm)
 *   Tendon slack length (cm)
 *   Pennation angle (degrees)
 *   Rigid tendon approximation used?  (yes/no)
 *
 * NOTE: not all properties printed above are native to the muscle
 *   PCSA = Fmo / specificTension
 *   Muscle volume = PCSA * Lmo
 */
void printMusclePropertiesToFile( Model* osimModel, double specificTensionUsedInNewtonPerCmSquared )
{
    
    ofstream musclePropertiesFile( "musclePropertiesFile.txt", ofstream::out );
    
    musclePropertiesFile << "Muscle" << "\t" << "PCSA (cm^2)" << "\t" << "Muscle Volume (cm^3)" << "\t" << "Peak force (N)" << "\t" << "Optimal fiber length (cm)" << "\t" << "Tendon slack length (cm)" << "\t" << "Pennation angle (degrees)" << "\t" << "Rigid tendon approximation used" << "\t" << "Fiber damping used" << endl;
    musclePropertiesFile << "-----------------------------------------------------------------------------------------------"<< endl;
    
    const Set<Muscle>& allMuscles = osimModel->getMuscles();
    double mTOcm = 100.0;
    double radTOdeg = SimTK_RADIAN_TO_DEGREE;
    
    string muscleName, rigidTendonYesNo;
    double peakForceInNewtons, optFiberLengthInCm, tendonSlackLengthInCm, pennationAngleInDeg, PCSAInCm2, volumeInCm3, fiberDamping;
    bool rigidTendon;
    
    for (int i = 0; i < allMuscles.getSize(); i++) {
        Millard2012EquilibriumMuscle& currentMuscle = dynamic_cast<Millard2012EquilibriumMuscle&>(allMuscles.get(i));
        
        muscleName = currentMuscle.getName();
        peakForceInNewtons = currentMuscle.getMaxIsometricForce();
        optFiberLengthInCm = currentMuscle.getOptimalFiberLength() * mTOcm;
        tendonSlackLengthInCm = currentMuscle.getTendonSlackLength() * mTOcm;
        pennationAngleInDeg = currentMuscle.getPennationAngleAtOptimalFiberLength() * radTOdeg;
        rigidTendon = currentMuscle.get_ignore_tendon_compliance();
            if (rigidTendon) { rigidTendonYesNo = "yes"; }
            else { rigidTendonYesNo = "no";}
        PCSAInCm2 = peakForceInNewtons / specificTensionUsedInNewtonPerCmSquared;
        volumeInCm3 = PCSAInCm2*optFiberLengthInCm;
        fiberDamping = currentMuscle.getFiberDamping();
        
        musclePropertiesFile << muscleName << "\t" << PCSAInCm2 << "\t" << volumeInCm3 << "\t" << peakForceInNewtons << "\t" << optFiberLengthInCm << "\t" << tendonSlackLengthInCm << "\t" << pennationAngleInDeg << "\t" << rigidTendonYesNo << "\t" << fiberDamping << endl;
        
    }
    
    musclePropertiesFile.close();
    
}