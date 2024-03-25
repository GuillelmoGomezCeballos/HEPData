import numpy as np

from hepdata_lib import Submission
from hepdata_lib import Table
from hepdata_lib import Variable, Uncertainty

from hepdata_lib import RootFileReader

import hepdata_lib

print(hepdata_lib.__version__)

sub = Submission()
     
sub.comment = "First measurements of the opposite-sign W boson pair production"+\
" cross section in proton-proton collisions at sqrt(s) = 13.6 TeV are presented. The data used in this study were collected"+\
" collisions at $\sqrt{s}$ = 13 TeV is presented. The data used in this study were collected with"+\
" with the CMS detector at the CERN LHC in 2022, and correspond to an integrated luminosity of 34.8 fb-1."+\
" Events are selected by requiring one electron and one muon of opposite charges. A maximum likelihood fit"+\
" leptons (electrons or muons). Two methods for reducing background contributions"+\
" is performed in event categories defined by the flavour and charge of the leptons, the number"+\
" of jets, and number of jets identified as originating from b quarks. An inclusive WW"+\
" production cross section of 125.7 +/- 5.6 pb is measured, in agreement with standard model predictions."+\
" Cross sections are also reported in a fiducial region close to that of the detector acceptance,"+\
" both inclusively and differentially as a function of the jet multiplicity in the event." 

sub.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SMP-24-001")
sub.add_link("arXiv", "http://arxiv.org/abs/arXiv:24xx.xxxxx")
sub.add_record_id(123456, "inspire")

#########################
tableMain_xs =  Table("Main result")
tableMain_xs.description = "Summary of inclusive cross section"
tableMain_xs.keywords["observables"] = ["SIG"]

tableMain_data = Variable("Category", is_independent=True, is_binned=False, units="")
tableMain_data.values = [  "Inclusive"
                     ]

tableMain_yields0 = Variable("Cross section", is_independent=False, is_binned=False, units="pb")
tableMain_yields0.values = [125.7
                        ]

tableMain_unc0 = Uncertainty("Total uncertainty", is_symmetric=True)
tableMain_unc0.values = [5.6
                     ]
tableMain_yields0.add_uncertainty(tableMain_unc0)

tableMain_xs.add_variable(tableMain_data)
tableMain_xs.add_variable(tableMain_yields0)

sub.add_table(tableMain_xs)
for tableMain in sub.tables:
        tableMain.keywords["cmenergies"] = [13600]
############################################
table3 = Table("Table 3")
table3.description = "Relative systematic uncertainties in the total cross section measurement."
table3.location = "Data from Table 3"

table3.keywords["observables"] = ["Uncertainty"]
table3.keywords["phrases"] = ["Electroweak", "Cross Section", "Proton-Proton", "WW production"]
table3.keywords["reactions"] = ["PP -> WW"]

data3 = np.loadtxt("HEPData/inputs/smp24001/table3.txt", dtype='string', skiprows=2)

print(data3)

table3_data = Variable("Source of uncertainty", is_independent=True, is_binned=False, units="")
table3_data.values = [str(x) for x in data3[:,0]]

table3_yields0 = Variable("Uncertainty", is_independent=False, is_binned=False, units="")
table3_yields0.values = [str(x) for x in data3[:,1]]

table3.add_variable(table3_data)
table3.add_variable(table3_yields0)

sub.add_table(table3)

for table3 in sub.tables:
    table3.keywords["cmenergies"] = [13600]
############################################
figure2_jetmulti = Table("Figure 2")
figure2_jetmulti.description = "Measured fraction of events for $N_J = 0, 1, \geq 2$ jets. The total uncertainty is reported."
figure2_jetmulti.keywords["observables"] = ["N"]

figure2_jetmulti.location = "Data from Figure 2"
figure2_jetmulti_labels = Variable("Number of jets", is_independent=True, is_binned=False, units="")
figure2_jetmulti_labels.values = [ str("$0$ Jet"),
                                  str("$1$ Jet"),
                                  str("$>=$ 2 Jet"),
                                ]

figure2_jetmulti_0 = Variable("Fraction of events", is_independent=False, is_binned=False, units="")
figure2_jetmulti_0.values = [
                            0.640,
                            0.243,
                            0.119,
                           ]


figure2_totalunc = Uncertainty("Total uncertainty", is_symmetric=True)
figure2_totalunc.values = [
                           0.016,
                           0.013,
                           0.011,
                          ]

figure2_jetmulti_0.add_uncertainty(figure2_totalunc)
figure2_jetmulti.add_variable(figure2_jetmulti_labels)
figure2_jetmulti.add_variable(figure2_jetmulti_0)

sub.add_table(figure2_jetmulti)
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]
############################################
table3aux_jetmulti = Table("Additional Table 3")
table3aux_jetmulti.description = "Fiducial cross sections for $N_J = 0, 1, \geq 2$ jets. The total uncertainty is reported."
table3aux_jetmulti.keywords["observables"] = ["N"]

table3aux_jetmulti.location = "Data from Additional Table 3"
table3aux_jetmulti_labels = Variable("Number of jets", is_independent=True, is_binned=False, units="")
table3aux_jetmulti_labels.values = [ str("$0$ Jet"),
                                  str("$1$ Jet"),
                                  str("$>=$ 2 Jet"),
                                ]

table3aux_jetmulti_0 = Variable("Fraction of events", is_independent=False, is_binned=False, units="")
table3aux_jetmulti_0.values = [
                            521,
                            198,
                             97,
                           ]

table3aux_totalunc = Uncertainty("Total uncertainty", is_symmetric=True)
table3aux_totalunc.values = [
                           27,
                           13,
                           10,
                          ]

table3aux_jetmulti_0.add_uncertainty(table3aux_totalunc)
table3aux_jetmulti.add_variable(table3aux_jetmulti_labels)
table3aux_jetmulti.add_variable(table3aux_jetmulti_0)

sub.add_table(table3aux_jetmulti)
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]
#########################################################
# Create a reader for the input file
reader_covariance_ww_fid_normalized0 = RootFileReader("HEPData/inputs/smp24001/robustHesserobustHesse_ww_fid_normalized0_obs.root")
# Read the histogram
data_covariance_ww_fid_normalized0 = reader_covariance_ww_fid_normalized0.read_hist_2d("h_covariance")
# Create variable objects
x_covariance_ww_fid_normalized0 = Variable("Bin X", is_independent=True, is_binned=True)
x_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["x_edges"]
y_covariance_ww_fid_normalized0 = Variable("Bin Y", is_independent=True, is_binned=False)
y_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["y"]
z_covariance_ww_fid_normalized0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
z_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["z"]

table_covariance_ww_fid_normalized0 = Table("Covariance Matrix ww_fid_normalized0")
table_covariance_ww_fid_normalized0.description = "Covariance Matrix fiducial and normalized cross sections fit (total, and one and two jet bin fractions)."
table_covariance_ww_fid_normalized0.location = "Supplementary material"
for var in [x_covariance_ww_fid_normalized0,y_covariance_ww_fid_normalized0,z_covariance_ww_fid_normalized0]:
    table_covariance_ww_fid_normalized0.add_variable(var)
sub.add_table(table_covariance_ww_fid_normalized0)
#########################################################
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]

outdir="./output"
sub.create_files(outdir)

import subprocess
cmd = ["zip", "-r", "output.zip", "output"]
subprocess.Popen(cmd)
