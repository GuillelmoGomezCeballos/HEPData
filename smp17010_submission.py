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

submission.read_abstract("HEPData/inputs/smp17010/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-17-010/")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:1909.04133")
submission.add_record_id(1753680, "inspire")

lumi_sf = 1.0/35800.0

### Begin Table 1
table1 = Table("Table 1")
table1.description = "Summary of data, expected signal, and background yields after the full selection. The predicted signal yields are quoted using aMC@NLO simulation. The statistical uncertainties in the simulated samples are below 0.1%."
table1.location = "Data from Table 1"

table1.keywords["observables"] = ["Events"]

data1 = np.loadtxt("HEPData/inputs/smp17010/total_yields.txt", dtype='string', skiprows=2)

print(data1)

table1_data = Variable("Final State", is_independent=True, is_binned=False, units="")
table1_data.values = [str(x) for x in data1[:,0]]

table1_yields1 = Variable("Data", is_independent=False, is_binned=False, units="")
table1_yields1.values = [float(x) for x in data1[:,1]]
table1_yields1.add_qualifier("Expected events", "Z selection")
table1_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table1_yields2 = Variable("Signal", is_independent=False, is_binned=False, units="")
table1_yields2.values = [float(x) for x in data1[:,2]]
table1_yields2.add_qualifier("Expected events", "Z selection")
table1_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table1_yields3 = Variable("Resonant background", is_independent=False, is_binned=False, units="")
table1_yields3.values = [float(x) for x in data1[:,3]]
table1_yields3.add_qualifier("Expected events", "Z selection")
table1_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table1_yields4 = Variable("Nonresonant background", is_independent=False, is_binned=False, units="")
table1_yields4.values = [float(x) for x in data1[:,4]]
table1_yields4.add_qualifier("Expected events", "Z selection")
table1_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table1.add_variable(table1_data)
table1.add_variable(table1_yields1)
table1.add_variable(table1_yields2)
table1.add_variable(table1_yields3)
table1.add_variable(table1_yields4)

submission.add_table(table1)

for table1 in submission.tables:
    table1.keywords["cmenergies"] = [13000]

### End Table 1

### Begin Table 2
table2 = Table("Table 2")
table2.description = "Summary of the systematic uncertainties for the inclusive fiducial cross section measurements."
table2.location = "Data from Table 2"

table2.keywords["observables"] = ["Events"]

data2 = np.loadtxt("HEPData/inputs/smp17010/total_unc.txt", dtype='string', skiprows=2)

print(data2)

table2_data = Variable("Final State", is_independent=True, is_binned=False, units="")
table2_data.values = [str(x) for x in data2[:,0]]

table2_yields1 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
table2_yields1.values = [float(x) for x in data2[:,1]]
table2_yields1.add_qualifier("Uncertainty in %", "Z selection")
table2_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields2 = Variable("Muon reconstruction efficiency", is_independent=False, is_binned=False, units="")
table2_yields2.values = [float(x) for x in data2[:,2]]
table2_yields2.add_qualifier("Uncertainty in %", "Z selection")
table2_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields3 = Variable("Muon selection efficiency", is_independent=False, is_binned=False, units="")
table2_yields3.values = [float(x) for x in data2[:,3]]
table2_yields3.add_qualifier("Uncertainty in %", "Z selection")
table2_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields4 = Variable("Muon momentum scale", is_independent=False, is_binned=False, units="")
table2_yields4.values = [float(x) for x in data2[:,4]]
table2_yields4.add_qualifier("Uncertainty in %", "Z selection")
table2_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields5 = Variable("Electron reconstruction efficiency", is_independent=False, is_binned=False, units="")
table2_yields5.values = [float(x) for x in data2[:,5]]
table2_yields5.add_qualifier("Uncertainty in %", "Z selection")
table2_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields6 = Variable("Electron selection efficiency", is_independent=False, is_binned=False, units="")
table2_yields6.values = [float(x) for x in data2[:,6]]
table2_yields6.add_qualifier("Uncertainty in %", "Z selection")
table2_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields7 = Variable("Electron momentum scale", is_independent=False, is_binned=False, units="")
table2_yields7.values = [float(x) for x in data2[:,7]]
table2_yields7.add_qualifier("Uncertainty in %", "Z selection")
table2_yields7.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields8 = Variable("Background estimation", is_independent=False, is_binned=False, units="")
table2_yields8.values = [float(x) for x in data2[:,8]]
table2_yields8.add_qualifier("Uncertainty in %", "Z selection")
table2_yields8.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields9 = Variable("Total (excluding luminosity)", is_independent=False, is_binned=False, units="")
table2_yields9.values = [float(x) for x in data2[:,9]]
table2_yields9.add_qualifier("Uncertainty in %", "Z selection")
table2_yields9.add_qualifier("SQRT(S)", 13, "TeV")

table2.add_variable(table2_data)
table2.add_variable(table2_yields1)
table2.add_variable(table2_yields2)
table2.add_variable(table2_yields3)
table2.add_variable(table2_yields4)
table2.add_variable(table2_yields5)
table2.add_variable(table2_yields6)
table2.add_variable(table2_yields7)
table2.add_variable(table2_yields8)
table2.add_variable(table2_yields9)

submission.add_table(table2)

for table2 in submission.tables:
    table2.keywords["cmenergies"] = [13000]

### End Table 2


### Begin Table 2
table3 = Table("Table 3")
table3.description = "The measured inclusive fiducial cross sections in the dimuon and dielectron final states. The combined measurement is also shown."
table3.location = "Data from Table 3"

table3.keywords["observables"] = ["Events"]

data3 = np.loadtxt("HEPData/inputs/smp17010/total_cross_section.txt", dtype='string', skiprows=2)

print(data3)

table3_data = Variable("Final State", is_independent=True, is_binned=False, units="")
table3_data.values = [str(x) for x in data3[:,0]]

table3_yields1 = Variable("Cross Section", is_independent=False, is_binned=False, units="")
table3_yields1.values = [float(x) for x in data3[:,1]]
table3_yields1.add_qualifier("pb", "Cross Section")
table3_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table3_yields2 = Variable("Experimental uncertainty", is_independent=False, is_binned=False, units="")
table3_yields2.values = [float(x) for x in data3[:,2]]
table3_yields2.add_qualifier("pb", "Cross Section")
table3_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table3_yields3 = Variable("Luminosity uncertainty", is_independent=False, is_binned=False, units="")
table3_yields3.values = [float(x) for x in data3[:,3]]
table3_yields3.add_qualifier("pb", "Cross Section")
table3_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table3.add_variable(table3_data)
table3.add_variable(table3_yields1)
table3.add_variable(table3_yields2)
table3.add_variable(table3_yields3)

submission.add_table(table3)

for table3 in submission.tables:
    table3.keywords["cmenergies"] = [13000]

### End Table 3

### Begin Fig1a
reader_Fig1a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPt_nsel0_dy3_rebin1_default.root")

tableFig1a = Table("Figure 1a")
tableFig1a.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of Z pt on dimuons."
tableFig1a.location = "Data from Figure 1a"
tableFig1a.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1a.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1a.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1a.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1a.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1a.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1a.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1a.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1a.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig1a.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1a_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_0.values = histoSystPlot_0["y"]

histoSystPlotFig1a_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_1.values = histoSystPlot_1["y"]

histoSystPlotFig1a_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_2.values = histoSystPlot_2["y"]

histoSystPlotFig1a_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_3.values = histoSystPlot_3["y"]

histoSystPlotFig1a_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_4.values = histoSystPlot_4["y"]

histoSystPlotFig1a_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_5.values = histoSystPlot_5["y"]

histoSystPlotFig1a_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_6.values = histoSystPlot_6["y"]

histoSystPlotFig1a_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1a_7.values = histoSystPlot_7["y"]

tableFig1a.add_variable(mmed_Fig1a)
tableFig1a.add_variable(histoSystPlotFig1a_0)
tableFig1a.add_variable(histoSystPlotFig1a_1)
tableFig1a.add_variable(histoSystPlotFig1a_2)
tableFig1a.add_variable(histoSystPlotFig1a_3)
tableFig1a.add_variable(histoSystPlotFig1a_4)
tableFig1a.add_variable(histoSystPlotFig1a_5)
tableFig1a.add_variable(histoSystPlotFig1a_6)
tableFig1a.add_variable(histoSystPlotFig1a_7)
submission.add_table(tableFig1a)
### End Fig1a

### Begin Fig1b
reader_Fig1b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPt_nsel1_dy3_rebin1_default.root")

tableFig1b = Table("Figure 1b")
tableFig1b.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of Z pt on dielectrons."
tableFig1b.location = "Data from Figure 1b"
tableFig1b.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1b.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1b.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1b.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1b.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1b.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1b.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1b.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1b.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1b = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig1b.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1b_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_0.values = histoSystPlot_0["y"]

histoSystPlotFig1b_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_1.values = histoSystPlot_1["y"]

histoSystPlotFig1b_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_2.values = histoSystPlot_2["y"]

histoSystPlotFig1b_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_3.values = histoSystPlot_3["y"]

histoSystPlotFig1b_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_4.values = histoSystPlot_4["y"]

histoSystPlotFig1b_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_5.values = histoSystPlot_5["y"]

histoSystPlotFig1b_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_6.values = histoSystPlot_6["y"]

histoSystPlotFig1b_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1b_7.values = histoSystPlot_7["y"]

tableFig1b.add_variable(mmed_Fig1b)
tableFig1b.add_variable(histoSystPlotFig1b_0)
tableFig1b.add_variable(histoSystPlotFig1b_1)
tableFig1b.add_variable(histoSystPlotFig1b_2)
tableFig1b.add_variable(histoSystPlotFig1b_3)
tableFig1b.add_variable(histoSystPlotFig1b_4)
tableFig1b.add_variable(histoSystPlotFig1b_5)
tableFig1b.add_variable(histoSystPlotFig1b_6)
tableFig1b.add_variable(histoSystPlotFig1b_7)
submission.add_table(tableFig1b)
### End Fig1b

### Begin Fig1c
reader_Fig1c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystRap_nsel0_dy3_rebin1_default.root")

tableFig1c = Table("Figure 1c")
tableFig1c.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of |y(Z)| on dimuons."
tableFig1c.location = "Data from Figure 1c"
tableFig1c.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1c.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1c.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1c.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1c.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1c.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1c.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1c.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1c.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1c = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig1c.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1c_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_0.values = histoSystPlot_0["y"]

histoSystPlotFig1c_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_1.values = histoSystPlot_1["y"]

histoSystPlotFig1c_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_2.values = histoSystPlot_2["y"]

histoSystPlotFig1c_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_3.values = histoSystPlot_3["y"]

histoSystPlotFig1c_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_4.values = histoSystPlot_4["y"]

histoSystPlotFig1c_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_5.values = histoSystPlot_5["y"]

histoSystPlotFig1c_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_6.values = histoSystPlot_6["y"]

histoSystPlotFig1c_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1c_7.values = histoSystPlot_7["y"]

tableFig1c.add_variable(mmed_Fig1c)
tableFig1c.add_variable(histoSystPlotFig1c_0)
tableFig1c.add_variable(histoSystPlotFig1c_1)
tableFig1c.add_variable(histoSystPlotFig1c_2)
tableFig1c.add_variable(histoSystPlotFig1c_3)
tableFig1c.add_variable(histoSystPlotFig1c_4)
tableFig1c.add_variable(histoSystPlotFig1c_5)
tableFig1c.add_variable(histoSystPlotFig1c_6)
tableFig1c.add_variable(histoSystPlotFig1c_7)
submission.add_table(tableFig1c)
### End Fig1c

### Begin Fig1d
reader_Fig1d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystRap_nsel1_dy3_rebin1_default.root")

tableFig1d = Table("Figure 1d")
tableFig1d.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of |y(Z)| on dielectrons."
tableFig1d.location = "Data from Figure 1d"
tableFig1d.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1d.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1d.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1d.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1d.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1d.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1d.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1d.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1d.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1d = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig1d.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1d_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_0.values = histoSystPlot_0["y"]

histoSystPlotFig1d_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_1.values = histoSystPlot_1["y"]

histoSystPlotFig1d_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_2.values = histoSystPlot_2["y"]

histoSystPlotFig1d_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_3.values = histoSystPlot_3["y"]

histoSystPlotFig1d_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_4.values = histoSystPlot_4["y"]

histoSystPlotFig1d_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_5.values = histoSystPlot_5["y"]

histoSystPlotFig1d_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_6.values = histoSystPlot_6["y"]

histoSystPlotFig1d_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1d_7.values = histoSystPlot_7["y"]

tableFig1d.add_variable(mmed_Fig1d)
tableFig1d.add_variable(histoSystPlotFig1d_0)
tableFig1d.add_variable(histoSystPlotFig1d_1)
tableFig1d.add_variable(histoSystPlotFig1d_2)
tableFig1d.add_variable(histoSystPlotFig1d_3)
tableFig1d.add_variable(histoSystPlotFig1d_4)
tableFig1d.add_variable(histoSystPlotFig1d_5)
tableFig1d.add_variable(histoSystPlotFig1d_6)
tableFig1d.add_variable(histoSystPlotFig1d_7)
submission.add_table(tableFig1d)
### End Fig1d

### Begin Fig1e
reader_Fig1e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPhiStar_nsel0_dy3_rebin1_default.root")

tableFig1e = Table("Figure 1e")
tableFig1e.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dimuons."
tableFig1e.location = "Data from Figure 1e"
tableFig1e.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1e.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1e.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1e.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1e.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1e.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1e.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1e.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1e.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1e = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig1e.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1e_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_0.values = histoSystPlot_0["y"]

histoSystPlotFig1e_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_1.values = histoSystPlot_1["y"]

histoSystPlotFig1e_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_2.values = histoSystPlot_2["y"]

histoSystPlotFig1e_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_3.values = histoSystPlot_3["y"]

histoSystPlotFig1e_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_4.values = histoSystPlot_4["y"]

histoSystPlotFig1e_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_5.values = histoSystPlot_5["y"]

histoSystPlotFig1e_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_6.values = histoSystPlot_6["y"]

histoSystPlotFig1e_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1e_7.values = histoSystPlot_7["y"]

tableFig1e.add_variable(mmed_Fig1e)
tableFig1e.add_variable(histoSystPlotFig1e_0)
tableFig1e.add_variable(histoSystPlotFig1e_1)
tableFig1e.add_variable(histoSystPlotFig1e_2)
tableFig1e.add_variable(histoSystPlotFig1e_3)
tableFig1e.add_variable(histoSystPlotFig1e_4)
tableFig1e.add_variable(histoSystPlotFig1e_5)
tableFig1e.add_variable(histoSystPlotFig1e_6)
tableFig1e.add_variable(histoSystPlotFig1e_7)
submission.add_table(tableFig1e)
### End Fig1e

### Begin Fig1f
reader_Fig1f = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPhiStar_nsel1_dy3_rebin1_default.root")

tableFig1f = Table("Figure 1f")
tableFig1f.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dielectrons."
tableFig1f.location = "Data from Figure 1f"
tableFig1f.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig1f.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig1f.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig1f.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig1f.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig1f.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig1f.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig1f.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig1f.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig1f = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig1f.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig1f_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_0.values = histoSystPlot_0["y"]

histoSystPlotFig1f_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_1.values = histoSystPlot_1["y"]

histoSystPlotFig1f_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_2.values = histoSystPlot_2["y"]

histoSystPlotFig1f_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_3.values = histoSystPlot_3["y"]

histoSystPlotFig1f_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_4.values = histoSystPlot_4["y"]

histoSystPlotFig1f_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_5.values = histoSystPlot_5["y"]

histoSystPlotFig1f_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_6.values = histoSystPlot_6["y"]

histoSystPlotFig1f_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig1f_7.values = histoSystPlot_7["y"]

tableFig1f.add_variable(mmed_Fig1f)
tableFig1f.add_variable(histoSystPlotFig1f_0)
tableFig1f.add_variable(histoSystPlotFig1f_1)
tableFig1f.add_variable(histoSystPlotFig1f_2)
tableFig1f.add_variable(histoSystPlotFig1f_3)
tableFig1f.add_variable(histoSystPlotFig1f_4)
tableFig1f.add_variable(histoSystPlotFig1f_5)
tableFig1f.add_variable(histoSystPlotFig1f_6)
tableFig1f.add_variable(histoSystPlotFig1f_7)
submission.add_table(tableFig1f)
### End Fig1f

### Begin Fig2a
reader_Fig2a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPt_nsel0_dy3_rebin1_default.root")

tableFig2a = Table("Figure 2a")
tableFig2a.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of Z pt on dimuons."
tableFig2a.location = "Data from Figure 2a"
tableFig2a.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2a.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2a.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2a.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2a.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2a.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2a.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2a.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2a.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig2a.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2a_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_0.values = histoSystPlot_0["y"]

histoSystPlotFig2a_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_1.values = histoSystPlot_1["y"]

histoSystPlotFig2a_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_2.values = histoSystPlot_2["y"]

histoSystPlotFig2a_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_3.values = histoSystPlot_3["y"]

histoSystPlotFig2a_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_4.values = histoSystPlot_4["y"]

histoSystPlotFig2a_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_5.values = histoSystPlot_5["y"]

histoSystPlotFig2a_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_6.values = histoSystPlot_6["y"]

histoSystPlotFig2a_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2a_7.values = histoSystPlot_7["y"]

tableFig2a.add_variable(mmed_Fig2a)
tableFig2a.add_variable(histoSystPlotFig2a_0)
tableFig2a.add_variable(histoSystPlotFig2a_1)
tableFig2a.add_variable(histoSystPlotFig2a_2)
tableFig2a.add_variable(histoSystPlotFig2a_3)
tableFig2a.add_variable(histoSystPlotFig2a_4)
tableFig2a.add_variable(histoSystPlotFig2a_5)
tableFig2a.add_variable(histoSystPlotFig2a_6)
tableFig2a.add_variable(histoSystPlotFig2a_7)
submission.add_table(tableFig2a)
### End Fig2a

### Begin Fig2b
reader_Fig2b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPt_nsel1_dy3_rebin1_default.root")

tableFig2b = Table("Figure 2b")
tableFig2b.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of Z pt on dielectrons."
tableFig2b.location = "Data from Figure 2b"
tableFig2b.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2b.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2b.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2b.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2b.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2b.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2b.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2b.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2b.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2b = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig2b.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2b_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_0.values = histoSystPlot_0["y"]

histoSystPlotFig2b_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_1.values = histoSystPlot_1["y"]

histoSystPlotFig2b_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_2.values = histoSystPlot_2["y"]

histoSystPlotFig2b_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_3.values = histoSystPlot_3["y"]

histoSystPlotFig2b_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_4.values = histoSystPlot_4["y"]

histoSystPlotFig2b_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_5.values = histoSystPlot_5["y"]

histoSystPlotFig2b_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_6.values = histoSystPlot_6["y"]

histoSystPlotFig2b_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2b_7.values = histoSystPlot_7["y"]

tableFig2b.add_variable(mmed_Fig2b)
tableFig2b.add_variable(histoSystPlotFig2b_0)
tableFig2b.add_variable(histoSystPlotFig2b_1)
tableFig2b.add_variable(histoSystPlotFig2b_2)
tableFig2b.add_variable(histoSystPlotFig2b_3)
tableFig2b.add_variable(histoSystPlotFig2b_4)
tableFig2b.add_variable(histoSystPlotFig2b_5)
tableFig2b.add_variable(histoSystPlotFig2b_6)
tableFig2b.add_variable(histoSystPlotFig2b_7)
submission.add_table(tableFig2b)
### End Fig2b

### Begin Fig2c
reader_Fig2c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystRap_nsel0_dy3_rebin1_default.root")

tableFig2c = Table("Figure 2c")
tableFig2c.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of |y(Z)| on dimuons."
tableFig2c.location = "Data from Figure 2c"
tableFig2c.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2c.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2c.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2c.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2c.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2c.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2c.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2c.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2c.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2c = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig2c.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2c_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_0.values = histoSystPlot_0["y"]

histoSystPlotFig2c_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_1.values = histoSystPlot_1["y"]

histoSystPlotFig2c_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_2.values = histoSystPlot_2["y"]

histoSystPlotFig2c_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_3.values = histoSystPlot_3["y"]

histoSystPlotFig2c_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_4.values = histoSystPlot_4["y"]

histoSystPlotFig2c_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_5.values = histoSystPlot_5["y"]

histoSystPlotFig2c_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_6.values = histoSystPlot_6["y"]

histoSystPlotFig2c_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2c_7.values = histoSystPlot_7["y"]

tableFig2c.add_variable(mmed_Fig2c)
tableFig2c.add_variable(histoSystPlotFig2c_0)
tableFig2c.add_variable(histoSystPlotFig2c_1)
tableFig2c.add_variable(histoSystPlotFig2c_2)
tableFig2c.add_variable(histoSystPlotFig2c_3)
tableFig2c.add_variable(histoSystPlotFig2c_4)
tableFig2c.add_variable(histoSystPlotFig2c_5)
tableFig2c.add_variable(histoSystPlotFig2c_6)
tableFig2c.add_variable(histoSystPlotFig2c_7)
submission.add_table(tableFig2c)
### End Fig2c

### Begin Fig2d
reader_Fig2d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystRap_nsel1_dy3_rebin1_default.root")

tableFig2d = Table("Figure 2d")
tableFig2d.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of |y(Z)| on dielectrons."
tableFig2d.location = "Data from Figure 2d"
tableFig2d.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2d.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2d.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2d.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2d.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2d.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2d.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2d.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2d.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2d = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig2d.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2d_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_0.values = histoSystPlot_0["y"]

histoSystPlotFig2d_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_1.values = histoSystPlot_1["y"]

histoSystPlotFig2d_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_2.values = histoSystPlot_2["y"]

histoSystPlotFig2d_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_3.values = histoSystPlot_3["y"]

histoSystPlotFig2d_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_4.values = histoSystPlot_4["y"]

histoSystPlotFig2d_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_5.values = histoSystPlot_5["y"]

histoSystPlotFig2d_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_6.values = histoSystPlot_6["y"]

histoSystPlotFig2d_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2d_7.values = histoSystPlot_7["y"]

tableFig2d.add_variable(mmed_Fig2d)
tableFig2d.add_variable(histoSystPlotFig2d_0)
tableFig2d.add_variable(histoSystPlotFig2d_1)
tableFig2d.add_variable(histoSystPlotFig2d_2)
tableFig2d.add_variable(histoSystPlotFig2d_3)
tableFig2d.add_variable(histoSystPlotFig2d_4)
tableFig2d.add_variable(histoSystPlotFig2d_5)
tableFig2d.add_variable(histoSystPlotFig2d_6)
tableFig2d.add_variable(histoSystPlotFig2d_7)
submission.add_table(tableFig2d)
### End Fig2d

### Begin Fig2e
reader_Fig2e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPhiStar_nsel0_dy3_rebin1_default.root")

tableFig2e = Table("Figure 2e")
tableFig2e.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dimuons."
tableFig2e.location = "Data from Figure 2e"
tableFig2e.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2e.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2e.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2e.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2e.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2e.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2e.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2e.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2e.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2e = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig2e.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2e_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_0.values = histoSystPlot_0["y"]

histoSystPlotFig2e_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_1.values = histoSystPlot_1["y"]

histoSystPlotFig2e_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_2.values = histoSystPlot_2["y"]

histoSystPlotFig2e_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_3.values = histoSystPlot_3["y"]

histoSystPlotFig2e_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_4.values = histoSystPlot_4["y"]

histoSystPlotFig2e_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_5.values = histoSystPlot_5["y"]

histoSystPlotFig2e_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_6.values = histoSystPlot_6["y"]

histoSystPlotFig2e_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2e_7.values = histoSystPlot_7["y"]

tableFig2e.add_variable(mmed_Fig2e)
tableFig2e.add_variable(histoSystPlotFig2e_0)
tableFig2e.add_variable(histoSystPlotFig2e_1)
tableFig2e.add_variable(histoSystPlotFig2e_2)
tableFig2e.add_variable(histoSystPlotFig2e_3)
tableFig2e.add_variable(histoSystPlotFig2e_4)
tableFig2e.add_variable(histoSystPlotFig2e_5)
tableFig2e.add_variable(histoSystPlotFig2e_6)
tableFig2e.add_variable(histoSystPlotFig2e_7)
submission.add_table(tableFig2e)
### End Fig2e

### Begin Fig2f
reader_Fig2f = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPhiStar_nsel1_dy3_rebin1_default.root")

tableFig2f = Table("Figure 2f")
tableFig2f.description = "The relative statistical and systematic uncertainties in % from various sources for the normalized cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dielectrons."
tableFig2f.location = "Data from Figure 2f"
tableFig2f.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig2f.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig2f.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig2f.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig2f.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig2f.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig2f.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig2f.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig2f.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig2f = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig2f.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig2f_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_0.values = histoSystPlot_0["y"]

histoSystPlotFig2f_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_1.values = histoSystPlot_1["y"]

histoSystPlotFig2f_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_2.values = histoSystPlot_2["y"]

histoSystPlotFig2f_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_3.values = histoSystPlot_3["y"]

histoSystPlotFig2f_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_4.values = histoSystPlot_4["y"]

histoSystPlotFig2f_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_5.values = histoSystPlot_5["y"]

histoSystPlotFig2f_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_6.values = histoSystPlot_6["y"]

histoSystPlotFig2f_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig2f_7.values = histoSystPlot_7["y"]

tableFig2f.add_variable(mmed_Fig2f)
tableFig2f.add_variable(histoSystPlotFig2f_0)
tableFig2f.add_variable(histoSystPlotFig2f_1)
tableFig2f.add_variable(histoSystPlotFig2f_2)
tableFig2f.add_variable(histoSystPlotFig2f_3)
tableFig2f.add_variable(histoSystPlotFig2f_4)
tableFig2f.add_variable(histoSystPlotFig2f_5)
tableFig2f.add_variable(histoSystPlotFig2f_6)
tableFig2f.add_variable(histoSystPlotFig2f_7)
submission.add_table(tableFig2f)
### End Fig2f

### Begin Fig3a
reader_Fig3a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap0_nsel0_dy3_rebin1_default.root")

tableFig3a = Table("Figure 3a")
tableFig3a.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dimuon final state."
tableFig3a.location = "Data from Figure 3a"
tableFig3a.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig3a.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig3a.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig3a.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig3a.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig3a.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig3a.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig3a.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig3a.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig3a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig3a.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig3a_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_0.values = histoSystPlot_0["y"]

histoSystPlotFig3a_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_1.values = histoSystPlot_1["y"]

histoSystPlotFig3a_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_2.values = histoSystPlot_2["y"]

histoSystPlotFig3a_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_3.values = histoSystPlot_3["y"]

histoSystPlotFig3a_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_4.values = histoSystPlot_4["y"]

histoSystPlotFig3a_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_5.values = histoSystPlot_5["y"]

histoSystPlotFig3a_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_6.values = histoSystPlot_6["y"]

histoSystPlotFig3a_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig3a_7.values = histoSystPlot_7["y"]

tableFig3a.add_variable(mmed_Fig3a)
tableFig3a.add_variable(histoSystPlotFig3a_0)
tableFig3a.add_variable(histoSystPlotFig3a_1)
tableFig3a.add_variable(histoSystPlotFig3a_2)
tableFig3a.add_variable(histoSystPlotFig3a_3)
tableFig3a.add_variable(histoSystPlotFig3a_4)
tableFig3a.add_variable(histoSystPlotFig3a_5)
tableFig3a.add_variable(histoSystPlotFig3a_6)
tableFig3a.add_variable(histoSystPlotFig3a_7)
submission.add_table(tableFig3a)
### End Fig3a

### Begin Fig3b
reader_Fig3b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap1_nsel0_dy3_rebin1_default.root")

tableFig3b = Table("Figure 3b")
tableFig3b.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dimuon final state."
tableFig3b.location = "Data from Figure 3b"
tableFig3b.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig3b.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig3b.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig3b.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig3b.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig3b.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig3b.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig3b.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig3b.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig3b = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig3b.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig3b_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_0.values = histoSystPlot_0["y"]

histoSystPlotFig3b_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_1.values = histoSystPlot_1["y"]

histoSystPlotFig3b_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_2.values = histoSystPlot_2["y"]

histoSystPlotFig3b_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_3.values = histoSystPlot_3["y"]

histoSystPlotFig3b_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_4.values = histoSystPlot_4["y"]

histoSystPlotFig3b_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_5.values = histoSystPlot_5["y"]

histoSystPlotFig3b_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_6.values = histoSystPlot_6["y"]

histoSystPlotFig3b_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig3b_7.values = histoSystPlot_7["y"]

tableFig3b.add_variable(mmed_Fig3b)
tableFig3b.add_variable(histoSystPlotFig3b_0)
tableFig3b.add_variable(histoSystPlotFig3b_1)
tableFig3b.add_variable(histoSystPlotFig3b_2)
tableFig3b.add_variable(histoSystPlotFig3b_3)
tableFig3b.add_variable(histoSystPlotFig3b_4)
tableFig3b.add_variable(histoSystPlotFig3b_5)
tableFig3b.add_variable(histoSystPlotFig3b_6)
tableFig3b.add_variable(histoSystPlotFig3b_7)
submission.add_table(tableFig3b)
### End Fig3b

### Begin Fig3c
reader_Fig3c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap2_nsel0_dy3_rebin1_default.root")

tableFig3c = Table("Figure 3c")
tableFig3c.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dimuon final state."
tableFig3c.location = "Data from Figure 3c"
tableFig3c.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig3c.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig3c.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig3c.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig3c.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig3c.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig3c.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig3c.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig3c.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig3c = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig3c.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig3c_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_0.values = histoSystPlot_0["y"]

histoSystPlotFig3c_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_1.values = histoSystPlot_1["y"]

histoSystPlotFig3c_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_2.values = histoSystPlot_2["y"]

histoSystPlotFig3c_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_3.values = histoSystPlot_3["y"]

histoSystPlotFig3c_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_4.values = histoSystPlot_4["y"]

histoSystPlotFig3c_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_5.values = histoSystPlot_5["y"]

histoSystPlotFig3c_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_6.values = histoSystPlot_6["y"]

histoSystPlotFig3c_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig3c_7.values = histoSystPlot_7["y"]

tableFig3c.add_variable(mmed_Fig3c)
tableFig3c.add_variable(histoSystPlotFig3c_0)
tableFig3c.add_variable(histoSystPlotFig3c_1)
tableFig3c.add_variable(histoSystPlotFig3c_2)
tableFig3c.add_variable(histoSystPlotFig3c_3)
tableFig3c.add_variable(histoSystPlotFig3c_4)
tableFig3c.add_variable(histoSystPlotFig3c_5)
tableFig3c.add_variable(histoSystPlotFig3c_6)
tableFig3c.add_variable(histoSystPlotFig3c_7)
submission.add_table(tableFig3c)
### End Fig3c

### Begin Fig3d
reader_Fig3d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap3_nsel0_dy3_rebin1_default.root")

tableFig3d = Table("Figure 3d")
tableFig3d.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dimuon final state."
tableFig3d.location = "Data from Figure 3d"
tableFig3d.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig3d.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig3d.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig3d.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig3d.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig3d.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig3d.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig3d.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig3d.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig3d = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig3d.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig3d_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_0.values = histoSystPlot_0["y"]

histoSystPlotFig3d_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_1.values = histoSystPlot_1["y"]

histoSystPlotFig3d_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_2.values = histoSystPlot_2["y"]

histoSystPlotFig3d_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_3.values = histoSystPlot_3["y"]

histoSystPlotFig3d_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_4.values = histoSystPlot_4["y"]

histoSystPlotFig3d_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_5.values = histoSystPlot_5["y"]

histoSystPlotFig3d_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_6.values = histoSystPlot_6["y"]

histoSystPlotFig3d_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig3d_7.values = histoSystPlot_7["y"]

tableFig3d.add_variable(mmed_Fig3d)
tableFig3d.add_variable(histoSystPlotFig3d_0)
tableFig3d.add_variable(histoSystPlotFig3d_1)
tableFig3d.add_variable(histoSystPlotFig3d_2)
tableFig3d.add_variable(histoSystPlotFig3d_3)
tableFig3d.add_variable(histoSystPlotFig3d_4)
tableFig3d.add_variable(histoSystPlotFig3d_5)
tableFig3d.add_variable(histoSystPlotFig3d_6)
tableFig3d.add_variable(histoSystPlotFig3d_7)
submission.add_table(tableFig3d)
### End Fig3d

### Begin Fig3e
reader_Fig3e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap4_nsel0_dy3_rebin1_default.root")

tableFig3e = Table("Figure 3e")
tableFig3e.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dimuon final state."
tableFig3e.location = "Data from Figure 3e"
tableFig3e.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig3e.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig3e.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig3e.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig3e.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig3e.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig3e.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig3e.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig3e.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig3e = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig3e.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig3e_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_0.values = histoSystPlot_0["y"]

histoSystPlotFig3e_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_1.values = histoSystPlot_1["y"]

histoSystPlotFig3e_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_2.values = histoSystPlot_2["y"]

histoSystPlotFig3e_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_3.values = histoSystPlot_3["y"]

histoSystPlotFig3e_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_4.values = histoSystPlot_4["y"]

histoSystPlotFig3e_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_5.values = histoSystPlot_5["y"]

histoSystPlotFig3e_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_6.values = histoSystPlot_6["y"]

histoSystPlotFig3e_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig3e_7.values = histoSystPlot_7["y"]

tableFig3e.add_variable(mmed_Fig3e)
tableFig3e.add_variable(histoSystPlotFig3e_0)
tableFig3e.add_variable(histoSystPlotFig3e_1)
tableFig3e.add_variable(histoSystPlotFig3e_2)
tableFig3e.add_variable(histoSystPlotFig3e_3)
tableFig3e.add_variable(histoSystPlotFig3e_4)
tableFig3e.add_variable(histoSystPlotFig3e_5)
tableFig3e.add_variable(histoSystPlotFig3e_6)
tableFig3e.add_variable(histoSystPlotFig3e_7)
submission.add_table(tableFig3e)
### End Fig3e

### Begin Fig4a
reader_Fig4a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap0_nsel1_dy3_rebin1_default.root")

tableFig4a = Table("Figure 4a")
tableFig4a.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dielectron final state."
tableFig4a.location = "Data from Figure 4a"
tableFig4a.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig4a.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig4a.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig4a.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig4a.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig4a.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig4a.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig4a.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig4a.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig4a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4a.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig4a_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_0.values = histoSystPlot_0["y"]

histoSystPlotFig4a_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_1.values = histoSystPlot_1["y"]

histoSystPlotFig4a_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_2.values = histoSystPlot_2["y"]

histoSystPlotFig4a_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_3.values = histoSystPlot_3["y"]

histoSystPlotFig4a_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_4.values = histoSystPlot_4["y"]

histoSystPlotFig4a_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_5.values = histoSystPlot_5["y"]

histoSystPlotFig4a_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_6.values = histoSystPlot_6["y"]

histoSystPlotFig4a_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig4a_7.values = histoSystPlot_7["y"]

tableFig4a.add_variable(mmed_Fig4a)
tableFig4a.add_variable(histoSystPlotFig4a_0)
tableFig4a.add_variable(histoSystPlotFig4a_1)
tableFig4a.add_variable(histoSystPlotFig4a_2)
tableFig4a.add_variable(histoSystPlotFig4a_3)
tableFig4a.add_variable(histoSystPlotFig4a_4)
tableFig4a.add_variable(histoSystPlotFig4a_5)
tableFig4a.add_variable(histoSystPlotFig4a_6)
tableFig4a.add_variable(histoSystPlotFig4a_7)
submission.add_table(tableFig4a)
### End Fig4a

### Begin Fig4b
reader_Fig4b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap1_nsel1_dy3_rebin1_default.root")

tableFig4b = Table("Figure 4b")
tableFig4b.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dielectron final state."
tableFig4b.location = "Data from Figure 4b"
tableFig4b.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig4b.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig4b.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig4b.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig4b.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig4b.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig4b.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig4b.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig4b.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig4b = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4b.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig4b_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_0.values = histoSystPlot_0["y"]

histoSystPlotFig4b_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_1.values = histoSystPlot_1["y"]

histoSystPlotFig4b_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_2.values = histoSystPlot_2["y"]

histoSystPlotFig4b_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_3.values = histoSystPlot_3["y"]

histoSystPlotFig4b_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_4.values = histoSystPlot_4["y"]

histoSystPlotFig4b_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_5.values = histoSystPlot_5["y"]

histoSystPlotFig4b_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_6.values = histoSystPlot_6["y"]

histoSystPlotFig4b_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig4b_7.values = histoSystPlot_7["y"]

tableFig4b.add_variable(mmed_Fig4b)
tableFig4b.add_variable(histoSystPlotFig4b_0)
tableFig4b.add_variable(histoSystPlotFig4b_1)
tableFig4b.add_variable(histoSystPlotFig4b_2)
tableFig4b.add_variable(histoSystPlotFig4b_3)
tableFig4b.add_variable(histoSystPlotFig4b_4)
tableFig4b.add_variable(histoSystPlotFig4b_5)
tableFig4b.add_variable(histoSystPlotFig4b_6)
tableFig4b.add_variable(histoSystPlotFig4b_7)
submission.add_table(tableFig4b)
### End Fig4b

### Begin Fig4c
reader_Fig4c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap2_nsel1_dy3_rebin1_default.root")

tableFig4c = Table("Figure 4c")
tableFig4c.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dielectron final state."
tableFig4c.location = "Data from Figure 4c"
tableFig4c.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig4c.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig4c.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig4c.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig4c.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig4c.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig4c.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig4c.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig4c.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig4c = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4c.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig4c_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_0.values = histoSystPlot_0["y"]

histoSystPlotFig4c_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_1.values = histoSystPlot_1["y"]

histoSystPlotFig4c_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_2.values = histoSystPlot_2["y"]

histoSystPlotFig4c_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_3.values = histoSystPlot_3["y"]

histoSystPlotFig4c_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_4.values = histoSystPlot_4["y"]

histoSystPlotFig4c_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_5.values = histoSystPlot_5["y"]

histoSystPlotFig4c_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_6.values = histoSystPlot_6["y"]

histoSystPlotFig4c_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig4c_7.values = histoSystPlot_7["y"]

tableFig4c.add_variable(mmed_Fig4c)
tableFig4c.add_variable(histoSystPlotFig4c_0)
tableFig4c.add_variable(histoSystPlotFig4c_1)
tableFig4c.add_variable(histoSystPlotFig4c_2)
tableFig4c.add_variable(histoSystPlotFig4c_3)
tableFig4c.add_variable(histoSystPlotFig4c_4)
tableFig4c.add_variable(histoSystPlotFig4c_5)
tableFig4c.add_variable(histoSystPlotFig4c_6)
tableFig4c.add_variable(histoSystPlotFig4c_7)
submission.add_table(tableFig4c)
### End Fig4c

### Begin Fig4d
reader_Fig4d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap3_nsel1_dy3_rebin1_default.root")

tableFig4d = Table("Figure 4d")
tableFig4d.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dielectron final state."
tableFig4d.location = "Data from Figure 4d"
tableFig4d.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig4d.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig4d.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig4d.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig4d.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig4d.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig4d.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig4d.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig4d.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig4d = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4d.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig4d_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_0.values = histoSystPlot_0["y"]

histoSystPlotFig4d_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_1.values = histoSystPlot_1["y"]

histoSystPlotFig4d_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_2.values = histoSystPlot_2["y"]

histoSystPlotFig4d_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_3.values = histoSystPlot_3["y"]

histoSystPlotFig4d_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_4.values = histoSystPlot_4["y"]

histoSystPlotFig4d_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_5.values = histoSystPlot_5["y"]

histoSystPlotFig4d_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_6.values = histoSystPlot_6["y"]

histoSystPlotFig4d_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig4d_7.values = histoSystPlot_7["y"]

tableFig4d.add_variable(mmed_Fig4d)
tableFig4d.add_variable(histoSystPlotFig4d_0)
tableFig4d.add_variable(histoSystPlotFig4d_1)
tableFig4d.add_variable(histoSystPlotFig4d_2)
tableFig4d.add_variable(histoSystPlotFig4d_3)
tableFig4d.add_variable(histoSystPlotFig4d_4)
tableFig4d.add_variable(histoSystPlotFig4d_5)
tableFig4d.add_variable(histoSystPlotFig4d_6)
tableFig4d.add_variable(histoSystPlotFig4d_7)
submission.add_table(tableFig4d)
### End Fig4d

### Begin Fig4e
reader_Fig4e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap4_nsel1_dy3_rebin1_default.root")

tableFig4e = Table("Figure 4e")
tableFig4e.description = "The relative statistical and systematic uncertainties in % from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
tableFig4e.location = "Data from Figure 4e"
tableFig4e.keywords["observables"] = ["N"]

histoSystPlot_0 = reader_Fig4e.read_hist_1d("histoSystPlot_0")
histoSystPlot_1 = reader_Fig4e.read_hist_1d("histoSystPlot_1")
histoSystPlot_2 = reader_Fig4e.read_hist_1d("histoSystPlot_2")
histoSystPlot_3 = reader_Fig4e.read_hist_1d("histoSystPlot_3")
histoSystPlot_4 = reader_Fig4e.read_hist_1d("histoSystPlot_4")
histoSystPlot_5 = reader_Fig4e.read_hist_1d("histoSystPlot_5")
histoSystPlot_6 = reader_Fig4e.read_hist_1d("histoSystPlot_6")
histoSystPlot_7 = reader_Fig4e.read_hist_1d("histoSystPlot_7")

histoSystPlot_0.keys()

for key in histoSystPlot_0.keys():
    print(key, type(histoSystPlot_0[key]), type(histoSystPlot_0[key][0]))

mmed_Fig4e = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4e.values = histoSystPlot_0["x_edges"]

# y-axis: N events
histoSystPlotFig4e_0 = Variable("Total uncertainty", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_0.values = histoSystPlot_0["y"]

histoSystPlotFig4e_1 = Variable("Unfolding", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_1.values = histoSystPlot_1["y"]

histoSystPlotFig4e_2 = Variable("Momentum resolution", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_2.values = histoSystPlot_2["y"]

histoSystPlotFig4e_3 = Variable("Background", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_3.values = histoSystPlot_3["y"]

histoSystPlotFig4e_4 = Variable("Indentification and trigger", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_4.values = histoSystPlot_4["y"]

histoSystPlotFig4e_5 = Variable("Reconstruction", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_5.values = histoSystPlot_5["y"]

histoSystPlotFig4e_6 = Variable("Statistical", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_6.values = histoSystPlot_6["y"]

histoSystPlotFig4e_7 = Variable("Luminosity", is_independent=False, is_binned=False, units="")
histoSystPlotFig4e_7.values = histoSystPlot_7["y"]

tableFig4e.add_variable(mmed_Fig4e)
tableFig4e.add_variable(histoSystPlotFig4e_0)
tableFig4e.add_variable(histoSystPlotFig4e_1)
tableFig4e.add_variable(histoSystPlotFig4e_2)
tableFig4e.add_variable(histoSystPlotFig4e_3)
tableFig4e.add_variable(histoSystPlotFig4e_4)
tableFig4e.add_variable(histoSystPlotFig4e_5)
tableFig4e.add_variable(histoSystPlotFig4e_6)
tableFig4e.add_variable(histoSystPlotFig4e_7)
submission.add_table(tableFig4e)
### End Fig4e

### Begin Fig5
reader_Fig5a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystRap_nsel0_dy3_rebin1_default.root")
reader_Fig5b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystRap_nsel1_dy3_rebin1_default.root")
reader_Fig5c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystRap_nsel2_dy3_rebin1_default.root")

tableFig5 = Table("Figure 5")
tableFig5.description = "The measured absolute cross sections in bins of |y(Z)|, using dressed level leptons. The cross sections are normalized by the bin width."
tableFig5.location = "Data from Figure 5"
tableFig5.keywords["observables"] = ["N"]

histo_unfoldFig5a = reader_Fig5a.read_hist_1d("unfold")
histo_unfoldFig5b = reader_Fig5b.read_hist_1d("unfold")
histo_unfoldFig5c = reader_Fig5c.read_hist_1d("unfold")

histo_unfoldFig5a.keys()

for key in histo_unfoldFig5a.keys():
    print(key, type(histo_unfoldFig5a[key]), type(histo_unfoldFig5a[key][0]))

mmed_Fig5 = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig5.values = histo_unfoldFig5a["x_edges"]

# y-axis: N events
unfoldFig5a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig5a.values = histo_unfoldFig5a["y"]

unc_unfoldFig5a = Uncertainty("", is_symmetric=True)
unc_unfoldFig5a.values = histo_unfoldFig5a["dy"]

unfoldFig5a.add_uncertainty(unc_unfoldFig5a)

unfoldFig5b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig5b.values = histo_unfoldFig5b["y"]

unc_unfoldFig5b = Uncertainty("", is_symmetric=True)
unc_unfoldFig5b.values = histo_unfoldFig5b["dy"]

unfoldFig5b.add_uncertainty(unc_unfoldFig5b)

unfoldFig5c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig5c.values = histo_unfoldFig5c["y"]

unc_unfoldFig5c = Uncertainty("", is_symmetric=True)
unc_unfoldFig5c.values = histo_unfoldFig5c["dy"]

unfoldFig5c.add_uncertainty(unc_unfoldFig5c)

unfoldFig5a.scale_values(lumi_sf)
unfoldFig5b.scale_values(lumi_sf)
unfoldFig5c.scale_values(lumi_sf)

tableFig5.add_variable(mmed_Fig5)
tableFig5.add_variable(unfoldFig5a)
tableFig5.add_variable(unfoldFig5b)
tableFig5.add_variable(unfoldFig5c)
submission.add_table(tableFig5)
### End Fig5

### Begin Fig6
reader_Fig6a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPt_nsel0_dy3_rebin1_default.root")
reader_Fig6b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPt_nsel1_dy3_rebin1_default.root")
reader_Fig6c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPt_nsel2_dy3_rebin1_default.root")

tableFig6 = Table("Figure 6")
tableFig6.description = "The measured absolute cross sections in bins of Z pt, using dressed level leptons. The cross sections are normalized by the bin width."
tableFig6.location = "Data from Figure 6"
tableFig6.keywords["observables"] = ["N"]

histo_unfoldFig6a = reader_Fig6a.read_hist_1d("unfold")
histo_unfoldFig6b = reader_Fig6b.read_hist_1d("unfold")
histo_unfoldFig6c = reader_Fig6c.read_hist_1d("unfold")

histo_unfoldFig6a.keys()

for key in histo_unfoldFig6a.keys():
    print(key, type(histo_unfoldFig6a[key]), type(histo_unfoldFig6a[key][0]))

mmed_Fig6 = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig6.values = histo_unfoldFig6a["x_edges"]

# y-axis: N events
unfoldFig6a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig6a.values = histo_unfoldFig6a["y"]

unc_unfoldFig6a = Uncertainty("", is_symmetric=True)
unc_unfoldFig6a.values = histo_unfoldFig6a["dy"]

unfoldFig6a.add_uncertainty(unc_unfoldFig6a)

unfoldFig6b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig6b.values = histo_unfoldFig6b["y"]

unc_unfoldFig6b = Uncertainty("", is_symmetric=True)
unc_unfoldFig6b.values = histo_unfoldFig6b["dy"]

unfoldFig6b.add_uncertainty(unc_unfoldFig6b)

unfoldFig6c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig6c.values = histo_unfoldFig6c["y"]

unc_unfoldFig6c = Uncertainty("", is_symmetric=True)
unc_unfoldFig6c.values = histo_unfoldFig6c["dy"]

unfoldFig6c.add_uncertainty(unc_unfoldFig6c)

unfoldFig6a.scale_values(lumi_sf)
unfoldFig6b.scale_values(lumi_sf)
unfoldFig6c.scale_values(lumi_sf)

tableFig6.add_variable(mmed_Fig6)
tableFig6.add_variable(unfoldFig6a)
tableFig6.add_variable(unfoldFig6b)
tableFig6.add_variable(unfoldFig6c)
submission.add_table(tableFig6)
### End Fig6

### Begin Fig8
reader_Fig8a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPhiStar_nsel0_dy3_rebin1_default.root")
reader_Fig8b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPhiStar_nsel1_dy3_rebin1_default.root")
reader_Fig8c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPhiStar_nsel2_dy3_rebin1_default.root")

tableFig8 = Table("Figure 8")
tableFig8.description = "The measured absolute cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$, using dressed level leptons. The cross sections are normalized by the bin width."
tableFig8.location = "Data from Figure 8"
tableFig8.keywords["observables"] = ["N"]

histo_unfoldFig8a = reader_Fig8a.read_hist_1d("unfold")
histo_unfoldFig8b = reader_Fig8b.read_hist_1d("unfold")
histo_unfoldFig8c = reader_Fig8c.read_hist_1d("unfold")

histo_unfoldFig8a.keys()

for key in histo_unfoldFig8a.keys():
    print(key, type(histo_unfoldFig8a[key]), type(histo_unfoldFig8a[key][0]))

mmed_Fig8 = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig8.values = histo_unfoldFig8a["x_edges"]

# y-axis: N events
unfoldFig8a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig8a.values = histo_unfoldFig8a["y"]

unc_unfoldFig8a = Uncertainty("", is_symmetric=True)
unc_unfoldFig8a.values = histo_unfoldFig8a["dy"]

unfoldFig8a.add_uncertainty(unc_unfoldFig8a)

unfoldFig8b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig8b.values = histo_unfoldFig8b["y"]

unc_unfoldFig8b = Uncertainty("", is_symmetric=True)
unc_unfoldFig8b.values = histo_unfoldFig8b["dy"]

unfoldFig8b.add_uncertainty(unc_unfoldFig8b)

unfoldFig8c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFig8c.values = histo_unfoldFig8c["y"]

unc_unfoldFig8c = Uncertainty("", is_symmetric=True)
unc_unfoldFig8c.values = histo_unfoldFig8c["dy"]

unfoldFig8c.add_uncertainty(unc_unfoldFig8c)

unfoldFig8a.scale_values(lumi_sf)
unfoldFig8b.scale_values(lumi_sf)
unfoldFig8c.scale_values(lumi_sf)

tableFig8.add_variable(mmed_Fig8)
tableFig8.add_variable(unfoldFig8a)
tableFig8.add_variable(unfoldFig8b)
tableFig8.add_variable(unfoldFig8c)
submission.add_table(tableFig8)
### End Fig8

### Begin Fig9to13
reader_Fig9to13a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap0_nsel2_dy3_rebin1_default.root")
reader_Fig9to13b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap1_nsel2_dy3_rebin1_default.root")
reader_Fig9to13c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap2_nsel2_dy3_rebin1_default.root")
reader_Fig9to13d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap3_nsel2_dy3_rebin1_default.root")
reader_Fig9to13e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfoldingSystPtRap4_nsel2_dy3_rebin1_default.root")

tableFig9to13 = Table("Figures 9 to 13")
tableFig9to13.description = "The measured absolute cross sections in bins of Z pt different |y(Z)| bins, using dressed level leptons. The cross sections are normalized by the bin width."
tableFig9to13.location = "Data from Figures 9 to 13"
tableFig9to13.keywords["observables"] = ["N"]

histo_unfoldFig9to13a = reader_Fig9to13a.read_hist_1d("unfold")
histo_unfoldFig9to13b = reader_Fig9to13b.read_hist_1d("unfold")
histo_unfoldFig9to13c = reader_Fig9to13c.read_hist_1d("unfold")
histo_unfoldFig9to13d = reader_Fig9to13d.read_hist_1d("unfold")
histo_unfoldFig9to13e = reader_Fig9to13e.read_hist_1d("unfold")

histo_unfoldFig9to13a.keys()

for key in histo_unfoldFig9to13a.keys():
    print(key, type(histo_unfoldFig9to13a[key]), type(histo_unfoldFig9to13a[key][0]))

mmed_Fig9to13 = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig9to13.values = histo_unfoldFig9to13a["x_edges"]

# y-axis: N events
unfoldFig9to13a = Variable("Dilepton cross section (pb) in 0 < |y(Z)| < 0.4 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13a.values = histo_unfoldFig9to13a["y"]

unc_unfoldFig9to13a = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13a.values = histo_unfoldFig9to13a["dy"]

unfoldFig9to13a.add_uncertainty(unc_unfoldFig9to13a)

unfoldFig9to13b = Variable("Dilepton cross section (pb) in 0.4 < |y(Z)| < 0.8 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13b.values = histo_unfoldFig9to13b["y"]

unc_unfoldFig9to13b = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13b.values = histo_unfoldFig9to13b["dy"]

unfoldFig9to13b.add_uncertainty(unc_unfoldFig9to13b)

unfoldFig9to13c = Variable("Dilepton cross section (pb) in 0.8 < |y(Z)| < 1.2 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13c.values = histo_unfoldFig9to13c["y"]

unc_unfoldFig9to13c = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13c.values = histo_unfoldFig9to13c["dy"]

unfoldFig9to13c.add_uncertainty(unc_unfoldFig9to13c)

unfoldFig9to13d = Variable("Dilepton cross section (pb) in 1.2 < |y(Z)| < 1.6 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13d.values = histo_unfoldFig9to13d["y"]

unc_unfoldFig9to13d = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13d.values = histo_unfoldFig9to13d["dy"]

unfoldFig9to13d.add_uncertainty(unc_unfoldFig9to13d)

unfoldFig9to13e = Variable("Dilepton cross section (pb) in 1.6 < |y(Z)| < 2.4 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13e.values = histo_unfoldFig9to13e["y"]

unc_unfoldFig9to13e = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13e.values = histo_unfoldFig9to13e["dy"]

unfoldFig9to13e.add_uncertainty(unc_unfoldFig9to13e)

unfoldFig9to13a.scale_values(lumi_sf)
unfoldFig9to13b.scale_values(lumi_sf)
unfoldFig9to13c.scale_values(lumi_sf)
unfoldFig9to13d.scale_values(lumi_sf)
unfoldFig9to13e.scale_values(lumi_sf)

tableFig9to13.add_variable(mmed_Fig9to13)
tableFig9to13.add_variable(unfoldFig9to13a)
tableFig9to13.add_variable(unfoldFig9to13b)
tableFig9to13.add_variable(unfoldFig9to13c)
tableFig9to13.add_variable(unfoldFig9to13d)
tableFig9to13.add_variable(unfoldFig9to13e)
submission.add_table(tableFig9to13)
### End Fig9to13

### Begin Fig14a
reader_Fig14a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPt_nsel2_dy3_rebin1_default.root")

tableFig14a = Table("Figure 14a")
tableFig14a.description = "The measured normalized cross sections in bins of Z pt, using dressed level leptons. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFig14a.location = "Data from Figure 14a"
tableFig14a.keywords["observables"] = ["N"]

histo_unfoldFig14a = reader_Fig14a.read_hist_1d("unfold")

histo_unfoldFig14a.keys()

inv_total_sum = 1.0/sum(histo_unfoldFig14a["y"])
for key in histo_unfoldFig14a.keys():
    print(key, type(histo_unfoldFig14a[key]), type(histo_unfoldFig14a[key][0]))

mmed_Fig14a = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig14a.values = histo_unfoldFig14a["x_edges"]

# y-axis: N events
unfoldFig14a = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14a.values = histo_unfoldFig14a["y"]

unc_unfoldFig14a = Uncertainty("", is_symmetric=True)
unc_unfoldFig14a.values = histo_unfoldFig14a["dy"]

unfoldFig14a.add_uncertainty(unc_unfoldFig14a)

unfoldFig14a.scale_values(inv_total_sum)

tableFig14a.add_variable(mmed_Fig14a)
tableFig14a.add_variable(unfoldFig14a)
submission.add_table(tableFig14a)
### End Fig14a

### Begin Fig14b
reader_Fig14b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPhiStar_nsel2_dy3_rebin1_default.root")

tableFig14b = Table("Figure 14b")
tableFig14b.description = "The measured normalized cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$, using dressed level leptons. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFig14b.location = "Data from Figure 14b"
tableFig14b.keywords["observables"] = ["N"]

histo_unfoldFig14b = reader_Fig14b.read_hist_1d("unfold")

histo_unfoldFig14b.keys()

inv_total_sum = 1.0/sum(histo_unfoldFig14b["y"])
for key in histo_unfoldFig14b.keys():
    print(key, type(histo_unfoldFig14b[key]), type(histo_unfoldFig14b[key][0]))

mmed_Fig14b = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_Fig14b.values = histo_unfoldFig14b["x_edges"]

# y-axis: N events
unfoldFig14b = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14b.values = histo_unfoldFig14b["y"]

unc_unfoldFig14b = Uncertainty("", is_symmetric=True)
unc_unfoldFig14b.values = histo_unfoldFig14b["dy"]

unfoldFig14b.add_uncertainty(unc_unfoldFig14b)

unfoldFig14b.scale_values(inv_total_sum)

tableFig14b.add_variable(mmed_Fig14b)
tableFig14b.add_variable(unfoldFig14b)
submission.add_table(tableFig14b)
### End Fig14b

### Begin Fig14c
reader_Fig14c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystRap_nsel2_dy3_rebin1_default.root")

tableFig14c = Table("Figure 14c")
tableFig14c.description = "The measured normalized cross sections in bins of |y(Z)|, using dressed level leptons. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFig14c.location = "Data from Figure 14c"
tableFig14c.keywords["observables"] = ["N"]

histo_unfoldFig14c = reader_Fig14c.read_hist_1d("unfold")

histo_unfoldFig14c.keys()

inv_total_sum = 1.0/sum(histo_unfoldFig14c["y"])
for key in histo_unfoldFig14c.keys():
    print(key, type(histo_unfoldFig14c[key]), type(histo_unfoldFig14c[key][0]))

mmed_Fig14c = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_Fig14c.values = histo_unfoldFig14c["x_edges"]

# y-axis: N events
unfoldFig14c = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14c.values = histo_unfoldFig14c["y"]

unc_unfoldFig14c = Uncertainty("", is_symmetric=True)
unc_unfoldFig14c.values = histo_unfoldFig14c["dy"]

unfoldFig14c.add_uncertainty(unc_unfoldFig14c)

unfoldFig14c.scale_values(inv_total_sum)

tableFig14c.add_variable(mmed_Fig14c)
tableFig14c.add_variable(unfoldFig14c)
submission.add_table(tableFig14c)
### End Fig14c

### Begin Fig15to19
reader_Fig15to19a = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPtRap0_nsel2_dy3_rebin1_default.root")
reader_Fig15to19b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPtRap1_nsel2_dy3_rebin1_default.root")
reader_Fig15to19c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPtRap2_nsel2_dy3_rebin1_default.root")
reader_Fig15to19d = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPtRap3_nsel2_dy3_rebin1_default.root")
reader_Fig15to19e = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPtRap4_nsel2_dy3_rebin1_default.root")

tableFig15to19 = Table("Figures 15 to 19")
tableFig15to19.description = "The measured normalized cross sections in bins of Z pt in |y(Z)| bins, using dressed level leptons. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFig15to19.location = "Data from Figure 15 to 19"
tableFig15to19.keywords["observables"] = ["N"]

histo_unfoldFig15to19a = reader_Fig15to19a.read_hist_1d("unfold")
histo_unfoldFig15to19b = reader_Fig15to19b.read_hist_1d("unfold")
histo_unfoldFig15to19c = reader_Fig15to19c.read_hist_1d("unfold")
histo_unfoldFig15to19d = reader_Fig15to19d.read_hist_1d("unfold")
histo_unfoldFig15to19e = reader_Fig15to19e.read_hist_1d("unfold")

histo_unfoldFig15to19a.keys()

inv_total_suma = 1.0/sum(histo_unfoldFig15to19a["y"])
inv_total_sumb = 1.0/sum(histo_unfoldFig15to19b["y"])
inv_total_sumc = 1.0/sum(histo_unfoldFig15to19c["y"])
inv_total_sumd = 1.0/sum(histo_unfoldFig15to19d["y"])
inv_total_sume = 1.0/sum(histo_unfoldFig15to19e["y"])
for key in histo_unfoldFig15to19a.keys():
    print(key, type(histo_unfoldFig15to19a[key]), type(histo_unfoldFig15to19a[key][0]))

mmed_Fig15to19 = Variable("$p_{T}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig15to19.values = histo_unfoldFig15to19a["x_edges"]

# y-axis: N events
unfoldFig15to19a = Variable("Normalized dilepton cross section in 0 < |y(Z)| < 0.4", is_independent=False, is_binned=False, units="")
unfoldFig15to19a.values = histo_unfoldFig15to19a["y"]
unc_unfoldFig15to19a = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19a.values = histo_unfoldFig15to19a["dy"]
unfoldFig15to19a.add_uncertainty(unc_unfoldFig15to19a)

unfoldFig15to19b = Variable("Normalized dilepton cross section in 0.4 < |y(Z)| < 0.8", is_independent=False, is_binned=False, units="")
unfoldFig15to19b.values = histo_unfoldFig15to19b["y"]
unc_unfoldFig15to19b = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19b.values = histo_unfoldFig15to19b["dy"]
unfoldFig15to19b.add_uncertainty(unc_unfoldFig15to19b)

unfoldFig15to19c = Variable("Normalized dilepton cross section in 0.8 < |y(Z)| < 1.2", is_independent=False, is_binned=False, units="")
unfoldFig15to19c.values = histo_unfoldFig15to19c["y"]
unc_unfoldFig15to19c = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19c.values = histo_unfoldFig15to19c["dy"]
unfoldFig15to19c.add_uncertainty(unc_unfoldFig15to19c)

unfoldFig15to19d = Variable("Normalized dilepton cross section in 1.2 < |y(Z)| < 1.6", is_independent=False, is_binned=False, units="")
unfoldFig15to19d.values = histo_unfoldFig15to19d["y"]
unc_unfoldFig15to19d = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19d.values = histo_unfoldFig15to19d["dy"]
unfoldFig15to19d.add_uncertainty(unc_unfoldFig15to19d)

unfoldFig15to19e = Variable("Normalized dilepton cross section in 1.6 < |y(Z)| < 2.4", is_independent=False, is_binned=False, units="")
unfoldFig15to19e.values = histo_unfoldFig15to19e["y"]
unc_unfoldFig15to19e = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19e.values = histo_unfoldFig15to19e["dy"]
unfoldFig15to19e.add_uncertainty(unc_unfoldFig15to19e)

unfoldFig15to19a.scale_values(inv_total_suma)
unfoldFig15to19b.scale_values(inv_total_sumb)
unfoldFig15to19c.scale_values(inv_total_sumc)
unfoldFig15to19d.scale_values(inv_total_sumd)
unfoldFig15to19e.scale_values(inv_total_sume)

tableFig15to19.add_variable(mmed_Fig15to19)
tableFig15to19.add_variable(unfoldFig15to19a)
tableFig15to19.add_variable(unfoldFig15to19b)
tableFig15to19.add_variable(unfoldFig15to19c)
tableFig15to19.add_variable(unfoldFig15to19d)
tableFig15to19.add_variable(unfoldFig15to19e)
submission.add_table(tableFig15to19)
### End Fig15to19

### Begin covariance mumu dressed
# Create a reader for the input file
reader_covariance_mm_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPt.root")
# Read the histogram
data_covariance_mm_Pt = reader_covariance_mm_Pt.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Pt.values = data_covariance_mm_Pt["x_edges"]
y_covariance_mm_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Pt.values = data_covariance_mm_Pt["y"]
z_covariance_mm_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Pt.values = data_covariance_mm_Pt["z"]

table_covariance_mm_Pt = Table("Covariance Matrix auxiliary Figure 1a")
table_covariance_mm_Pt.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt in the dimuon final state."
table_covariance_mm_Pt.location = "Supplementary material"
for var in [x_covariance_mm_Pt,y_covariance_mm_Pt,z_covariance_mm_Pt]:
    table_covariance_mm_Pt.add_variable(var)
submission.add_table(table_covariance_mm_Pt)

# Create a reader for the input file
reader_covariance_mm_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystRap.root")
# Read the histogram
data_covariance_mm_Rap = reader_covariance_mm_Rap.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Rap.values = data_covariance_mm_Rap["x_edges"]
y_covariance_mm_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Rap.values = data_covariance_mm_Rap["y"]
z_covariance_mm_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Rap.values = data_covariance_mm_Rap["z"]

table_covariance_mm_Rap = Table("Covariance Matrix auxiliary Figure 1b")
table_covariance_mm_Rap.description = "Covariance matrix using dressed level leptons for all bins used in bins of |y(Z)| in the dimuon final state."
table_covariance_mm_Rap.location = "Supplementary material"
for var in [x_covariance_mm_Rap,y_covariance_mm_Rap,z_covariance_mm_Rap]:
    table_covariance_mm_Rap.add_variable(var)
submission.add_table(table_covariance_mm_Rap)

# Create a reader for the input file
reader_covariance_mm_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPhiStar.root")
# Read the histogram
data_covariance_mm_PhiStar = reader_covariance_mm_PhiStar.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["x_edges"]
y_covariance_mm_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["y"]
z_covariance_mm_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["z"]

table_covariance_mm_PhiStar = Table("Covariance Matrix auxiliary Figure 1c")
table_covariance_mm_PhiStar.description = "Covariance matrix using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dimuon final state."
table_covariance_mm_PhiStar.location = "Supplementary material"
for var in [x_covariance_mm_PhiStar,y_covariance_mm_PhiStar,z_covariance_mm_PhiStar]:
    table_covariance_mm_PhiStar.add_variable(var)
submission.add_table(table_covariance_mm_PhiStar)

# Create a reader for the input file
reader_covariance_mm_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPtRap0.root")
# Read the histogram
data_covariance_mm_PtRap0 = reader_covariance_mm_PtRap0.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["x_edges"]
y_covariance_mm_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["y"]
z_covariance_mm_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["z"]

table_covariance_mm_PtRap0 = Table("Covariance Matrix auxiliary Figure 1d")
table_covariance_mm_PtRap0.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dimuon final state."
table_covariance_mm_PtRap0.location = "Supplementary material"
for var in [x_covariance_mm_PtRap0,y_covariance_mm_PtRap0,z_covariance_mm_PtRap0]:
    table_covariance_mm_PtRap0.add_variable(var)
submission.add_table(table_covariance_mm_PtRap0)

# Create a reader for the input file
reader_covariance_mm_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPtRap1.root")
# Read the histogram
data_covariance_mm_PtRap1 = reader_covariance_mm_PtRap1.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["x_edges"]
y_covariance_mm_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["y"]
z_covariance_mm_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["z"]

table_covariance_mm_PtRap1 = Table("Covariance Matrix auxiliary Figure 1e")
table_covariance_mm_PtRap1.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dimuon final state."
table_covariance_mm_PtRap1.location = "Supplementary material"
for var in [x_covariance_mm_PtRap1,y_covariance_mm_PtRap1,z_covariance_mm_PtRap1]:
    table_covariance_mm_PtRap1.add_variable(var)
submission.add_table(table_covariance_mm_PtRap1)

# Create a reader for the input file
reader_covariance_mm_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPtRap2.root")
# Read the histogram
data_covariance_mm_PtRap2 = reader_covariance_mm_PtRap2.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["x_edges"]
y_covariance_mm_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["y"]
z_covariance_mm_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["z"]

table_covariance_mm_PtRap2 = Table("Covariance Matrix auxiliary Figure 1f")
table_covariance_mm_PtRap2.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dimuon final state."
table_covariance_mm_PtRap2.location = "Supplementary material"
for var in [x_covariance_mm_PtRap2,y_covariance_mm_PtRap2,z_covariance_mm_PtRap2]:
    table_covariance_mm_PtRap2.add_variable(var)
submission.add_table(table_covariance_mm_PtRap2)

# Create a reader for the input file
reader_covariance_mm_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPtRap3.root")
# Read the histogram
data_covariance_mm_PtRap3 = reader_covariance_mm_PtRap3.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["x_edges"]
y_covariance_mm_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["y"]
z_covariance_mm_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["z"]

table_covariance_mm_PtRap3 = Table("Covariance Matrix auxiliary Figure 1g")
table_covariance_mm_PtRap3.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dimuon final state."
table_covariance_mm_PtRap3.location = "Supplementary material"
for var in [x_covariance_mm_PtRap3,y_covariance_mm_PtRap3,z_covariance_mm_PtRap3]:
    table_covariance_mm_PtRap3.add_variable(var)
submission.add_table(table_covariance_mm_PtRap3)

# Create a reader for the input file
reader_covariance_mm_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03_SystPtRap4.root")
# Read the histogram
data_covariance_mm_PtRap4 = reader_covariance_mm_PtRap4.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["x_edges"]
y_covariance_mm_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["y"]
z_covariance_mm_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["z"]

table_covariance_mm_PtRap4 = Table("Covariance Matrix auxiliary Figure 1h")
table_covariance_mm_PtRap4.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dimuon final state."
table_covariance_mm_PtRap4.location = "Supplementary material"
for var in [x_covariance_mm_PtRap4,y_covariance_mm_PtRap4,z_covariance_mm_PtRap4]:
    table_covariance_mm_PtRap4.add_variable(var)
submission.add_table(table_covariance_mm_PtRap4)
### End covariance mumu

### Begin covariance ee dressed
# Create a reader for the input file
reader_covariance_ee_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPt.root")
# Read the histogram
data_covariance_ee_Pt = reader_covariance_ee_Pt.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Pt.values = data_covariance_ee_Pt["x_edges"]
y_covariance_ee_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Pt.values = data_covariance_ee_Pt["y"]
z_covariance_ee_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Pt.values = data_covariance_ee_Pt["z"]

table_covariance_ee_Pt = Table("Covariance Matrix auxiliary Figure 2a")
table_covariance_ee_Pt.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt in the dielectron final state."
table_covariance_ee_Pt.location = "Supplementary material"
for var in [x_covariance_ee_Pt,y_covariance_ee_Pt,z_covariance_ee_Pt]:
    table_covariance_ee_Pt.add_variable(var)
submission.add_table(table_covariance_ee_Pt)

# Create a reader for the input file
reader_covariance_ee_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystRap.root")
# Read the histogram
data_covariance_ee_Rap = reader_covariance_ee_Rap.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Rap.values = data_covariance_ee_Rap["x_edges"]
y_covariance_ee_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Rap.values = data_covariance_ee_Rap["y"]
z_covariance_ee_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Rap.values = data_covariance_ee_Rap["z"]

table_covariance_ee_Rap = Table("Covariance Matrix auxiliary Figure 2b")
table_covariance_ee_Rap.description = "Covariance matrix using dressed level leptons for all bins used in bins of |y(Z)| in the dielectron final state."
table_covariance_ee_Rap.location = "Supplementary material"
for var in [x_covariance_ee_Rap,y_covariance_ee_Rap,z_covariance_ee_Rap]:
    table_covariance_ee_Rap.add_variable(var)
submission.add_table(table_covariance_ee_Rap)

# Create a reader for the input file
reader_covariance_ee_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPhiStar.root")
# Read the histogram
data_covariance_ee_PhiStar = reader_covariance_ee_PhiStar.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["x_edges"]
y_covariance_ee_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["y"]
z_covariance_ee_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["z"]

table_covariance_ee_PhiStar = Table("Covariance Matrix auxiliary Figure 2c")
table_covariance_ee_PhiStar.description = "Covariance matrix using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dielectron final state."
table_covariance_ee_PhiStar.location = "Supplementary material"
for var in [x_covariance_ee_PhiStar,y_covariance_ee_PhiStar,z_covariance_ee_PhiStar]:
    table_covariance_ee_PhiStar.add_variable(var)
submission.add_table(table_covariance_ee_PhiStar)

# Create a reader for the input file
reader_covariance_ee_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPtRap0.root")
# Read the histogram
data_covariance_ee_PtRap0 = reader_covariance_ee_PtRap0.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["x_edges"]
y_covariance_ee_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["y"]
z_covariance_ee_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["z"]

table_covariance_ee_PtRap0 = Table("Covariance Matrix auxiliary Figure 2d")
table_covariance_ee_PtRap0.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dielectron final state."
table_covariance_ee_PtRap0.location = "Supplementary material"
for var in [x_covariance_ee_PtRap0,y_covariance_ee_PtRap0,z_covariance_ee_PtRap0]:
    table_covariance_ee_PtRap0.add_variable(var)
submission.add_table(table_covariance_ee_PtRap0)

# Create a reader for the input file
reader_covariance_ee_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPtRap1.root")
# Read the histogram
data_covariance_ee_PtRap1 = reader_covariance_ee_PtRap1.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["x_edges"]
y_covariance_ee_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["y"]
z_covariance_ee_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["z"]

table_covariance_ee_PtRap1 = Table("Covariance Matrix auxiliary Figure 2e")
table_covariance_ee_PtRap1.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dielectron final state."
table_covariance_ee_PtRap1.location = "Supplementary material"
for var in [x_covariance_ee_PtRap1,y_covariance_ee_PtRap1,z_covariance_ee_PtRap1]:
    table_covariance_ee_PtRap1.add_variable(var)
submission.add_table(table_covariance_ee_PtRap1)

# Create a reader for the input file
reader_covariance_ee_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPtRap2.root")
# Read the histogram
data_covariance_ee_PtRap2 = reader_covariance_ee_PtRap2.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["x_edges"]
y_covariance_ee_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["y"]
z_covariance_ee_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["z"]

table_covariance_ee_PtRap2 = Table("Covariance Matrix auxiliary Figure 2f")
table_covariance_ee_PtRap2.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dielectron final state."
table_covariance_ee_PtRap2.location = "Supplementary material"
for var in [x_covariance_ee_PtRap2,y_covariance_ee_PtRap2,z_covariance_ee_PtRap2]:
    table_covariance_ee_PtRap2.add_variable(var)
submission.add_table(table_covariance_ee_PtRap2)

# Create a reader for the input file
reader_covariance_ee_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPtRap3.root")
# Read the histogram
data_covariance_ee_PtRap3 = reader_covariance_ee_PtRap3.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["x_edges"]
y_covariance_ee_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["y"]
z_covariance_ee_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["z"]

table_covariance_ee_PtRap3 = Table("Covariance Matrix auxiliary Figure 2g")
table_covariance_ee_PtRap3.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dielectron final state."
table_covariance_ee_PtRap3.location = "Supplementary material"
for var in [x_covariance_ee_PtRap3,y_covariance_ee_PtRap3,z_covariance_ee_PtRap3]:
    table_covariance_ee_PtRap3.add_variable(var)
submission.add_table(table_covariance_ee_PtRap3)

# Create a reader for the input file
reader_covariance_ee_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13_SystPtRap4.root")
# Read the histogram
data_covariance_ee_PtRap4 = reader_covariance_ee_PtRap4.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["x_edges"]
y_covariance_ee_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["y"]
z_covariance_ee_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["z"]

table_covariance_ee_PtRap4 = Table("Covariance Matrix auxiliary Figure 2h")
table_covariance_ee_PtRap4.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
table_covariance_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_ee_PtRap4)
### End covariance ee


### Begin covariance mumu born
# Create a reader for the input file
reader_covariance_mm_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPt.root")
# Read the histogram
data_covariance_mm_Pt = reader_covariance_mm_Pt.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Pt.values = data_covariance_mm_Pt["x_edges"]
y_covariance_mm_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Pt.values = data_covariance_mm_Pt["y"]
z_covariance_mm_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Pt.values = data_covariance_mm_Pt["z"]

table_covariance_mm_Pt = Table("Covariance Matrix auxiliary Figure 3a")
table_covariance_mm_Pt.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt in the dimuon final state."
table_covariance_mm_Pt.location = "Supplementary material"
for var in [x_covariance_mm_Pt,y_covariance_mm_Pt,z_covariance_mm_Pt]:
    table_covariance_mm_Pt.add_variable(var)
submission.add_table(table_covariance_mm_Pt)

# Create a reader for the input file
reader_covariance_mm_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystRap.root")
# Read the histogram
data_covariance_mm_Rap = reader_covariance_mm_Rap.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Rap.values = data_covariance_mm_Rap["x_edges"]
y_covariance_mm_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Rap.values = data_covariance_mm_Rap["y"]
z_covariance_mm_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Rap.values = data_covariance_mm_Rap["z"]

table_covariance_mm_Rap = Table("Covariance Matrix auxiliary Figure 3b")
table_covariance_mm_Rap.description = "Covariance matrix using born level leptons for all bins used in bins of |y(Z)| in the dimuon final state."
table_covariance_mm_Rap.location = "Supplementary material"
for var in [x_covariance_mm_Rap,y_covariance_mm_Rap,z_covariance_mm_Rap]:
    table_covariance_mm_Rap.add_variable(var)
submission.add_table(table_covariance_mm_Rap)

# Create a reader for the input file
reader_covariance_mm_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPhiStar.root")
# Read the histogram
data_covariance_mm_PhiStar = reader_covariance_mm_PhiStar.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["x_edges"]
y_covariance_mm_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["y"]
z_covariance_mm_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["z"]

table_covariance_mm_PhiStar = Table("Covariance Matrix auxiliary Figure 3c")
table_covariance_mm_PhiStar.description = "Covariance matrix using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dimuon final state."
table_covariance_mm_PhiStar.location = "Supplementary material"
for var in [x_covariance_mm_PhiStar,y_covariance_mm_PhiStar,z_covariance_mm_PhiStar]:
    table_covariance_mm_PhiStar.add_variable(var)
submission.add_table(table_covariance_mm_PhiStar)

# Create a reader for the input file
reader_covariance_mm_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPtRap0.root")
# Read the histogram
data_covariance_mm_PtRap0 = reader_covariance_mm_PtRap0.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["x_edges"]
y_covariance_mm_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["y"]
z_covariance_mm_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["z"]

table_covariance_mm_PtRap0 = Table("Covariance Matrix auxiliary Figure 3d")
table_covariance_mm_PtRap0.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dimuon final state."
table_covariance_mm_PtRap0.location = "Supplementary material"
for var in [x_covariance_mm_PtRap0,y_covariance_mm_PtRap0,z_covariance_mm_PtRap0]:
    table_covariance_mm_PtRap0.add_variable(var)
submission.add_table(table_covariance_mm_PtRap0)

# Create a reader for the input file
reader_covariance_mm_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPtRap1.root")
# Read the histogram
data_covariance_mm_PtRap1 = reader_covariance_mm_PtRap1.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["x_edges"]
y_covariance_mm_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["y"]
z_covariance_mm_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["z"]

table_covariance_mm_PtRap1 = Table("Covariance Matrix auxiliary Figure 3e")
table_covariance_mm_PtRap1.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dimuon final state."
table_covariance_mm_PtRap1.location = "Supplementary material"
for var in [x_covariance_mm_PtRap1,y_covariance_mm_PtRap1,z_covariance_mm_PtRap1]:
    table_covariance_mm_PtRap1.add_variable(var)
submission.add_table(table_covariance_mm_PtRap1)

# Create a reader for the input file
reader_covariance_mm_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPtRap2.root")
# Read the histogram
data_covariance_mm_PtRap2 = reader_covariance_mm_PtRap2.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["x_edges"]
y_covariance_mm_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["y"]
z_covariance_mm_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["z"]

table_covariance_mm_PtRap2 = Table("Covariance Matrix auxiliary Figure 3f")
table_covariance_mm_PtRap2.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dimuon final state."
table_covariance_mm_PtRap2.location = "Supplementary material"
for var in [x_covariance_mm_PtRap2,y_covariance_mm_PtRap2,z_covariance_mm_PtRap2]:
    table_covariance_mm_PtRap2.add_variable(var)
submission.add_table(table_covariance_mm_PtRap2)

# Create a reader for the input file
reader_covariance_mm_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPtRap3.root")
# Read the histogram
data_covariance_mm_PtRap3 = reader_covariance_mm_PtRap3.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["x_edges"]
y_covariance_mm_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["y"]
z_covariance_mm_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["z"]

table_covariance_mm_PtRap3 = Table("Covariance Matrix auxiliary Figure 3g")
table_covariance_mm_PtRap3.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dimuon final state."
table_covariance_mm_PtRap3.location = "Supplementary material"
for var in [x_covariance_mm_PtRap3,y_covariance_mm_PtRap3,z_covariance_mm_PtRap3]:
    table_covariance_mm_PtRap3.add_variable(var)
submission.add_table(table_covariance_mm_PtRap3)

# Create a reader for the input file
reader_covariance_mm_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03_SystPtRap4.root")
# Read the histogram
data_covariance_mm_PtRap4 = reader_covariance_mm_PtRap4.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["x_edges"]
y_covariance_mm_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["y"]
z_covariance_mm_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["z"]

table_covariance_mm_PtRap4 = Table("Covariance Matrix auxiliary Figure 3h")
table_covariance_mm_PtRap4.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dimuon final state."
table_covariance_mm_PtRap4.location = "Supplementary material"
for var in [x_covariance_mm_PtRap4,y_covariance_mm_PtRap4,z_covariance_mm_PtRap4]:
    table_covariance_mm_PtRap4.add_variable(var)
submission.add_table(table_covariance_mm_PtRap4)
### End covariance mumu

### Begin covariance ee born
# Create a reader for the input file
reader_covariance_ee_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPt.root")
# Read the histogram
data_covariance_ee_Pt = reader_covariance_ee_Pt.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Pt.values = data_covariance_ee_Pt["x_edges"]
y_covariance_ee_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Pt.values = data_covariance_ee_Pt["y"]
z_covariance_ee_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Pt.values = data_covariance_ee_Pt["z"]

table_covariance_ee_Pt = Table("Covariance Matrix auxiliary Figure 4a")
table_covariance_ee_Pt.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt in the dielectron final state."
table_covariance_ee_Pt.location = "Supplementary material"
for var in [x_covariance_ee_Pt,y_covariance_ee_Pt,z_covariance_ee_Pt]:
    table_covariance_ee_Pt.add_variable(var)
submission.add_table(table_covariance_ee_Pt)

# Create a reader for the input file
reader_covariance_ee_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystRap.root")
# Read the histogram
data_covariance_ee_Rap = reader_covariance_ee_Rap.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Rap.values = data_covariance_ee_Rap["x_edges"]
y_covariance_ee_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Rap.values = data_covariance_ee_Rap["y"]
z_covariance_ee_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Rap.values = data_covariance_ee_Rap["z"]

table_covariance_ee_Rap = Table("Covariance Matrix auxiliary Figure 4b")
table_covariance_ee_Rap.description = "Covariance matrix using born level leptons for all bins used in bins of |y(Z)| in the dielectron final state."
table_covariance_ee_Rap.location = "Supplementary material"
for var in [x_covariance_ee_Rap,y_covariance_ee_Rap,z_covariance_ee_Rap]:
    table_covariance_ee_Rap.add_variable(var)
submission.add_table(table_covariance_ee_Rap)

# Create a reader for the input file
reader_covariance_ee_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPhiStar.root")
# Read the histogram
data_covariance_ee_PhiStar = reader_covariance_ee_PhiStar.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["x_edges"]
y_covariance_ee_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["y"]
z_covariance_ee_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["z"]

table_covariance_ee_PhiStar = Table("Covariance Matrix auxiliary Figure 4c")
table_covariance_ee_PhiStar.description = "Covariance matrix using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dielectron final state."
table_covariance_ee_PhiStar.location = "Supplementary material"
for var in [x_covariance_ee_PhiStar,y_covariance_ee_PhiStar,z_covariance_ee_PhiStar]:
    table_covariance_ee_PhiStar.add_variable(var)
submission.add_table(table_covariance_ee_PhiStar)

# Create a reader for the input file
reader_covariance_ee_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPtRap0.root")
# Read the histogram
data_covariance_ee_PtRap0 = reader_covariance_ee_PtRap0.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["x_edges"]
y_covariance_ee_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["y"]
z_covariance_ee_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["z"]

table_covariance_ee_PtRap0 = Table("Covariance Matrix auxiliary Figure 4d")
table_covariance_ee_PtRap0.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dielectron final state."
table_covariance_ee_PtRap0.location = "Supplementary material"
for var in [x_covariance_ee_PtRap0,y_covariance_ee_PtRap0,z_covariance_ee_PtRap0]:
    table_covariance_ee_PtRap0.add_variable(var)
submission.add_table(table_covariance_ee_PtRap0)

# Create a reader for the input file
reader_covariance_ee_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPtRap1.root")
# Read the histogram
data_covariance_ee_PtRap1 = reader_covariance_ee_PtRap1.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["x_edges"]
y_covariance_ee_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["y"]
z_covariance_ee_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["z"]

table_covariance_ee_PtRap1 = Table("Covariance Matrix auxiliary Figure 4e")
table_covariance_ee_PtRap1.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dielectron final state."
table_covariance_ee_PtRap1.location = "Supplementary material"
for var in [x_covariance_ee_PtRap1,y_covariance_ee_PtRap1,z_covariance_ee_PtRap1]:
    table_covariance_ee_PtRap1.add_variable(var)
submission.add_table(table_covariance_ee_PtRap1)

# Create a reader for the input file
reader_covariance_ee_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPtRap2.root")
# Read the histogram
data_covariance_ee_PtRap2 = reader_covariance_ee_PtRap2.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["x_edges"]
y_covariance_ee_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["y"]
z_covariance_ee_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["z"]

table_covariance_ee_PtRap2 = Table("Covariance Matrix auxiliary Figure 4f")
table_covariance_ee_PtRap2.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dielectron final state."
table_covariance_ee_PtRap2.location = "Supplementary material"
for var in [x_covariance_ee_PtRap2,y_covariance_ee_PtRap2,z_covariance_ee_PtRap2]:
    table_covariance_ee_PtRap2.add_variable(var)
submission.add_table(table_covariance_ee_PtRap2)

# Create a reader for the input file
reader_covariance_ee_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPtRap3.root")
# Read the histogram
data_covariance_ee_PtRap3 = reader_covariance_ee_PtRap3.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["x_edges"]
y_covariance_ee_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["y"]
z_covariance_ee_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["z"]

table_covariance_ee_PtRap3 = Table("Covariance Matrix auxiliary Figure 4g")
table_covariance_ee_PtRap3.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dielectron final state."
table_covariance_ee_PtRap3.location = "Supplementary material"
for var in [x_covariance_ee_PtRap3,y_covariance_ee_PtRap3,z_covariance_ee_PtRap3]:
    table_covariance_ee_PtRap3.add_variable(var)
submission.add_table(table_covariance_ee_PtRap3)

# Create a reader for the input file
reader_covariance_ee_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13_SystPtRap4.root")
# Read the histogram
data_covariance_ee_PtRap4 = reader_covariance_ee_PtRap4.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["x_edges"]
y_covariance_ee_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["y"]
z_covariance_ee_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["z"]

table_covariance_ee_PtRap4 = Table("Covariance Matrix auxiliary Figure 4h")
table_covariance_ee_PtRap4.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
table_covariance_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_ee_PtRap4)
### End covariance ee

### Begin covariance mumu dressed
# Create a reader for the input file
reader_covariance_mm_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPt.root")
# Read the histogram
data_covariance_mm_Pt = reader_covariance_mm_Pt.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Pt.values = data_covariance_mm_Pt["x_edges"]
y_covariance_mm_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Pt.values = data_covariance_mm_Pt["y"]
z_covariance_mm_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Pt.values = data_covariance_mm_Pt["z"]

table_covariance_XSRatio_mm_Pt = Table("Covariance Matrix auxiliary Figure 5a")
table_covariance_XSRatio_mm_Pt.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt in the dimuon final state."
table_covariance_XSRatio_mm_Pt.location = "Supplementary material"
for var in [x_covariance_mm_Pt,y_covariance_mm_Pt,z_covariance_mm_Pt]:
    table_covariance_XSRatio_mm_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_Pt)

# Create a reader for the input file
reader_covariance_mm_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystRap.root")
# Read the histogram
data_covariance_mm_Rap = reader_covariance_mm_Rap.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Rap.values = data_covariance_mm_Rap["x_edges"]
y_covariance_mm_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Rap.values = data_covariance_mm_Rap["y"]
z_covariance_mm_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Rap.values = data_covariance_mm_Rap["z"]

table_covariance_XSRatio_mm_Rap = Table("Covariance Matrix auxiliary Figure 5b")
table_covariance_XSRatio_mm_Rap.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of |y(Z)| in the dimuon final state."
table_covariance_XSRatio_mm_Rap.location = "Supplementary material"
for var in [x_covariance_mm_Rap,y_covariance_mm_Rap,z_covariance_mm_Rap]:
    table_covariance_XSRatio_mm_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_Rap)

# Create a reader for the input file
reader_covariance_mm_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_mm_PhiStar = reader_covariance_mm_PhiStar.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["x_edges"]
y_covariance_mm_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["y"]
z_covariance_mm_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["z"]

table_covariance_XSRatio_mm_PhiStar = Table("Covariance Matrix auxiliary Figure 5c")
table_covariance_XSRatio_mm_PhiStar.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dimuon final state."
table_covariance_XSRatio_mm_PhiStar.location = "Supplementary material"
for var in [x_covariance_mm_PhiStar,y_covariance_mm_PhiStar,z_covariance_mm_PhiStar]:
    table_covariance_XSRatio_mm_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PhiStar)

# Create a reader for the input file
reader_covariance_mm_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPtRap0.root")
# Read the histogram
data_covariance_mm_PtRap0 = reader_covariance_mm_PtRap0.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["x_edges"]
y_covariance_mm_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["y"]
z_covariance_mm_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["z"]

table_covariance_XSRatio_mm_PtRap0 = Table("Covariance Matrix auxiliary Figure 5d")
table_covariance_XSRatio_mm_PtRap0.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap0.location = "Supplementary material"
for var in [x_covariance_mm_PtRap0,y_covariance_mm_PtRap0,z_covariance_mm_PtRap0]:
    table_covariance_XSRatio_mm_PtRap0.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap0)

# Create a reader for the input file
reader_covariance_mm_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPtRap1.root")
# Read the histogram
data_covariance_mm_PtRap1 = reader_covariance_mm_PtRap1.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["x_edges"]
y_covariance_mm_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["y"]
z_covariance_mm_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["z"]

table_covariance_XSRatio_mm_PtRap1 = Table("Covariance Matrix auxiliary Figure 5e")
table_covariance_XSRatio_mm_PtRap1.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap1.location = "Supplementary material"
for var in [x_covariance_mm_PtRap1,y_covariance_mm_PtRap1,z_covariance_mm_PtRap1]:
    table_covariance_XSRatio_mm_PtRap1.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap1)

# Create a reader for the input file
reader_covariance_mm_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPtRap2.root")
# Read the histogram
data_covariance_mm_PtRap2 = reader_covariance_mm_PtRap2.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["x_edges"]
y_covariance_mm_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["y"]
z_covariance_mm_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["z"]

table_covariance_XSRatio_mm_PtRap2 = Table("Covariance Matrix auxiliary Figure 5f")
table_covariance_XSRatio_mm_PtRap2.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap2.location = "Supplementary material"
for var in [x_covariance_mm_PtRap2,y_covariance_mm_PtRap2,z_covariance_mm_PtRap2]:
    table_covariance_XSRatio_mm_PtRap2.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap2)

# Create a reader for the input file
reader_covariance_mm_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPtRap3.root")
# Read the histogram
data_covariance_mm_PtRap3 = reader_covariance_mm_PtRap3.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["x_edges"]
y_covariance_mm_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["y"]
z_covariance_mm_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["z"]

table_covariance_XSRatio_mm_PtRap3 = Table("Covariance Matrix auxiliary Figure 5g")
table_covariance_XSRatio_mm_PtRap3.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap3.location = "Supplementary material"
for var in [x_covariance_mm_PtRap3,y_covariance_mm_PtRap3,z_covariance_mm_PtRap3]:
    table_covariance_XSRatio_mm_PtRap3.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap3)

# Create a reader for the input file
reader_covariance_mm_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix03__XSRatioSystPtRap4.root")
# Read the histogram
data_covariance_mm_PtRap4 = reader_covariance_mm_PtRap4.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["x_edges"]
y_covariance_mm_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["y"]
z_covariance_mm_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["z"]

table_covariance_XSRatio_mm_PtRap4 = Table("Covariance Matrix auxiliary Figure 5h")
table_covariance_XSRatio_mm_PtRap4.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap4.location = "Supplementary material"
for var in [x_covariance_mm_PtRap4,y_covariance_mm_PtRap4,z_covariance_mm_PtRap4]:
    table_covariance_XSRatio_mm_PtRap4.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap4)
### End covariance mumu

### Begin covariance ee dressed
# Create a reader for the input file
reader_covariance_ee_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPt.root")
# Read the histogram
data_covariance_ee_Pt = reader_covariance_ee_Pt.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Pt.values = data_covariance_ee_Pt["x_edges"]
y_covariance_ee_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Pt.values = data_covariance_ee_Pt["y"]
z_covariance_ee_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Pt.values = data_covariance_ee_Pt["z"]

table_covariance_XSRatio_ee_Pt = Table("Covariance Matrix auxiliary Figure 6a")
table_covariance_XSRatio_ee_Pt.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt in the dielectron final state."
table_covariance_XSRatio_ee_Pt.location = "Supplementary material"
for var in [x_covariance_ee_Pt,y_covariance_ee_Pt,z_covariance_ee_Pt]:
    table_covariance_XSRatio_ee_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_Pt)

# Create a reader for the input file
reader_covariance_ee_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystRap.root")
# Read the histogram
data_covariance_ee_Rap = reader_covariance_ee_Rap.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Rap.values = data_covariance_ee_Rap["x_edges"]
y_covariance_ee_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Rap.values = data_covariance_ee_Rap["y"]
z_covariance_ee_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Rap.values = data_covariance_ee_Rap["z"]

table_covariance_XSRatio_ee_Rap = Table("Covariance Matrix auxiliary Figure 6b")
table_covariance_XSRatio_ee_Rap.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of |y(Z)| in the dielectron final state."
table_covariance_XSRatio_ee_Rap.location = "Supplementary material"
for var in [x_covariance_ee_Rap,y_covariance_ee_Rap,z_covariance_ee_Rap]:
    table_covariance_XSRatio_ee_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_Rap)

# Create a reader for the input file
reader_covariance_ee_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_ee_PhiStar = reader_covariance_ee_PhiStar.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["x_edges"]
y_covariance_ee_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["y"]
z_covariance_ee_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["z"]

table_covariance_XSRatio_ee_PhiStar = Table("Covariance Matrix auxiliary Figure 6c")
table_covariance_XSRatio_ee_PhiStar.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dielectron final state."
table_covariance_XSRatio_ee_PhiStar.location = "Supplementary material"
for var in [x_covariance_ee_PhiStar,y_covariance_ee_PhiStar,z_covariance_ee_PhiStar]:
    table_covariance_XSRatio_ee_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PhiStar)

# Create a reader for the input file
reader_covariance_ee_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPtRap0.root")
# Read the histogram
data_covariance_ee_PtRap0 = reader_covariance_ee_PtRap0.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["x_edges"]
y_covariance_ee_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["y"]
z_covariance_ee_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["z"]

table_covariance_XSRatio_ee_PtRap0 = Table("Covariance Matrix auxiliary Figure 6d")
table_covariance_XSRatio_ee_PtRap0.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap0.location = "Supplementary material"
for var in [x_covariance_ee_PtRap0,y_covariance_ee_PtRap0,z_covariance_ee_PtRap0]:
    table_covariance_XSRatio_ee_PtRap0.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap0)

# Create a reader for the input file
reader_covariance_ee_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPtRap1.root")
# Read the histogram
data_covariance_ee_PtRap1 = reader_covariance_ee_PtRap1.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["x_edges"]
y_covariance_ee_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["y"]
z_covariance_ee_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["z"]

table_covariance_XSRatio_ee_PtRap1 = Table("Covariance Matrix auxiliary Figure 6e")
table_covariance_XSRatio_ee_PtRap1.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap1.location = "Supplementary material"
for var in [x_covariance_ee_PtRap1,y_covariance_ee_PtRap1,z_covariance_ee_PtRap1]:
    table_covariance_XSRatio_ee_PtRap1.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap1)

# Create a reader for the input file
reader_covariance_ee_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPtRap2.root")
# Read the histogram
data_covariance_ee_PtRap2 = reader_covariance_ee_PtRap2.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["x_edges"]
y_covariance_ee_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["y"]
z_covariance_ee_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["z"]

table_covariance_XSRatio_ee_PtRap2 = Table("Covariance Matrix auxiliary Figure 6f")
table_covariance_XSRatio_ee_PtRap2.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap2.location = "Supplementary material"
for var in [x_covariance_ee_PtRap2,y_covariance_ee_PtRap2,z_covariance_ee_PtRap2]:
    table_covariance_XSRatio_ee_PtRap2.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap2)

# Create a reader for the input file
reader_covariance_ee_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPtRap3.root")
# Read the histogram
data_covariance_ee_PtRap3 = reader_covariance_ee_PtRap3.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["x_edges"]
y_covariance_ee_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["y"]
z_covariance_ee_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["z"]

table_covariance_XSRatio_ee_PtRap3 = Table("Covariance Matrix auxiliary Figure 6g")
table_covariance_XSRatio_ee_PtRap3.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap3.location = "Supplementary material"
for var in [x_covariance_ee_PtRap3,y_covariance_ee_PtRap3,z_covariance_ee_PtRap3]:
    table_covariance_XSRatio_ee_PtRap3.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap3)

# Create a reader for the input file
reader_covariance_ee_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix13__XSRatioSystPtRap4.root")
# Read the histogram
data_covariance_ee_PtRap4 = reader_covariance_ee_PtRap4.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["x_edges"]
y_covariance_ee_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["y"]
z_covariance_ee_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["z"]

table_covariance_XSRatio_ee_PtRap4 = Table("Covariance Matrix auxiliary Figure 6h")
table_covariance_XSRatio_ee_PtRap4.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_XSRatio_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap4)
### End covariance ee


### Begin covariance mumu born
# Create a reader for the input file
reader_covariance_mm_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPt.root")
# Read the histogram
data_covariance_mm_Pt = reader_covariance_mm_Pt.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Pt.values = data_covariance_mm_Pt["x_edges"]
y_covariance_mm_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Pt.values = data_covariance_mm_Pt["y"]
z_covariance_mm_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Pt.values = data_covariance_mm_Pt["z"]

table_covariance_XSRatio_mm_Pt = Table("Covariance Matrix auxiliary Figure 7a")
table_covariance_XSRatio_mm_Pt.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt in the dimuon final state."
table_covariance_XSRatio_mm_Pt.location = "Supplementary material"
for var in [x_covariance_mm_Pt,y_covariance_mm_Pt,z_covariance_mm_Pt]:
    table_covariance_XSRatio_mm_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_Pt)

# Create a reader for the input file
reader_covariance_mm_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystRap.root")
# Read the histogram
data_covariance_mm_Rap = reader_covariance_mm_Rap.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_Rap.values = data_covariance_mm_Rap["x_edges"]
y_covariance_mm_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Rap.values = data_covariance_mm_Rap["y"]
z_covariance_mm_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Rap.values = data_covariance_mm_Rap["z"]

table_covariance_XSRatio_mm_Rap = Table("Covariance Matrix auxiliary Figure 7b")
table_covariance_XSRatio_mm_Rap.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of |y(Z)| in the dimuon final state."
table_covariance_XSRatio_mm_Rap.location = "Supplementary material"
for var in [x_covariance_mm_Rap,y_covariance_mm_Rap,z_covariance_mm_Rap]:
    table_covariance_XSRatio_mm_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_Rap)

# Create a reader for the input file
reader_covariance_mm_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_mm_PhiStar = reader_covariance_mm_PhiStar.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["x_edges"]
y_covariance_mm_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["y"]
z_covariance_mm_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["z"]

table_covariance_XSRatio_mm_PhiStar = Table("Covariance Matrix auxiliary Figure 7c")
table_covariance_XSRatio_mm_PhiStar.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dimuon final state."
table_covariance_XSRatio_mm_PhiStar.location = "Supplementary material"
for var in [x_covariance_mm_PhiStar,y_covariance_mm_PhiStar,z_covariance_mm_PhiStar]:
    table_covariance_XSRatio_mm_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PhiStar)

# Create a reader for the input file
reader_covariance_mm_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPtRap0.root")
# Read the histogram
data_covariance_mm_PtRap0 = reader_covariance_mm_PtRap0.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["x_edges"]
y_covariance_mm_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["y"]
z_covariance_mm_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["z"]

table_covariance_XSRatio_mm_PtRap0 = Table("Covariance Matrix auxiliary Figure 7d")
table_covariance_XSRatio_mm_PtRap0.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap0.location = "Supplementary material"
for var in [x_covariance_mm_PtRap0,y_covariance_mm_PtRap0,z_covariance_mm_PtRap0]:
    table_covariance_XSRatio_mm_PtRap0.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap0)

# Create a reader for the input file
reader_covariance_mm_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPtRap1.root")
# Read the histogram
data_covariance_mm_PtRap1 = reader_covariance_mm_PtRap1.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["x_edges"]
y_covariance_mm_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["y"]
z_covariance_mm_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["z"]

table_covariance_XSRatio_mm_PtRap1 = Table("Covariance Matrix auxiliary Figure 7e")
table_covariance_XSRatio_mm_PtRap1.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap1.location = "Supplementary material"
for var in [x_covariance_mm_PtRap1,y_covariance_mm_PtRap1,z_covariance_mm_PtRap1]:
    table_covariance_XSRatio_mm_PtRap1.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap1)

# Create a reader for the input file
reader_covariance_mm_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPtRap2.root")
# Read the histogram
data_covariance_mm_PtRap2 = reader_covariance_mm_PtRap2.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["x_edges"]
y_covariance_mm_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["y"]
z_covariance_mm_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["z"]

table_covariance_XSRatio_mm_PtRap2 = Table("Covariance Matrix auxiliary Figure 7f")
table_covariance_XSRatio_mm_PtRap2.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap2.location = "Supplementary material"
for var in [x_covariance_mm_PtRap2,y_covariance_mm_PtRap2,z_covariance_mm_PtRap2]:
    table_covariance_XSRatio_mm_PtRap2.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap2)

# Create a reader for the input file
reader_covariance_mm_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPtRap3.root")
# Read the histogram
data_covariance_mm_PtRap3 = reader_covariance_mm_PtRap3.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["x_edges"]
y_covariance_mm_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["y"]
z_covariance_mm_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["z"]

table_covariance_XSRatio_mm_PtRap3 = Table("Covariance Matrix auxiliary Figure 7g")
table_covariance_XSRatio_mm_PtRap3.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap3.location = "Supplementary material"
for var in [x_covariance_mm_PtRap3,y_covariance_mm_PtRap3,z_covariance_mm_PtRap3]:
    table_covariance_XSRatio_mm_PtRap3.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap3)

# Create a reader for the input file
reader_covariance_mm_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix03__XSRatioSystPtRap4.root")
# Read the histogram
data_covariance_mm_PtRap4 = reader_covariance_mm_PtRap4.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["x_edges"]
y_covariance_mm_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["y"]
z_covariance_mm_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["z"]

table_covariance_XSRatio_mm_PtRap4 = Table("Covariance Matrix auxiliary Figure 7h")
table_covariance_XSRatio_mm_PtRap4.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dimuon final state."
table_covariance_XSRatio_mm_PtRap4.location = "Supplementary material"
for var in [x_covariance_mm_PtRap4,y_covariance_mm_PtRap4,z_covariance_mm_PtRap4]:
    table_covariance_XSRatio_mm_PtRap4.add_variable(var)
submission.add_table(table_covariance_XSRatio_mm_PtRap4)
### End covariance mumu

### Begin covariance ee born
# Create a reader for the input file
reader_covariance_ee_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPt.root")
# Read the histogram
data_covariance_ee_Pt = reader_covariance_ee_Pt.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Pt.values = data_covariance_ee_Pt["x_edges"]
y_covariance_ee_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Pt.values = data_covariance_ee_Pt["y"]
z_covariance_ee_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Pt.values = data_covariance_ee_Pt["z"]

table_covariance_XSRatio_ee_Pt = Table("Covariance Matrix auxiliary Figure 8a")
table_covariance_XSRatio_ee_Pt.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt in the dielectron final state."
table_covariance_XSRatio_ee_Pt.location = "Supplementary material"
for var in [x_covariance_ee_Pt,y_covariance_ee_Pt,z_covariance_ee_Pt]:
    table_covariance_XSRatio_ee_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_Pt)

# Create a reader for the input file
reader_covariance_ee_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystRap.root")
# Read the histogram
data_covariance_ee_Rap = reader_covariance_ee_Rap.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_Rap.values = data_covariance_ee_Rap["x_edges"]
y_covariance_ee_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Rap.values = data_covariance_ee_Rap["y"]
z_covariance_ee_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Rap.values = data_covariance_ee_Rap["z"]

table_covariance_XSRatio_ee_Rap = Table("Covariance Matrix auxiliary Figure 8b")
table_covariance_XSRatio_ee_Rap.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of |y(Z)| in the dielectron final state."
table_covariance_XSRatio_ee_Rap.location = "Supplementary material"
for var in [x_covariance_ee_Rap,y_covariance_ee_Rap,z_covariance_ee_Rap]:
    table_covariance_XSRatio_ee_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_Rap)

# Create a reader for the input file
reader_covariance_ee_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_ee_PhiStar = reader_covariance_ee_PhiStar.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["x_edges"]
y_covariance_ee_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["y"]
z_covariance_ee_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["z"]

table_covariance_XSRatio_ee_PhiStar = Table("Covariance Matrix auxiliary Figure 8c")
table_covariance_XSRatio_ee_PhiStar.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dielectron final state."
table_covariance_XSRatio_ee_PhiStar.location = "Supplementary material"
for var in [x_covariance_ee_PhiStar,y_covariance_ee_PhiStar,z_covariance_ee_PhiStar]:
    table_covariance_XSRatio_ee_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PhiStar)

# Create a reader for the input file
reader_covariance_ee_PtRap0 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPtRap0.root")
# Read the histogram
data_covariance_ee_PtRap0 = reader_covariance_ee_PtRap0.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["x_edges"]
y_covariance_ee_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["y"]
z_covariance_ee_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["z"]

table_covariance_XSRatio_ee_PtRap0 = Table("Covariance Matrix auxiliary Figure 8d")
table_covariance_XSRatio_ee_PtRap0.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0 < |y(Z)| < 0.4 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap0.location = "Supplementary material"
for var in [x_covariance_ee_PtRap0,y_covariance_ee_PtRap0,z_covariance_ee_PtRap0]:
    table_covariance_XSRatio_ee_PtRap0.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap0)

# Create a reader for the input file
reader_covariance_ee_PtRap1 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPtRap1.root")
# Read the histogram
data_covariance_ee_PtRap1 = reader_covariance_ee_PtRap1.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap1 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["x_edges"]
y_covariance_ee_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["y"]
z_covariance_ee_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["z"]

table_covariance_XSRatio_ee_PtRap1 = Table("Covariance Matrix auxiliary Figure 8e")
table_covariance_XSRatio_ee_PtRap1.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0.4 < |y(Z)| < 0.8 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap1.location = "Supplementary material"
for var in [x_covariance_ee_PtRap1,y_covariance_ee_PtRap1,z_covariance_ee_PtRap1]:
    table_covariance_XSRatio_ee_PtRap1.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap1)

# Create a reader for the input file
reader_covariance_ee_PtRap2 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPtRap2.root")
# Read the histogram
data_covariance_ee_PtRap2 = reader_covariance_ee_PtRap2.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap2 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["x_edges"]
y_covariance_ee_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["y"]
z_covariance_ee_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["z"]

table_covariance_XSRatio_ee_PtRap2 = Table("Covariance Matrix auxiliary Figure 8f")
table_covariance_XSRatio_ee_PtRap2.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 0.8 < |y(Z)| < 1.2 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap2.location = "Supplementary material"
for var in [x_covariance_ee_PtRap2,y_covariance_ee_PtRap2,z_covariance_ee_PtRap2]:
    table_covariance_XSRatio_ee_PtRap2.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap2)

# Create a reader for the input file
reader_covariance_ee_PtRap3 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPtRap3.root")
# Read the histogram
data_covariance_ee_PtRap3 = reader_covariance_ee_PtRap3.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap3 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["x_edges"]
y_covariance_ee_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["y"]
z_covariance_ee_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["z"]

table_covariance_XSRatio_ee_PtRap3 = Table("Covariance Matrix auxiliary Figure 8g")
table_covariance_XSRatio_ee_PtRap3.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 1.2 < |y(Z)| < 1.6 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap3.location = "Supplementary material"
for var in [x_covariance_ee_PtRap3,y_covariance_ee_PtRap3,z_covariance_ee_PtRap3]:
    table_covariance_XSRatio_ee_PtRap3.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap3)

# Create a reader for the input file
reader_covariance_ee_PtRap4 = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix13__XSRatioSystPtRap4.root")
# Read the histogram
data_covariance_ee_PtRap4 = reader_covariance_ee_PtRap4.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap4 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["x_edges"]
y_covariance_ee_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["y"]
z_covariance_ee_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["z"]

table_covariance_XSRatio_ee_PtRap4 = Table("Covariance Matrix auxiliary Figure 8h")
table_covariance_XSRatio_ee_PtRap4.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_XSRatio_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap4)
### End covariance ee

### Begin FigAux9
reader_FigAux9a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystRap_nsel0_dy3_rebin1_default.root")
reader_FigAux9b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystRap_nsel1_dy3_rebin1_default.root")
reader_FigAux9c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystRap_nsel2_dy3_rebin1_default.root")

tableFigAux9 = Table("Auxiliary Figure 9")
tableFigAux9.description = "The measured absolute cross sections in bins of |y(Z)|, using born level leptons. The cross sections are normalized by the bin width."
tableFigAux9.location = "Data from Auxiliary Figure 9"
tableFigAux9.keywords["observables"] = ["N"]

histo_unfoldFigAux9a = reader_FigAux9a.read_hist_1d("unfold")
histo_unfoldFigAux9b = reader_FigAux9b.read_hist_1d("unfold")
histo_unfoldFigAux9c = reader_FigAux9c.read_hist_1d("unfold")

histo_unfoldFigAux9a.keys()

for key in histo_unfoldFigAux9a.keys():
    print(key, type(histo_unfoldFigAux9a[key]), type(histo_unfoldFigAux9a[key][0]))

mmed_FigAux9 = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_FigAux9.values = histo_unfoldFigAux9a["x_edges"]

# y-axis: N events
unfoldFigAux9a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux9a.values = histo_unfoldFigAux9a["y"]

unc_unfoldFigAux9a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux9a.values = histo_unfoldFigAux9a["dy"]

unfoldFigAux9a.add_uncertainty(unc_unfoldFigAux9a)

unfoldFigAux9b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux9b.values = histo_unfoldFigAux9b["y"]

unc_unfoldFigAux9b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux9b.values = histo_unfoldFigAux9b["dy"]

unfoldFigAux9b.add_uncertainty(unc_unfoldFigAux9b)

unfoldFigAux9c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux9c.values = histo_unfoldFigAux9c["y"]

unc_unfoldFigAux9c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux9c.values = histo_unfoldFigAux9c["dy"]

unfoldFigAux9c.add_uncertainty(unc_unfoldFigAux9c)

unfoldFigAux9a.scale_values(lumi_sf)
unfoldFigAux9b.scale_values(lumi_sf)
unfoldFigAux9c.scale_values(lumi_sf)

tableFigAux9.add_variable(mmed_FigAux9)
tableFigAux9.add_variable(unfoldFigAux9a)
tableFigAux9.add_variable(unfoldFigAux9b)
tableFigAux9.add_variable(unfoldFigAux9c)
submission.add_table(tableFigAux9)
### End FigAux9

### Begin FigAux10
reader_FigAux10a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPt_nsel0_dy3_rebin1_default.root")
reader_FigAux10b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPt_nsel1_dy3_rebin1_default.root")
reader_FigAux10c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPt_nsel2_dy3_rebin1_default.root")

tableFigAux10 = Table("Auxiliary Figure 10")
tableFigAux10.description = "The measured absolute cross sections in bins of Z pt, using born level leptons. The cross sections are normalized by the bin width. The first bin (0-1 GeV) is not shown as large differences were observed in aMC@NLO and POWHEG predictions at Born level."
tableFigAux10.location = "Data from Auxiliary Figure 10"
tableFigAux10.keywords["observables"] = ["N"]

histo_unfoldFigAux10a = reader_FigAux10a.read_hist_1d("unfold")
histo_unfoldFigAux10b = reader_FigAux10b.read_hist_1d("unfold")
histo_unfoldFigAux10c = reader_FigAux10c.read_hist_1d("unfold")

histo_unfoldFigAux10a.keys()

for key in histo_unfoldFigAux10a.keys():
    print(key, type(histo_unfoldFigAux10a[key]), type(histo_unfoldFigAux10a[key][0]))

print(histo_unfoldFigAux10a["x"])
histo_unfoldFigAux10a["x"].pop(0)
histo_unfoldFigAux10b["x"].pop(0)
histo_unfoldFigAux10c["x"].pop(0)
histo_unfoldFigAux10a["y"].pop(0)
histo_unfoldFigAux10b["y"].pop(0)
histo_unfoldFigAux10c["y"].pop(0)
histo_unfoldFigAux10a["dy"].pop(0)
histo_unfoldFigAux10b["dy"].pop(0)
histo_unfoldFigAux10c["dy"].pop(0)
print(histo_unfoldFigAux10a["x"])

mmed_FigAux10 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_FigAux10.values = histo_unfoldFigAux10a["x"]

# y-axis: N events
unfoldFigAux10a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux10a.values = histo_unfoldFigAux10a["y"]

unc_unfoldFigAux10a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux10a.values = histo_unfoldFigAux10a["dy"]

unfoldFigAux10a.add_uncertainty(unc_unfoldFigAux10a)

unfoldFigAux10b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux10b.values = histo_unfoldFigAux10b["y"]

unc_unfoldFigAux10b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux10b.values = histo_unfoldFigAux10b["dy"]

unfoldFigAux10b.add_uncertainty(unc_unfoldFigAux10b)

unfoldFigAux10c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux10c.values = histo_unfoldFigAux10c["y"]

unc_unfoldFigAux10c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux10c.values = histo_unfoldFigAux10c["dy"]

unfoldFigAux10c.add_uncertainty(unc_unfoldFigAux10c)

unfoldFigAux10a.scale_values(lumi_sf)
unfoldFigAux10b.scale_values(lumi_sf)
unfoldFigAux10c.scale_values(lumi_sf)

tableFigAux10.add_variable(mmed_FigAux10)
tableFigAux10.add_variable(unfoldFigAux10a)
tableFigAux10.add_variable(unfoldFigAux10b)
tableFigAux10.add_variable(unfoldFigAux10c)
submission.add_table(tableFigAux10)
### End FigAux10

### Begin FigAux11
reader_FigAux11a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPhiStar_nsel0_dy3_rebin1_default.root")
reader_FigAux11b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPhiStar_nsel1_dy3_rebin1_default.root")
reader_FigAux11c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPhiStar_nsel2_dy3_rebin1_default.root")

tableFigAux11 = Table("Auxiliary Figure 11")
tableFigAux11.description = "The measured absolute cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$, using born level leptons. The cross sections are normalized by the bin width."
tableFigAux11.location = "Data from Auxiliary Figure 11"
tableFigAux11.keywords["observables"] = ["N"]

histo_unfoldFigAux11a = reader_FigAux11a.read_hist_1d("unfold")
histo_unfoldFigAux11b = reader_FigAux11b.read_hist_1d("unfold")
histo_unfoldFigAux11c = reader_FigAux11c.read_hist_1d("unfold")

histo_unfoldFigAux11a.keys()

for key in histo_unfoldFigAux11a.keys():
    print(key, type(histo_unfoldFigAux11a[key]), type(histo_unfoldFigAux11a[key][0]))

mmed_FigAux11 = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_FigAux11.values = histo_unfoldFigAux11a["x_edges"]

# y-axis: N events
unfoldFigAux11a = Variable("Dimuon cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux11a.values = histo_unfoldFigAux11a["y"]

unc_unfoldFigAux11a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux11a.values = histo_unfoldFigAux11a["dy"]

unfoldFigAux11a.add_uncertainty(unc_unfoldFigAux11a)

unfoldFigAux11b = Variable("Dielectron cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux11b.values = histo_unfoldFigAux11b["y"]

unc_unfoldFigAux11b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux11b.values = histo_unfoldFigAux11b["dy"]

unfoldFigAux11b.add_uncertainty(unc_unfoldFigAux11b)

unfoldFigAux11c = Variable("Dilepton cross section (pb)", is_independent=False, is_binned=False, units="")
unfoldFigAux11c.values = histo_unfoldFigAux11c["y"]

unc_unfoldFigAux11c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux11c.values = histo_unfoldFigAux11c["dy"]

unfoldFigAux11c.add_uncertainty(unc_unfoldFigAux11c)

unfoldFigAux11a.scale_values(lumi_sf)
unfoldFigAux11b.scale_values(lumi_sf)
unfoldFigAux11c.scale_values(lumi_sf)

tableFigAux11.add_variable(mmed_FigAux11)
tableFigAux11.add_variable(unfoldFigAux11a)
tableFigAux11.add_variable(unfoldFigAux11b)
tableFigAux11.add_variable(unfoldFigAux11c)
submission.add_table(tableFigAux11)
### End FigAux11

### Begin FigAux12to16
reader_FigAux12to16a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPtRap0_nsel2_dy3_rebin1_default.root")
reader_FigAux12to16b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPtRap1_nsel2_dy3_rebin1_default.root")
reader_FigAux12to16c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPtRap2_nsel2_dy3_rebin1_default.root")
reader_FigAux12to16d = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPtRap3_nsel2_dy3_rebin1_default.root")
reader_FigAux12to16e = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfoldingSystPtRap4_nsel2_dy3_rebin1_default.root")

tableFigAux12to16 = Table("Auxiliary Figures 12 to 16")
tableFigAux12to16.description = "The measured absolute cross sections in bins of Z pt different |y(Z)| bins, using born level leptons. The cross sections are normalized by the bin width. The first bin (0-1 GeV) is not shown as large differences were observed in aMC@NLO and POWHEG predictions at Born level."
tableFigAux12to16.location = "Data from Auxiliary Figures 12 to 16"
tableFigAux12to16.keywords["observables"] = ["N"]

histo_unfoldFigAux12to16a = reader_FigAux12to16a.read_hist_1d("unfold")
histo_unfoldFigAux12to16b = reader_FigAux12to16b.read_hist_1d("unfold")
histo_unfoldFigAux12to16c = reader_FigAux12to16c.read_hist_1d("unfold")
histo_unfoldFigAux12to16d = reader_FigAux12to16d.read_hist_1d("unfold")
histo_unfoldFigAux12to16e = reader_FigAux12to16e.read_hist_1d("unfold")

histo_unfoldFigAux12to16a.keys()

for key in histo_unfoldFigAux12to16a.keys():
    print(key, type(histo_unfoldFigAux12to16a[key]), type(histo_unfoldFigAux12to16a[key][0]))

print(histo_unfoldFigAux12to16a["x"])
histo_unfoldFigAux12to16a["x"].pop(0)
histo_unfoldFigAux12to16b["x"].pop(0)
histo_unfoldFigAux12to16c["x"].pop(0)
histo_unfoldFigAux12to16d["x"].pop(0)
histo_unfoldFigAux12to16e["x"].pop(0)
histo_unfoldFigAux12to16a["y"].pop(0)
histo_unfoldFigAux12to16b["y"].pop(0)
histo_unfoldFigAux12to16c["y"].pop(0)
histo_unfoldFigAux12to16d["y"].pop(0)
histo_unfoldFigAux12to16e["y"].pop(0)
histo_unfoldFigAux12to16a["dy"].pop(0)
histo_unfoldFigAux12to16b["dy"].pop(0)
histo_unfoldFigAux12to16c["dy"].pop(0)
histo_unfoldFigAux12to16d["dy"].pop(0)
histo_unfoldFigAux12to16e["dy"].pop(0)
print(histo_unfoldFigAux12to16a["x"])


mmed_FigAux12to16 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_FigAux12to16.values = histo_unfoldFigAux12to16a["x"]

# y-axis: N events
unfoldFigAux12to16a = Variable("Dilepton cross section (pb) in 0 < |y(Z)| < 0.4 bin", is_independent=False, is_binned=False, units="")
unfoldFigAux12to16a.values = histo_unfoldFigAux12to16a["y"]

unc_unfoldFigAux12to16a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux12to16a.values = histo_unfoldFigAux12to16a["dy"]

unfoldFigAux12to16a.add_uncertainty(unc_unfoldFigAux12to16a)

unfoldFigAux12to16b = Variable("Dilepton cross section (pb) in 0.4 < |y(Z)| < 0.8 bin", is_independent=False, is_binned=False, units="")
unfoldFigAux12to16b.values = histo_unfoldFigAux12to16b["y"]

unc_unfoldFigAux12to16b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux12to16b.values = histo_unfoldFigAux12to16b["dy"]

unfoldFigAux12to16b.add_uncertainty(unc_unfoldFigAux12to16b)

unfoldFigAux12to16c = Variable("Dilepton cross section (pb) in 0.8 < |y(Z)| < 1.2 bin", is_independent=False, is_binned=False, units="")
unfoldFigAux12to16c.values = histo_unfoldFigAux12to16c["y"]

unc_unfoldFigAux12to16c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux12to16c.values = histo_unfoldFigAux12to16c["dy"]

unfoldFigAux12to16c.add_uncertainty(unc_unfoldFigAux12to16c)

unfoldFigAux12to16d = Variable("Dilepton cross section (pb) in 1.2 < |y(Z)| < 1.6 bin", is_independent=False, is_binned=False, units="")
unfoldFigAux12to16d.values = histo_unfoldFigAux12to16d["y"]

unc_unfoldFigAux12to16d = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux12to16d.values = histo_unfoldFigAux12to16d["dy"]

unfoldFigAux12to16d.add_uncertainty(unc_unfoldFigAux12to16d)

unfoldFigAux12to16e = Variable("Dilepton cross section (pb) in 1.6 < |y(Z)| < 2.4 bin", is_independent=False, is_binned=False, units="")
unfoldFigAux12to16e.values = histo_unfoldFigAux12to16e["y"]

unc_unfoldFigAux12to16e = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux12to16e.values = histo_unfoldFigAux12to16e["dy"]

unfoldFigAux12to16e.add_uncertainty(unc_unfoldFigAux12to16e)

unfoldFigAux12to16a.scale_values(lumi_sf)
unfoldFigAux12to16b.scale_values(lumi_sf)
unfoldFigAux12to16c.scale_values(lumi_sf)
unfoldFigAux12to16d.scale_values(lumi_sf)
unfoldFigAux12to16e.scale_values(lumi_sf)

tableFigAux12to16.add_variable(mmed_FigAux12to16)
tableFigAux12to16.add_variable(unfoldFigAux12to16a)
tableFigAux12to16.add_variable(unfoldFigAux12to16b)
tableFigAux12to16.add_variable(unfoldFigAux12to16c)
tableFigAux12to16.add_variable(unfoldFigAux12to16d)
tableFigAux12to16.add_variable(unfoldFigAux12to16e)
submission.add_table(tableFigAux12to16)
### End FigAux12to16

### Begin FigAux17a
reader_FigAux17a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPt_nsel2_dy3_rebin1_default.root")

tableFigAux17a = Table("Auxiliary Figure 17a")
tableFigAux17a.description = "The measured normalized cross sections in bins of Z pt, using born level leptons. The first bin (0-1 GeV) is not shown as large differences were observed in aMC@NLO and POWHEG predictions at Born level. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFigAux17a.location = "Data from Auxiliary Figure 17a"
tableFigAux17a.keywords["observables"] = ["N"]

histo_unfoldFigAux17a = reader_FigAux17a.read_hist_1d("unfold")

histo_unfoldFigAux17a.keys()

inv_total_sum = 1.0/sum(histo_unfoldFigAux17a["y"])
for key in histo_unfoldFigAux17a.keys():
    print(key, type(histo_unfoldFigAux17a[key]), type(histo_unfoldFigAux17a[key][0]))

print(histo_unfoldFigAux17a["x"])
histo_unfoldFigAux17a["x"].pop(0)
histo_unfoldFigAux17a["y"].pop(0)
histo_unfoldFigAux17a["dy"].pop(0)
print(histo_unfoldFigAux17a["x"])

mmed_FigAux17a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_FigAux17a.values = histo_unfoldFigAux17a["x"]

# y-axis: N events
unfoldFigAux17a = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFigAux17a.values = histo_unfoldFigAux17a["y"]

unc_unfoldFigAux17a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux17a.values = histo_unfoldFigAux17a["dy"]

unfoldFigAux17a.add_uncertainty(unc_unfoldFigAux17a)

unfoldFigAux17a.scale_values(inv_total_sum)

tableFigAux17a.add_variable(mmed_FigAux17a)
tableFigAux17a.add_variable(unfoldFigAux17a)
submission.add_table(tableFigAux17a)
### End FigAux17a

### Begin FigAux17b
reader_FigAux17b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPhiStar_nsel2_dy3_rebin1_default.root")

tableFigAux17b = Table("Auxiliary Figure 17b")
tableFigAux17b.description = "The measured normalized cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$, using born level leptons. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFigAux17b.location = "Data from Auxiliary Figure 17b"
tableFigAux17b.keywords["observables"] = ["N"]

histo_unfoldFigAux17b = reader_FigAux17b.read_hist_1d("unfold")

histo_unfoldFigAux17b.keys()

inv_total_sum = 1.0/sum(histo_unfoldFigAux17b["y"])
for key in histo_unfoldFigAux17b.keys():
    print(key, type(histo_unfoldFigAux17b[key]), type(histo_unfoldFigAux17b[key][0]))

mmed_FigAux17b = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=True, units="")
mmed_FigAux17b.values = histo_unfoldFigAux17b["x_edges"]

# y-axis: N events
unfoldFigAux17b = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFigAux17b.values = histo_unfoldFigAux17b["y"]

unc_unfoldFigAux17b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux17b.values = histo_unfoldFigAux17b["dy"]

unfoldFigAux17b.add_uncertainty(unc_unfoldFigAux17b)

unfoldFigAux17b.scale_values(inv_total_sum)

tableFigAux17b.add_variable(mmed_FigAux17b)
tableFigAux17b.add_variable(unfoldFigAux17b)
submission.add_table(tableFigAux17b)
### End FigAux17b

### Begin FigAux17c
reader_FigAux17c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystRap_nsel2_dy3_rebin1_default.root")

tableFigAux17c = Table("Auxiliary Figure 17c")
tableFigAux17c.description = "The measured normalized cross sections in bins of |y(Z)|, using born level leptons."
tableFigAux17c.location = "Data from Auxiliary Figure 17c"
tableFigAux17c.keywords["observables"] = ["N"]

histo_unfoldFigAux17c = reader_FigAux17c.read_hist_1d("unfold")

histo_unfoldFigAux17c.keys()

inv_total_sum = 1.0/sum(histo_unfoldFigAux17c["y"])
for key in histo_unfoldFigAux17c.keys():
    print(key, type(histo_unfoldFigAux17c[key]), type(histo_unfoldFigAux17c[key][0]))

mmed_FigAux17c = Variable("|y(Z)|", is_independent=True, is_binned=True, units="")
mmed_FigAux17c.values = histo_unfoldFigAux17c["x_edges"]

# y-axis: N events
unfoldFigAux17c = Variable("Normalized dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFigAux17c.values = histo_unfoldFigAux17c["y"]

unc_unfoldFigAux17c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux17c.values = histo_unfoldFigAux17c["dy"]

unfoldFigAux17c.add_uncertainty(unc_unfoldFigAux17c)

unfoldFigAux17c.scale_values(inv_total_sum)

tableFigAux17c.add_variable(mmed_FigAux17c)
tableFigAux17c.add_variable(unfoldFigAux17c)
submission.add_table(tableFigAux17c)
### End FigAux17c

### Begin FigAux18to22
reader_FigAux18to22a = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPtRap0_nsel2_dy3_rebin1_default.root")
reader_FigAux18to22b = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPtRap1_nsel2_dy3_rebin1_default.root")
reader_FigAux18to22c = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPtRap2_nsel2_dy3_rebin1_default.root")
reader_FigAux18to22d = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPtRap3_nsel2_dy3_rebin1_default.root")
reader_FigAux18to22e = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/outputs/histoUnfolding_XSRatioSystPtRap4_nsel2_dy3_rebin1_default.root")

tableFigAux18to22 = Table("Auxiliary Figures 18 to 22")
tableFigAux18to22.description = "The measured normalized cross sections (left) in bins of Z pt in |y(Z)| bins, using born level leptons. The first bin (0-1 GeV) is not shown as large differences were observed in aMC@NLO and POWHEG predictions at Born level. The cross sections are divided by the bin width and then the distributions are normalized to 1."
tableFigAux18to22.location = "Data from Auxiliary Figures 16 to 20"
tableFigAux18to22.keywords["observables"] = ["N"]

histo_unfoldFigAux18to22a = reader_FigAux18to22a.read_hist_1d("unfold")
histo_unfoldFigAux18to22b = reader_FigAux18to22b.read_hist_1d("unfold")
histo_unfoldFigAux18to22c = reader_FigAux18to22c.read_hist_1d("unfold")
histo_unfoldFigAux18to22d = reader_FigAux18to22d.read_hist_1d("unfold")
histo_unfoldFigAux18to22e = reader_FigAux18to22e.read_hist_1d("unfold")

histo_unfoldFigAux18to22a.keys()

inv_total_suma = 1.0/sum(histo_unfoldFigAux18to22a["y"])
inv_total_sumb = 1.0/sum(histo_unfoldFigAux18to22b["y"])
inv_total_sumc = 1.0/sum(histo_unfoldFigAux18to22c["y"])
inv_total_sumd = 1.0/sum(histo_unfoldFigAux18to22d["y"])
inv_total_sume = 1.0/sum(histo_unfoldFigAux18to22e["y"])
for key in histo_unfoldFigAux18to22a.keys():
    print(key, type(histo_unfoldFigAux18to22a[key]), type(histo_unfoldFigAux18to22a[key][0]))

print(histo_unfoldFigAux18to22a["x"])
histo_unfoldFigAux18to22a["x"].pop(0)
histo_unfoldFigAux18to22b["x"].pop(0)
histo_unfoldFigAux18to22c["x"].pop(0)
histo_unfoldFigAux18to22d["x"].pop(0)
histo_unfoldFigAux18to22e["x"].pop(0)
histo_unfoldFigAux18to22a["y"].pop(0)
histo_unfoldFigAux18to22b["y"].pop(0)
histo_unfoldFigAux18to22c["y"].pop(0)
histo_unfoldFigAux18to22d["y"].pop(0)
histo_unfoldFigAux18to22e["y"].pop(0)
histo_unfoldFigAux18to22a["dy"].pop(0)
histo_unfoldFigAux18to22b["dy"].pop(0)
histo_unfoldFigAux18to22c["dy"].pop(0)
histo_unfoldFigAux18to22d["dy"].pop(0)
histo_unfoldFigAux18to22e["dy"].pop(0)
print(histo_unfoldFigAux18to22a["x"])

mmed_FigAux18to22 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_FigAux18to22.values = histo_unfoldFigAux18to22a["x"]

# y-axis: N events
unfoldFigAux18to22a = Variable("Normalized dilepton cross section in 0 < |y(Z)| < 0.4", is_independent=False, is_binned=False, units="")
unfoldFigAux18to22a.values = histo_unfoldFigAux18to22a["y"]
unc_unfoldFigAux18to22a = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux18to22a.values = histo_unfoldFigAux18to22a["dy"]
unfoldFigAux18to22a.add_uncertainty(unc_unfoldFigAux18to22a)

unfoldFigAux18to22b = Variable("Normalized dilepton cross section in 0.4 < |y(Z)| < 0.8", is_independent=False, is_binned=False, units="")
unfoldFigAux18to22b.values = histo_unfoldFigAux18to22b["y"]
unc_unfoldFigAux18to22b = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux18to22b.values = histo_unfoldFigAux18to22b["dy"]
unfoldFigAux18to22b.add_uncertainty(unc_unfoldFigAux18to22b)

unfoldFigAux18to22c = Variable("Normalized dilepton cross section in 0.8 < |y(Z)| < 1.2", is_independent=False, is_binned=False, units="")
unfoldFigAux18to22c.values = histo_unfoldFigAux18to22c["y"]
unc_unfoldFigAux18to22c = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux18to22c.values = histo_unfoldFigAux18to22c["dy"]
unfoldFigAux18to22c.add_uncertainty(unc_unfoldFigAux18to22c)

unfoldFigAux18to22d = Variable("Normalized dilepton cross section in 1.2 < |y(Z)| < 1.6", is_independent=False, is_binned=False, units="")
unfoldFigAux18to22d.values = histo_unfoldFigAux18to22d["y"]
unc_unfoldFigAux18to22d = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux18to22d.values = histo_unfoldFigAux18to22d["dy"]
unfoldFigAux18to22d.add_uncertainty(unc_unfoldFigAux18to22d)

unfoldFigAux18to22e = Variable("Normalized dilepton cross section in 1.6 < |y(Z)| < 2.4", is_independent=False, is_binned=False, units="")
unfoldFigAux18to22e.values = histo_unfoldFigAux18to22e["y"]
unc_unfoldFigAux18to22e = Uncertainty("", is_symmetric=True)
unc_unfoldFigAux18to22e.values = histo_unfoldFigAux18to22e["dy"]
unfoldFigAux18to22e.add_uncertainty(unc_unfoldFigAux18to22e)

unfoldFigAux18to22a.scale_values(inv_total_suma)
unfoldFigAux18to22b.scale_values(inv_total_sumb)
unfoldFigAux18to22c.scale_values(inv_total_sumc)
unfoldFigAux18to22d.scale_values(inv_total_sumd)
unfoldFigAux18to22e.scale_values(inv_total_sume)

tableFigAux18to22.add_variable(mmed_FigAux18to22)
tableFigAux18to22.add_variable(unfoldFigAux18to22a)
tableFigAux18to22.add_variable(unfoldFigAux18to22b)
tableFigAux18to22.add_variable(unfoldFigAux18to22c)
tableFigAux18to22.add_variable(unfoldFigAux18to22d)
tableFigAux18to22.add_variable(unfoldFigAux18to22e)
submission.add_table(tableFigAux18to22)
### End FigAux18to22

### Begin covariance ll dressed
# Create a reader for the input file
reader_covariance_ll_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23_SystPt.root")
# Read the histogram
data_covariance_ll_Pt = reader_covariance_ll_Pt.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Pt.values = data_covariance_ll_Pt["x_edges"]
y_covariance_ll_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Pt.values = data_covariance_ll_Pt["y"]
z_covariance_ll_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Pt.values = data_covariance_ll_Pt["z"]

table_covariance_ll_Pt = Table("Covariance Matrix auxiliary Figure 23a")
table_covariance_ll_Pt.description = "Covariance matrix using dressed level leptons for all bins used in bins of Z pt in the dilepton final state."
table_covariance_ll_Pt.location = "Covariance Matrix auxiliary Figure 23a"
for var in [x_covariance_ll_Pt,y_covariance_ll_Pt,z_covariance_ll_Pt]:
    table_covariance_ll_Pt.add_variable(var)
submission.add_table(table_covariance_ll_Pt)

# Create a reader for the input file
reader_covariance_ll_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23_SystRap.root")
# Read the histogram
data_covariance_ll_Rap = reader_covariance_ll_Rap.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Rap.values = data_covariance_ll_Rap["x_edges"]
y_covariance_ll_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Rap.values = data_covariance_ll_Rap["y"]
z_covariance_ll_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Rap.values = data_covariance_ll_Rap["z"]

table_covariance_ll_Rap = Table("Covariance Matrix auxiliary Figure 23b")
table_covariance_ll_Rap.description = "Covariance matrix using dressed level leptons for all bins used in bins of |y(Z)| in the dilepton final state."
table_covariance_ll_Rap.location = "Covariance Matrix auxiliary Figure 23b"
for var in [x_covariance_ll_Rap,y_covariance_ll_Rap,z_covariance_ll_Rap]:
    table_covariance_ll_Rap.add_variable(var)
submission.add_table(table_covariance_ll_Rap)

# Create a reader for the input file
reader_covariance_ll_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23_SystPhiStar.root")
# Read the histogram
data_covariance_ll_PhiStar = reader_covariance_ll_PhiStar.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["x_edges"]
y_covariance_ll_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["y"]
z_covariance_ll_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["z"]

table_covariance_ll_PhiStar = Table("Covariance Matrix auxiliary Figure 23c")
table_covariance_ll_PhiStar.description = "Covariance matrix using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dilepton final state."
table_covariance_ll_PhiStar.location = "Covariance Matrix auxiliary Figure 23c"
for var in [x_covariance_ll_PhiStar,y_covariance_ll_PhiStar,z_covariance_ll_PhiStar]:
    table_covariance_ll_PhiStar.add_variable(var)
submission.add_table(table_covariance_ll_PhiStar)

### Begin covariance ll born
# Create a reader for the input file
reader_covariance_ll_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23_SystPt.root")
# Read the histogram
data_covariance_ll_Pt = reader_covariance_ll_Pt.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Pt.values = data_covariance_ll_Pt["x_edges"]
y_covariance_ll_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Pt.values = data_covariance_ll_Pt["y"]
z_covariance_ll_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Pt.values = data_covariance_ll_Pt["z"]

table_covariance_ll_Pt = Table("Covariance Matrix auxiliary Figure 24a")
table_covariance_ll_Pt.description = "Covariance matrix using born level leptons for all bins used in bins of Z pt in the dilepton final state."
table_covariance_ll_Pt.location = "Covariance Matrix auxiliary Figure 24a"
for var in [x_covariance_ll_Pt,y_covariance_ll_Pt,z_covariance_ll_Pt]:
    table_covariance_ll_Pt.add_variable(var)
submission.add_table(table_covariance_ll_Pt)

# Create a reader for the input file
reader_covariance_ll_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23_SystRap.root")
# Read the histogram
data_covariance_ll_Rap = reader_covariance_ll_Rap.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Rap.values = data_covariance_ll_Rap["x_edges"]
y_covariance_ll_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Rap.values = data_covariance_ll_Rap["y"]
z_covariance_ll_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Rap.values = data_covariance_ll_Rap["z"]

table_covariance_ll_Rap = Table("Covariance Matrix auxiliary Figure 24b")
table_covariance_ll_Rap.description = "Covariance matrix using born level leptons for all bins used in bins of |y(Z)| in the dilepton final state."
table_covariance_ll_Rap.location = "Covariance Matrix auxiliary Figure 24b"
for var in [x_covariance_ll_Rap,y_covariance_ll_Rap,z_covariance_ll_Rap]:
    table_covariance_ll_Rap.add_variable(var)
submission.add_table(table_covariance_ll_Rap)

# Create a reader for the input file
reader_covariance_ll_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23_SystPhiStar.root")
# Read the histogram
data_covariance_ll_PhiStar = reader_covariance_ll_PhiStar.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["x_edges"]
y_covariance_ll_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["y"]
z_covariance_ll_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["z"]

table_covariance_ll_PhiStar = Table("Covariance Matrix auxiliary Figure 24c")
table_covariance_ll_PhiStar.description = "Covariance matrix using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dilepton final state."
table_covariance_ll_PhiStar.location = "Covariance Matrix auxiliary Figure 24c"
for var in [x_covariance_ll_PhiStar,y_covariance_ll_PhiStar,z_covariance_ll_PhiStar]:
    table_covariance_ll_PhiStar.add_variable(var)
submission.add_table(table_covariance_ll_PhiStar)

### Begin covariance ll dressed
# Create a reader for the input file
reader_covariance_ll_Pt = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23__XSRatioSystPt.root")
# Read the histogram
data_covariance_ll_Pt = reader_covariance_ll_Pt.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Pt.values = data_covariance_ll_Pt["x_edges"]
y_covariance_ll_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Pt.values = data_covariance_ll_Pt["y"]
z_covariance_ll_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Pt.values = data_covariance_ll_Pt["z"]

table_covariance_XSRatio_ll_Pt = Table("Covariance Matrix auxiliary Figure 25a")
table_covariance_XSRatio_ll_Pt.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of Z pt in the dilepton final state."
table_covariance_XSRatio_ll_Pt.location = "Covariance Matrix auxiliary Figure 25a"
for var in [x_covariance_ll_Pt,y_covariance_ll_Pt,z_covariance_ll_Pt]:
    table_covariance_XSRatio_ll_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_Pt)

# Create a reader for the input file
reader_covariance_ll_Rap = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23__XSRatioSystRap.root")
# Read the histogram
data_covariance_ll_Rap = reader_covariance_ll_Rap.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Rap.values = data_covariance_ll_Rap["x_edges"]
y_covariance_ll_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Rap.values = data_covariance_ll_Rap["y"]
z_covariance_ll_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Rap.values = data_covariance_ll_Rap["z"]

table_covariance_XSRatio_ll_Rap = Table("Covariance Matrix auxiliary Figure 25b")
table_covariance_XSRatio_ll_Rap.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of |y(Z)| in the dilepton final state."
table_covariance_XSRatio_ll_Rap.location = "Covariance Matrix auxiliary Figure 25b"
for var in [x_covariance_ll_Rap,y_covariance_ll_Rap,z_covariance_ll_Rap]:
    table_covariance_XSRatio_ll_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_Rap)

# Create a reader for the input file
reader_covariance_ll_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/output_root/matrix23__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_ll_PhiStar = reader_covariance_ll_PhiStar.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["x_edges"]
y_covariance_ll_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["y"]
z_covariance_ll_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["z"]

table_covariance_XSRatio_ll_PhiStar = Table("Covariance Matrix auxiliary Figure 25c")
table_covariance_XSRatio_ll_PhiStar.description = "Covariance matrix for normalized cross sections using dressed level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dilepton final state."
table_covariance_XSRatio_ll_PhiStar.location = "Covariance Matrix auxiliary Figure 25c"
for var in [x_covariance_ll_PhiStar,y_covariance_ll_PhiStar,z_covariance_ll_PhiStar]:
    table_covariance_XSRatio_ll_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_PhiStar)

### Begin covariance ll born
# Create a reader for the input file
reader_covariance_ll_Pt = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23__XSRatioSystPt.root")
# Read the histogram
data_covariance_ll_Pt = reader_covariance_ll_Pt.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Pt = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Pt.values = data_covariance_ll_Pt["x_edges"]
y_covariance_ll_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Pt.values = data_covariance_ll_Pt["y"]
z_covariance_ll_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Pt.values = data_covariance_ll_Pt["z"]

table_covariance_XSRatio_ll_Pt = Table("Covariance Matrix auxiliary Figure 26a")
table_covariance_XSRatio_ll_Pt.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt in the dilepton final state."
table_covariance_XSRatio_ll_Pt.location = "Covariance Matrix auxiliary Figure 26a"
for var in [x_covariance_ll_Pt,y_covariance_ll_Pt,z_covariance_ll_Pt]:
    table_covariance_XSRatio_ll_Pt.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_Pt)

# Create a reader for the input file
reader_covariance_ll_Rap = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23__XSRatioSystRap.root")
# Read the histogram
data_covariance_ll_Rap = reader_covariance_ll_Rap.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_Rap = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_Rap.values = data_covariance_ll_Rap["x_edges"]
y_covariance_ll_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_Rap.values = data_covariance_ll_Rap["y"]
z_covariance_ll_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_Rap.values = data_covariance_ll_Rap["z"]

table_covariance_XSRatio_ll_Rap = Table("Covariance Matrix auxiliary Figure 26b")
table_covariance_XSRatio_ll_Rap.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of |y(Z)| in the dilepton final state."
table_covariance_XSRatio_ll_Rap.location = "Covariance Matrix auxiliary Figure 26b"
for var in [x_covariance_ll_Rap,y_covariance_ll_Rap,z_covariance_ll_Rap]:
    table_covariance_XSRatio_ll_Rap.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_Rap)

# Create a reader for the input file
reader_covariance_ll_PhiStar = RootFileReader("HEPData/inputs/smp17010/folders_bornleptons/output_root/matrix23__XSRatioSystPhiStar.root")
# Read the histogram
data_covariance_ll_PhiStar = reader_covariance_ll_PhiStar.read_hist_2d("covariance_totsum_2")
# Create variable objects
x_covariance_ll_PhiStar = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["x_edges"]
y_covariance_ll_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["y"]
z_covariance_ll_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ll_PhiStar.values = data_covariance_ll_PhiStar["z"]

table_covariance_XSRatio_ll_PhiStar = Table("Covariance Matrix auxiliary Figure 26c")
table_covariance_XSRatio_ll_PhiStar.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dilepton final state."
table_covariance_XSRatio_ll_PhiStar.location = "Covariance Matrix auxiliary Figure 26c"
for var in [x_covariance_ll_PhiStar,y_covariance_ll_PhiStar,z_covariance_ll_PhiStar]:
    table_covariance_XSRatio_ll_PhiStar.add_variable(var)
submission.add_table(table_covariance_XSRatio_ll_PhiStar)

outdir = "smp17010_output"
submission.create_files(outdir)
