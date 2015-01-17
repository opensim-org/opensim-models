# Plot the baseline results (muscle Rates and metabolic cost)

# Utils contains tools to browse for files and folders
import org.opensim.utils as utils
import os

# Obtain Directory containing baseline results
#resultsFolderCMC = getInstallDir() + "/Models/gait10dof18musc/CMC/ResultsCMC"
resultsFolderCMC = utils.FileUtils.getInstance().browseForFolder("Select the folder with baseline CMC Results");

# Obtain the legend name
#legendName = "Baseline"
legendName = os.path.split(resultsFolderCMC)[1]

# Plot the total metabolic energy
totalEnergyPlot = createPlotterPanel("Total Metabolic Energy")
src = addDataSource(totalEnergyPlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(totalEnergyPlot, src, "time", "metabolics_TOTAL")
crv.setLegend(legendName)

# Plot the gastrocnemius muscle Rates
GastrocRatePlot = createPlotterPanel("Gastrocnemius Muscle Metabolic Rate (Right)")
src = addDataSource(GastrocRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(GastrocRatePlot, src, "time", "metabolics_gastroc_r")
crv.setLegend(legendName)

# Plot the soleus muscle Rates
SoleusRatePlot = createPlotterPanel("Soleus Muscle Metabolic Rate (Right)")
src = addDataSource(SoleusRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(SoleusRatePlot, src, "time", "metabolics_soleus_r")
crv.setLegend(legendName)

# Plot the tibialis anterior muscle Rates
TibAntRatePlot = createPlotterPanel("Tibialis Anterior Muscle Metabolic Rate (Right)")
src = addDataSource(TibAntRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(TibAntRatePlot, src, "time", "metabolics_tib_ant_r")
crv.setLegend(legendName)

# Plot the iliopsoas metabolic rate
psoasRatePlot = createPlotterPanel("Iliopsoas Muscle Metabolic Rate (Right)")
src = addDataSource(psoasRatePlot, resultsFolderCMC+"/walk_subject_MetabolicsReporter_probes.sto")
crv = addCurve(psoasRatePlot, src, "time", "metabolics_iliopsoas_r")
crv.setLegend(legendName)