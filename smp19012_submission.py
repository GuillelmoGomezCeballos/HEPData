
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
submission.add_link("arXiv", "https://arxiv.org/abs/2005.01173")
submission.add_record_id(200501173, "inspire")

### Begin Table 2
table2 = Table("Table 2")
table2.description = "Relative systematic uncertainties in the EW $W^\pm W^\pm$ and WZ cross section measurements in units of percent."
table2.location = "Data from Table 2"

table2.keywords["observables"] = ["Uncertainty"]

data2 = np.loadtxt("HEPData/inputs/smp19012/systematics.txt", dtype='string', skiprows=2)

print(data2)

table2_data = Variable("Source of uncertainty", is_independent=True, is_binned=False, units="")
table2_data.values = [str(x) for x in data2[:,0]]

table2_yields0 = Variable("Uncertainty", is_independent=False, is_binned=False, units="")
table2_yields0.values = [float(x) for x in data2[:,1]]
table2_yields0.add_qualifier("Source of uncertainty", "WW")
table2_yields0.add_qualifier("SQRT(S)", 13, "TeV")

table2_yields1 = Variable("Uncertainty", is_independent=False, is_binned=False, units="")
table2_yields1.values = [float(x) for x in data2[:,2]]
table2_yields1.add_qualifier("Source of uncertainty", "WZ")
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
table4a.description = "Expected and observed yields from the standard model processeses in the WW signal region. The combination of the statistical and systematic uncertainties are shown. The predicted yields are shown with their best-fit normalizations from the simultaneous fit."
table4a.location = "Data from Table 4a"

table4a.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/total_yields_ww.txt", dtype='string', skiprows=2)

print(data4)

table4a_data = Variable("Process", is_independent=True, is_binned=False, units="")
table4a_data.values = [str(x) for x in data4[:,0]]

table4a_yields0 = Variable("Prefit yields", is_independent=False, is_binned=False, units="")
table4a_yields0.values = [float(x) for x in data4[:,1]]
table4a_yields0.add_qualifier("SQRT(S)", 13, "TeV")
table4a_yields0.add_qualifier("WW selection", "Yields")
table4a_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table4a_unc0.values = [float(x) for x in data4[:,2]]
table4a_yields0.add_uncertainty(table4a_unc0)

table4a_yields1 = Variable("Postfit yields", is_independent=False, is_binned=False, units="")
table4a_yields1.values = [float(x) for x in data4[:,3]]
table4a_unc1 = Uncertainty("total uncertainty", is_symmetric=True)
table4a_unc1.values = [float(x) for x in data4[:,4]]
table4a_yields1.add_uncertainty(table4a_unc1)

table4a.add_variable(table4a_data)
table4a.add_variable(table4a_yields0)
table4a.add_variable(table4a_yields1)

submission.add_table(table4a)

for table4a in submission.tables:
    table4a.keywords["cmenergies"] = [13000]

### End Table 4a

### Begin Table 4b
table4b = Table("Table 4b")
table4b.description = "Expected and observed yields from the standard model processeses in the WZ signal region. The combination of the statistical and systematic uncertainties are shown. The predicted yields are shown with their best-fit normalizations from the simultaneous fit."
table4b.location = "Data from Table 4b"

table4b.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/total_yields_wz.txt", dtype='string', skiprows=2)

print(data4)

table4b_data = Variable("Process", is_independent=True, is_binned=False, units="")
table4b_data.values = [str(x) for x in data4[:,0]]

table4b_yields0 = Variable("Prefit yields", is_independent=False, is_binned=False, units="")
table4b_yields0.values = [float(x) for x in data4[:,1]]
table4b_yields0.add_qualifier("SQRT(S)", 13, "TeV")
table4b_yields0.add_qualifier("WZ selection", "Yields")
table4b_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table4b_unc0.values = [float(x) for x in data4[:,2]]
table4b_yields0.add_uncertainty(table4b_unc0)

table4b_yields1 = Variable("Postfit yields", is_independent=False, is_binned=False, units="")
table4b_yields1.values = [float(x) for x in data4[:,3]]
table4b_unc1 = Uncertainty("total uncertainty", is_symmetric=True)
table4b_unc1.values = [float(x) for x in data4[:,4]]
table4b_yields1.add_uncertainty(table4b_unc1)

table4b.add_variable(table4b_data)
table4b.add_variable(table4b_yields0)
table4b.add_variable(table4b_yields1)

submission.add_table(table4b)

for table4b in submission.tables:
    table4b.keywords["cmenergies"] = [13000]

### End Table 4b

### Begin Table 5
table5 = Table("Table 5")
table5.description = "The measured inclusive fiducial cross section measurements. The WW fiducial region is defined by requiring two same-sign leptons with $p_{T}>20$, $|\eta|<2.5$, and $m_{ll}>20$, and two jets with $m_{jj}>500$ and $|\Delta \eta_{jj}|>2.5$. The jets at generator level are clustered from stable particles, excluding neutrinos, using the anti-kt clustering algorithm with R = 0.4, and are required to have $p_{T}>50$ and $|\eta|<4.7$. The jets within $\Delta R<0.4$ of the selected charged leptons are not included. The WZ fiducial region is defined by requiring three leptons with $p_{T}>20$, $|\eta|<2.5$, a pair of opposite charge same-flavor lepton pair with $|m_{ll}-m_{Z}|<15$, and two jets with $m_{jj}>500$ and $|\Delta \eta_{jj}|>2.5$."
table5.location = "Data from Table 5"

table5.keywords["observables"] = ["Events"]

data4 = np.loadtxt("HEPData/inputs/smp19012/cross_sections.txt", dtype='string', skiprows=2)

print(data4)

table5_data = Variable("Process", is_independent=True, is_binned=False, units="")
table5_data.values = [str(x) for x in data4[:,0]]

table5_yields0 = Variable("Observed result", is_independent=False, is_binned=False, units="")
table5_yields0.values = [float(x) for x in data4[:,1]]
table5_yields0.add_qualifier("Fiducial cross section", "Cross section (fb)")
table5_yields0.add_qualifier("SQRT(S)", 13, "TeV")
table5_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc0.values = [float(x) for x in data4[:,2]]
table5_yields0.add_uncertainty(table5_unc0)

table5_yields1 = Variable("Theoretical prediction without NLO corrections", is_independent=False, is_binned=False, units="")
table5_yields1.values = [float(x) for x in data4[:,3]]
table5_unc1 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc1.values = [float(x) for x in data4[:,4]]
table5_yields1.add_uncertainty(table5_unc1)

table5_yields2 = Variable("Theoretical prediction with NLO corrections", is_independent=False, is_binned=False, units="")
table5_yields2.values = [float(x) for x in data4[:,5]]
table5_unc2 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc2.values = [float(x) for x in data4[:,6]]
table5_yields2.add_uncertainty(table5_unc2)

table5.add_variable(table5_data)
table5.add_variable(table5_yields0)
table5.add_variable(table5_yields1)
table5.add_variable(table5_yields2)

submission.add_table(table5)

for table5 in submission.tables:
    table5.keywords["cmenergies"] = [13000]

### End Table 5

### Begin Fig3a
reader_Fig3a = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_mjj_2019.root")

tableFig3a = Table("Figure 3a")
tableFig3a.description = "Distributions of $m_{jj}$ in the WW signal region."
tableFig3a.location = "Data from Figure 3a"
tableFig3a.keywords["observables"] = ["N"]

histo0_Fig3a    = reader_Fig3a.read_hist_1d("histo0")  # data
histo5_Fig3a    = reader_Fig3a.read_hist_1d("histo5")  # WpWp
histo7_Fig3a    = reader_Fig3a.read_hist_1d("histo7")  # EWk WZ
histo8_Fig3a    = reader_Fig3a.read_hist_1d("histo8")  # QCD WZ
histo9_Fig3a    = reader_Fig3a.read_hist_1d("histo9")  # ZZ
histo10_Fig3a   = reader_Fig3a.read_hist_1d("histo10") # Nonprompt
histo12_Fig3a   = reader_Fig3a.read_hist_1d("histo12") # TVX
histo13_Fig3a   = reader_Fig3a.read_hist_1d("histo13") # VG
histo16_Fig3a   = reader_Fig3a.read_hist_1d("histo16") # WS
histo18_Fig3a   = reader_Fig3a.read_hist_1d("histo18") # Other
histo_Bck_Fig3a = reader_Fig3a.read_hist_1d("hBck")

histo_Bck_Fig3a.keys()

mmed_Fig3a = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3a.values = histo0_Fig3a["x"]

# y-axis: N events

totalbackground_Fig3a = Variable("Number of background events/GeV", is_independent=False, is_binned=False, units="")
totalbackground_Fig3a.values = histo_Bck_Fig3a["y"]

unc_totalbackground_Fig3a = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig3a.values = histo_Bck_Fig3a["dy"]

totalbackground_Fig3a.add_uncertainty(unc_totalbackground_Fig3a)

WW_Fig3a = Variable("Number of W^{+/-}W^{+/-} events/GeV", is_independent=False, is_binned=False, units="")
WW_Fig3a.values = histo5_Fig3a["y"]

EWKWZ_Fig3a = Variable("Number of EW WZ events/GeV", is_independent=False, is_binned=False, units="")
EWKWZ_Fig3a.values = histo7_Fig3a["y"]

QCDWZ_Fig3a = Variable("Number of QCD WZ events/GeV", is_independent=False, is_binned=False, units="")
QCDWZ_Fig3a.values = histo8_Fig3a["y"]

ZZ_Fig3a = Variable("Number of ZZ events/GeV", is_independent=False, is_binned=False, units="")
ZZ_Fig3a.values = histo9_Fig3a["y"]

Fake_Fig3a = Variable("Number of nonprompt events/GeV", is_independent=False, is_binned=False, units="")
Fake_Fig3a.values = histo10_Fig3a["y"]

TVX_Fig3a = Variable("Number of tVx events/GeV", is_independent=False, is_binned=False, units="")
TVX_Fig3a.values = histo12_Fig3a["y"]

VG_Fig3a = Variable("Number of V#gamma events/GeV", is_independent=False, is_binned=False, units="")
VG_Fig3a.values = histo13_Fig3a["y"]

WS_Fig3a = Variable("Number of wrong-sign events/GeV", is_independent=False, is_binned=False, units="")
WS_Fig3a.values = histo16_Fig3a["y"]

Other_Fig3a = Variable("Number of Other events/GeV", is_independent=False, is_binned=False, units="")
Other_Fig3a.values = histo18_Fig3a["y"]

Data_Fig3a = Variable("Number of data events/GeV", is_independent=False, is_binned=False, units="")
Data_Fig3a.values = histo0_Fig3a["y"]

#unc_data_Fig3a = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig3a.values = histo0_Fig3a["dy"]
#Data_Fig3a.add_uncertainty(unc_data_Fig3a)

tableFig3a.add_variable(mmed_Fig3a)
tableFig3a.add_variable(totalbackground_Fig3a)
tableFig3a.add_variable(WW_Fig3a)
tableFig3a.add_variable(EWKWZ_Fig3a)
tableFig3a.add_variable(QCDWZ_Fig3a)
tableFig3a.add_variable(ZZ_Fig3a)
tableFig3a.add_variable(Fake_Fig3a)
tableFig3a.add_variable(TVX_Fig3a)
tableFig3a.add_variable(VG_Fig3a)
tableFig3a.add_variable(WS_Fig3a)
tableFig3a.add_variable(Other_Fig3a)
tableFig3a.add_variable(Data_Fig3a)
submission.add_table(tableFig3a)
### End Fig3a

### Begin Fig3b
reader_Fig3b = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_mll_2019.root")

tableFig3b = Table("Figure 3b")
tableFig3b.description = "Distributions of $m_{ll}$ in the WW signal region."
tableFig3b.location = "Data from Figure 3b"
tableFig3b.keywords["observables"] = ["N"]

histo0_Fig3b    = reader_Fig3b.read_hist_1d("histo0")  # data
histo5_Fig3b    = reader_Fig3b.read_hist_1d("histo5")  # WpWp
histo7_Fig3b    = reader_Fig3b.read_hist_1d("histo7")  # EWk WZ
histo8_Fig3b    = reader_Fig3b.read_hist_1d("histo8")  # QCD WZ
histo9_Fig3b    = reader_Fig3b.read_hist_1d("histo9")  # ZZ
histo10_Fig3b   = reader_Fig3b.read_hist_1d("histo10") # Nonprompt
histo12_Fig3b   = reader_Fig3b.read_hist_1d("histo12") # TVX
histo13_Fig3b   = reader_Fig3b.read_hist_1d("histo13") # VG
histo16_Fig3b   = reader_Fig3b.read_hist_1d("histo16") # WS
histo18_Fig3b   = reader_Fig3b.read_hist_1d("histo18") # Other
histo_Bck_Fig3b = reader_Fig3b.read_hist_1d("hBck")

histo_Bck_Fig3b.keys()

mmed_Fig3b = Variable("$mm_{ll}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3b.values = histo0_Fig3b["x"]

# y-axis: N events

totalbackground_Fig3b = Variable("Number of background events/GeV", is_independent=False, is_binned=False, units="")
totalbackground_Fig3b.values = histo_Bck_Fig3b["y"]

unc_totalbackground_Fig3b = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig3b.values = histo_Bck_Fig3b["dy"]

totalbackground_Fig3b.add_uncertainty(unc_totalbackground_Fig3b)

WW_Fig3b = Variable("Number of W^{+/-}W^{+/-} events/GeV", is_independent=False, is_binned=False, units="")
WW_Fig3b.values = histo5_Fig3b["y"]

EWKWZ_Fig3b = Variable("Number of EW WZ events/GeV", is_independent=False, is_binned=False, units="")
EWKWZ_Fig3b.values = histo7_Fig3b["y"]

QCDWZ_Fig3b = Variable("Number of QCD WZ events/GeV", is_independent=False, is_binned=False, units="")
QCDWZ_Fig3b.values = histo8_Fig3b["y"]

ZZ_Fig3b = Variable("Number of ZZ events/GeV", is_independent=False, is_binned=False, units="")
ZZ_Fig3b.values = histo9_Fig3b["y"]

Fake_Fig3b = Variable("Number of nonprompt events/GeV", is_independent=False, is_binned=False, units="")
Fake_Fig3b.values = histo10_Fig3b["y"]

TVX_Fig3b = Variable("Number of tVx events/GeV", is_independent=False, is_binned=False, units="")
TVX_Fig3b.values = histo12_Fig3b["y"]

VG_Fig3b = Variable("Number of V#gamma events/GeV", is_independent=False, is_binned=False, units="")
VG_Fig3b.values = histo13_Fig3b["y"]

WS_Fig3b = Variable("Number of wrong-sign events/GeV", is_independent=False, is_binned=False, units="")
WS_Fig3b.values = histo16_Fig3b["y"]

Other_Fig3b = Variable("Number of Other events/GeV", is_independent=False, is_binned=False, units="")
Other_Fig3b.values = histo18_Fig3b["y"]

Data_Fig3b = Variable("Number of data events/GeV", is_independent=False, is_binned=False, units="")
Data_Fig3b.values = histo0_Fig3b["y"]

#unc_data_Fig3b = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig3b.values = histo0_Fig3b["dy"]
#Data_Fig3b.add_uncertainty(unc_data_Fig3b)

tableFig3b.add_variable(mmed_Fig3b)
tableFig3b.add_variable(totalbackground_Fig3b)
tableFig3b.add_variable(WW_Fig3b)
tableFig3b.add_variable(EWKWZ_Fig3b)
tableFig3b.add_variable(QCDWZ_Fig3b)
tableFig3b.add_variable(ZZ_Fig3b)
tableFig3b.add_variable(Fake_Fig3b)
tableFig3b.add_variable(TVX_Fig3b)
tableFig3b.add_variable(VG_Fig3b)
tableFig3b.add_variable(WS_Fig3b)
tableFig3b.add_variable(Other_Fig3b)
tableFig3b.add_variable(Data_Fig3b)
submission.add_table(tableFig3b)
### End Fig3b

### Begin Fig3c
reader_Fig3c = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_mjj_2019.root")

tableFig3c = Table("Figure 3c")
tableFig3c.description = "Distributions of $m_{jj}$ in the WZ signal region."
tableFig3c.location = "Data from Figure 3c"
tableFig3c.keywords["observables"] = ["N"]

histo0_Fig3c    = reader_Fig3c.read_hist_1d("histo0")  # data
histo7_Fig3c    = reader_Fig3c.read_hist_1d("histo7")  # EWk WZ
histo8_Fig3c    = reader_Fig3c.read_hist_1d("histo8")  # QCD WZ
histo9_Fig3c    = reader_Fig3c.read_hist_1d("histo9")  # ZZ
histo10_Fig3c   = reader_Fig3c.read_hist_1d("histo10") # Nonprompt
histo12_Fig3c   = reader_Fig3c.read_hist_1d("histo12") # TVX
histo13_Fig3c   = reader_Fig3c.read_hist_1d("histo13") # VG
histo16_Fig3c   = reader_Fig3c.read_hist_1d("histo16") # WS
histo18_Fig3c   = reader_Fig3c.read_hist_1d("histo18") # Other
histo_Bck_Fig3c = reader_Fig3c.read_hist_1d("hBck")

histo_Bck_Fig3c.keys()

mmed_Fig3c = Variable("$m_{jj}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig3c.values = histo0_Fig3c["x"]

# y-axis: N events

totalbackground_Fig3c = Variable("Number of background events/GeV", is_independent=False, is_binned=False, units="")
totalbackground_Fig3c.values = histo_Bck_Fig3c["y"]

unc_totalbackground_Fig3c = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig3c.values = histo_Bck_Fig3c["dy"]

totalbackground_Fig3c.add_uncertainty(unc_totalbackground_Fig3c)

EWKWZ_Fig3c = Variable("Number of EW WZ events/GeV", is_independent=False, is_binned=False, units="")
EWKWZ_Fig3c.values = histo7_Fig3c["y"]

QCDWZ_Fig3c = Variable("Number of QCD WZ events/GeV", is_independent=False, is_binned=False, units="")
QCDWZ_Fig3c.values = histo8_Fig3c["y"]

ZZ_Fig3c = Variable("Number of ZZ events/GeV", is_independent=False, is_binned=False, units="")
ZZ_Fig3c.values = histo9_Fig3c["y"]

Fake_Fig3c = Variable("Number of nonprompt events/GeV", is_independent=False, is_binned=False, units="")
Fake_Fig3c.values = histo10_Fig3c["y"]

TVX_Fig3c = Variable("Number of tVx events/GeV", is_independent=False, is_binned=False, units="")
TVX_Fig3c.values = histo12_Fig3c["y"]

VG_Fig3c = Variable("Number of V#gamma events/GeV", is_independent=False, is_binned=False, units="")
VG_Fig3c.values = histo13_Fig3c["y"]

WS_Fig3c = Variable("Number of wrong-sign events/GeV", is_independent=False, is_binned=False, units="")
WS_Fig3c.values = histo16_Fig3c["y"]

Other_Fig3c = Variable("Number of Other events/GeV", is_independent=False, is_binned=False, units="")
Other_Fig3c.values = histo18_Fig3c["y"]

Data_Fig3c = Variable("Number of data events/GeV", is_independent=False, is_binned=False, units="")
Data_Fig3c.values = histo0_Fig3c["y"]

#unc_data_Fig3c = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig3c.values = histo0_Fig3c["dy"]
#Data_Fig3c.add_uncertainty(unc_data_Fig3c)

tableFig3c.add_variable(mmed_Fig3c)
tableFig3c.add_variable(totalbackground_Fig3c)
tableFig3c.add_variable(EWKWZ_Fig3c)
tableFig3c.add_variable(QCDWZ_Fig3c)
tableFig3c.add_variable(ZZ_Fig3c)
tableFig3c.add_variable(Fake_Fig3c)
tableFig3c.add_variable(TVX_Fig3c)
tableFig3c.add_variable(VG_Fig3c)
tableFig3c.add_variable(WS_Fig3c)
tableFig3c.add_variable(Other_Fig3c)
tableFig3c.add_variable(Data_Fig3c)
submission.add_table(tableFig3c)
### End Fig3c

### Begin Fig3d
reader_Fig3d = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_bdt_2019.root")

tableFig3d = Table("Figure 3d")
tableFig3d.description = "Distributions of BDT score in the WZ signal region."
tableFig3d.location = "Data from Figure 3d"
tableFig3d.keywords["observables"] = ["N"]

histo0_Fig3d    = reader_Fig3d.read_hist_1d("histo0")  # data
histo7_Fig3d    = reader_Fig3d.read_hist_1d("histo7")  # EWk WZ
histo8_Fig3d    = reader_Fig3d.read_hist_1d("histo8")  # QCD WZ
histo9_Fig3d    = reader_Fig3d.read_hist_1d("histo9")  # ZZ
histo10_Fig3d   = reader_Fig3d.read_hist_1d("histo10") # Nonprompt
histo12_Fig3d   = reader_Fig3d.read_hist_1d("histo12") # TVX
histo13_Fig3d   = reader_Fig3d.read_hist_1d("histo13") # VG
histo16_Fig3d   = reader_Fig3d.read_hist_1d("histo16") # WS
histo18_Fig3d   = reader_Fig3d.read_hist_1d("histo18") # Other
histo_Bck_Fig3d = reader_Fig3d.read_hist_1d("hBck")

histo_Bck_Fig3d.keys()

mmed_Fig3d = Variable("BDT score", is_independent=True, is_binned=False, units="")
mmed_Fig3d.values = histo0_Fig3d["x"]

# y-axis: N events

totalbackground_Fig3d = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig3d.values = histo_Bck_Fig3d["y"]

unc_totalbackground_Fig3d = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig3d.values = histo_Bck_Fig3d["dy"]

totalbackground_Fig3d.add_uncertainty(unc_totalbackground_Fig3d)

EWKWZ_Fig3d = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig3d.values = histo7_Fig3d["y"]

QCDWZ_Fig3d = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig3d.values = histo8_Fig3d["y"]

ZZ_Fig3d = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig3d.values = histo9_Fig3d["y"]

Fake_Fig3d = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig3d.values = histo10_Fig3d["y"]

TVX_Fig3d = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig3d.values = histo12_Fig3d["y"]

VG_Fig3d = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig3d.values = histo13_Fig3d["y"]

WS_Fig3d = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig3d.values = histo16_Fig3d["y"]

Other_Fig3d = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig3d.values = histo18_Fig3d["y"]

Data_Fig3d = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig3d.values = histo0_Fig3d["y"]

#unc_data_Fig3d = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig3d.values = histo0_Fig3d["dy"]
#Data_Fig3d.add_uncertainty(unc_data_Fig3d)

tableFig3d.add_variable(mmed_Fig3d)
tableFig3d.add_variable(totalbackground_Fig3d)
tableFig3d.add_variable(EWKWZ_Fig3d)
tableFig3d.add_variable(QCDWZ_Fig3d)
tableFig3d.add_variable(ZZ_Fig3d)
tableFig3d.add_variable(Fake_Fig3d)
tableFig3d.add_variable(TVX_Fig3d)
tableFig3d.add_variable(VG_Fig3d)
tableFig3d.add_variable(WS_Fig3d)
tableFig3d.add_variable(Other_Fig3d)
tableFig3d.add_variable(Data_Fig3d)
submission.add_table(tableFig3d)
### End Fig3d

### Begin Fig4a
reader_Fig4a = RootFileReader("HEPData/inputs/smp19012/unf_WWMJJ_normalized0.root")

tableFig4a = Table("Figure 4a")
tableFig4a.description = "Absolute WW cross section in $m_{jj}$ bins."
tableFig4a.location = "Data from Figure 4a"
tableFig4a.keywords["observables"] = ["N"]

histo_unfoldFig4a = reader_Fig4a.read_hist_1d("unfold")

histo_unfoldFig4a.keys()

for key in histo_unfoldFig4a.keys():
    print(key, type(histo_unfoldFig4a[key]), type(histo_unfoldFig4a[key][0]))

mmed_Fig4a = Variable("$m_{jj}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4a.values = histo_unfoldFig4a["x_edges"]

# y-axis: N events
unfoldFig4a = Variable("WW cross section (fb/GeV)", is_independent=False, is_binned=False, units="")
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
reader_Fig4b = RootFileReader("HEPData/inputs/smp19012/unf_WWMJJ_normalized1.root")

tableFig4b = Table("Figure 4b")
tableFig4b.description = "Normalized WW cross section in $m_{jj}$ bins."
tableFig4b.location = "Data from Figure 4b"
tableFig4b.keywords["observables"] = ["N"]

histo_unfoldFig4b = reader_Fig4b.read_hist_1d("unfold")

histo_unfoldFig4b.keys()

for key in histo_unfoldFig4b.keys():
    print(key, type(histo_unfoldFig4b[key]), type(histo_unfoldFig4b[key][0]))

mmed_Fig4b = Variable("$m_{jj}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4b.values = histo_unfoldFig4b["x_edges"]

# y-axis: N events
unfoldFig4b = Variable("Normalized WW cross section", is_independent=False, is_binned=False, units="")
unfoldFig4b.values = histo_unfoldFig4b["y"]

unc_unfoldFig4b = Uncertainty("", is_symmetric=True)
unc_unfoldFig4b.values = histo_unfoldFig4b["dy"]

unfoldFig4b.add_uncertainty(unc_unfoldFig4b)

unfoldFig4b.scale_values(1)

tableFig4b.add_variable(mmed_Fig4b)
tableFig4b.add_variable(unfoldFig4b)
submission.add_table(tableFig4b)
### End Fig4b

### Begin Fig4c
reader_Fig4c = RootFileReader("HEPData/inputs/smp19012/unf_WWMLL_normalized0.root")

tableFig4c = Table("Figure 4c")
tableFig4c.description = "Absolute WW cross section in $m_{ll}$ bins."
tableFig4c.location = "Data from Figure 4c"
tableFig4c.keywords["observables"] = ["N"]

histo_unfoldFig4c = reader_Fig4c.read_hist_1d("unfold")

histo_unfoldFig4c.keys()

for key in histo_unfoldFig4c.keys():
    print(key, type(histo_unfoldFig4c[key]), type(histo_unfoldFig4c[key][0]))

mmed_Fig4c = Variable("$m_{ll}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4c.values = histo_unfoldFig4c["x_edges"]

# y-axis: N events
unfoldFig4c = Variable("WW cross section (fb/GeV)", is_independent=False, is_binned=False, units="")
unfoldFig4c.values = histo_unfoldFig4c["y"]

unc_unfoldFig4c = Uncertainty("", is_symmetric=True)
unc_unfoldFig4c.values = histo_unfoldFig4c["dy"]

unfoldFig4c.add_uncertainty(unc_unfoldFig4c)

unfoldFig4c.scale_values(1)

tableFig4c.add_variable(mmed_Fig4c)
tableFig4c.add_variable(unfoldFig4c)
submission.add_table(tableFig4c)
### End Fig4c

### Begin Fig4d
reader_Fig4d = RootFileReader("HEPData/inputs/smp19012/unf_WWMLL_normalized1.root")

tableFig4d = Table("Figure 4d")
tableFig4d.description = "Normalized WW cross section in $m_{ll}$ bins."
tableFig4d.location = "Data from Figure 4d"
tableFig4d.keywords["observables"] = ["N"]

histo_unfoldFig4d = reader_Fig4d.read_hist_1d("unfold")

histo_unfoldFig4d.keys()

for key in histo_unfoldFig4d.keys():
    print(key, type(histo_unfoldFig4d[key]), type(histo_unfoldFig4d[key][0]))

mmed_Fig4d = Variable("$m_{ll}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4d.values = histo_unfoldFig4d["x_edges"]

# y-axis: N events
unfoldFig4d = Variable("Normalized WW cross section", is_independent=False, is_binned=False, units="")
unfoldFig4d.values = histo_unfoldFig4d["y"]

unc_unfoldFig4d = Uncertainty("", is_symmetric=True)
unc_unfoldFig4d.values = histo_unfoldFig4d["dy"]

unfoldFig4d.add_uncertainty(unc_unfoldFig4d)

unfoldFig4d.scale_values(1)

tableFig4d.add_variable(mmed_Fig4d)
tableFig4d.add_variable(unfoldFig4d)
submission.add_table(tableFig4d)
### End Fig4d

### Begin Fig4e
reader_Fig4e = RootFileReader("HEPData/inputs/smp19012/unf_WWPTL1_normalized0.root")

tableFig4e = Table("Figure 4e")
tableFig4e.description = "Absolute WW cross section in $p_{T}^{l max}$ bins."
tableFig4e.location = "Data from Figure 4e"
tableFig4e.keywords["observables"] = ["N"]

histo_unfoldFig4e = reader_Fig4e.read_hist_1d("unfold")

histo_unfoldFig4e.keys()

for key in histo_unfoldFig4e.keys():
    print(key, type(histo_unfoldFig4e[key]), type(histo_unfoldFig4e[key][0]))

mmed_Fig4e = Variable("$p_{T}^{l max}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4e.values = histo_unfoldFig4e["x_edges"]

# y-axis: N events
unfoldFig4e = Variable("WW cross section (fb/GeV)", is_independent=False, is_binned=False, units="")
unfoldFig4e.values = histo_unfoldFig4e["y"]

unc_unfoldFig4e = Uncertainty("", is_symmetric=True)
unc_unfoldFig4e.values = histo_unfoldFig4e["dy"]

unfoldFig4e.add_uncertainty(unc_unfoldFig4e)

unfoldFig4e.scale_values(1)

tableFig4e.add_variable(mmed_Fig4e)
tableFig4e.add_variable(unfoldFig4e)
submission.add_table(tableFig4e)
### End Fig4e

### Begin Fig4f
reader_Fig4f = RootFileReader("HEPData/inputs/smp19012/unf_WWPTL1_normalized1.root")

tableFig4f = Table("Figure 4f")
tableFig4f.description = "Normalized WW cross section in $p_{T}^{l max}$ bins."
tableFig4f.location = "Data from Figure 4f"
tableFig4f.keywords["observables"] = ["N"]

histo_unfoldFig4f = reader_Fig4f.read_hist_1d("unfold")

histo_unfoldFig4f.keys()

for key in histo_unfoldFig4f.keys():
    print(key, type(histo_unfoldFig4f[key]), type(histo_unfoldFig4f[key][0]))

mmed_Fig4f = Variable("$p_{T}^{l max}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig4f.values = histo_unfoldFig4f["x_edges"]

# y-axis: N events
unfoldFig4f = Variable("Normalized WW cross section", is_independent=False, is_binned=False, units="")
unfoldFig4f.values = histo_unfoldFig4f["y"]

unc_unfoldFig4f = Uncertainty("", is_symmetric=True)
unc_unfoldFig4f.values = histo_unfoldFig4f["dy"]

unfoldFig4f.add_uncertainty(unc_unfoldFig4f)

unfoldFig4f.scale_values(1)

tableFig4f.add_variable(mmed_Fig4f)
tableFig4f.add_variable(unfoldFig4f)
submission.add_table(tableFig4f)
### End Fig4f

### Begin Fig5a
reader_Fig5a = RootFileReader("HEPData/inputs/smp19012/unf_WZMJJ_normalized0.root")

tableFig5a = Table("Figure 5a")
tableFig5a.description = "Absolute WZ cross section in $m_{jj}$ bins."
tableFig5a.location = "Data from Figure 5a"
tableFig5a.keywords["observables"] = ["N"]

histo_unfoldFig5a = reader_Fig5a.read_hist_1d("unfold")

histo_unfoldFig5a.keys()

for key in histo_unfoldFig5a.keys():
    print(key, type(histo_unfoldFig5a[key]), type(histo_unfoldFig5a[key][0]))

mmed_Fig5a = Variable("$m_{jj}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig5a.values = histo_unfoldFig5a["x_edges"]

# y-axis: N events
unfoldFig5a = Variable("WZ cross section (fb/GeV)", is_independent=False, is_binned=False, units="")
unfoldFig5a.values = histo_unfoldFig5a["y"]

unc_unfoldFig5a = Uncertainty("", is_symmetric=True)
unc_unfoldFig5a.values = histo_unfoldFig5a["dy"]

unfoldFig5a.add_uncertainty(unc_unfoldFig5a)

unfoldFig5a.scale_values(1)

tableFig5a.add_variable(mmed_Fig5a)
tableFig5a.add_variable(unfoldFig5a)
submission.add_table(tableFig5a)
### End Fig5a

### Begin Fig5b
reader_Fig5b = RootFileReader("HEPData/inputs/smp19012/unf_WZMJJ_normalized1.root")

tableFig5b = Table("Figure 5b")
tableFig5b.description = "Normalized WZ cross section in $m_{jj}$ bins."
tableFig5b.location = "Data from Figure 5b"
tableFig5b.keywords["observables"] = ["N"]

histo_unfoldFig5b = reader_Fig5b.read_hist_1d("unfold")

histo_unfoldFig5b.keys()

for key in histo_unfoldFig5b.keys():
    print(key, type(histo_unfoldFig5b[key]), type(histo_unfoldFig5b[key][0]))

mmed_Fig5b = Variable("$m_{jj}$", is_independent=True, is_binned=True, units="GeV")
mmed_Fig5b.values = histo_unfoldFig5b["x_edges"]

# y-axis: N events
unfoldFig5b = Variable("Normalized WZ cross section", is_independent=False, is_binned=False, units="")
unfoldFig5b.values = histo_unfoldFig5b["y"]

unc_unfoldFig5b = Uncertainty("", is_symmetric=True)
unc_unfoldFig5b.values = histo_unfoldFig5b["dy"]

unfoldFig5b.add_uncertainty(unc_unfoldFig5b)

unfoldFig5b.scale_values(1)

tableFig5b.add_variable(mmed_Fig5b)
tableFig5b.add_variable(unfoldFig5b)
submission.add_table(tableFig5b)
### End Fig5b

### Begin Fig6a
reader_Fig6a = RootFileReader("HEPData/inputs/smp19012/ssww_wwsel_aqgc_fullmtww_2019.root")

tableFig6a = Table("Figure 6a")
tableFig6a.description = "Distributions of $m_{T}^{WW}$ in the WW signal region."
tableFig6a.location = "Data from Figure 6a"
tableFig6a.keywords["observables"] = ["N"]

histo0_Fig6a    = reader_Fig6a.read_hist_1d("histo0")  # data
histo5_Fig6a    = reader_Fig6a.read_hist_1d("histo5")  # WpWp
histo7_Fig6a    = reader_Fig6a.read_hist_1d("histo7")  # EWk WZ
histo8_Fig6a    = reader_Fig6a.read_hist_1d("histo8")  # QCD WZ
histo9_Fig6a    = reader_Fig6a.read_hist_1d("histo9")  # ZZ
histo10_Fig6a   = reader_Fig6a.read_hist_1d("histo10") # Nonprompt
histo12_Fig6a   = reader_Fig6a.read_hist_1d("histo12") # TVX
histo13_Fig6a   = reader_Fig6a.read_hist_1d("histo13") # VG
histo16_Fig6a   = reader_Fig6a.read_hist_1d("histo16") # WS
histo18_Fig6a   = reader_Fig6a.read_hist_1d("histo18") # Other
histo19_Fig6a   = reader_Fig6a.read_hist_1d("histo19") # BSM1
histo20_Fig6a   = reader_Fig6a.read_hist_1d("histo20") # BSM2
histo_Bck_Fig6a = reader_Fig6a.read_hist_1d("hBck")

histo_Bck_Fig6a.keys()

mmed_Fig6a = Variable("$m_{ll}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig6a.values = histo0_Fig6a["x"]

# y-axis: N events

totalbackground_Fig6a = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig6a.values = histo_Bck_Fig6a["y"]

unc_totalbackground_Fig6a = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig6a.values = histo_Bck_Fig6a["dy"]

totalbackground_Fig6a.add_uncertainty(unc_totalbackground_Fig6a)

WW_Fig6a = Variable("Number of W^{+/-}W^{+/-} events", is_independent=False, is_binned=False, units="")
WW_Fig6a.values = histo5_Fig6a["y"]

EWKWZ_Fig6a = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig6a.values = histo7_Fig6a["y"]

QCDWZ_Fig6a = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig6a.values = histo8_Fig6a["y"]

ZZ_Fig6a = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig6a.values = histo9_Fig6a["y"]

Fake_Fig6a = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig6a.values = histo10_Fig6a["y"]

TVX_Fig6a = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig6a.values = histo12_Fig6a["y"]

VG_Fig6a = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig6a.values = histo13_Fig6a["y"]

WS_Fig6a = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig6a.values = histo16_Fig6a["y"]

Other_Fig6a = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig6a.values = histo18_Fig6a["y"]

BSM1_Fig6a = Variable("Number of aQGC f$_{T2}$/$\Lambda^{4}$ = 2.9 TeV$^{-4}$ events", is_independent=False, is_binned=False, units="")
BSM1_Fig6a.values = histo19_Fig6a["y"]

BSM2_Fig6a = Variable("Number of aQGC f$_{S0}$/$\Lambda^{4}$ = 20 TeV$^{-4}$ events", is_independent=False, is_binned=False, units="")
BSM2_Fig6a.values = histo20_Fig6a["y"]

Data_Fig6a = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig6a.values = histo0_Fig6a["y"]

#unc_data_Fig6a = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig6a.values = histo0_Fig6a["dy"]
#Data_Fig6a.add_uncertainty(unc_data_Fig6a)

tableFig6a.add_variable(mmed_Fig6a)
tableFig6a.add_variable(totalbackground_Fig6a)
tableFig6a.add_variable(WW_Fig6a)
tableFig6a.add_variable(EWKWZ_Fig6a)
tableFig6a.add_variable(QCDWZ_Fig6a)
tableFig6a.add_variable(ZZ_Fig6a)
tableFig6a.add_variable(Fake_Fig6a)
tableFig6a.add_variable(TVX_Fig6a)
tableFig6a.add_variable(VG_Fig6a)
tableFig6a.add_variable(WS_Fig6a)
tableFig6a.add_variable(Other_Fig6a)
tableFig6a.add_variable(BSM1_Fig6a)
tableFig6a.add_variable(BSM2_Fig6a)
tableFig6a.add_variable(Data_Fig6a)
submission.add_table(tableFig6a)
### End Fig6a

### Begin Fig6b
reader_Fig6b = RootFileReader("HEPData/inputs/smp19012/ssww_wzsel_aqgc_fullmtwz_2019.root")

tableFig6b = Table("Figure 6b")
tableFig6b.description = "Distributions of $m_{T}^{WZ}$ in the WZ signal region."
tableFig6b.location = "Data from Figure 6b"
tableFig6b.keywords["observables"] = ["N"]

histo0_Fig6b    = reader_Fig6b.read_hist_1d("histo0")  # data
histo7_Fig6b    = reader_Fig6b.read_hist_1d("histo7")  # EWk WZ
histo8_Fig6b    = reader_Fig6b.read_hist_1d("histo8")  # QCD WZ
histo9_Fig6b    = reader_Fig6b.read_hist_1d("histo9")  # ZZ
histo10_Fig6b   = reader_Fig6b.read_hist_1d("histo10") # Nonprompt
histo12_Fig6b   = reader_Fig6b.read_hist_1d("histo12") # TVX
histo13_Fig6b   = reader_Fig6b.read_hist_1d("histo13") # VG
histo16_Fig6b   = reader_Fig6b.read_hist_1d("histo16") # WS
histo18_Fig6b   = reader_Fig6b.read_hist_1d("histo18") # Other
histo19_Fig6b   = reader_Fig6b.read_hist_1d("histo19") # BSM1
histo20_Fig6b   = reader_Fig6b.read_hist_1d("histo20") # BSM2
histo_Bck_Fig6b = reader_Fig6b.read_hist_1d("hBck")

histo_Bck_Fig6b.keys()

mmed_Fig6b = Variable("$m_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_Fig6b.values = histo0_Fig6b["x"]

# y-axis: N events

totalbackground_Fig6b = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_Fig6b.values = histo_Bck_Fig6b["y"]

unc_totalbackground_Fig6b = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_Fig6b.values = histo_Bck_Fig6b["dy"]

totalbackground_Fig6b.add_uncertainty(unc_totalbackground_Fig6b)

EWKWZ_Fig6b = Variable("Number of EW WZ events", is_independent=False, is_binned=False, units="")
EWKWZ_Fig6b.values = histo7_Fig6b["y"]

QCDWZ_Fig6b = Variable("Number of QCD WZ events", is_independent=False, is_binned=False, units="")
QCDWZ_Fig6b.values = histo8_Fig6b["y"]

ZZ_Fig6b = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_Fig6b.values = histo9_Fig6b["y"]

Fake_Fig6b = Variable("Number of nonprompt events", is_independent=False, is_binned=False, units="")
Fake_Fig6b.values = histo10_Fig6b["y"]

TVX_Fig6b = Variable("Number of tVx events", is_independent=False, is_binned=False, units="")
TVX_Fig6b.values = histo12_Fig6b["y"]

VG_Fig6b = Variable("Number of V#gamma events", is_independent=False, is_binned=False, units="")
VG_Fig6b.values = histo13_Fig6b["y"]

WS_Fig6b = Variable("Number of wrong-sign events", is_independent=False, is_binned=False, units="")
WS_Fig6b.values = histo16_Fig6b["y"]

Other_Fig6b = Variable("Number of Other events", is_independent=False, is_binned=False, units="")
Other_Fig6b.values = histo18_Fig6b["y"]

BSM1_Fig6b = Variable("Number of aQGC f$_{T2}$/$\Lambda^{4}$ = 2.9 TeV$^{-4}$ events", is_independent=False, is_binned=False, units="")
BSM1_Fig6b.values = histo19_Fig6a["y"]

BSM2_Fig6b = Variable("Number of aQGC f$_{S0}$/$\Lambda^{4}$ = 20 TeV$^{-4}$ events", is_independent=False, is_binned=False, units="")
BSM2_Fig6b.values = histo20_Fig6b["y"]

Data_Fig6b = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_Fig6b.values = histo0_Fig6b["y"]

#unc_data_Fig6b = Uncertainty("Poisson errors", is_symmetric=True)
#unc_data_Fig6b.values = histo0_Fig6b["dy"]
#Data_Fig6b.add_uncertainty(unc_data_Fig6b)

tableFig6b.add_variable(mmed_Fig6b)
tableFig6b.add_variable(totalbackground_Fig6b)
tableFig6b.add_variable(EWKWZ_Fig6b)
tableFig6b.add_variable(QCDWZ_Fig6b)
tableFig6b.add_variable(ZZ_Fig6b)
tableFig6b.add_variable(Fake_Fig6b)
tableFig6b.add_variable(TVX_Fig6b)
tableFig6b.add_variable(VG_Fig6b)
tableFig6b.add_variable(WS_Fig6b)
tableFig6b.add_variable(Other_Fig6b)
tableFig6b.add_variable(BSM1_Fig6b)
tableFig6b.add_variable(BSM2_Fig6b)
tableFig6b.add_variable(Data_Fig6b)
submission.add_table(tableFig6b)
### End Fig6b

### Begin Table 6
table6 = Table("Table 6")
table6.description = "Observed and expected lower and upper 95\% confidence level limits in TeV$^{-4}$ on the parameters of the quartic, obtained without using any unitarization procedure."
table6.location = "Data from Table 6"

table6.keywords["observables"] = ["Limits"]

data6 = np.loadtxt("HEPData/inputs/smp19012/aqgc_limits.txt", dtype='string', skiprows=2)

table6_data = Variable("Operator", is_independent=True, is_binned=False, units="")
table6_data.values = [str(x) for x in data6[:,0]]

table6_yields1 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields1.values = [str(x) for x in data6[:,1]]
table6_yields1.add_qualifier("Lmits", "Expected WW negative")
table6_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields2 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields2.values = [str(x) for x in data6[:,2]]
table6_yields2.add_qualifier("Lmits", "Expected WW positive")
table6_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields3 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields3.values = [str(x) for x in data6[:,3]]
table6_yields3.add_qualifier("Lmits", "Observed WW negative")
table6_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields4 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields4.values = [str(x) for x in data6[:,4]]
table6_yields4.add_qualifier("Lmits", "Observed WW positive")
table6_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields5 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields5.values = [str(x) for x in data6[:,5]]
table6_yields5.add_qualifier("Lmits", "Expected WZ negative")
table6_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields6 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields6.values = [str(x) for x in data6[:,6]]
table6_yields6.add_qualifier("Lmits", "Expected WZ positive")
table6_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields7 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields7.values = [str(x) for x in data6[:,7]]
table6_yields7.add_qualifier("Lmits", "Observed WZ negative")
table6_yields7.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields8 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields8.values = [str(x) for x in data6[:,8]]
table6_yields8.add_qualifier("Lmits", "Observed WZ positive")
table6_yields8.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields9 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields9.values = [str(x) for x in data6[:,9]]
table6_yields9.add_qualifier("Lmits", "Expected WW+WZ negative")
table6_yields9.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields10 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields10.values = [str(x) for x in data6[:,10]]
table6_yields10.add_qualifier("Lmits", "Expected WW+WZ positive")
table6_yields10.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields11 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields11.values = [str(x) for x in data6[:,11]]
table6_yields11.add_qualifier("Lmits", "Observed WW+WZ negative")
table6_yields11.add_qualifier("SQRT(S)", 13, "TeV")

table6_yields12 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table6_yields12.values = [str(x) for x in data6[:,12]]
table6_yields12.add_qualifier("Lmits", "Observed WW+WZ positive")
table6_yields12.add_qualifier("SQRT(S)", 13, "TeV")

table6.add_variable(table6_data)
table6.add_variable(table6_yields1)
table6.add_variable(table6_yields2)
table6.add_variable(table6_yields3)
table6.add_variable(table6_yields4)
table6.add_variable(table6_yields5)
table6.add_variable(table6_yields6)
table6.add_variable(table6_yields7)
table6.add_variable(table6_yields8)
table6.add_variable(table6_yields9)
table6.add_variable(table6_yields10)
table6.add_variable(table6_yields11)
table6.add_variable(table6_yields12)

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

table7_yields1 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields1.values = [str(x) for x in data7[:,1]]
table7_yields1.add_qualifier("Lmits", "Expected WW negative")
table7_yields1.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields2 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields2.values = [str(x) for x in data7[:,2]]
table7_yields2.add_qualifier("Lmits", "Expected WW positive")
table7_yields2.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields3 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields3.values = [str(x) for x in data7[:,3]]
table7_yields3.add_qualifier("Lmits", "Observed WW negative")
table7_yields3.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields4 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields4.values = [str(x) for x in data7[:,4]]
table7_yields4.add_qualifier("Lmits", "Observed WW positive")
table7_yields4.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields5 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields5.values = [str(x) for x in data7[:,5]]
table7_yields5.add_qualifier("Lmits", "Expected WZ negative")
table7_yields5.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields6 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields6.values = [str(x) for x in data7[:,6]]
table7_yields6.add_qualifier("Lmits", "Expected WZ positive")
table7_yields6.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields7 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields7.values = [str(x) for x in data7[:,7]]
table7_yields7.add_qualifier("Lmits", "Observed WZ negative")
table7_yields7.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields8 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields8.values = [str(x) for x in data7[:,8]]
table7_yields8.add_qualifier("Lmits", "Observed WZ positive")
table7_yields8.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields9 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields9.values = [str(x) for x in data7[:,9]]
table7_yields9.add_qualifier("Lmits", "Expected WW+WZ negative")
table7_yields9.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields10 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields10.values = [str(x) for x in data7[:,10]]
table7_yields10.add_qualifier("Lmits", "Expected WW+WZ positive")
table7_yields10.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields11 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields11.values = [str(x) for x in data7[:,11]]
table7_yields11.add_qualifier("Lmits", "Observed WW+WZ negative")
table7_yields11.add_qualifier("SQRT(S)", 13, "TeV")

table7_yields12 = Variable("Limits (TeV$^{-4}$)", is_independent=False, is_binned=False, units="")
table7_yields12.values = [str(x) for x in data7[:,12]]
table7_yields12.add_qualifier("Lmits", "Observed WW+WZ positive")
table7_yields12.add_qualifier("SQRT(S)", 13, "TeV")

table7.add_variable(table7_data)
table7.add_variable(table7_yields1)
table7.add_variable(table7_yields2)
table7.add_variable(table7_yields3)
table7.add_variable(table7_yields4)
table7.add_variable(table7_yields5)
table7.add_variable(table7_yields6)
table7.add_variable(table7_yields7)
table7.add_variable(table7_yields8)
table7.add_variable(table7_yields9)
table7.add_variable(table7_yields10)
table7.add_variable(table7_yields11)
table7.add_variable(table7_yields12)

submission.add_table(table7)

for table7 in submission.tables:
    table7.keywords["cmenergies"] = [13000]

### End Table 7

outdir = "smp19012_output"
submission.create_files(outdir)
