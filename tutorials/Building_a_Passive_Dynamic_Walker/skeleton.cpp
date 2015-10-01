//==============================================================================
//The OpenSim Main header must be included in all files
#include <OpenSim/OpenSim.h>
// Set the namespace to shorten the declarations
// Note: Several classes appear in both namespaces and require using the full name
using namespace OpenSim;
using namespace SimTK;
//______________________________________________________________________________
/**
 * 
 */
int main()
{
    try {
        // TODO: Add Code to Begin Model here
        // ********** BEGIN CODE **********
 
 
        // **********  END CODE  **********
    }
    catch (OpenSim::Exception ex)
    {
        std::cout << ex.getMessage() << std::endl;
        return 1;
    }
    catch (SimTK::Exception::Base ex)
    {
        std::cout << ex.getMessage() << std::endl;
        return 1;
    }
    catch (std::exception ex)
    {
        std::cout << ex.what() << std::endl;
        return 1;
    }
    catch (...)
    {
        std::cout << "UNRECOGNIZED EXCEPTION" << std::endl;
        return 1;
    }
    std::cout << "OpenSim example completed successfully" << std::endl;
    std::cout << "Press return to continue" << std::endl;
    std::cin.get();
    return 0;
 } 