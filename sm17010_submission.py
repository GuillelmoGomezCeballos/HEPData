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
table2_yields1.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields2 = Variable("Muon reconstruction efficiency", is_independent=False, is_binned=False, units="")
table2_yields2.values = [float(x) for x in data2[:,2]]
table2_yields2.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields3 = Variable("Muon selection efficiency", is_independent=False, is_binned=False, units="")
table2_yields3.values = [float(x) for x in data2[:,3]]
table2_yields3.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields4 = Variable("Muon momentum scale", is_independent=False, is_binned=False, units="")
table2_yields4.values = [float(x) for x in data2[:,4]]
table2_yields4.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields5 = Variable("Electron reconstruction efficiency", is_independent=False, is_binned=False, units="")
table2_yields5.values = [float(x) for x in data2[:,5]]
table2_yields5.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields6 = Variable("Electron selection efficiency", is_independent=False, is_binned=False, units="")
table2_yields6.values = [float(x) for x in data2[:,6]]
table2_yields6.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields7 = Variable("Electron momentum scale", is_independent=False, is_binned=False, units="")
table2_yields7.values = [float(x) for x in data2[:,7]]
table2_yields7.add_qualifier("Uncertainty in \%", "Z selection")
table2_yields7.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields8 = Variable("Electron momentum scale", is_independent=False, is_binned=False, units="")
table2_yields8.values = [float(x) for x in data2[:,7]]
table2_yields8.add_qualifier("Background estimation", "Z selection")
table2_yields8.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields9 = Variable("Total (excluding luminosity)", is_independent=False, is_binned=False, units="")
table2_yields9.values = [float(x) for x in data2[:,7]]
table2_yields9.add_qualifier("Uncertainty in \%", "Z selection")
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
table3_data.values = [str(x) for x in data1[:,0]]

table3_yields1 = Variable("Cross Section", is_independent=False, is_binned=False, units="")
table3_yields1.values = [float(x) for x in data1[:,1]]
table3_yields1.add_qualifier("pb", "Cross Section")
table3_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table3_yields2 = Variable("Experimental uncertainty", is_independent=False, is_binned=False, units="")
table3_yields2.values = [float(x) for x in data1[:,2]]
table3_yields2.add_qualifier("pb", "Cross Section")
table3_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table3_yields3 = Variable("Luminosity uncertainty", is_independent=False, is_binned=False, units="")
table3_yields3.values = [float(x) for x in data1[:,3]]
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
tableFig1a.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of Z pt on dimuons."
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

mmed_Fig1a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig1a.values = histoSystPlot_0["x"]

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
tableFig1b.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of Z pt on dielectrons."
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

mmed_Fig1b = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig1b.values = histoSystPlot_0["x"]

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
tableFig1c.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of rapidity on dimuons."
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

mmed_Fig1c = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig1c.values = histoSystPlot_0["x"]

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
tableFig1d.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of rapidity on dielectrons."
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

mmed_Fig1d = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig1d.values = histoSystPlot_0["x"]

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
tableFig1e.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dimuons."
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

mmed_Fig1e = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig1e.values = histoSystPlot_0["x"]

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
tableFig1f.description = "The relative statistical and systematic uncertainties from various sources for the absolute cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dielectrons."
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

mmed_Fig1f = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig1f.values = histoSystPlot_0["x"]

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
tableFig2a.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of Z pt on dimuons."
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

mmed_Fig2a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2a.values = histoSystPlot_0["x"]

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
tableFig2b.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of Z pt on dielectrons."
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

mmed_Fig2b = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2b.values = histoSystPlot_0["x"]

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
tableFig2c.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of rapidity on dimuons."
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

mmed_Fig2c = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig2c.values = histoSystPlot_0["x"]

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
tableFig2d.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of rapidity on dielectrons."
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

mmed_Fig2d = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig2d.values = histoSystPlot_0["x"]

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
tableFig2e.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dimuons."
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

mmed_Fig2e = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig2e.values = histoSystPlot_0["x"]

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
tableFig2f.description = "The relative statistical and systematic uncertainties from various sources for the normalized cross section measurements in bins of $\phi^{\scriptscriptstyle *}_\eta$ on dielectrons."
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

mmed_Fig2f = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig2f.values = histoSystPlot_0["x"]

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
tableFig3a.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0 < rapidity < 0.4 bin in the dimuon final state."
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

mmed_Fig3a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3a.values = histoSystPlot_0["x"]

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
tableFig3b.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.4 < rapidity < 0.8 bin in the dimuon final state."
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

mmed_Fig3b = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3b.values = histoSystPlot_0["x"]

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
tableFig3c.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.8 < rapidity < 1.2 bin in the dimuon final state."
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

mmed_Fig3c = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3c.values = histoSystPlot_0["x"]

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
tableFig3d.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.2 < rapidity < 1.6 bin in the dimuon final state."
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

mmed_Fig3d = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3d.values = histoSystPlot_0["x"]

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
tableFig3e.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.6 < rapidity < 2.4 bin in the dimuon final state."
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

mmed_Fig3e = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3e.values = histoSystPlot_0["x"]

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
tableFig4a.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0 < rapidity < 0.4 bin in the dielectron final state."
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

mmed_Fig4a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig4a.values = histoSystPlot_0["x"]

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
tableFig4b.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.4 < rapidity < 0.8 bin in the dielectron final state."
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

mmed_Fig4b = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig4b.values = histoSystPlot_0["x"]

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
tableFig4c.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 0.8 < rapidity < 1.2 bin in the dielectron final state."
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

mmed_Fig4c = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig4c.values = histoSystPlot_0["x"]

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
tableFig4d.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.2 < rapidity < 1.6 bin in the dielectron final state."
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

mmed_Fig4d = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig4d.values = histoSystPlot_0["x"]

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
tableFig4e.description = "The relative statistical and systematic uncertainties from various sources for the absolute double-differential cross section measurements in bins of Z pt for the 1.6 < rapidity < 2.4 bin in the dielectron final state."
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

mmed_Fig4e = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig4e.values = histoSystPlot_0["x"]

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
tableFig5.description = "The measured absolute cross sections in bins of rapidity."
tableFig5.location = "Data from Figure 5"
tableFig5.keywords["observables"] = ["N"]

histo_unfoldFig5a = reader_Fig5a.read_hist_1d("unfold")
histo_unfoldFig5b = reader_Fig5b.read_hist_1d("unfold")
histo_unfoldFig5c = reader_Fig5c.read_hist_1d("unfold")

histo_unfoldFig5a.keys()

for key in histo_unfoldFig5a.keys():
    print(key, type(histo_unfoldFig5a[key]), type(histo_unfoldFig5a[key][0]))

mmed_Fig5 = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig5.values = histo_unfoldFig5a["x"]

# y-axis: N events
unfoldFig5a = Variable("Dimuon cross section", is_independent=False, is_binned=False, units="")
unfoldFig5a.values = histo_unfoldFig5a["y"]

unc_unfoldFig5a = Uncertainty("", is_symmetric=True)
unc_unfoldFig5a.values = histo_unfoldFig5a["dy"]

unfoldFig5a.add_uncertainty(unc_unfoldFig5a)

unfoldFig5b = Variable("Dielectron cross section", is_independent=False, is_binned=False, units="")
unfoldFig5b.values = histo_unfoldFig5b["y"]

unc_unfoldFig5b = Uncertainty("", is_symmetric=True)
unc_unfoldFig5b.values = histo_unfoldFig5b["dy"]

unfoldFig5b.add_uncertainty(unc_unfoldFig5b)

unfoldFig5c = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
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
tableFig6.description = "The measured absolute cross sections in bins of Z pt."
tableFig6.location = "Data from Figure 6"
tableFig6.keywords["observables"] = ["N"]

histo_unfoldFig6a = reader_Fig6a.read_hist_1d("unfold")
histo_unfoldFig6b = reader_Fig6b.read_hist_1d("unfold")
histo_unfoldFig6c = reader_Fig6c.read_hist_1d("unfold")

histo_unfoldFig6a.keys()

for key in histo_unfoldFig6a.keys():
    print(key, type(histo_unfoldFig6a[key]), type(histo_unfoldFig6a[key][0]))

mmed_Fig6 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig6.values = histo_unfoldFig6a["x"]

# y-axis: N events
unfoldFig6a = Variable("Dimuon cross section", is_independent=False, is_binned=False, units="")
unfoldFig6a.values = histo_unfoldFig6a["y"]

unc_unfoldFig6a = Uncertainty("", is_symmetric=True)
unc_unfoldFig6a.values = histo_unfoldFig6a["dy"]

unfoldFig6a.add_uncertainty(unc_unfoldFig6a)

unfoldFig6b = Variable("Dielectron cross section", is_independent=False, is_binned=False, units="")
unfoldFig6b.values = histo_unfoldFig6b["y"]

unc_unfoldFig6b = Uncertainty("", is_symmetric=True)
unc_unfoldFig6b.values = histo_unfoldFig6b["dy"]

unfoldFig6b.add_uncertainty(unc_unfoldFig6b)

unfoldFig6c = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
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
tableFig8.description = "The measured absolute cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$."
tableFig8.location = "Data from Figure 8"
tableFig8.keywords["observables"] = ["N"]

histo_unfoldFig8a = reader_Fig8a.read_hist_1d("unfold")
histo_unfoldFig8b = reader_Fig8b.read_hist_1d("unfold")
histo_unfoldFig8c = reader_Fig8c.read_hist_1d("unfold")

histo_unfoldFig8a.keys()

for key in histo_unfoldFig8a.keys():
    print(key, type(histo_unfoldFig8a[key]), type(histo_unfoldFig8a[key][0]))

mmed_Fig8 = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig8.values = histo_unfoldFig8a["x"]

# y-axis: N events
unfoldFig8a = Variable("Dimuon cross section", is_independent=False, is_binned=False, units="")
unfoldFig8a.values = histo_unfoldFig8a["y"]

unc_unfoldFig8a = Uncertainty("", is_symmetric=True)
unc_unfoldFig8a.values = histo_unfoldFig8a["dy"]

unfoldFig8a.add_uncertainty(unc_unfoldFig8a)

unfoldFig8b = Variable("Dielectron cross section", is_independent=False, is_binned=False, units="")
unfoldFig8b.values = histo_unfoldFig8b["y"]

unc_unfoldFig8b = Uncertainty("", is_symmetric=True)
unc_unfoldFig8b.values = histo_unfoldFig8b["dy"]

unfoldFig8b.add_uncertainty(unc_unfoldFig8b)

unfoldFig8c = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
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
tableFig9to13.description = "The measured absolute cross sections in bins of Z pt different rapidity bins."
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

mmed_Fig9to13 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig9to13.values = histo_unfoldFig9to13a["x"]

# y-axis: N events
unfoldFig9to13a = Variable("Dilepton cross section in 0 < rapidity < 0.4 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13a.values = histo_unfoldFig9to13a["y"]

unc_unfoldFig9to13a = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13a.values = histo_unfoldFig9to13a["dy"]

unfoldFig9to13a.add_uncertainty(unc_unfoldFig9to13a)

unfoldFig9to13b = Variable("Dilepton cross section in 0.4 < rapidity < 0.8 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13b.values = histo_unfoldFig9to13b["y"]

unc_unfoldFig9to13b = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13b.values = histo_unfoldFig9to13b["dy"]

unfoldFig9to13b.add_uncertainty(unc_unfoldFig9to13b)

unfoldFig9to13c = Variable("Dilepton cross section in 0.8 < rapidity < 1.2 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13c.values = histo_unfoldFig9to13c["y"]

unc_unfoldFig9to13c = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13c.values = histo_unfoldFig9to13c["dy"]

unfoldFig9to13c.add_uncertainty(unc_unfoldFig9to13c)

unfoldFig9to13d = Variable("Dilepton cross section in 1.2 < rapidity < 1.6 bin", is_independent=False, is_binned=False, units="")
unfoldFig9to13d.values = histo_unfoldFig9to13d["y"]

unc_unfoldFig9to13d = Uncertainty("", is_symmetric=True)
unc_unfoldFig9to13d.values = histo_unfoldFig9to13d["dy"]

unfoldFig9to13d.add_uncertainty(unc_unfoldFig9to13d)

unfoldFig9to13e = Variable("Dilepton cross section in 1.6 < rapidity < 2.4 bin", is_independent=False, is_binned=False, units="")
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
tableFig14a.description = "The measured normalized cross sections in bins of Z pt."
tableFig14a.location = "Data from Figure 14a"
tableFig14a.keywords["observables"] = ["N"]

histo_unfoldFig14a = reader_Fig14a.read_hist_1d("unfold")
histo_unfoldFig14a = reader_Fig14a.read_hist_1d("unfold")

histo_unfoldFig14a.keys()

for key in histo_unfoldFig14a.keys():
    print(key, type(histo_unfoldFig14a[key]), type(histo_unfoldFig14a[key][0]))

mmed_Fig14a = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig14a.values = histo_unfoldFig14a["x"]

# y-axis: N events
unfoldFig14a = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14a.values = histo_unfoldFig14a["y"]

unc_unfoldFig14a = Uncertainty("", is_symmetric=True)
unc_unfoldFig14a.values = histo_unfoldFig14a["dy"]

unfoldFig14a.add_uncertainty(unc_unfoldFig14a)

unfoldFig14a.scale_values(lumi_sf)

tableFig14a.add_variable(mmed_Fig14a)
tableFig14a.add_variable(unfoldFig14a)
submission.add_table(tableFig14a)
### End Fig14a

### Begin Fig14b
reader_Fig14b = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystPhiStar_nsel2_dy3_rebin1_default.root")

tableFig14b = Table("Figure 14b")
tableFig14b.description = "The measured normalized cross sections in bins of $\phi^{\scriptscriptstyle *}_\eta$."
tableFig14b.location = "Data from Figure 14b"
tableFig14b.keywords["observables"] = ["N"]

histo_unfoldFig14b = reader_Fig14b.read_hist_1d("unfold")
histo_unfoldFig14b = reader_Fig14b.read_hist_1d("unfold")

histo_unfoldFig14b.keys()

for key in histo_unfoldFig14b.keys():
    print(key, type(histo_unfoldFig14b[key]), type(histo_unfoldFig14b[key][0]))

mmed_Fig14b = Variable("$\phi^{\scriptscriptstyle *}_\eta$", is_independent=True, is_binned=False, units="")
mmed_Fig14b.values = histo_unfoldFig14b["x"]

# y-axis: N events
unfoldFig14b = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14b.values = histo_unfoldFig14b["y"]

unc_unfoldFig14b = Uncertainty("", is_symmetric=True)
unc_unfoldFig14b.values = histo_unfoldFig14b["dy"]

unfoldFig14b.add_uncertainty(unc_unfoldFig14b)

unfoldFig14b.scale_values(lumi_sf)

tableFig14b.add_variable(mmed_Fig14b)
tableFig14b.add_variable(unfoldFig14b)
submission.add_table(tableFig14b)
### End Fig14b

### Begin Fig14c
reader_Fig14c = RootFileReader("HEPData/inputs/smp17010/folders_dressedleptons/outputs/histoUnfolding_XSRatioSystRap_nsel2_dy3_rebin1_default.root")

tableFig14c = Table("Figure 14c")
tableFig14c.description = "The measured normalized cross sections in bins of rapidity."
tableFig14c.location = "Data from Figure 14c"
tableFig14c.keywords["observables"] = ["N"]

histo_unfoldFig14c = reader_Fig14c.read_hist_1d("unfold")
histo_unfoldFig14c = reader_Fig14c.read_hist_1d("unfold")

histo_unfoldFig14c.keys()

for key in histo_unfoldFig14c.keys():
    print(key, type(histo_unfoldFig14c[key]), type(histo_unfoldFig14c[key][0]))

mmed_Fig14c = Variable("Rapidity", is_independent=True, is_binned=False, units="")
mmed_Fig14c.values = histo_unfoldFig14c["x"]

# y-axis: N events
unfoldFig14c = Variable("Dilepton cross section", is_independent=False, is_binned=False, units="")
unfoldFig14c.values = histo_unfoldFig14c["y"]

unc_unfoldFig14c = Uncertainty("", is_symmetric=True)
unc_unfoldFig14c.values = histo_unfoldFig14c["dy"]

unfoldFig14c.add_uncertainty(unc_unfoldFig14c)

unfoldFig14c.scale_values(lumi_sf)

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
tableFig15to19.description = "The measured normalized cross sections (left) in bins of Z pt in rapidity bins."
tableFig15to19.location = "Data from Figure 15 to 19"
tableFig15to19.keywords["observables"] = ["N"]

histo_unfoldFig15to19a = reader_Fig15to19a.read_hist_1d("unfold")
histo_unfoldFig15to19b = reader_Fig15to19b.read_hist_1d("unfold")
histo_unfoldFig15to19c = reader_Fig15to19c.read_hist_1d("unfold")
histo_unfoldFig15to19d = reader_Fig15to19d.read_hist_1d("unfold")
histo_unfoldFig15to19e = reader_Fig15to19e.read_hist_1d("unfold")

histo_unfoldFig15to19a.keys()

for key in histo_unfoldFig15to19a.keys():
    print(key, type(histo_unfoldFig15to19a[key]), type(histo_unfoldFig15to19a[key][0]))

mmed_Fig15to19 = Variable("$p_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig15to19.values = histo_unfoldFig15to19a["x"]

# y-axis: N events
unfoldFig15to19a = Variable("Dilepton cross section in 0 < rapidity < 0.4", is_independent=False, is_binned=False, units="")
unfoldFig15to19a.values = histo_unfoldFig15to19a["y"]
unc_unfoldFig15to19a = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19a.values = histo_unfoldFig15to19a["dy"]
unfoldFig15to19a.add_uncertainty(unc_unfoldFig15to19a)

unfoldFig15to19b = Variable("Dilepton cross section in 0.4 < rapidity < 0.8", is_independent=False, is_binned=False, units="")
unfoldFig15to19b.values = histo_unfoldFig15to19b["y"]
unc_unfoldFig15to19b = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19b.values = histo_unfoldFig15to19b["dy"]
unfoldFig15to19b.add_uncertainty(unc_unfoldFig15to19b)

unfoldFig15to19c = Variable("Dilepton cross section in 0.8 < rapidity < 1.2", is_independent=False, is_binned=False, units="")
unfoldFig15to19c.values = histo_unfoldFig15to19c["y"]
unc_unfoldFig15to19c = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19c.values = histo_unfoldFig15to19c["dy"]
unfoldFig15to19c.add_uncertainty(unc_unfoldFig15to19c)

unfoldFig15to19d = Variable("Dilepton cross section in 1.2 < rapidity < 1.6", is_independent=False, is_binned=False, units="")
unfoldFig15to19d.values = histo_unfoldFig15to19d["y"]
unc_unfoldFig15to19d = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19d.values = histo_unfoldFig15to19d["dy"]
unfoldFig15to19d.add_uncertainty(unc_unfoldFig15to19d)

unfoldFig15to19e = Variable("Dilepton cross section in 1.6 < rapidity < 2.4", is_independent=False, is_binned=False, units="")
unfoldFig15to19e.values = histo_unfoldFig15to19e["y"]
unc_unfoldFig15to19e = Uncertainty("", is_symmetric=True)
unc_unfoldFig15to19e.values = histo_unfoldFig15to19e["dy"]
unfoldFig15to19e.add_uncertainty(unc_unfoldFig15to19e)

unfoldFig15to19a.scale_values(lumi_sf)
unfoldFig15to19b.scale_values(lumi_sf)
unfoldFig15to19c.scale_values(lumi_sf)
unfoldFig15to19d.scale_values(lumi_sf)
unfoldFig15to19e.scale_values(lumi_sf)

tableFig15to19.add_variable(mmed_Fig15to19)
tableFig15to19.add_variable(unfoldFig15to19a)
tableFig15to19.add_variable(unfoldFig15to19b)
tableFig15to19.add_variable(unfoldFig15to19c)
tableFig15to19.add_variable(unfoldFig15to19d)
tableFig15to19.add_variable(unfoldFig15to19e)
submission.add_table(tableFig15to19)
### End Fig15to19

### Begin covariance mumu
# Create a reader for the input file
reader_covariance_mm_Pt = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_Pt.root")
# Read the histogram
data_covariance_mm_Pt = reader_covariance_mm_Pt.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Pt = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_Pt.values = data_covariance_mm_Pt["x"]
y_covariance_mm_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Pt.values = data_covariance_mm_Pt["y"]
z_covariance_mm_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Pt.values = data_covariance_mm_Pt["z"]

table_covariance_mm_Pt = Table("Covariance Matrix auxiliary 1a")
table_covariance_mm_Pt.description = "Covariance matrix for all bins used in bins of Z pt in the dimuon final state."
table_covariance_mm_Pt.location = "Supplementary material"
for var in [x_covariance_mm_Pt,y_covariance_mm_Pt,z_covariance_mm_Pt]:
    table_covariance_mm_Pt.add_variable(var)
submission.add_table(table_covariance_mm_Pt)

# Create a reader for the input file
reader_covariance_mm_Rap = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_Rap.root")
# Read the histogram
data_covariance_mm_Rap = reader_covariance_mm_Rap.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_Rap = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_Rap.values = data_covariance_mm_Rap["x"]
y_covariance_mm_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_Rap.values = data_covariance_mm_Rap["y"]
z_covariance_mm_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_Rap.values = data_covariance_mm_Rap["z"]

table_covariance_mm_Rap = Table("Covariance Matrix auxiliary 1b")
table_covariance_mm_Rap.description = "Covariance matrix for all bins used in bins of rapidity in the dimuon final state."
table_covariance_mm_Rap.location = "Supplementary material"
for var in [x_covariance_mm_Rap,y_covariance_mm_Rap,z_covariance_mm_Rap]:
    table_covariance_mm_Rap.add_variable(var)
submission.add_table(table_covariance_mm_Rap)

# Create a reader for the input file
reader_covariance_mm_PhiStar = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PhiStar.root")
# Read the histogram
data_covariance_mm_PhiStar = reader_covariance_mm_PhiStar.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PhiStar = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["x"]
y_covariance_mm_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["y"]
z_covariance_mm_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PhiStar.values = data_covariance_mm_PhiStar["z"]

table_covariance_mm_PhiStar = Table("Covariance Matrix auxiliary 1c")
table_covariance_mm_PhiStar.description = "Covariance matrix for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dimuon final state."
table_covariance_mm_PhiStar.location = "Supplementary material"
for var in [x_covariance_mm_PhiStar,y_covariance_mm_PhiStar,z_covariance_mm_PhiStar]:
    table_covariance_mm_PhiStar.add_variable(var)
submission.add_table(table_covariance_mm_PhiStar)

# Create a reader for the input file
reader_covariance_mm_PtRap0 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PtRap0.root")
# Read the histogram
data_covariance_mm_PtRap0 = reader_covariance_mm_PtRap0.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap0 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["x"]
y_covariance_mm_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["y"]
z_covariance_mm_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap0.values = data_covariance_mm_PtRap0["z"]

table_covariance_mm_PtRap0 = Table("Covariance Matrix auxiliary 1d")
table_covariance_mm_PtRap0.description = "Covariance matrix for all bins used in bins of Z pt for the 0 < rapidity < 0.4 bin in the dimuon final state."
table_covariance_mm_PtRap0.location = "Supplementary material"
for var in [x_covariance_mm_PtRap0,y_covariance_mm_PtRap0,z_covariance_mm_PtRap0]:
    table_covariance_mm_PtRap0.add_variable(var)
submission.add_table(table_covariance_mm_PtRap0)

# Create a reader for the input file
reader_covariance_mm_PtRap1 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PtRap1.root")
# Read the histogram
data_covariance_mm_PtRap1 = reader_covariance_mm_PtRap1.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap1 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["x"]
y_covariance_mm_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["y"]
z_covariance_mm_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap1.values = data_covariance_mm_PtRap1["z"]

table_covariance_mm_PtRap1 = Table("Covariance Matrix auxiliary 1e")
table_covariance_mm_PtRap1.description = "Covariance matrix for all bins used in bins of Z pt for the 0.4 < rapidity < 0.8 bin in the dimuon final state."
table_covariance_mm_PtRap1.location = "Supplementary material"
for var in [x_covariance_mm_PtRap1,y_covariance_mm_PtRap1,z_covariance_mm_PtRap1]:
    table_covariance_mm_PtRap1.add_variable(var)
submission.add_table(table_covariance_mm_PtRap1)

# Create a reader for the input file
reader_covariance_mm_PtRap2 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PtRap2.root")
# Read the histogram
data_covariance_mm_PtRap2 = reader_covariance_mm_PtRap2.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap2 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["x"]
y_covariance_mm_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["y"]
z_covariance_mm_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap2.values = data_covariance_mm_PtRap2["z"]

table_covariance_mm_PtRap2 = Table("Covariance Matrix auxiliary 1f")
table_covariance_mm_PtRap2.description = "Covariance matrix for all bins used in bins of Z pt for the 0.8 < rapidity < 1.2 bin in the dimuon final state."
table_covariance_mm_PtRap2.location = "Supplementary material"
for var in [x_covariance_mm_PtRap2,y_covariance_mm_PtRap2,z_covariance_mm_PtRap2]:
    table_covariance_mm_PtRap2.add_variable(var)
submission.add_table(table_covariance_mm_PtRap2)

# Create a reader for the input file
reader_covariance_mm_PtRap3 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PtRap3.root")
# Read the histogram
data_covariance_mm_PtRap3 = reader_covariance_mm_PtRap3.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap3 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["x"]
y_covariance_mm_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["y"]
z_covariance_mm_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap3.values = data_covariance_mm_PtRap3["z"]

table_covariance_mm_PtRap3 = Table("Covariance Matrix auxiliary 1g")
table_covariance_mm_PtRap3.description = "Covariance matrix for all bins used in bins of Z pt for the 1.2 < rapidity < 1.6 bin in the dimuon final state."
table_covariance_mm_PtRap3.location = "Supplementary material"
for var in [x_covariance_mm_PtRap3,y_covariance_mm_PtRap3,z_covariance_mm_PtRap3]:
    table_covariance_mm_PtRap3.add_variable(var)
submission.add_table(table_covariance_mm_PtRap3)

# Create a reader for the input file
reader_covariance_mm_PtRap4 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix03_PtRap4.root")
# Read the histogram
data_covariance_mm_PtRap4 = reader_covariance_mm_PtRap4.read_hist_2d("covariance_totsum_0")
# Create variable objects
x_covariance_mm_PtRap4 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["x"]
y_covariance_mm_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["y"]
z_covariance_mm_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_mm_PtRap4.values = data_covariance_mm_PtRap4["z"]

table_covariance_mm_PtRap4 = Table("Covariance Matrix auxiliary 1h")
table_covariance_mm_PtRap4.description = "Covariance matrix for all bins used in bins of Z pt for the 1.6 < rapidity < 2.4 bin in the dimuon final state."
table_covariance_mm_PtRap4.location = "Supplementary material"
for var in [x_covariance_mm_PtRap4,y_covariance_mm_PtRap4,z_covariance_mm_PtRap4]:
    table_covariance_mm_PtRap4.add_variable(var)
submission.add_table(table_covariance_mm_PtRap4)
### End covariance mumu

### Begin covariance ee
# Create a reader for the input file
reader_covariance_ee_Pt = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_Pt.root")
# Read the histogram
data_covariance_ee_Pt = reader_covariance_ee_Pt.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Pt = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_Pt.values = data_covariance_ee_Pt["x"]
y_covariance_ee_Pt = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Pt.values = data_covariance_ee_Pt["y"]
z_covariance_ee_Pt = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Pt.values = data_covariance_ee_Pt["z"]

table_covariance_ee_Pt = Table("Covariance Matrix auxiliary 2a")
table_covariance_ee_Pt.description = "Covariance matrix for all bins used in bins of Z pt in the dielectron final state."
table_covariance_ee_Pt.location = "Supplementary material"
for var in [x_covariance_ee_Pt,y_covariance_ee_Pt,z_covariance_ee_Pt]:
    table_covariance_ee_Pt.add_variable(var)
submission.add_table(table_covariance_ee_Pt)

# Create a reader for the input file
reader_covariance_ee_Rap = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_Rap.root")
# Read the histogram
data_covariance_ee_Rap = reader_covariance_ee_Rap.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_Rap = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_Rap.values = data_covariance_ee_Rap["x"]
y_covariance_ee_Rap = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_Rap.values = data_covariance_ee_Rap["y"]
z_covariance_ee_Rap = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_Rap.values = data_covariance_ee_Rap["z"]

table_covariance_ee_Rap = Table("Covariance Matrix auxiliary 2b")
table_covariance_ee_Rap.description = "Covariance matrix for all bins used in bins of rapidity in the dielectron final state."
table_covariance_ee_Rap.location = "Supplementary material"
for var in [x_covariance_ee_Rap,y_covariance_ee_Rap,z_covariance_ee_Rap]:
    table_covariance_ee_Rap.add_variable(var)
submission.add_table(table_covariance_ee_Rap)

# Create a reader for the input file
reader_covariance_ee_PhiStar = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PhiStar.root")
# Read the histogram
data_covariance_ee_PhiStar = reader_covariance_ee_PhiStar.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PhiStar = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["x"]
y_covariance_ee_PhiStar = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["y"]
z_covariance_ee_PhiStar = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PhiStar.values = data_covariance_ee_PhiStar["z"]

table_covariance_ee_PhiStar = Table("Covariance Matrix auxiliary 2c")
table_covariance_ee_PhiStar.description = "Covariance matrix for all bins used in bins of $\phi^{\scriptscriptstyle *}_\eta$ in the dielectron final state."
table_covariance_ee_PhiStar.location = "Supplementary material"
for var in [x_covariance_ee_PhiStar,y_covariance_ee_PhiStar,z_covariance_ee_PhiStar]:
    table_covariance_ee_PhiStar.add_variable(var)
submission.add_table(table_covariance_ee_PhiStar)

# Create a reader for the input file
reader_covariance_ee_PtRap0 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PtRap0.root")
# Read the histogram
data_covariance_ee_PtRap0 = reader_covariance_ee_PtRap0.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap0 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["x"]
y_covariance_ee_PtRap0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["y"]
z_covariance_ee_PtRap0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap0.values = data_covariance_ee_PtRap0["z"]

table_covariance_ee_PtRap0 = Table("Covariance Matrix auxiliary 2d")
table_covariance_ee_PtRap0.description = "Covariance matrix for all bins used in bins of Z pt for the 0 < rapidity < 0.4 bin in the dielectron final state."
table_covariance_ee_PtRap0.location = "Supplementary material"
for var in [x_covariance_ee_PtRap0,y_covariance_ee_PtRap0,z_covariance_ee_PtRap0]:
    table_covariance_ee_PtRap0.add_variable(var)
submission.add_table(table_covariance_ee_PtRap0)

# Create a reader for the input file
reader_covariance_ee_PtRap1 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PtRap1.root")
# Read the histogram
data_covariance_ee_PtRap1 = reader_covariance_ee_PtRap1.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap1 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["x"]
y_covariance_ee_PtRap1 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["y"]
z_covariance_ee_PtRap1 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap1.values = data_covariance_ee_PtRap1["z"]

table_covariance_ee_PtRap1 = Table("Covariance Matrix auxiliary 2e")
table_covariance_ee_PtRap1.description = "Covariance matrix for all bins used in bins of Z pt for the 0.4 < rapidity < 0.8 bin in the dielectron final state."
table_covariance_ee_PtRap1.location = "Supplementary material"
for var in [x_covariance_ee_PtRap1,y_covariance_ee_PtRap1,z_covariance_ee_PtRap1]:
    table_covariance_ee_PtRap1.add_variable(var)
submission.add_table(table_covariance_ee_PtRap1)

# Create a reader for the input file
reader_covariance_ee_PtRap2 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PtRap2.root")
# Read the histogram
data_covariance_ee_PtRap2 = reader_covariance_ee_PtRap2.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap2 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["x"]
y_covariance_ee_PtRap2 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["y"]
z_covariance_ee_PtRap2 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap2.values = data_covariance_ee_PtRap2["z"]

table_covariance_ee_PtRap2 = Table("Covariance Matrix auxiliary 2f")
table_covariance_ee_PtRap2.description = "Covariance matrix for all bins used in bins of Z pt for the 0.8 < rapidity < 1.2 bin in the dielectron final state."
table_covariance_ee_PtRap2.location = "Supplementary material"
for var in [x_covariance_ee_PtRap2,y_covariance_ee_PtRap2,z_covariance_ee_PtRap2]:
    table_covariance_ee_PtRap2.add_variable(var)
submission.add_table(table_covariance_ee_PtRap2)

# Create a reader for the input file
reader_covariance_ee_PtRap3 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PtRap3.root")
# Read the histogram
data_covariance_ee_PtRap3 = reader_covariance_ee_PtRap3.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap3 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["x"]
y_covariance_ee_PtRap3 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["y"]
z_covariance_ee_PtRap3 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap3.values = data_covariance_ee_PtRap3["z"]

table_covariance_ee_PtRap3 = Table("Covariance Matrix auxiliary 2g")
table_covariance_ee_PtRap3.description = "Covariance matrix for all bins used in bins of Z pt for the 1.2 < rapidity < 1.6 bin in the dielectron final state."
table_covariance_ee_PtRap3.location = "Supplementary material"
for var in [x_covariance_ee_PtRap3,y_covariance_ee_PtRap3,z_covariance_ee_PtRap3]:
    table_covariance_ee_PtRap3.add_variable(var)
submission.add_table(table_covariance_ee_PtRap3)

# Create a reader for the input file
reader_covariance_ee_PtRap4 = RootFileReader("HEPData/inputs/smp17010/output_root/matrix13_PtRap4.root")
# Read the histogram
data_covariance_ee_PtRap4 = reader_covariance_ee_PtRap4.read_hist_2d("covariance_totsum_1")
# Create variable objects
x_covariance_ee_PtRap4 = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["x"]
y_covariance_ee_PtRap4 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["y"]
z_covariance_ee_PtRap4 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ee_PtRap4.values = data_covariance_ee_PtRap4["z"]

table_covariance_ee_PtRap4 = Table("Covariance Matrix auxiliary 2h")
table_covariance_ee_PtRap4.description = "Covariance matrix for all bins used in bins of Z pt for the 1.6 < rapidity < 2.4 bin in the dielectron final state."
table_covariance_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_ee_PtRap4)
### End covariance ee

"""
### Begin WZ CR
reader_wzcr = RootFileReader("HEPData/inputs/exo19007/histo_zhg_region1.root")

tableWZCR = Table("Figure 2b")
tableWZCR.description = "$\mathrm{M_{\mathrm{T}}}$ distribution for the WZ control region."
tableWZCR.location = "Data from Figure 2b"
tableWZCR.keywords["observables"] = ["N"]

histo_Data_wzcr  = reader_wzcr.read_hist_1d("histo_Data")
histo_ZZ_wzcr    = reader_wzcr.read_hist_1d("histo_ZZ")
histo_WZ_wzcr    = reader_wzcr.read_hist_1d("histo_WZ")
histo_VVV_wzcr   = reader_wzcr.read_hist_1d("histo_VVV")
histo_VG_wzcr    = reader_wzcr.read_hist_1d("histo_VG")
histo_WZ_wzcr    = reader_wzcr.read_hist_1d("histo_WZ")
histo_ZH125_wzcr = reader_wzcr.read_hist_1d("histo_ZH125")
histo_ZH200_wzcr = reader_wzcr.read_hist_1d("histo_ZH200")
histo_ZH300_wzcr = reader_wzcr.read_hist_1d("histo_ZH300")
histo_Bck_wzcr   = reader_wzcr.read_hist_1d("histo_WZ")

histo_Bck_wzcr.keys()

mmed_wzcr = Variable("$M_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_wzcr.values = histo_ZH125_wzcr["x"]

# y-axis: N events
ZH125_wzcr = Variable("Number of ZH(125) signal events", is_independent=False, is_binned=False, units="")
ZH125_wzcr.values = histo_ZH125_wzcr["y"]

ZH200_wzcr = Variable("Number of ZH(200) signal events", is_independent=False, is_binned=False, units="")
ZH200_wzcr.values = histo_ZH200_wzcr["y"]

ZH300_wzcr = Variable("Number of ZH(300) signal events", is_independent=False, is_binned=False, units="")
ZH300_wzcr.values = histo_ZH300_wzcr["y"]

totalbackground_wzcr = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_wzcr.values = histo_Bck_wzcr["y"]

unc_totalbackground_wzcr = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_wzcr.values = histo_Bck_wzcr["dy"]

totalbackground_wzcr.add_uncertainty(unc_totalbackground_wzcr)

ZZ_wzcr = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_wzcr.values = histo_ZZ_wzcr["y"]

WZ_wzcr = Variable("Number of WZ events", is_independent=False, is_binned=False, units="")
WZ_wzcr.values = histo_WZ_wzcr["y"]

VVV_wzcr = Variable("Number of VVV events", is_independent=False, is_binned=False, units="")
VVV_wzcr.values = histo_VVV_wzcr["y"]

VG_wzcr = Variable("Number of VG events", is_independent=False, is_binned=False, units="")
VG_wzcr.values = histo_VG_wzcr["y"]

EM_wzcr = Variable("Number of nonresonant events", is_independent=False, is_binned=False, units="")
EM_wzcr.values = histo_WZ_wzcr["y"]

Data_wzcr = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_wzcr.values = histo_Data_wzcr["y"]

unc_data_wzcr = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_wzcr.values = histo_Data_wzcr["dy"]
Data_wzcr.add_uncertainty(unc_data_wzcr)

tableWZCR.add_variable(mmed_wzcr)
tableWZCR.add_variable(ZH125_wzcr)
tableWZCR.add_variable(ZH200_wzcr)
tableWZCR.add_variable(ZH300_wzcr)
tableWZCR.add_variable(totalbackground_wzcr)
tableWZCR.add_variable(ZZ_wzcr)
tableWZCR.add_variable(WZ_wzcr)
tableWZCR.add_variable(VVV_wzcr)
tableWZCR.add_variable(VG_wzcr)
tableWZCR.add_variable(EM_wzcr)
tableWZCR.add_variable(Data_wzcr)
submission.add_table(tableWZCR)
### End WZ CR

### Begin ZZ CR
reader_zzcr = RootFileReader("HEPData/inputs/exo19007/histo_zhg_region2.root")

tableZZCR = Table("Figure 2c")
tableZZCR.description = "$\mathrm{M_{\mathrm{T}}}$ distribution for the ZZ control region."
tableZZCR.location = "Data from Figure 2c"
tableZZCR.keywords["observables"] = ["N"]

histo_Data_zzcr  = reader_zzcr.read_hist_1d("histo_Data")
histo_ZZ_zzcr    = reader_zzcr.read_hist_1d("histo_ZZ")
histo_WZ_zzcr    = reader_zzcr.read_hist_1d("histo_WZ")
histo_VVV_zzcr   = reader_zzcr.read_hist_1d("histo_VVV")
histo_VG_zzcr    = reader_zzcr.read_hist_1d("histo_VG")
histo_ZZ_zzcr    = reader_zzcr.read_hist_1d("histo_ZZ")
histo_ZH125_zzcr = reader_zzcr.read_hist_1d("histo_ZH125")
histo_ZH200_zzcr = reader_zzcr.read_hist_1d("histo_ZH200")
histo_ZH300_zzcr = reader_zzcr.read_hist_1d("histo_ZH300")
histo_Bck_zzcr   = reader_zzcr.read_hist_1d("histo_ZZ")

histo_Bck_zzcr.keys()

mmed_zzcr = Variable("$M_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_zzcr.values = histo_ZH125_zzcr["x"]

# y-axis: N events
ZH125_zzcr = Variable("Number of ZH(125) signal events", is_independent=False, is_binned=False, units="")
ZH125_zzcr.values = histo_ZH125_zzcr["y"]

ZH200_zzcr = Variable("Number of ZH(200) signal events", is_independent=False, is_binned=False, units="")
ZH200_zzcr.values = histo_ZH200_zzcr["y"]

ZH300_zzcr = Variable("Number of ZH(300) signal events", is_independent=False, is_binned=False, units="")
ZH300_zzcr.values = histo_ZH300_zzcr["y"]

totalbackground_zzcr = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_zzcr.values = histo_Bck_zzcr["y"]

unc_totalbackground_zzcr = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_zzcr.values = histo_Bck_zzcr["dy"]

totalbackground_zzcr.add_uncertainty(unc_totalbackground_zzcr)

ZZ_zzcr = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_zzcr.values = histo_ZZ_zzcr["y"]

WZ_zzcr = Variable("Number of WZ events", is_independent=False, is_binned=False, units="")
WZ_zzcr.values = histo_WZ_zzcr["y"]

VVV_zzcr = Variable("Number of VVV events", is_independent=False, is_binned=False, units="")
VVV_zzcr.values = histo_VVV_zzcr["y"]

VG_zzcr = Variable("Number of VG events", is_independent=False, is_binned=False, units="")
VG_zzcr.values = histo_VG_zzcr["y"]

EM_zzcr = Variable("Number of nonresonant events", is_independent=False, is_binned=False, units="")
EM_zzcr.values = histo_ZZ_zzcr["y"]

Data_zzcr = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_zzcr.values = histo_Data_zzcr["y"]

unc_data_zzcr = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_zzcr.values = histo_Data_zzcr["dy"]
Data_zzcr.add_uncertainty(unc_data_zzcr)

tableZZCR.add_variable(mmed_zzcr)
tableZZCR.add_variable(ZH125_zzcr)
tableZZCR.add_variable(ZH200_zzcr)
tableZZCR.add_variable(ZH300_zzcr)
tableZZCR.add_variable(totalbackground_zzcr)
tableZZCR.add_variable(ZZ_zzcr)
tableZZCR.add_variable(WZ_zzcr)
tableZZCR.add_variable(VVV_zzcr)
tableZZCR.add_variable(VG_zzcr)
tableZZCR.add_variable(EM_zzcr)
tableZZCR.add_variable(Data_zzcr)
submission.add_table(tableZZCR)
### End ZZ CR

### Begin ETAGLT1SR CR
reader_etaglt1sr = RootFileReader("HEPData/inputs/exo19007/histo_zhg_region3.root")

tableETAGLT1SR = Table("Figure 3a")
tableETAGLT1SR.description = "$\mathrm{M_{\mathrm{T}}}$ distribution for the signal region, events with $|\eta_{\gamma}|<1$."
tableETAGLT1SR.location = "Data from Figure 3a"
tableETAGLT1SR.keywords["observables"] = ["N"]

histo_Data_etaglt1sr  = reader_etaglt1sr.read_hist_1d("histo_Data")
histo_ZZ_etaglt1sr    = reader_etaglt1sr.read_hist_1d("histo_ZZ")
histo_WZ_etaglt1sr    = reader_etaglt1sr.read_hist_1d("histo_WZ")
histo_VVV_etaglt1sr   = reader_etaglt1sr.read_hist_1d("histo_VVV")
histo_VG_etaglt1sr    = reader_etaglt1sr.read_hist_1d("histo_VG")
histo_EM_etaglt1sr    = reader_etaglt1sr.read_hist_1d("histo_EM")
histo_ZH125_etaglt1sr = reader_etaglt1sr.read_hist_1d("histo_ZH125")
histo_ZH200_etaglt1sr = reader_etaglt1sr.read_hist_1d("histo_ZH200")
histo_ZH300_etaglt1sr = reader_etaglt1sr.read_hist_1d("histo_ZH300")
histo_Bck_etaglt1sr   = reader_etaglt1sr.read_hist_1d("histo_EM")

histo_Bck_etaglt1sr.keys()

mmed_etaglt1sr = Variable("$M_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_etaglt1sr.values = histo_ZH125_etaglt1sr["x"]

# y-axis: N events
ZH125_etaglt1sr = Variable("Number of ZH(125) signal events", is_independent=False, is_binned=False, units="")
ZH125_etaglt1sr.values = histo_ZH125_etaglt1sr["y"]

ZH200_etaglt1sr = Variable("Number of ZH(200) signal events", is_independent=False, is_binned=False, units="")
ZH200_etaglt1sr.values = histo_ZH200_etaglt1sr["y"]

ZH300_etaglt1sr = Variable("Number of ZH(300) signal events", is_independent=False, is_binned=False, units="")
ZH300_etaglt1sr.values = histo_ZH300_etaglt1sr["y"]

totalbackground_etaglt1sr = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_etaglt1sr.values = histo_Bck_etaglt1sr["y"]

unc_totalbackground_etaglt1sr = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_etaglt1sr.values = histo_Bck_etaglt1sr["dy"]

totalbackground_etaglt1sr.add_uncertainty(unc_totalbackground_etaglt1sr)

ZZ_etaglt1sr = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_etaglt1sr.values = histo_ZZ_etaglt1sr["y"]

WZ_etaglt1sr = Variable("Number of WZ events", is_independent=False, is_binned=False, units="")
WZ_etaglt1sr.values = histo_WZ_etaglt1sr["y"]

VVV_etaglt1sr = Variable("Number of VVV events", is_independent=False, is_binned=False, units="")
VVV_etaglt1sr.values = histo_VVV_etaglt1sr["y"]

VG_etaglt1sr = Variable("Number of VG events", is_independent=False, is_binned=False, units="")
VG_etaglt1sr.values = histo_VG_etaglt1sr["y"]

EM_etaglt1sr = Variable("Number of nonresonant events", is_independent=False, is_binned=False, units="")
EM_etaglt1sr.values = histo_EM_etaglt1sr["y"]

Data_etaglt1sr = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_etaglt1sr.values = histo_Data_etaglt1sr["y"]

unc_data_etaglt1sr = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_etaglt1sr.values = histo_Data_etaglt1sr["dy"]
Data_etaglt1sr.add_uncertainty(unc_data_etaglt1sr)

tableETAGLT1SR.add_variable(mmed_etaglt1sr)
tableETAGLT1SR.add_variable(ZH125_etaglt1sr)
tableETAGLT1SR.add_variable(ZH200_etaglt1sr)
tableETAGLT1SR.add_variable(ZH300_etaglt1sr)
tableETAGLT1SR.add_variable(totalbackground_etaglt1sr)
tableETAGLT1SR.add_variable(ZZ_etaglt1sr)
tableETAGLT1SR.add_variable(WZ_etaglt1sr)
tableETAGLT1SR.add_variable(VVV_etaglt1sr)
tableETAGLT1SR.add_variable(VG_etaglt1sr)
tableETAGLT1SR.add_variable(EM_etaglt1sr)
tableETAGLT1SR.add_variable(Data_etaglt1sr)
submission.add_table(tableETAGLT1SR)
### End ETAGLT1SR CR

### Begin ETAGGT1SR CR
reader_etaggt1sr = RootFileReader("HEPData/inputs/exo19007/histo_zhg_region4.root")

tableETAGGT1SR = Table("Figure 3b")
tableETAGGT1SR.description = "$\mathrm{M_{\mathrm{T}}}$ distribution for the signal region, events with $|\eta_{\gamma}|>1$."
tableETAGGT1SR.location = "Data from Figure 3b"
tableETAGGT1SR.keywords["observables"] = ["N"]

histo_Data_etaggt1sr  = reader_etaggt1sr.read_hist_1d("histo_Data")
histo_ZZ_etaggt1sr    = reader_etaggt1sr.read_hist_1d("histo_ZZ")
histo_WZ_etaggt1sr    = reader_etaggt1sr.read_hist_1d("histo_WZ")
histo_VVV_etaggt1sr   = reader_etaggt1sr.read_hist_1d("histo_VVV")
histo_VG_etaggt1sr    = reader_etaggt1sr.read_hist_1d("histo_VG")
histo_EM_etaggt1sr    = reader_etaggt1sr.read_hist_1d("histo_EM")
histo_ZH125_etaggt1sr = reader_etaggt1sr.read_hist_1d("histo_ZH125")
histo_ZH200_etaggt1sr = reader_etaggt1sr.read_hist_1d("histo_ZH200")
histo_ZH300_etaggt1sr = reader_etaggt1sr.read_hist_1d("histo_ZH300")
histo_Bck_etaggt1sr   = reader_etaggt1sr.read_hist_1d("histo_EM")

histo_Bck_etaggt1sr.keys()

mmed_etaggt1sr = Variable("$M_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_etaggt1sr.values = histo_ZH125_etaggt1sr["x"]

# y-axis: N events
ZH125_etaggt1sr = Variable("Number of ZH(125) signal events", is_independent=False, is_binned=False, units="")
ZH125_etaggt1sr.values = histo_ZH125_etaggt1sr["y"]

ZH200_etaggt1sr = Variable("Number of ZH(200) signal events", is_independent=False, is_binned=False, units="")
ZH200_etaggt1sr.values = histo_ZH200_etaggt1sr["y"]

ZH300_etaggt1sr = Variable("Number of ZH(300) signal events", is_independent=False, is_binned=False, units="")
ZH300_etaggt1sr.values = histo_ZH300_etaggt1sr["y"]

totalbackground_etaggt1sr = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_etaggt1sr.values = histo_Bck_etaggt1sr["y"]

unc_totalbackground_etaggt1sr = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_etaggt1sr.values = histo_Bck_etaggt1sr["dy"]

totalbackground_etaggt1sr.add_uncertainty(unc_totalbackground_etaggt1sr)

ZZ_etaggt1sr = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_etaggt1sr.values = histo_ZZ_etaggt1sr["y"]

WZ_etaggt1sr = Variable("Number of WZ events", is_independent=False, is_binned=False, units="")
WZ_etaggt1sr.values = histo_WZ_etaggt1sr["y"]

VVV_etaggt1sr = Variable("Number of VVV events", is_independent=False, is_binned=False, units="")
VVV_etaggt1sr.values = histo_VVV_etaggt1sr["y"]

VG_etaggt1sr = Variable("Number of VG events", is_independent=False, is_binned=False, units="")
VG_etaggt1sr.values = histo_VG_etaggt1sr["y"]

EM_etaggt1sr = Variable("Number of nonresonant events", is_independent=False, is_binned=False, units="")
EM_etaggt1sr.values = histo_EM_etaggt1sr["y"]

Data_etaggt1sr = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_etaggt1sr.values = histo_Data_etaggt1sr["y"]

unc_data_etaggt1sr = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_etaggt1sr.values = histo_Data_etaggt1sr["dy"]
Data_etaggt1sr.add_uncertainty(unc_data_etaggt1sr)

tableETAGGT1SR.add_variable(mmed_etaggt1sr)
tableETAGGT1SR.add_variable(ZH125_etaggt1sr)
tableETAGGT1SR.add_variable(ZH200_etaggt1sr)
tableETAGGT1SR.add_variable(ZH300_etaggt1sr)
tableETAGGT1SR.add_variable(totalbackground_etaggt1sr)
tableETAGGT1SR.add_variable(ZZ_etaggt1sr)
tableETAGGT1SR.add_variable(WZ_etaggt1sr)
tableETAGGT1SR.add_variable(VVV_etaggt1sr)
tableETAGGT1SR.add_variable(VG_etaggt1sr)
tableETAGGT1SR.add_variable(EM_etaggt1sr)
tableETAGGT1SR.add_variable(Data_etaggt1sr)
submission.add_table(tableETAGGT1SR)
### End ETAGGT1SR CR

submission.add_additional_resource(description="Generator configuration files", location="HEPData/inputs/exo19007/zh_signal.tar.gz", copy_file=True)

### Begin hDEffMuEtaPt
# Create a reader for the input file
reader_EffMu = RootFileReader("HEPData/inputs/exo19007/histo_objectEfficiency.root")
# Read the histogram
data_EffMu = reader_EffMu.read_hist_2d("hDEffMuEtaPt")
# Create variable objects
x_EffMu = Variable("$|\eta|$", is_independent=True, is_binned=False)
x_EffMu.values = data_EffMu["x"]
y_EffMu = Variable("$\mathrm{p_\mathrm{T}}$ (GeV)", is_independent=True, is_binned=False)
y_EffMu.values = data_EffMu["y"]
z_EffMu = Variable("Muon efficiency", is_independent=False, is_binned=False)
z_EffMu.values = data_EffMu["z"]

table_EffMu = Table("Muon efficiency")
table_EffMu.description = "Muon reconstruction, identification, and isolation efficiency as a function of $|\eta|$ and $\mathrm{p_\mathrm{T}}$."
table_EffMu.location = "Supplementary material"
for var in [x_EffMu,y_EffMu,z_EffMu]:
    table_EffMu.add_variable(var)
submission.add_table(table_EffMu)
### End hDEffMuEtaPt

### Begin hDEffElEtaPt
# Create a reader for the input file
reader_EffEl = RootFileReader("HEPData/inputs/exo19007/histo_objectEfficiency.root")
# Read the histogram
data_EffEl = reader_EffEl.read_hist_2d("hDEffElEtaPt")
# Create variable objects
x_EffEl = Variable("$|\eta|$", is_independent=True, is_binned=False)
x_EffEl.values = data_EffEl["x"]
y_EffEl = Variable("$\mathrm{p_\mathrm{T}}$ (GeV)", is_independent=True, is_binned=False)
y_EffEl.values = data_EffEl["y"]
z_EffEl = Variable("Electron efficiency", is_independent=False, is_binned=False)
z_EffEl.values = data_EffEl["z"]

table_EffEl = Table("Electron efficiency")
table_EffEl.description = "Electron reconstruction, identification, and isolation efficiency as a function of $|\eta|$ and $\mathrm{p_\mathrm{T}}$."
table_EffEl.location = "Supplementary material"
for var in [x_EffEl,y_EffEl,z_EffEl]:
    table_EffEl.add_variable(var)
submission.add_table(table_EffEl)
### End hDEffElEtaPt

### Begin hDEffPhEtaPt
# Create a reader for the input file
reader_EffPh = RootFileReader("HEPData/inputs/exo19007/histo_objectEfficiency.root")
# Read the histogram
data_EffPh = reader_EffPh.read_hist_2d("hDEffPhEtaPt")
# Create variable objects
x_EffPh = Variable("$|\eta|$", is_independent=True, is_binned=False)
x_EffPh.values = data_EffPh["x"]
y_EffPh = Variable("$\mathrm{p_\mathrm{T}}$ (GeV)", is_independent=True, is_binned=False)
y_EffPh.values = data_EffPh["y"]
z_EffPh = Variable("Photon reconstruction, identification, and isolation efficiency", is_independent=False, is_binned=False)
z_EffPh.values = data_EffPh["z"]

table_EffPh = Table("Photon efficiency")
table_EffPh.description = "Photon efficiency as a function of $|\eta|$ and $\mathrm{p_\mathrm{T}}$."
table_EffPh.location = "Supplementary material"
for var in [x_EffPh,y_EffPh,z_EffPh]:
    table_EffPh.add_variable(var)
submission.add_table(table_EffPh)
### End hDEffPhEtaPt


### Begin covariance
# Create a reader for the input file
reader_covariance = RootFileReader("HEPData/inputs/exo19007/fitDiagnosticszhg_comb_125.root")
# Read the histogram
data_covariance = reader_covariance.read_hist_2d("shapes_fit_b/overall_total_covar")
# Create variable objects
x_covariance = Variable("Bin X", is_independent=True, is_binned=False)
x_covariance.values = data_covariance["x"]
y_covariance = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance.values = data_covariance["y"]
z_covariance = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance.values = data_covariance["z"]

table_covariance = Table("Covariance Matrix")
table_covariance.description = "Covariance matrix for all bins used in the analysis. There are 45 bins in total, 15 for every data-taking year. For every year, the first bin corresponds to events in the $\mathrm{e}\mu$ control region, the following five bins correspond to events with $|\eta^\gamma|< 1$ in the signal region, the next five bins correspond to events with $|\eta^\gamma|> 1$ in the signal region, the next two bins correspond to events in the WZ control region, and finally the last two bins correspond to events in the ZZ control region."
table_covariance.location = "Supplementary material"
for var in [x_covariance,y_covariance,z_covariance]:
    table_covariance.add_variable(var)
submission.add_table(table_covariance)
### End covariance

"""

outdir = "smp17010_output"
submission.create_files(outdir)
