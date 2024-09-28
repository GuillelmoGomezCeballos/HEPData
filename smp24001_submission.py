import numpy as np

from hepdata_lib import Submission
from hepdata_lib import Table
from hepdata_lib import Variable, Uncertainty

from hepdata_lib import RootFileReader

import hepdata_lib

print(hepdata_lib.__version__)

sub = Submission()
     
sub.comment = "Measurements at sqrt(s)= 13.6 TeV of the opposite-sign W boson pair production cross section in proton-proton collisions are presented. The data used in this study were collected with the CMS detector at the CERN LHC in 2022, and correspond to an integrated luminosity of 34.8 fb-1. Events are selected by requiring one electron and one muon of opposite charge. A maximum likelihood fit is performed on signal- and background-enriched data categories defined by the flavour and charge of the leptons, the number of jets, and number of jets originating from b quarks. The overall sensitivity is significantly better than previous results with a similar integrated luminosity. The improvement comes from a more refined control of experimental uncertainties and an improved fit strategy. An inclusive WW production cross section of  125.7 +/- 5.6 pb is measured, in agreement with standard model predictions. Cross sections are also reported in a fiducial region close to that of the detector acceptance, both inclusively and differentially, as a function of the jet multiplicity in the event. For the first time in proton-proton collisions, WW events with zero, one, and at least two jets are studied simultaneously and compared with recent theoretical predictions." 

sub.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/SMP-24-001/index.html")
sub.add_link("arXiv", "http://arxiv.org/abs/2406.05101")
sub.add_link("Statistical models", "https://doi.org/10.17181/bp9fx-6qs64")
sub.add_record_id(2796231, "inspire")

#########################
tableMain_xs =  Table("Main result")
tableMain_xs.description = "Summary of inclusive cross section."
tableMain_xs.location = ""
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

tableMain_unc1 = Uncertainty("Statistical uncertainty", is_symmetric=True)
tableMain_unc1.values = [2.3
                     ]
tableMain_yields0.add_uncertainty(tableMain_unc1)

tableMain_unc2 = Uncertainty("Systematic uncertainty", is_symmetric=True)
tableMain_unc2.values = [4.8
                     ]
tableMain_yields0.add_uncertainty(tableMain_unc2)

tableMain_unc3 = Uncertainty("Luminosity uncertainty", is_symmetric=True)
tableMain_unc3.values = [1.8
                     ]
tableMain_yields0.add_uncertainty(tableMain_unc3)

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
figure3_jetmulti = Table("Figure 3")
figure3_jetmulti.description = "Measured fraction of events for $N_j = 0, 1, \geq 2$ jets. The total uncertainty is reported."
figure3_jetmulti.keywords["observables"] = ["N"]

figure3_jetmulti.location = "Data from Figure 3"
figure3_jetmulti_labels = Variable("Number of jets", is_independent=True, is_binned=False, units="")
figure3_jetmulti_labels.values = [ str("$0$ Jet"),
                                  str("$1$ Jet"),
                                  str("$>=$ 2 Jet"),
                                ]

figure3_jetmulti_0 = Variable("Fraction of events", is_independent=False, is_binned=False, units="")
figure3_jetmulti_0.values = [
                            0.639,
                            0.242,
                            0.119,
                           ]


figure3_totalunc = Uncertainty("Total uncertainty", is_symmetric=True)
figure3_totalunc.values = [
                           0.016,
                           0.013,
                           0.011,
                          ]

figure3_jetmulti_0.add_uncertainty(figure3_totalunc)
figure3_jetmulti.add_variable(figure3_jetmulti_labels)
figure3_jetmulti.add_variable(figure3_jetmulti_0)

sub.add_table(figure3_jetmulti)
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]
############################################
table1aux = Table("Additional Table 1")
table1aux.description = "Correlation matrix from inclusive and normalized cross section measurements"
table1aux.location = "Data from Additional Table 1"

table1aux.keywords["observables"] = ["Uncertainty"]
table1aux.keywords["phrases"] = ["Electroweak", "Cross Section", "Proton-Proton", "WW production"]
table1aux.keywords["reactions"] = ["PP -> WW"]

data1aux = np.loadtxt("HEPData/inputs/smp24001/table1_aux.txt", dtype='string', skiprows=2)

print(data1aux)

table1aux_data = Variable("Observable", is_independent=True, is_binned=False, units="")
table1aux_data.values = [str(x) for x in data1aux[:,0]]

table1aux_yields0 = Variable("Correlation", is_independent=False, is_binned=False, units="")
table1aux_yields0.values = [str(x) for x in data1aux[:,1]]

table1aux_yields1 = Variable("Correlation", is_independent=False, is_binned=False, units="")
table1aux_yields1.values = [str(x) for x in data1aux[:,2]]

table1aux_yields2 = Variable("Correlation", is_independent=False, is_binned=False, units="")
table1aux_yields2.values = [str(x) for x in data1aux[:,3]]

table1aux_yields3 = Variable("Correlation", is_independent=False, is_binned=False, units="")
table1aux_yields3.values = [str(x) for x in data1aux[:,4]]

table1aux.add_variable(table1aux_data)
table1aux.add_variable(table1aux_yields0)
table1aux.add_variable(table1aux_yields1)
table1aux.add_variable(table1aux_yields2)
table1aux.add_variable(table1aux_yields3)

sub.add_table(table1aux)

for table1aux in sub.tables:
    table1aux.keywords["cmenergies"] = [13600]
############################################
table3aux_jetmulti = Table("Additional Table 3")
table3aux_jetmulti.description = "Fiducial cross sections for $N_j = 0, 1, \geq 2$ jets. The total uncertainty is reported."
table3aux_jetmulti.keywords["observables"] = ["N"]

table3aux_jetmulti.location = "Data from Additional Table 3"
table3aux_jetmulti_labels = Variable("Number of jets", is_independent=True, is_binned=False, units="")
table3aux_jetmulti_labels.values = [ str("$0$ Jet"),
                                  str("$1$ Jet"),
                                  str("$>=$ 2 Jet"),
                                ]

table3aux_jetmulti_0 = Variable("Cross section", is_independent=False, is_binned=False, units="pb")
table3aux_jetmulti_0.values = [
                            0.521,
                            0.198,
                            0.097,
                           ]

table3aux_totalunc = Uncertainty("Total uncertainty", is_symmetric=True)
table3aux_totalunc.values = [
                           0.027,
                           0.013,
                           0.010,
                          ]

table3aux_jetmulti_0.add_uncertainty(table3aux_totalunc)
table3aux_jetmulti.add_variable(table3aux_jetmulti_labels)
table3aux_jetmulti.add_variable(table3aux_jetmulti_0)

sub.add_table(table3aux_jetmulti)
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]
#########################################################
## Create a reader for the input file
#reader_covariance_ww_fid_normalized0 = RootFileReader("HEPData/inputs/smp24001/robustHesserobustHesse_ww_fid_normalized0_obs.root")
## Read the histogram
#data_covariance_ww_fid_normalized0 = reader_covariance_ww_fid_normalized0.read_hist_2d("h_covariance")
## Create variable objects
#x_covariance_ww_fid_normalized0 = Variable("Bin X", is_independent=True, is_binned=True)
#x_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["x_edges"]
#y_covariance_ww_fid_normalized0 = Variable("Bin Y", is_independent=True, is_binned=False)
#y_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["y"]
#z_covariance_ww_fid_normalized0 = Variable("covariance Matrix", is_independent=False, is_binned=False)
#z_covariance_ww_fid_normalized0.values = data_covariance_ww_fid_normalized0["z"]
#
#table_covariance_ww_fid_normalized0 = Table("Covariance Matrix")
#table_covariance_ww_fid_normalized0.description = "Covariance Matrix from fiducial and normalized cross sections measurements (total, and one and two jet bin fractions)."
#table_covariance_ww_fid_normalized0.location = "Supplementary material"
#for var in [x_covariance_ww_fid_normalized0,y_covariance_ww_fid_normalized0,z_covariance_ww_fid_normalized0]:
#    table_covariance_ww_fid_normalized0.add_variable(var)
#sub.add_table(table_covariance_ww_fid_normalized0)
############################################
tablexaux = Table("Additional Covariance Matrix Table")
tablexaux.description = "Covariance Matrix from fiducial and normalized cross sections measurements (total, and one and two jet bin fractions)."
tablexaux.location = "Data from Covariance Matrix Table"

tablexaux.keywords["observables"] = ["Uncertainty"]
tablexaux.keywords["phrases"] = ["Electroweak", "Cross Section", "Proton-Proton", "WW production"]
tablexaux.keywords["reactions"] = ["PP -> WW"]

dataxaux = np.loadtxt("HEPData/inputs/smp24001/tablex_aux.txt", dtype='string', skiprows=2)

print(dataxaux)

tablexaux_data = Variable("Observable", is_independent=True, is_binned=False, units="")
tablexaux_data.values = [str(x) for x in dataxaux[:,0]]

tablexaux_yields0 = Variable("Covariance", is_independent=False, is_binned=False, units="")
tablexaux_yields0.values = [str(x) for x in dataxaux[:,1]]

tablexaux_yields1 = Variable("Covariance", is_independent=False, is_binned=False, units="")
tablexaux_yields1.values = [str(x) for x in dataxaux[:,2]]

tablexaux_yields2 = Variable("Covariance", is_independent=False, is_binned=False, units="")
tablexaux_yields2.values = [str(x) for x in dataxaux[:,3]]

tablexaux.add_variable(tablexaux_data)
tablexaux.add_variable(tablexaux_yields0)
tablexaux.add_variable(tablexaux_yields1)
tablexaux.add_variable(tablexaux_yields2)

sub.add_table(tablexaux)

for tablexaux in sub.tables:
    tablexaux.keywords["cmenergies"] = [13600]


#########################################################
for table in sub.tables:
        table.keywords["cmenergies"] = [13600]

outdir="./output"
sub.create_files(outdir)

import subprocess
cmd = ["zip", "-r", "output.zip", "output"]
subprocess.Popen(cmd)
