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

submission.read_abstract("HEPData/inputs/smp19012/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-19-012/")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:XXXX.XXXXX")
submission.add_record_id(1753680, "inspire")

### Begin Table 2
table2 = Table("Table 2")
table2.description = "Relative systematic uncertainties in the EW WW and WZ fiducial cross section measurements in units of percent."
table2.location = "Data from Table 2"

table2.keywords["observables"] = ["Uncertainty"]

data2 = np.loadtxt("HEPData/inputs/smp19012/systematics.txt", dtype='string', skiprows=2)

print(data2)

table2_data = Variable("Source of uncertainty", is_independent=True, is_binned=False, units="")
table2_data.values = [str(x) for x in data2[:,0]]

table2_yields0 = Variable("Uncertainty", is_independent=False, is_binned=False, units="")
table2_yields0.values = [float(x) for x in data2[:,1]]
table2_yields0.add_qualifier("Source of uncertainty", "WW EW")
table2_yields0.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields1 = Variable("Uncertainty", is_independent=False, is_binned=False, units="")
table2_yields1.values = [float(x) for x in data2[:,2]]
table2_yields1.add_qualifier("Source of uncertainty", "WZ EWK")
table2_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table2.add_variable(table2_data)
table2.add_variable(table2_yields0)
table2.add_variable(table2_yields1)

submission.add_table(table2)

for table2 in submission.tables:
    table2.keywords["cmenergies"] = [13000]

### End Table 2

### Begin Table 4a
table4a = Table("Table 4a")
table4a.description = "Expected and observed yields from various various SM processes in WW signal region. The combination of the statistical and systematic uncertainties are shown. The predicted yields are shown with their best-fit normalizations from the simultaneous fit."
table4a.location = "Data from Table 4a"

table4a.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/total_yields_ww.txt", dtype='string', skiprows=2)

print(data4)

table4a_data = Variable("Process", is_independent=True, is_binned=False, units="")
table4a_data.values = [str(x) for x in data4[:,0]]

table4a_yields0 = Variable("Events", is_independent=False, is_binned=False, units="")
table4a_yields0.values = [float(x) for x in data4[:,1]]
table4a_yields0.add_qualifier("Expected events", "WW selection")
table4a_yields0.add_qualifier("SQRT(S)", 13, "TeV")

table4a_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table4a_unc0.values = [float(x) for x in data4[:,2]]

table4a_yields0.add_uncertainty(table4a_unc0)

table4a.add_variable(table4a_data)
table4a.add_variable(table4a_yields0)

submission.add_table(table4a)

for table4a in submission.tables:
    table4a.keywords["cmenergies"] = [13000]

### End Table 4a

### Begin Table 4b
table4b = Table("Table 4b")
table4b.description = "Expected and observed yields from various various SM processes in WZ signal region. The combination of the statistical and systematic uncertainties are shown. The predicted yields are shown with their best-fit normalizations from the simultaneous fit."
table4b.location = "Data from Table 4b"

table4b.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/total_yields_ww.txt", dtype='string', skiprows=2)

print(data4)

table4b_data = Variable("Process", is_independent=True, is_binned=False, units="")
table4b_data.values = [str(x) for x in data4[:,0]]

table4b_yields0 = Variable("Events", is_independent=False, is_binned=False, units="")
table4b_yields0.values = [float(x) for x in data4[:,1]]
table4b_yields0.add_qualifier("Expected events", "WZ selection")
table4b_yields0.add_qualifier("SQRT(S)", 13, "TeV")

table4b_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table4b_unc0.values = [float(x) for x in data4[:,2]]

table4b_yields0.add_uncertainty(table4b_unc0)

table4b.add_variable(table4b_data)
table4b.add_variable(table4b_yields0)

submission.add_table(table4b)

for table4b in submission.tables:
    table4b.keywords["cmenergies"] = [13000]

### End Table 4b

### Begin Table 5
table5 = Table("Table 5")
table5.description = "The measured inclusive fiducial cross section measurements."
table5.location = "Data from Table 5"

table5.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/cross_sections.txt", dtype='string', skiprows=2)

print(data4)

table5_data = Variable("Process", is_independent=True, is_binned=False, units="")
table5_data.values = [str(x) for x in data4[:,0]]

table5_yields0 = Variable("Events", is_independent=False, is_binned=False, units="")
table5_yields0.values = [float(x) for x in data4[:,1]]
table5_yields0.add_qualifier("Expected events", "Cross section (fb)")
table5_yields0.add_qualifier("SQRT(S)", 13, "TeV")

table5_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc0.values = [float(x) for x in data4[:,2]]

table5_yields0.add_uncertainty(table5_unc0)

table5.add_variable(table5_data)
table5.add_variable(table5_yields0)

submission.add_table(table5)

for table5 in submission.tables:
    table5.keywords["cmenergies"] = [13000]

### End Table 5

### Begin Fig2a
reader_Fig2a = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_mjj_2019.root")

tableFig2a = Table("Figure 2a")
tableFig2a.description = "Distributions of $m_{jj}$ in the WW signal region"
tableFig2a.location = "Data from Figure 2a"
tableFig2a.keywords["observables"] = ["N"]

histo0_Fig2a    = reader_Fig2a.read_hist_1d("histo0")  # data
histo5_Fig2a    = reader_Fig2a.read_hist_1d("histo5")  # WpWp
histo7_Fig2a    = reader_Fig2a.read_hist_1d("histo7")  # EWk WZ
histo8_Fig2a    = reader_Fig2a.read_hist_1d("histo8")  # QCD WZ
histo9_Fig2a    = reader_Fig2a.read_hist_1d("histo9")  # ZZ
histo10_Fig2a   = reader_Fig2a.read_hist_1d("histo10") # Nonprompt
histo12_Fig2a   = reader_Fig2a.read_hist_1d("histo12") # TVX
histo13_Fig2a   = reader_Fig2a.read_hist_1d("histo13") # VG
histo16_Fig2a   = reader_Fig2a.read_hist_1d("histo16") # WS
histo18_Fig2a   = reader_Fig2a.read_hist_1d("histo18") # Other
histo_Bck_Fig2a = reader_Fig2a.read_hist_1d("hBck")

histo_Bck_Fig2a.keys()

mmed_Fig2a = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2a.values = histo0_Fig2a["x"]

# y-axis: N events

totalbackground_Fig2a = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig2a.values = histo_Bck_Fig2a["y"]

unc_totalbackground_Fig2a = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig2a.values = histo_Bck_Fig2a["dy"]

totalbackground_Fig2a.add_uncertainty(unc_totalbackground_Fig2a)

WW_Fig2a = Variable("Number of W^{+/-}W^{+/-} events", is_independent=False, is_binned=False, units="")
WW_Fig2a.values = histo5_Fig2a["y"]

EWKWZ_Fig2a = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig2a.values = histo7_Fig2a["y"]

QCDWZ_Fig2a = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig2a.values = histo8_Fig2a["y"]

ZZ_Fig2a = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig2a.values = histo9_Fig2a["y"]

Fake_Fig2a = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig2a.values = histo10_Fig2a["y"]

TVX_Fig2a = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig2a.values = histo12_Fig2a["y"]

VG_Fig2a = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig2a.values = histo13_Fig2a["y"]

WS_Fig2a = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig2a.values = histo16_Fig2a["y"]

Other_Fig2a = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig2a.values = histo18_Fig2a["y"]

Data_Fig2a = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig2a.values = histo0_Fig2a["y"]

unc_data_Fig2a = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_Fig2a.values = histo0_Fig2a["dy"]
Data_Fig2a.add_uncertainty(unc_data_Fig2a)

tableFig2a.add_variable(mmed_Fig2a)
tableFig2a.add_variable(totalbackground_Fig2a)
tableFig2a.add_variable(WW_Fig2a)
tableFig2a.add_variable(EWKWZ_Fig2a)
tableFig2a.add_variable(QCDWZ_Fig2a)
tableFig2a.add_variable(ZZ_Fig2a)
tableFig2a.add_variable(Fake_Fig2a)
tableFig2a.add_variable(TVX_Fig2a)
tableFig2a.add_variable(VG_Fig2a)
tableFig2a.add_variable(WS_Fig2a)
tableFig2a.add_variable(Other_Fig2a)
tableFig2a.add_variable(Data_Fig2a)
submission.add_table(tableFig2a)
### End Fig2a

### Begin Fig2b
reader_Fig2b = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_mll_2019.root")

tableFig2b = Table("Figure 2b")
tableFig2b.description = "Distributions of $m_{ll}$ in the WW signal region"
tableFig2b.location = "Data from Figure 2b"
tableFig2b.keywords["observables"] = ["N"]

histo0_Fig2b    = reader_Fig2b.read_hist_1d("histo0")  # data
histo5_Fig2b    = reader_Fig2b.read_hist_1d("histo5")  # WpWp
histo7_Fig2b    = reader_Fig2b.read_hist_1d("histo7")  # EWk WZ
histo8_Fig2b    = reader_Fig2b.read_hist_1d("histo8")  # QCD WZ
histo9_Fig2b    = reader_Fig2b.read_hist_1d("histo9")  # ZZ
histo10_Fig2b   = reader_Fig2b.read_hist_1d("histo10") # Nonprompt
histo12_Fig2b   = reader_Fig2b.read_hist_1d("histo12") # TVX
histo13_Fig2b   = reader_Fig2b.read_hist_1d("histo13") # VG
histo16_Fig2b   = reader_Fig2b.read_hist_1d("histo16") # WS
histo18_Fig2b   = reader_Fig2b.read_hist_1d("histo18") # Other
histo_Bck_Fig2b = reader_Fig2b.read_hist_1d("hBck")

histo_Bck_Fig2b.keys()

mmed_Fig2b = Variable("$mm_{ll}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2b.values = histo0_Fig2b["x"]

# y-axis: N events

totalbackground_Fig2b = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig2b.values = histo_Bck_Fig2b["y"]

unc_totalbackground_Fig2b = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig2b.values = histo_Bck_Fig2b["dy"]

totalbackground_Fig2b.add_uncertainty(unc_totalbackground_Fig2b)

WW_Fig2b = Variable("Number of W^{+/-}W^{+/-} events", is_independent=False, is_binned=False, units="")
WW_Fig2b.values = histo5_Fig2b["y"]

EWKWZ_Fig2b = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig2b.values = histo7_Fig2b["y"]

QCDWZ_Fig2b = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig2b.values = histo8_Fig2b["y"]

ZZ_Fig2b = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig2b.values = histo9_Fig2b["y"]

Fake_Fig2b = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig2b.values = histo10_Fig2b["y"]

TVX_Fig2b = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig2b.values = histo12_Fig2b["y"]

VG_Fig2b = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig2b.values = histo13_Fig2b["y"]

WS_Fig2b = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig2b.values = histo16_Fig2b["y"]

Other_Fig2b = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig2b.values = histo18_Fig2b["y"]

Data_Fig2b = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig2b.values = histo0_Fig2b["y"]

unc_data_Fig2b = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_Fig2b.values = histo0_Fig2b["dy"]
Data_Fig2b.add_uncertainty(unc_data_Fig2b)

tableFig2b.add_variable(mmed_Fig2b)
tableFig2b.add_variable(totalbackground_Fig2b)
tableFig2b.add_variable(WW_Fig2b)
tableFig2b.add_variable(EWKWZ_Fig2b)
tableFig2b.add_variable(QCDWZ_Fig2b)
tableFig2b.add_variable(ZZ_Fig2b)
tableFig2b.add_variable(Fake_Fig2b)
tableFig2b.add_variable(TVX_Fig2b)
tableFig2b.add_variable(VG_Fig2b)
tableFig2b.add_variable(WS_Fig2b)
tableFig2b.add_variable(Other_Fig2b)
tableFig2b.add_variable(Data_Fig2b)
submission.add_table(tableFig2b)
### End Fig2b

### Begin Fig2c
reader_Fig2c = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_mjj_2019.root")

tableFig2c = Table("Figure 2c")
tableFig2c.description = "Distributions of $m_{jj}$ in the WZ signal region"
tableFig2c.location = "Data from Figure 2c"
tableFig2c.keywords["observables"] = ["N"]

histo0_Fig2c    = reader_Fig2c.read_hist_1d("histo0")  # data
histo7_Fig2c    = reader_Fig2c.read_hist_1d("histo7")  # EWk WZ
histo8_Fig2c    = reader_Fig2c.read_hist_1d("histo8")  # QCD WZ
histo9_Fig2c    = reader_Fig2c.read_hist_1d("histo9")  # ZZ
histo10_Fig2c   = reader_Fig2c.read_hist_1d("histo10") # Nonprompt
histo12_Fig2c   = reader_Fig2c.read_hist_1d("histo12") # TVX
histo13_Fig2c   = reader_Fig2c.read_hist_1d("histo13") # VG
histo16_Fig2c   = reader_Fig2c.read_hist_1d("histo16") # WS
histo18_Fig2c   = reader_Fig2c.read_hist_1d("histo18") # Other
histo_Bck_Fig2c = reader_Fig2c.read_hist_1d("hBck")

histo_Bck_Fig2c.keys()

mmed_Fig2c = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2c.values = histo0_Fig2c["x"]

# y-axis: N events

totalbackground_Fig2c = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig2c.values = histo_Bck_Fig2c["y"]

unc_totalbackground_Fig2c = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig2c.values = histo_Bck_Fig2c["dy"]

totalbackground_Fig2c.add_uncertainty(unc_totalbackground_Fig2c)

EWKWZ_Fig2c = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig2c.values = histo7_Fig2c["y"]

QCDWZ_Fig2c = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig2c.values = histo8_Fig2c["y"]

ZZ_Fig2c = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig2c.values = histo9_Fig2c["y"]

Fake_Fig2c = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig2c.values = histo10_Fig2c["y"]

TVX_Fig2c = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig2c.values = histo12_Fig2c["y"]

VG_Fig2c = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig2c.values = histo13_Fig2c["y"]

WS_Fig2c = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig2c.values = histo16_Fig2c["y"]

Other_Fig2c = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig2c.values = histo18_Fig2c["y"]

Data_Fig2c = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig2c.values = histo0_Fig2c["y"]

unc_data_Fig2c = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_Fig2c.values = histo0_Fig2c["dy"]
Data_Fig2c.add_uncertainty(unc_data_Fig2c)

tableFig2c.add_variable(mmed_Fig2c)
tableFig2c.add_variable(totalbackground_Fig2c)
tableFig2c.add_variable(EWKWZ_Fig2c)
tableFig2c.add_variable(QCDWZ_Fig2c)
tableFig2c.add_variable(ZZ_Fig2c)
tableFig2c.add_variable(Fake_Fig2c)
tableFig2c.add_variable(TVX_Fig2c)
tableFig2c.add_variable(VG_Fig2c)
tableFig2c.add_variable(WS_Fig2c)
tableFig2c.add_variable(Other_Fig2c)
tableFig2c.add_variable(Data_Fig2c)
submission.add_table(tableFig2c)
### End Fig2c

### Begin Fig2d
reader_Fig2d = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_bdt_2019.root")

tableFig2d = Table("Figure 2d")
tableFig2d.description = "Distributions of BDT score in the WZ signal region"
tableFig2d.location = "Data from Figure 2d"
tableFig2d.keywords["observables"] = ["N"]

histo0_Fig2d    = reader_Fig2d.read_hist_1d("histo0")  # data
histo7_Fig2d    = reader_Fig2d.read_hist_1d("histo7")  # EWk WZ
histo8_Fig2d    = reader_Fig2d.read_hist_1d("histo8")  # QCD WZ
histo9_Fig2d    = reader_Fig2d.read_hist_1d("histo9")  # ZZ
histo10_Fig2d   = reader_Fig2d.read_hist_1d("histo10") # Nonprompt
histo12_Fig2d   = reader_Fig2d.read_hist_1d("histo12") # TVX
histo13_Fig2d   = reader_Fig2d.read_hist_1d("histo13") # VG
histo16_Fig2d   = reader_Fig2d.read_hist_1d("histo16") # WS
histo18_Fig2d   = reader_Fig2d.read_hist_1d("histo18") # Other
histo_Bck_Fig2d = reader_Fig2d.read_hist_1d("hBck")

histo_Bck_Fig2d.keys()

mmed_Fig2d = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig2d.values = histo0_Fig2d["x"]

# y-axis: N events

totalbackground_Fig2d = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig2d.values = histo_Bck_Fig2d["y"]

unc_totalbackground_Fig2d = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig2d.values = histo_Bck_Fig2d["dy"]

totalbackground_Fig2d.add_uncertainty(unc_totalbackground_Fig2d)

EWKWZ_Fig2d = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig2d.values = histo7_Fig2d["y"]

QCDWZ_Fig2d = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig2d.values = histo8_Fig2d["y"]

ZZ_Fig2d = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig2d.values = histo9_Fig2d["y"]

Fake_Fig2d = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig2d.values = histo10_Fig2d["y"]

TVX_Fig2d = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig2d.values = histo12_Fig2d["y"]

VG_Fig2d = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig2d.values = histo13_Fig2d["y"]

WS_Fig2d = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig2d.values = histo16_Fig2d["y"]

Other_Fig2d = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig2d.values = histo18_Fig2d["y"]

Data_Fig2d = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig2d.values = histo0_Fig2d["y"]

unc_data_Fig2d = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_Fig2d.values = histo0_Fig2d["dy"]
Data_Fig2d.add_uncertainty(unc_data_Fig2d)

tableFig2d.add_variable(mmed_Fig2d)
tableFig2d.add_variable(totalbackground_Fig2d)
tableFig2d.add_variable(EWKWZ_Fig2d)
tableFig2d.add_variable(QCDWZ_Fig2d)
tableFig2d.add_variable(ZZ_Fig2d)
tableFig2d.add_variable(Fake_Fig2d)
tableFig2d.add_variable(TVX_Fig2d)
tableFig2d.add_variable(VG_Fig2d)
tableFig2d.add_variable(WS_Fig2d)
tableFig2d.add_variable(Other_Fig2d)
tableFig2d.add_variable(Data_Fig2d)
submission.add_table(tableFig2d)
### End Fig2d

### Begin Fig3a
reader_Fig3a = RootFileReader("HEPData/inputs/smp19012/unf_WWMJJ_normalized0.root")

tableFig3a = Table("Figure 3a")
tableFig3a.description = "Absolute WW cross section in $m_{jj}$ bins."
tableFig3a.location = "Data from Figure 3a"
tableFig3a.keywords["observables"] = ["N"]

histo_unfoldFig3a = reader_Fig3a.read_hist_1d("unfold")

histo_unfoldFig3a.keys()

for key in histo_unfoldFig3a.keys():
    print(key, type(histo_unfoldFig3a[key]), type(histo_unfoldFig3a[key][0]))

mmed_Fig3a = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="")
mmed_Fig3a.values = histo_unfoldFig3a["x"]

# y-axis: N events
unfoldFig3a = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3a.values = histo_unfoldFig3a["y"]

unc_unfoldFig3a = Uncertainty("", is_symmetric=True)
unc_unfoldFig3a.values = histo_unfoldFig3a["dy"]

unfoldFig3a.add_uncertainty(unc_unfoldFig3a)

unfoldFig3a.scale_values(1)

tableFig3a.add_variable(mmed_Fig3a)
tableFig3a.add_variable(unfoldFig3a)
submission.add_table(tableFig3a)
### End Fig3a

### Begin Fig3b
reader_Fig3b = RootFileReader("HEPData/inputs/smp19012/unf_WWMJJ_normalized1.root")

tableFig3b = Table("Figure 3b")
tableFig3b.description = "Normalized WW cross section in $m_{jj}$ bins."
tableFig3b.location = "Data from Figure 3b"
tableFig3b.keywords["observables"] = ["N"]

histo_unfoldFig3b = reader_Fig3b.read_hist_1d("unfold")

histo_unfoldFig3b.keys()

for key in histo_unfoldFig3b.keys():
    print(key, type(histo_unfoldFig3b[key]), type(histo_unfoldFig3b[key][0]))

mmed_Fig3b = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="")
mmed_Fig3b.values = histo_unfoldFig3b["x"]

# y-axis: N events
unfoldFig3b = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3b.values = histo_unfoldFig3b["y"]

unc_unfoldFig3b = Uncertainty("", is_symmetric=True)
unc_unfoldFig3b.values = histo_unfoldFig3b["dy"]

unfoldFig3b.add_uncertainty(unc_unfoldFig3b)

unfoldFig3b.scale_values(1)

tableFig3b.add_variable(mmed_Fig3b)
tableFig3b.add_variable(unfoldFig3b)
submission.add_table(tableFig3b)
### End Fig3b

### Begin Fig3c
reader_Fig3c = RootFileReader("HEPData/inputs/smp19012/unf_WWMLL_normalized0.root")

tableFig3c = Table("Figure 3c")
tableFig3c.description = "Absolute WW cross section in $m_{ll}$ bins."
tableFig3c.location = "Data from Figure 3c"
tableFig3c.keywords["observables"] = ["N"]

histo_unfoldFig3c = reader_Fig3c.read_hist_1d("unfold")

histo_unfoldFig3c.keys()

for key in histo_unfoldFig3c.keys():
    print(key, type(histo_unfoldFig3c[key]), type(histo_unfoldFig3c[key][0]))

mmed_Fig3c = Variable("$m_{ll}$", is_independent=True, is_binned=False, units="")
mmed_Fig3c.values = histo_unfoldFig3c["x"]

# y-axis: N events
unfoldFig3c = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3c.values = histo_unfoldFig3c["y"]

unc_unfoldFig3c = Uncertainty("", is_symmetric=True)
unc_unfoldFig3c.values = histo_unfoldFig3c["dy"]

unfoldFig3c.add_uncertainty(unc_unfoldFig3c)

unfoldFig3c.scale_values(1)

tableFig3c.add_variable(mmed_Fig3c)
tableFig3c.add_variable(unfoldFig3c)
submission.add_table(tableFig3c)
### End Fig3c

### Begin Fig3d
reader_Fig3d = RootFileReader("HEPData/inputs/smp19012/unf_WWMLL_normalized1.root")

tableFig3d = Table("Figure 3d")
tableFig3d.description = "Normalized WW cross section in $m_{ll}$ bins."
tableFig3d.location = "Data from Figure 3d"
tableFig3d.keywords["observables"] = ["N"]

histo_unfoldFig3d = reader_Fig3d.read_hist_1d("unfold")

histo_unfoldFig3d.keys()

for key in histo_unfoldFig3d.keys():
    print(key, type(histo_unfoldFig3d[key]), type(histo_unfoldFig3d[key][0]))

mmed_Fig3d = Variable("$m_{ll}$", is_independent=True, is_binned=False, units="")
mmed_Fig3d.values = histo_unfoldFig3d["x"]

# y-axis: N events
unfoldFig3d = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3d.values = histo_unfoldFig3d["y"]

unc_unfoldFig3d = Uncertainty("", is_symmetric=True)
unc_unfoldFig3d.values = histo_unfoldFig3d["dy"]

unfoldFig3d.add_uncertainty(unc_unfoldFig3d)

unfoldFig3d.scale_values(1)

tableFig3d.add_variable(mmed_Fig3d)
tableFig3d.add_variable(unfoldFig3d)
submission.add_table(tableFig3d)
### End Fig3d

### Begin Fig3e
reader_Fig3e = RootFileReader("HEPData/inputs/smp19012/unf_WWPTL1_normalized0.root")

tableFig3e = Table("Figure 3e")
tableFig3e.description = "Absolute WW cross section in $p_{T}^{l max}$ bins."
tableFig3e.location = "Data from Figure 3e"
tableFig3e.keywords["observables"] = ["N"]

histo_unfoldFig3e = reader_Fig3e.read_hist_1d("unfold")

histo_unfoldFig3e.keys()

for key in histo_unfoldFig3e.keys():
    print(key, type(histo_unfoldFig3e[key]), type(histo_unfoldFig3e[key][0]))

mmed_Fig3e = Variable("$p_{T}^{l max}$", is_independent=True, is_binned=False, units="")
mmed_Fig3e.values = histo_unfoldFig3e["x"]

# y-axis: N events
unfoldFig3e = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3e.values = histo_unfoldFig3e["y"]

unc_unfoldFig3e = Uncertainty("", is_symmetric=True)
unc_unfoldFig3e.values = histo_unfoldFig3e["dy"]

unfoldFig3e.add_uncertainty(unc_unfoldFig3e)

unfoldFig3e.scale_values(1)

tableFig3e.add_variable(mmed_Fig3e)
tableFig3e.add_variable(unfoldFig3e)
submission.add_table(tableFig3e)
### End Fig3e

### Begin Fig3f
reader_Fig3f = RootFileReader("HEPData/inputs/smp19012/unf_WWPTL1_normalized1.root")

tableFig3f = Table("Figure 3f")
tableFig3f.description = "Normalized WW cross section in $p_{T}^{l max}$ bins."
tableFig3f.location = "Data from Figure 3f"
tableFig3f.keywords["observables"] = ["N"]

histo_unfoldFig3f = reader_Fig3f.read_hist_1d("unfold")

histo_unfoldFig3f.keys()

for key in histo_unfoldFig3f.keys():
    print(key, type(histo_unfoldFig3f[key]), type(histo_unfoldFig3f[key][0]))

mmed_Fig3f = Variable("$p_{T}^{l max}$", is_independent=True, is_binned=False, units="")
mmed_Fig3f.values = histo_unfoldFig3f["x"]

# y-axis: N events
unfoldFig3f = Variable("WW cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig3f.values = histo_unfoldFig3f["y"]

unc_unfoldFig3f = Uncertainty("", is_symmetric=True)
unc_unfoldFig3f.values = histo_unfoldFig3f["dy"]

unfoldFig3f.add_uncertainty(unc_unfoldFig3f)

unfoldFig3f.scale_values(1)

tableFig3f.add_variable(mmed_Fig3f)
tableFig3f.add_variable(unfoldFig3f)
submission.add_table(tableFig3f)
### End Fig3f

### Begin Fig4a
reader_Fig4a = RootFileReader("HEPData/inputs/smp19012/unf_WZMJJ_normalized0.root")

tableFig4a = Table("Figure 4a")
tableFig4a.description = "Absolute WW cross section in $m_{jj}$ bins."
tableFig4a.location = "Data from Figure 4a"
tableFig4a.keywords["observables"] = ["N"]

histo_unfoldFig4a = reader_Fig4a.read_hist_1d("unfold")

histo_unfoldFig4a.keys()

for key in histo_unfoldFig4a.keys():
    print(key, type(histo_unfoldFig4a[key]), type(histo_unfoldFig4a[key][0]))

mmed_Fig4a = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="")
mmed_Fig4a.values = histo_unfoldFig4a["x"]

# y-axis: N events
unfoldFig4a = Variable("WZ cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig4a.values = histo_unfoldFig4a["y"]

unc_unfoldFig4a = Uncertainty("", is_symmetric=True)
unc_unfoldFig4a.values = histo_unfoldFig4a["dy"]

unfoldFig4a.add_uncertainty(unc_unfoldFig4a)

unfoldFig4a.scale_values(1)

tableFig4a.add_variable(mmed_Fig4a)
tableFig4a.add_variable(unfoldFig4a)
submission.add_table(tableFig4a)
### End Fig4a

### Begin Fig4b
reader_Fig4b = RootFileReader("HEPData/inputs/smp19012/unf_WZMJJ_normalized1.root")

tableFig4b = Table("Figure 4b")
tableFig4b.description = "Normalized WW cross section in $m_{jj}$ bins."
tableFig4b.location = "Data from Figure 4b"
tableFig4b.keywords["observables"] = ["N"]

histo_unfoldFig4b = reader_Fig4b.read_hist_1d("unfold")

histo_unfoldFig4b.keys()

for key in histo_unfoldFig4b.keys():
    print(key, type(histo_unfoldFig4b[key]), type(histo_unfoldFig4b[key][0]))

mmed_Fig4b = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="")
mmed_Fig4b.values = histo_unfoldFig4b["x"]

# y-axis: N events
unfoldFig4b = Variable("WZ cross section (fb)", is_independent=False, is_binned=False, units="")
unfoldFig4b.values = histo_unfoldFig4b["y"]

unc_unfoldFig4b = Uncertainty("", is_symmetric=True)
unc_unfoldFig4b.values = histo_unfoldFig4b["dy"]

unfoldFig4b.add_uncertainty(unc_unfoldFig4b)

unfoldFig4b.scale_values(1)

tableFig4b.add_variable(mmed_Fig4b)
tableFig4b.add_variable(unfoldFig4b)
submission.add_table(tableFig4b)
### End Fig4b

### Begin Fig5a
reader_Fig5a = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_aqgc_fullmtww_2019.root")

tableFig5a = Table("Figure 5a")
tableFig5a.description = "Distributions of $m_{T}^{WW}$ in the WW signal region"
tableFig5a.location = "Data from Figure 5a"
tableFig5a.keywords["observables"] = ["N"]

histo0_Fig5a    = reader_Fig5a.read_hist_1d("histo0")  # data
histo5_Fig5a    = reader_Fig5a.read_hist_1d("histo5")  # WpWp
histo7_Fig5a    = reader_Fig5a.read_hist_1d("histo7")  # EWk WZ
histo8_Fig5a    = reader_Fig5a.read_hist_1d("histo8")  # QCD WZ
histo9_Fig5a    = reader_Fig5a.read_hist_1d("histo9")  # ZZ
histo10_Fig5a   = reader_Fig5a.read_hist_1d("histo10") # Nonprompt
histo12_Fig5a   = reader_Fig5a.read_hist_1d("histo12") # TVX
histo13_Fig5a   = reader_Fig5a.read_hist_1d("histo13") # VG
histo16_Fig5a   = reader_Fig5a.read_hist_1d("histo16") # WS
histo18_Fig5a   = reader_Fig5a.read_hist_1d("histo18") # Other
histo_Bck_Fig5a = reader_Fig5a.read_hist_1d("hBck")

histo_Bck_Fig5a.keys()

mmed_Fig5a = Variable("$m_{ll}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig5a.values = histo0_Fig5a["x"]

# y-axis: N events

totalbackground_Fig5a = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig5a.values = histo_Bck_Fig5a["y"]

unc_totalbackground_Fig5a = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig5a.values = histo_Bck_Fig5a["dy"]

totalbackground_Fig5a.add_uncertainty(unc_totalbackground_Fig5a)

WW_Fig5a = Variable("Number of W^{+/-}W^{+/-} events", is_independent=False, is_binned=False, units="")
WW_Fig5a.values = histo5_Fig5a["y"]

EWKWZ_Fig5a = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig5a.values = histo7_Fig5a["y"]

QCDWZ_Fig5a = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig5a.values = histo8_Fig5a["y"]

ZZ_Fig5a = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig5a.values = histo9_Fig5a["y"]

Fake_Fig5a = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig5a.values = histo10_Fig5a["y"]

TVX_Fig5a = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig5a.values = histo12_Fig5a["y"]

VG_Fig5a = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig5a.values = histo13_Fig5a["y"]

WS_Fig5a = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig5a.values = histo16_Fig5a["y"]

Other_Fig5a = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig5a.values = histo18_Fig5a["y"]

Data_Fig5a = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig5a.values = histo0_Fig5a["y"]

#unc_data_Fig5a = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig5a.values = histo0_Fig5a["dy"]
#Data_Fig5a.add_uncertainty(unc_data_Fig5a)

tableFig5a.add_variable(mmed_Fig5a)
tableFig5a.add_variable(totalbackground_Fig5a)
tableFig5a.add_variable(WW_Fig5a)
tableFig5a.add_variable(EWKWZ_Fig5a)
tableFig5a.add_variable(QCDWZ_Fig5a)
tableFig5a.add_variable(ZZ_Fig5a)
tableFig5a.add_variable(Fake_Fig5a)
tableFig5a.add_variable(TVX_Fig5a)
tableFig5a.add_variable(VG_Fig5a)
tableFig5a.add_variable(WS_Fig5a)
tableFig5a.add_variable(Other_Fig5a)
tableFig5a.add_variable(Data_Fig5a)
submission.add_table(tableFig5a)
### End Fig5a

### Begin Fig5b
reader_Fig5b = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_aqgc_fullmtwz_2019.root")

tableFig5b = Table("Figure 5b")
tableFig5b.description = "Distributions of $m_{T}^{WZ}$ in the WZ signal region"
tableFig5b.location = "Data from Figure 5b"
tableFig5b.keywords["observables"] = ["N"]

histo0_Fig5b    = reader_Fig5b.read_hist_1d("histo0")  # data
histo7_Fig5b    = reader_Fig5b.read_hist_1d("histo7")  # EWk WZ
histo8_Fig5b    = reader_Fig5b.read_hist_1d("histo8")  # QCD WZ
histo9_Fig5b    = reader_Fig5b.read_hist_1d("histo9")  # ZZ
histo10_Fig5b   = reader_Fig5b.read_hist_1d("histo10") # Nonprompt
histo12_Fig5b   = reader_Fig5b.read_hist_1d("histo12") # TVX
histo13_Fig5b   = reader_Fig5b.read_hist_1d("histo13") # VG
histo16_Fig5b   = reader_Fig5b.read_hist_1d("histo16") # WS
histo18_Fig5b   = reader_Fig5b.read_hist_1d("histo18") # Other
histo_Bck_Fig5b = reader_Fig5b.read_hist_1d("hBck")

histo_Bck_Fig5b.keys()

mmed_Fig5b = Variable("$m_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig5b.values = histo0_Fig5b["x"]

# y-axis: N events

totalbackground_Fig5b = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig5b.values = histo_Bck_Fig5b["y"]

unc_totalbackground_Fig5b = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig5b.values = histo_Bck_Fig5b["dy"]

totalbackground_Fig5b.add_uncertainty(unc_totalbackground_Fig5b)

EWKWZ_Fig5b = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig5b.values = histo7_Fig5b["y"]

QCDWZ_Fig5b = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig5b.values = histo8_Fig5b["y"]

ZZ_Fig5b = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig5b.values = histo9_Fig5b["y"]

Fake_Fig5b = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig5b.values = histo10_Fig5b["y"]

TVX_Fig5b = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig5b.values = histo12_Fig5b["y"]

VG_Fig5b = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig5b.values = histo13_Fig5b["y"]

WS_Fig5b = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig5b.values = histo16_Fig5b["y"]

Other_Fig5b = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig5b.values = histo18_Fig5b["y"]

Data_Fig5b = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig5b.values = histo0_Fig5b["y"]

#unc_data_Fig5b = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig5b.values = histo0_Fig5b["dy"]
#Data_Fig5b.add_uncertainty(unc_data_Fig5b)

tableFig5b.add_variable(mmed_Fig5b)
tableFig5b.add_variable(totalbackground_Fig5b)
tableFig5b.add_variable(EWKWZ_Fig5b)
tableFig5b.add_variable(QCDWZ_Fig5b)
tableFig5b.add_variable(ZZ_Fig5b)
tableFig5b.add_variable(Fake_Fig5b)
tableFig5b.add_variable(TVX_Fig5b)
tableFig5b.add_variable(VG_Fig5b)
tableFig5b.add_variable(WS_Fig5b)
tableFig5b.add_variable(Other_Fig5b)
tableFig5b.add_variable(Data_Fig5b)
submission.add_table(tableFig5b)
### End Fig5b

### Begin Table 6
table6 = Table("Table 6")
table6.description = "Observed and expected lower and upper 95\% confidence level limits in TeV$^{-4}$ on the parameters of the quartic, obtained without using any unitarization procedure."
table6.location = "Data from Table 6"

table6.keywords["observables"] = ["Limits"]

data6 = np.loadtxt("HEPData/inputs/smp19012/aqgc_limits.txt", dtype='string', skiprows=2)

print(data6)

table6_data = Variable("Operator", is_independent=True, is_binned=False, units="")
table6_data.values = [str(x) for x in data6[:,0]]

table6_yields1 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields1.values = [str(x) for x in data6[:,1]]
table6_yields1.add_qualifier("Lmits", "Expected WW")
table6_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields2 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields2.values = [str(x) for x in data6[:,2]]
table6_yields2.add_qualifier("Lmits", "Observed WW")
table6_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields3 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields3.values = [str(x) for x in data6[:,3]]
table6_yields3.add_qualifier("Lmits", "Expected WZ")
table6_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields4 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields4.values = [str(x) for x in data6[:,4]]
table6_yields4.add_qualifier("Lmits", "Observed WZ")
table6_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields5 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields5.values = [str(x) for x in data6[:,5]]
table6_yields5.add_qualifier("Lmits", "Expected WW+WZ")
table6_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields6 = Variable("Limits", is_independent=False, is_binned=False, units="")
table6_yields6.values = [str(x) for x in data6[:,6]]
table6_yields6.add_qualifier("Lmits", "Observed WW+WZ")
table6_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table6.add_variable(table6_data)
table6.add_variable(table6_yields1)
table6.add_variable(table6_yields2)
table6.add_variable(table6_yields3)
table6.add_variable(table6_yields4)
table6.add_variable(table6_yields5)
table6.add_variable(table6_yields6)

submission.add_table(table6)

for table6 in submission.tables:
    table6.keywords["cmenergies"] = [13000]
### End Table 6

### Begin Table 7
table7 = Table("Table 7")
table7.description = "Observed and expected lower and upper 95\% confidence level limits in TeV$^{-4}$ on the parameters of the quartic by cutting the EFT expansion at the unitarity limit."
table7.location = "Data from Table 7"

table7.keywords["observables"] = ["Limits"]

data7 = np.loadtxt("HEPData/inputs/smp19012/aqgc_limits_unitarity.txt", dtype='string', skiprows=2)

print(data7)

table7_data = Variable("Operator", is_independent=True, is_binned=False, units="")
table7_data.values = [str(x) for x in data7[:,0]]

table7_yields1 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields1.values = [str(x) for x in data7[:,1]]
table7_yields1.add_qualifier("Lmits", "Expected WW")
table7_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields2 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields2.values = [str(x) for x in data7[:,2]]
table7_yields2.add_qualifier("Lmits", "Observed WW")
table7_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields3 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields3.values = [str(x) for x in data7[:,3]]
table7_yields3.add_qualifier("Lmits", "Expected WZ")
table7_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields4 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields4.values = [str(x) for x in data7[:,4]]
table7_yields4.add_qualifier("Lmits", "Observed WZ")
table7_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields5 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields5.values = [str(x) for x in data7[:,5]]
table7_yields5.add_qualifier("Lmits", "Expected WW+WZ")
table7_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields6 = Variable("Limits", is_independent=False, is_binned=False, units="")
table7_yields6.values = [str(x) for x in data7[:,6]]
table7_yields6.add_qualifier("Lmits", "Observed WW+WZ")
table7_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table7.add_variable(table7_data)
table7.add_variable(table7_yields1)
table7.add_variable(table7_yields2)
table7.add_variable(table7_yields3)
table7.add_variable(table7_yields4)
table7.add_variable(table7_yields5)
table7.add_variable(table7_yields6)

submission.add_table(table7)

for table7 in submission.tables:
    table7.keywords["cmenergies"] = [13000]

### End Table 7

outdir = "smp19012_output"
submission.create_files(outdir)
