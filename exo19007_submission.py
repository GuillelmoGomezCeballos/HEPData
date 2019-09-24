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

submission.read_abstract("HEPData/inputs/exo19007/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-19-007/")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:19xx.xxxxx")
submission.add_record_id(123456, "inspire")

### Begin Table 2
table2 = Table("Table 2")
table2.description = "Observed yields, background estimates after the fit to data, and signal predictions after the event selection in the signal region. The signal size corresponds to $0.1 \sigma_{\mathrm{\mathrm{ZH}}}$  for all three $m_{\mathrm{\mathrm{H}}}$ values shown. The combined statistical and systematic uncertainties are reported."
table2.location = "Data from Table 2"

table2.keywords["observables"] = ["Events"]

data2 = np.loadtxt("HEPData/inputs/exo19007/total_yields.txt", dtype='string', skiprows=2)

print(data2)

table2_data = Variable("Process", is_independent=True, is_binned=False, units="")
table2_data.values = [str(x) for x in data2[:,0]]

table2_yields = Variable("Events", is_independent=False, is_binned=False, units="")
table2_yields.values = [float(x) for x in data2[:,1]]
table2_yields.add_qualifier("Expected events", "ZH selection")
table2_yields.add_qualifier("SQRT(S)", 13, "TeV")

table2_unc = Uncertainty("total uncertainty", is_symmetric=True)
table2_unc.values = [float(x) for x in data2[:,2]]

table2_yields.add_uncertainty(table2_unc)

table2.add_variable(table2_data)
table2.add_variable(table2_yields)

submission.add_table(table2)

for table2 in submission.tables:
    table2.keywords["cmenergies"] = [13000]

### End Table 2

### Begin Table cut flow
table_cut_flow = Table("Table cut flow")
table_cut_flow.description = "Expected yields for different processes after several selection stages. The preselection requires two leptons and at least one photon with $\mathrm{p_\mathrm{T}}$ larger than 25, 20, and 25 GeV, respectively; in addition the dilepton $\mathrm{p_\mathrm{T}}$ must be larger than 60 GeV, and the $\mathrm{p_\mathrm{T}}^{\mathrm{miss}}$ larger than 70 GeV. The signal prediction corresponds to $0.1 \sigma_{\mathrm{\mathrm{ZH}}}$ at $m_{H}$ = 125 GeV."
table_cut_flow.location = "Supplementary material"

table_cut_flow.keywords["observables"] = ["Events"]

data_cut_flow = np.loadtxt("HEPData/inputs/exo19007/cutflow_yields.txt", dtype='string', skiprows=2)

print(data_cut_flow)

d_cut_flow = Variable("Cut", is_independent=True, is_binned=False, units="")
d_cut_flow.values= [str(x) for x in data_cut_flow[:,0]]

ZH125_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
ZH125_cut_flow.values = [float(x) for x in data_cut_flow[:,1]]
ZH125_cut_flow.add_qualifier("Process", "ZH(125) events")
ZH125_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

EM_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
EM_cut_flow.values = [float(x) for x in data_cut_flow[:,2]]
EM_cut_flow.add_qualifier("Process", "Nonresonant events")
EM_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

WZ_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
WZ_cut_flow.values = [float(x) for x in data_cut_flow[:,3]]
WZ_cut_flow.add_qualifier("Process", "WZ events")
WZ_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

ZZ_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
ZZ_cut_flow.values = [float(x) for x in data_cut_flow[:,4]]
ZZ_cut_flow.add_qualifier("Process", "ZZ events")
ZZ_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

VG_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
VG_cut_flow.values = [float(x) for x in data_cut_flow[:,5]]
VG_cut_flow.add_qualifier("Process", "Zgamma events")
VG_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

VVV_cut_flow = Variable("Events", is_independent=False, is_binned=False, units="")
VVV_cut_flow.values = [float(x) for x in data_cut_flow[:,6]]
VVV_cut_flow.add_qualifier("Process", "VVV events")
VVV_cut_flow.add_qualifier("SQRT(S)", 13, "TeV")

table_cut_flow.add_variable(d_cut_flow)
table_cut_flow.add_variable(ZH125_cut_flow)
table_cut_flow.add_variable(EM_cut_flow)
table_cut_flow.add_variable(WZ_cut_flow)
table_cut_flow.add_variable(ZZ_cut_flow)
table_cut_flow.add_variable(VG_cut_flow)
table_cut_flow.add_variable(VVV_cut_flow)

submission.add_table(table_cut_flow)

for table_cut_flow in submission.tables:
    table_cut_flow.keywords["cmenergies"] = [13000]

### End Table cut flow


### Begin Table limits
table_limits = Table("Table limits")
table_limits.description = "Expected and observed upper limits at 95\% confidence level on the product of $\sigma_{\mathrm{\mathrm{ZH}}}$ and $\mathcal{B}$($\mathrm{H}$ -> $\mathrm{invisible}+\gamma$) as a function of $m_{\mathrm{\mathrm{H}}}$."
table_limits.location = "Data from Figure 4"

table_limits.keywords["observables"] = ["Cross section in pb"]

data_limits = np.loadtxt("HEPData/inputs/exo19007/cross_section_limits.txt", dtype='float')

print(data_limits)

mass_limits = Variable("Mass", is_independent=True, is_binned=False, units="")
mass_limits.values = data_limits[:,0]

obs_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
obs_limits.values = data_limits[:,1]
obs_limits.add_qualifier("Cross section limits", "Observed limits")
obs_limits.add_qualifier("SQRT(S)", 13, "TeV")

theo_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
theo_limits.values = data_limits[:,2]
theo_limits.add_qualifier("Cross section limits", "Theoretical cross section assuming $0.1 \sigma_{\mathrm{\mathrm{ZH}}}$")
theo_limits.add_qualifier("SQRT(S)", 13, "TeV")

exp_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
exp_limits.values = data_limits[:,3]
exp_limits.add_qualifier("Cross section limits", "Expected limits")
exp_limits.add_qualifier("SQRT(S)", 13, "TeV")

minus2sigma_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
minus2sigma_limits.values = data_limits[:,4]
minus2sigma_limits.add_qualifier("Cross section limits", "-2 sigma limits")
minus2sigma_limits.add_qualifier("SQRT(S)", 13, "TeV")

minus1sigma_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
minus1sigma_limits.values = data_limits[:,5]
minus1sigma_limits.add_qualifier("Cross section limits", "-1 sigma limits")
minus1sigma_limits.add_qualifier("SQRT(S)", 13, "TeV")

plus1sigma_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
plus1sigma_limits.values = data_limits[:,6]
plus1sigma_limits.add_qualifier("Cross section limits", "+1 sigma limits")
plus1sigma_limits.add_qualifier("SQRT(S)", 13, "TeV")

plus2sigma_limits = Variable("Cross section in pb", is_independent=False, is_binned=False, units="")
plus2sigma_limits.values = data_limits[:,7]
plus2sigma_limits.add_qualifier("Cross section limits", "+2 sigma limits")
plus2sigma_limits.add_qualifier("SQRT(S)", 13, "TeV")

table_limits.add_variable(mass_limits)
table_limits.add_variable(obs_limits)
table_limits.add_variable(theo_limits)
table_limits.add_variable(minus2sigma_limits)
table_limits.add_variable(minus1sigma_limits)
table_limits.add_variable(plus1sigma_limits)
table_limits.add_variable(plus2sigma_limits)

submission.add_table(table_limits)

for table_limits in submission.tables:
    table_limits.keywords["cmenergies"] = [13000]

### End Table limits


### Begin EM CR
reader_emcr = RootFileReader("HEPData/inputs/exo19007/histo_zhg_region0.root")

tableEMCR = Table("Figure 2a")
tableEMCR.description = "$\mathrm{M_{\mathrm{T}}}$ distribution for the $\mathrm{e}\mu$ control region."
tableEMCR.location = "Data from Figure 2a"
tableEMCR.keywords["observables"] = ["N"]

histo_Data_emcr  = reader_emcr.read_hist_1d("histo_Data")
histo_ZZ_emcr    = reader_emcr.read_hist_1d("histo_ZZ")
histo_WZ_emcr    = reader_emcr.read_hist_1d("histo_WZ")
histo_VVV_emcr   = reader_emcr.read_hist_1d("histo_VVV")
histo_VG_emcr    = reader_emcr.read_hist_1d("histo_VG")
histo_EM_emcr    = reader_emcr.read_hist_1d("histo_EM")
histo_ZH125_emcr = reader_emcr.read_hist_1d("histo_ZH125")
histo_ZH200_emcr = reader_emcr.read_hist_1d("histo_ZH200")
histo_ZH300_emcr = reader_emcr.read_hist_1d("histo_ZH300")
histo_Bck_emcr   = reader_emcr.read_hist_1d("histo_EM")

histo_Bck_emcr.keys()

for key in histo_Bck_emcr.keys():
    print(key, type(histo_Bck_emcr[key]), type(histo_Bck_emcr[key][0]))

mmed_emcr = Variable("$M_{T}$", is_independent=True, is_binned=False, units="GeV")
mmed_emcr.values = histo_ZH125_emcr["x"]

# y-axis: N events
ZH125_emcr = Variable("Number of ZH(125) signal events", is_independent=False, is_binned=False, units="")
ZH125_emcr.values = histo_ZH125_emcr["y"]

ZH200_emcr = Variable("Number of ZH(200) signal events", is_independent=False, is_binned=False, units="")
ZH200_emcr.values = histo_ZH200_emcr["y"]

ZH300_emcr = Variable("Number of ZH(300) signal events", is_independent=False, is_binned=False, units="")
ZH300_emcr.values = histo_ZH300_emcr["y"]

totalbackground_emcr = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground_emcr.values = histo_Bck_emcr["y"]

unc_totalbackground_emcr = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground_emcr.values = histo_Bck_emcr["dy"]

totalbackground_emcr.add_uncertainty(unc_totalbackground_emcr)

ZZ_emcr = Variable("Number of ZZ events", is_independent=False, is_binned=False, units="")
ZZ_emcr.values = histo_ZZ_emcr["y"]

WZ_emcr = Variable("Number of WZ events", is_independent=False, is_binned=False, units="")
WZ_emcr.values = histo_WZ_emcr["y"]

VVV_emcr = Variable("Number of VVV events", is_independent=False, is_binned=False, units="")
VVV_emcr.values = histo_VVV_emcr["y"]

VG_emcr = Variable("Number of VG events", is_independent=False, is_binned=False, units="")
VG_emcr.values = histo_VG_emcr["y"]

EM_emcr = Variable("Number of nonresonant events", is_independent=False, is_binned=False, units="")
EM_emcr.values = histo_EM_emcr["y"]

Data_emcr = Variable("Number of data events", is_independent=False, is_binned=False, units="")
Data_emcr.values = histo_Data_emcr["y"]

unc_data_emcr = Uncertainty("Poisson errors", is_symmetric=True)
unc_data_emcr.values = histo_Data_emcr["dy"]
Data_emcr.add_uncertainty(unc_data_emcr)

tableEMCR.add_variable(mmed_emcr)
tableEMCR.add_variable(ZH125_emcr)
tableEMCR.add_variable(ZH200_emcr)
tableEMCR.add_variable(ZH300_emcr)
tableEMCR.add_variable(totalbackground_emcr)
tableEMCR.add_variable(ZZ_emcr)
tableEMCR.add_variable(WZ_emcr)
tableEMCR.add_variable(VVV_emcr)
tableEMCR.add_variable(VG_emcr)
tableEMCR.add_variable(EM_emcr)
tableEMCR.add_variable(Data_emcr)
submission.add_table(tableEMCR)
### End EM CR

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

outdir = "exo19007_output"
submission.create_files(outdir)
