#!/usr/bin/python

from __future__ import print_function
from hepdata_lib import Variable, Uncertainty
from hepdata_lib import Uncertainty

import hepdata_lib
from hepdata_lib import Submission

import numpy as np
submission = Submission()

submission.read_abstract("hepdata_lib/examples/example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/B2G-16-029/")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:1802.09407")
submission.add_record_id(1657397, "inspire")

### Table
from hepdata_lib import Table
table = Table("Additional Figure 1")
table.description = "Signal selection efficiency times acceptance as a function of resonance mass for a spin-2 bulk graviton decaying to WW and a spin-1 W' decaying to WZ."
table.location = "Data from additional Figure 1"

table.keywords["observables"] = ["ACC", "EFF"]
table.keywords["reactions"] = ["P P --> GRAVITON --> W+ W-", "P P --> WPRIME --> W+/W- Z0"]

data = np.loadtxt("hepdata_lib/examples/example_inputs/effacc_signal.txt", skiprows=2)

print(data)

### Variable
from hepdata_lib import Variable
d = Variable("Resonance mass", is_independent=True, is_binned=False, units="GeV")
d.values = data[:,0]

BulkG = Variable("Efficiency times acceptance", is_independent=False, is_binned=False, units="")
BulkG.values = data[:,1]
BulkG.add_qualifier("Efficiency times acceptance", "Bulk graviton --> WW")
BulkG.add_qualifier("SQRT(S)", 13, "TeV")

Wprime = Variable("Efficiency times acceptance", is_independent=False, is_binned=False, units="")
Wprime.values = data[:,2]
Wprime.add_qualifier("Efficiency times acceptance", "Wprime --> WZ")
Wprime.add_qualifier("SQRT(S)", 13, "TeV")

table.add_variable(d)
table.add_variable(BulkG)
table.add_variable(Wprime)

table.add_image("hepdata_lib/examples/example_inputs/signalEffVsMass.pdf")

submission.add_table(table)

for table in submission.tables:
    table.keywords["cmenergies"] = [13000]

### Histogram
from hepdata_lib import Table
table2 = Table("Figure 4a")
table2.description = "Distribution in the reconstructed B quark mass, after applying all selections to events with no forward jet, compared to the background distributions estimated before fitting. The plot refers to the low-mass mB analysis. The expectations for signal MC events are given by the blue histogram lines. Different contributions to background are indicated by the colour-filled histograms. The grey-hatched error band shows total uncertainties in the background expectation. The ratio of observations to background expectations is given in the lower panel, together with the total uncertainties prior to fitting, indicated by the grey-hatched band."
table2.location = "Data from Figure 4 (upper left), located on page 12."
table2.keywords["observables"] = ["N"]
table2.add_image("hepdata_lib/examples/example_inputs/CMS-B2G-17-009_Figure_004-a.pdf")

from hepdata_lib import RootFileReader

reader = RootFileReader("hepdata_lib/examples/example_inputs/mlfit_lm_1000.root")
reader_data = RootFileReader("hepdata_lib/examples/example_inputs/Data_cat0_singleH.root")
reader_signal = RootFileReader("hepdata_lib/examples/example_inputs/BprimeBToHB1000_cat0_singleH.root")

TotalBackground = reader.read_hist_1d("shapes_prefit/cat0_singleH/total_background")
TT = reader.read_hist_1d("shapes_prefit/cat0_singleH/TT")
QCD = reader.read_hist_1d("shapes_prefit/cat0_singleH/QCDTT")
WJets = reader.read_hist_1d("shapes_prefit/cat0_singleH/WJets")
ZJets = reader.read_hist_1d("shapes_prefit/cat0_singleH/ZJets")

Data = reader_data.read_hist_1d("h_bprimemass_SRlm")

signal = reader_signal.read_hist_1d("h_bprimemass_SRlm")

TotalBackground.keys()

for key in TotalBackground.keys():
    print(key, type(TotalBackground[key]), type(TotalBackground[key][0]))


# x-axis: B quark mass
mmed = Variable("$M_{bH}$", is_independent=True, is_binned=False, units="GeV")
mmed.values = signal["x"]

# y-axis: N events
sig = Variable("Number of signal events", is_independent=False, is_binned=False, units="")
sig.values = signal["y"]

totalbackground = Variable("Number of background events", is_independent=False, is_binned=False, units="")
totalbackground.values = TotalBackground["y"]

tt = Variable("Number of ttbar events", is_independent=False, is_binned=False, units="")
tt.values = TT["y"]

qcd = Variable("Number of qcd events", is_independent=False, is_binned=False, units="")
qcd.values = QCD["y"]

wjets = Variable("Number of wjets events", is_independent=False, is_binned=False, units="")
wjets.values = WJets["y"]

zjets = Variable("Number of zjets events", is_independent=False, is_binned=False, units="")
zjets.values = ZJets["y"]

data = Variable("Number of data events", is_independent=False, is_binned=False, units="")
data.values = Data["y"]

unc_totalbackground = Uncertainty("total uncertainty", is_symmetric=True)
unc_totalbackground.values = TotalBackground["dy"]

unc_data = Uncertainty("Poisson errors", is_symmetric=True)
unc_data.values = Data["dy"]

totalbackground.add_uncertainty(unc_totalbackground)
data.add_uncertainty(unc_data)

table2.add_variable(mmed)
table2.add_variable(sig)
table2.add_variable(totalbackground)
table2.add_variable(tt)
table2.add_variable(qcd)
table2.add_variable(zjets)
table2.add_variable(wjets)
table2.add_variable(data)
submission.add_table(table2)

outdir = "example_output"
submission.create_files(outdir)

