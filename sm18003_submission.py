
#!/usr/bin/python

from __future__ import print_function
from hepdata_lib import Variable, Uncertainty
from hepdata_lib import Uncertainty
from hepdata_lib import RootFileReader

import hepdata_lib
from hepdata_lib import Submission

from hepdata_lib import Table
from hepdata_lib import Variable

import numpy as np
submission = Submission()

submission.read_abstract("HEPData/inputs/smp18003/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-18-003/")
submission.add_link("arXiv", "https://arxiv.org/abs/XXX")
submission.add_record_id(999999999, "inspire")

### Begin Figure 2
figure2 = Table("Figure 2")
figure2.description = "The measured inclusive fiducial cross section."
figure2.location = "Data from Figure 2"

figure2.keywords["observables"] = ["Events"]

figure2_load = np.loadtxt("HEPData/inputs/smp18003/cross_section_results.txt", dtype='string', skiprows=2)

print(figure2_load)

figure2_data = Variable("Final State", is_independent=True, is_binned=False, units="")
figure2_data.values = [str(x) for x in figure2_load[:,0]]

figure2_yields1 = Variable("Cross Section", is_independent=False, is_binned=False, units="")
figure2_yields1.values = [float(x) for x in figure2_load[:,1]]
figure2_yields1.add_qualifier("fb", "Cross Section")

figure2_yields2 = Variable("Positive uncertainty", is_independent=False, is_binned=False, units="")
figure2_yields2.values = [float(x) for x in figure2_load[:,2]]
figure2_yields2.add_qualifier("fb", "Cross Section")

figure2_yields3 = Variable("Negative uncertainty", is_independent=False, is_binned=False, units="")
figure2_yields3.values = [float(x) for x in figure2_load[:,3]]
figure2_yields3.add_qualifier("fb", "Cross Section")

figure2.add_variable(figure2_data)
figure2.add_variable(figure2_yields1)
figure2.add_variable(figure2_yields2)
figure2.add_variable(figure2_yields3)

submission.add_table(figure2)

for figure2 in submission.tables:
    figure2.keywords["cmenergies"] = [13000]

### End Figure 2

### Begin Table 2
table2 = Table("Table 2")
table2.description = "Experimental uncertainties affecting transfer factors used in the analysis to estimate the W boson background in the SR."
table2.location = "Data from Table 2"

table2.keywords["observables"] = ["Uncertainty"]

data2 = np.loadtxt("HEPData/inputs/smp18003/table2.txt", dtype='string', skiprows=2)

print(data2)

table2_data = Variable("Source of uncertainty", is_independent=True, is_binned=False, units="")
table2_data.values = [str(x) for x in data2[:,0]]

table2_yields0 = Variable("Process", is_independent=False, is_binned=False, units="")
table2_yields0.values = [str(x) for x in data2[:,1]]

table2_yields1 = Variable("Uncertainty (%)", is_independent=False, is_binned=False, units="")
table2_yields1.values = [str(x) for x in data2[:,2]]

table2.add_variable(table2_data)
table2.add_variable(table2_yields0)
table2.add_variable(table2_yields1)

submission.add_table(table2)

for table2 in submission.tables:
    table2.keywords["cmenergies"] = [13000]
### End Table 2

### Begin Table 3
table3 = Table("Table 3")
table3.description = "Uncertainties assigned to the simulation based processes in SR and CRs."
table3.location = "Data from Table 3"

table3.keywords["observables"] = ["Uncertainty"]

data3 = np.loadtxt("HEPData/inputs/smp18003/table3.txt", dtype='string', skiprows=2)

print(data3)

table3_data = Variable("Source of uncertainty", is_independent=True, is_binned=False, units="")
table3_data.values = [str(x) for x in data3[:,0]]

table3_yields0 = Variable("Process", is_independent=False, is_binned=False, units="")
table3_yields0.values = [str(x) for x in data3[:,1]]

table3_yields1 = Variable("Uncertainty (%)", is_independent=False, is_binned=False, units="")
table3_yields1.values = [str(x) for x in data3[:,2]]

table3.add_variable(table3_data)
table3.add_variable(table3_yields0)
table3.add_variable(table3_yields1)

submission.add_table(table3)

for table3 in submission.tables:
    table3.keywords["cmenergies"] = [13000]
### End Table 3

### Begin Table 4
table4 = Table("Table 4")
table4.description = "Cross section measurements at high Z pt values in the  Z -> ll and Z -> $\nu\nu$ channels, and in their combination. The theoretical predictions from Madgraph MC@NLO at NLO in QCD and corrected to NLO in EW using the NNPDF 3.0 are also reported."
table4.location = "Data from Table 4"

table4.keywords["observables"] = ["Uncertainty"]

data4 = np.loadtxt("HEPData/inputs/smp18003/table4.txt", dtype='string', skiprows=2)

print(data4)

table4_data = Variable("Z pt (GeV)", is_independent=True, is_binned=False, units="")
table4_data.values = [str(x) for x in data4[:,0]]

table4_yields0 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields0.values = [str(x) for x in data4[:,1]]
table4_yields0.add_qualifier("Z pt (GeV)", "Z -> ee")

table4_yields1 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields1.values = [str(x) for x in data4[:,2]]
table4_yields1.add_qualifier("Z pt (GeV)", "Z -> $\mu\mu$")

table4_yields2 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields2.values = [str(x) for x in data4[:,3]]
table4_yields2.add_qualifier("Z pt (GeV)", "Z -> ll")

table4_yields3 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields3.values = [str(x) for x in data4[:,4]]
table4_yields3.add_qualifier("Z pt (GeV)", "Z -> $\nu\nu$")

table4_yields4 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields4.values = [str(x) for x in data4[:,5]]
table4_yields4.add_qualifier("Z pt (GeV)", "Z -> ll+$\nu\nu$")

table4_yields5 = Variable("Cross section (fb)", is_independent=False, is_binned=False, units="")
table4_yields5.values = [str(x) for x in data4[:,6]]
table4_yields5.add_qualifier("Z pt (GeV)", "Theory")

table4.add_variable(table4_data)
table4.add_variable(table4_yields0)
table4.add_variable(table4_yields1)
table4.add_variable(table4_yields2)
table4.add_variable(table4_yields3)
table4.add_variable(table4_yields4)
table4.add_variable(table4_yields5)

submission.add_table(table4)

for table4 in submission.tables:
    table4.keywords["cmenergies"] = [13000]
### End Table 4

### Begin Table 5
table5 = Table("Table 5")
table5.description = "Cross section measurements normalized to the total cross section at high Z pt values in the  Z -> ll and Z -> $\nu\nu$ channels, and in their combination."
table5.location = "Data from Table 5"

table5.keywords["observables"] = ["Uncertainty"]

data5 = np.loadtxt("HEPData/inputs/smp18003/table5.txt", dtype='string', skiprows=2)

print(data5)

table5_data = Variable("Z pt (GeV)", is_independent=True, is_binned=False, units="")
table5_data.values = [str(x) for x in data5[:,0]]

table5_yields0 = Variable("Cross section", is_independent=False, is_binned=False, units="")
table5_yields0.values = [str(x) for x in data5[:,1]]
table5_yields0.add_qualifier("Z pt (GeV)", "Z -> ee")

table5_yields1 = Variable("Cross section", is_independent=False, is_binned=False, units="")
table5_yields1.values = [str(x) for x in data5[:,2]]
table5_yields1.add_qualifier("Z pt (GeV)", "Z -> $\nu\nu$")

table5_yields2 = Variable("Cross section", is_independent=False, is_binned=False, units="")
table5_yields2.values = [str(x) for x in data5[:,3]]
table5_yields2.add_qualifier("Z pt (GeV)", "Z -> ll+$\nu\nu$")

table5.add_variable(table5_data)
table5.add_variable(table5_yields0)
table5.add_variable(table5_yields1)
table5.add_variable(table5_yields2)

submission.add_table(table5)

for table5 in submission.tables:
    table5.keywords["cmenergies"] = [13000]
### End Table 5

### Begin FigAux1a
reader_FigAux1a = RootFileReader("HEPData/inputs/smp18003/ZnnSystHist.root")

tableFigAux1a = Table("Figure Aux1a")
tableFigAux1a.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of Z pt on neutrinos."
tableFigAux1a.location = "Data from Figure Aux1a"
tableFigAux1a.keywords["observables"] = ["N"]

histoSystPlot_0  = reader_FigAux1a.read_hist_1d("histoResult_0_0")
histoSystPlot_1  = reader_FigAux1a.read_hist_1d("histoResult_1_0")
histoSystPlot_2  = reader_FigAux1a.read_hist_1d("histoResult_2_0")
histoSystPlot_3  = reader_FigAux1a.read_hist_1d("histoResult_3_0")
histoSystPlot_4  = reader_FigAux1a.read_hist_1d("histoResult_4_0")
histoSystPlot_5  = reader_FigAux1a.read_hist_1d("histoResult_5_0")
histoSystPlot_6  = reader_FigAux1a.read_hist_1d("histoResult_6_0")
histoSystPlot_7  = reader_FigAux1a.read_hist_1d("histoResult_7_0")
histoSystPlot_8  = reader_FigAux1a.read_hist_1d("histoResult_8_0")
histoSystPlot_9  = reader_FigAux1a.read_hist_1d("histoResult_9_0")
histoSystPlot_10 = reader_FigAux1a.read_hist_1d("histoResult_10_0")
histoSystPlot_11 = reader_FigAux1a.read_hist_1d("histoResult_11_0")
histoSystPlot_12 = reader_FigAux1a.read_hist_1d("histoResult_12_0")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_FigAux1a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_FigAux1a.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFigAux1a_0 = Variable("MC Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_0.values = histoSystPlot_0["y"]

histoSystPlotFigAux1a_1 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_1.values = histoSystPlot_1["y"]

histoSystPlotFigAux1a_2 = Variable("Jet energy scale", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_2.values = histoSystPlot_2["y"]

histoSystPlotFigAux1a_3 = Variable("Lepton indentification", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_3.values = histoSystPlot_3["y"]

histoSystPlotFigAux1a_4 = Variable("Theory", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_4.values = histoSystPlot_4["y"]

histoSystPlotFigAux1a_5 = Variable("Lepton resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_5.values = histoSystPlot_5["y"]

histoSystPlotFigAux1a_6 = Variable("Pileup", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_6.values = histoSystPlot_6["y"]

histoSystPlotFigAux1a_7 = Variable("Btagging", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_7.values = histoSystPlot_7["y"]

histoSystPlotFigAux1a_8 = Variable("Background normalization", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_8.values = histoSystPlot_8["y"]

histoSystPlotFigAux1a_9 = Variable("Trigger efficiency", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_9.values = histoSystPlot_9["y"]

histoSystPlotFigAux1a_10 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_10.values = histoSystPlot_10["y"]

histoSystPlotFigAux1a_11 = Variable("Data uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_11.values = histoSystPlot_11["y"]

histoSystPlotFigAux1a_12 = Variable("Total systematic uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1a_12.values = histoSystPlot_12["y"]

tableFigAux1a.add_variable(mmed_FigAux1a)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_0)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_1)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_2)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_3)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_4)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_5)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_6)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_7)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_8)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_9)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_10)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_11)
tableFigAux1a.add_variable(histoSystPlotFigAux1a_12)
submission.add_table(tableFigAux1a)
### End FigAux1a

### Begin FigAux1b
reader_FigAux1b = RootFileReader("HEPData/inputs/smp18003/ZnnSystHist.root")

tableFigAux1b = Table("Figure Aux1b")
tableFigAux1b.description = "The relative statistical and systematic uncertainties from various sources for the relative cross section measurements in bins of Z pt on neutrinos."
tableFigAux1b.location = "Data from Figure Aux1b"
tableFigAux1b.keywords["observables"] = ["N"]

histoSystPlot_0  = reader_FigAux1b.read_hist_1d("histoResult_0_1")
histoSystPlot_1  = reader_FigAux1b.read_hist_1d("histoResult_1_1")
histoSystPlot_2  = reader_FigAux1b.read_hist_1d("histoResult_2_1")
histoSystPlot_3  = reader_FigAux1b.read_hist_1d("histoResult_3_1")
histoSystPlot_4  = reader_FigAux1b.read_hist_1d("histoResult_4_1")
histoSystPlot_5  = reader_FigAux1b.read_hist_1d("histoResult_5_1")
histoSystPlot_6  = reader_FigAux1b.read_hist_1d("histoResult_6_1")
histoSystPlot_7  = reader_FigAux1b.read_hist_1d("histoResult_7_1")
histoSystPlot_8  = reader_FigAux1b.read_hist_1d("histoResult_8_1")
histoSystPlot_9  = reader_FigAux1b.read_hist_1d("histoResult_9_1")
histoSystPlot_10 = reader_FigAux1b.read_hist_1d("histoResult_10_1")
histoSystPlot_11 = reader_FigAux1b.read_hist_1d("histoResult_11_1")
histoSystPlot_12 = reader_FigAux1b.read_hist_1d("histoResult_12_1")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_FigAux1b = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_FigAux1b.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFigAux1b_0 = Variable("MC Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_0.values = histoSystPlot_0["y"]

histoSystPlotFigAux1b_1 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_1.values = histoSystPlot_1["y"]

histoSystPlotFigAux1b_2 = Variable("Jet energy scale", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_2.values = histoSystPlot_2["y"]

histoSystPlotFigAux1b_3 = Variable("Lepton indentification", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_3.values = histoSystPlot_3["y"]

histoSystPlotFigAux1b_4 = Variable("Theory", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_4.values = histoSystPlot_4["y"]

histoSystPlotFigAux1b_5 = Variable("Lepton resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_5.values = histoSystPlot_5["y"]

histoSystPlotFigAux1b_6 = Variable("Pileup", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_6.values = histoSystPlot_6["y"]

histoSystPlotFigAux1b_7 = Variable("Btagging", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_7.values = histoSystPlot_7["y"]

histoSystPlotFigAux1b_8 = Variable("Background normalization", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_8.values = histoSystPlot_8["y"]

histoSystPlotFigAux1b_9 = Variable("Trigger efficiency", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_9.values = histoSystPlot_9["y"]

histoSystPlotFigAux1b_10 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_10.values = histoSystPlot_10["y"]

histoSystPlotFigAux1b_11 = Variable("Data uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_11.values = histoSystPlot_11["y"]

histoSystPlotFigAux1b_12 = Variable("Total systematic uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1b_12.values = histoSystPlot_12["y"]

tableFigAux1b.add_variable(mmed_FigAux1b)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_0)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_1)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_2)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_3)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_4)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_5)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_6)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_7)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_8)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_9)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_10)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_11)
tableFigAux1b.add_variable(histoSystPlotFigAux1b_12)
submission.add_table(tableFigAux1b)
### End FigAux1b

### Begin FigAux1c
reader_FigAux1c = RootFileReader("HEPData/inputs/smp18003/ZnnSystHist.root")

tableFigAux1c = Table("Figure Aux1c")
tableFigAux1c.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of Z pt on neutrinos and charged leptons."
tableFigAux1c.location = "Data from Figure Aux1c"
tableFigAux1c.keywords["observables"] = ["N"]

histoSystPlot_0  = reader_FigAux1c.read_hist_1d("histoResult_0_2")
histoSystPlot_1  = reader_FigAux1c.read_hist_1d("histoResult_1_2")
histoSystPlot_2  = reader_FigAux1c.read_hist_1d("histoResult_2_2")
histoSystPlot_3  = reader_FigAux1c.read_hist_1d("histoResult_3_2")
histoSystPlot_4  = reader_FigAux1c.read_hist_1d("histoResult_4_2")
histoSystPlot_5  = reader_FigAux1c.read_hist_1d("histoResult_5_2")
histoSystPlot_6  = reader_FigAux1c.read_hist_1d("histoResult_6_2")
histoSystPlot_7  = reader_FigAux1c.read_hist_1d("histoResult_7_2")
histoSystPlot_8  = reader_FigAux1c.read_hist_1d("histoResult_8_2")
histoSystPlot_9  = reader_FigAux1c.read_hist_1d("histoResult_9_2")
histoSystPlot_10 = reader_FigAux1c.read_hist_1d("histoResult_10_2")
histoSystPlot_11 = reader_FigAux1c.read_hist_1d("histoResult_11_2")
histoSystPlot_12 = reader_FigAux1c.read_hist_1d("histoResult_12_2")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_FigAux1c = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_FigAux1c.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFigAux1c_0 = Variable("MC Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_0.values = histoSystPlot_0["y"]

histoSystPlotFigAux1c_1 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_1.values = histoSystPlot_1["y"]

histoSystPlotFigAux1c_2 = Variable("Jet energy scale", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_2.values = histoSystPlot_2["y"]

histoSystPlotFigAux1c_3 = Variable("Lepton indentification", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_3.values = histoSystPlot_3["y"]

histoSystPlotFigAux1c_4 = Variable("Theory", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_4.values = histoSystPlot_4["y"]

histoSystPlotFigAux1c_5 = Variable("Lepton resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_5.values = histoSystPlot_5["y"]

histoSystPlotFigAux1c_6 = Variable("Pileup", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_6.values = histoSystPlot_6["y"]

histoSystPlotFigAux1c_7 = Variable("Btagging", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_7.values = histoSystPlot_7["y"]

histoSystPlotFigAux1c_8 = Variable("Background normalization", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_8.values = histoSystPlot_8["y"]

histoSystPlotFigAux1c_9 = Variable("Trigger efficiency", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_9.values = histoSystPlot_9["y"]

histoSystPlotFigAux1c_10 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_10.values = histoSystPlot_10["y"]

histoSystPlotFigAux1c_11 = Variable("Data uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_11.values = histoSystPlot_11["y"]

histoSystPlotFigAux1c_12 = Variable("Total systematic uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1c_12.values = histoSystPlot_12["y"]

tableFigAux1c.add_variable(mmed_FigAux1c)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_0)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_1)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_2)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_3)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_4)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_5)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_6)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_7)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_8)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_9)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_10)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_11)
tableFigAux1c.add_variable(histoSystPlotFigAux1c_12)
submission.add_table(tableFigAux1c)
### End FigAux1c

### Begin FigAux1d
reader_FigAux1d = RootFileReader("HEPData/inputs/smp18003/ZnnSystHist.root")

tableFigAux1d = Table("Figure Aux1d")
tableFigAux1d.description = "The relative statistical and systematic uncertainties from various sources for the relative cross section measurements in bins of Z pt on neutrinos."
tableFigAux1d.location = "Data from Figure Aux1d"
tableFigAux1d.keywords["observables"] = ["N"]

histoSystPlot_0  = reader_FigAux1d.read_hist_1d("histoResult_0_3")
histoSystPlot_1  = reader_FigAux1d.read_hist_1d("histoResult_1_3")
histoSystPlot_2  = reader_FigAux1d.read_hist_1d("histoResult_2_3")
histoSystPlot_3  = reader_FigAux1d.read_hist_1d("histoResult_3_3")
histoSystPlot_4  = reader_FigAux1d.read_hist_1d("histoResult_4_3")
histoSystPlot_5  = reader_FigAux1d.read_hist_1d("histoResult_5_3")
histoSystPlot_6  = reader_FigAux1d.read_hist_1d("histoResult_6_3")
histoSystPlot_7  = reader_FigAux1d.read_hist_1d("histoResult_7_3")
histoSystPlot_8  = reader_FigAux1d.read_hist_1d("histoResult_8_3")
histoSystPlot_9  = reader_FigAux1d.read_hist_1d("histoResult_9_3")
histoSystPlot_10 = reader_FigAux1d.read_hist_1d("histoResult_10_3")
histoSystPlot_11 = reader_FigAux1d.read_hist_1d("histoResult_11_3")
histoSystPlot_12 = reader_FigAux1d.read_hist_1d("histoResult_12_3")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_FigAux1d = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_FigAux1d.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFigAux1d_0 = Variable("MC Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_0.values = histoSystPlot_0["y"]

histoSystPlotFigAux1d_1 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_1.values = histoSystPlot_1["y"]

histoSystPlotFigAux1d_2 = Variable("Jet energy scale", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_2.values = histoSystPlot_2["y"]

histoSystPlotFigAux1d_3 = Variable("Lepton indentification", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_3.values = histoSystPlot_3["y"]

histoSystPlotFigAux1d_4 = Variable("Theory", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_4.values = histoSystPlot_4["y"]

histoSystPlotFigAux1d_5 = Variable("Lepton resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_5.values = histoSystPlot_5["y"]

histoSystPlotFigAux1d_6 = Variable("Pileup", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_6.values = histoSystPlot_6["y"]

histoSystPlotFigAux1d_7 = Variable("Btagging", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_7.values = histoSystPlot_7["y"]

histoSystPlotFigAux1d_8 = Variable("Background normalization", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_8.values = histoSystPlot_8["y"]

histoSystPlotFigAux1d_9 = Variable("Trigger efficiency", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_9.values = histoSystPlot_9["y"]

histoSystPlotFigAux1d_10 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_10.values = histoSystPlot_10["y"]

histoSystPlotFigAux1d_11 = Variable("Data uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_11.values = histoSystPlot_11["y"]

histoSystPlotFigAux1d_12 = Variable("Total systematic uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFigAux1d_12.values = histoSystPlot_12["y"]

tableFigAux1d.add_variable(mmed_FigAux1d)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_0)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_1)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_2)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_3)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_4)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_5)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_6)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_7)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_8)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_9)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_10)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_11)
tableFigAux1d.add_variable(histoSystPlotFigAux1d_12)
submission.add_table(tableFigAux1d)
### End FigAux1d

outdir = "smp18003_output"
submission.create_files(outdir)
