#!/usr/bin/python

from __future__ import print_function
from hepdata_lib import Variable, Uncertainty
from hepdata_lib import Uncertainty

import hepdata_lib
from hepdata_lib import Submission

import numpy as np
submission = Submission()

lumi_sf = 1.0/35800.0

submission.read_abstract("hepdata_lib/examples/example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/B2G-16-029/")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:1802.09407")
submission.add_record_id(1657397, "inspire")

### Table
from hepdata_lib import Table
from hepdata_lib import Variable
from hepdata_lib import RootFileReader

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

table_covariance_XSRatio_mm_Pt = Table("cov matr norm xs aux 1a")
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

table_covariance_XSRatio_mm_Rap = Table("cov matr norm xs aux 1c")
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

table_covariance_XSRatio_mm_PhiStar = Table("cov matr norm xs aux 1e")
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

table_covariance_XSRatio_mm_PtRap0 = Table("cov matr norm xs aux 2a")
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

table_covariance_XSRatio_mm_PtRap1 = Table("cov matr norm xs aux 2b")
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

table_covariance_XSRatio_mm_PtRap2 = Table("cov matr norm xs aux 2c")
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

table_covariance_XSRatio_mm_PtRap3 = Table("cov matr norm xs aux 2d")
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

table_covariance_XSRatio_mm_PtRap4 = Table("cov matr norm xs aux 2e")
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

table_covariance_XSRatio_ee_Pt = Table("cov matr norm xs aux 1b")
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

table_covariance_XSRatio_ee_Rap = Table("cov matr norm xs aux 1d")
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

table_covariance_XSRatio_ee_PhiStar = Table("cov matr norm xs aux 1f")
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

table_covariance_XSRatio_ee_PtRap0 = Table("cov matr norm xs aux 3a")
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

table_covariance_XSRatio_ee_PtRap1 = Table("cov matr norm xs aux 3b")
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

table_covariance_XSRatio_ee_PtRap2 = Table("cov matr norm xs aux 3c")
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

table_covariance_XSRatio_ee_PtRap3 = Table("cov matr norm xs aux 3d")
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

table_covariance_XSRatio_ee_PtRap4 = Table("cov matr norm xs aux 3e")
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

table_covariance_XSRatio_mm_Pt = Table("cov matr norm xs aux 4a")
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

table_covariance_XSRatio_mm_Rap = Table("cov matr norm xs aux 4c")
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

table_covariance_XSRatio_mm_PhiStar = Table("cov matr norm xs aux 4e")
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

table_covariance_XSRatio_mm_PtRap0 = Table("cov matr norm xs aux 5a")
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

table_covariance_XSRatio_mm_PtRap1 = Table("cov matr norm xs aux 5b")
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

table_covariance_XSRatio_mm_PtRap2 = Table("cov matr norm xs aux 5c")
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

table_covariance_XSRatio_mm_PtRap3 = Table("cov matr norm xs aux 5d")
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

table_covariance_XSRatio_mm_PtRap4 = Table("cov matr norm xs aux 5e")
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

table_covariance_XSRatio_ee_Pt = Table("cov matr norm xs aux 4b")
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

table_covariance_XSRatio_ee_Rap = Table("cov matr norm xs aux 4d")
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

table_covariance_XSRatio_ee_PhiStar = Table("cov matr norm xs aux 4f")
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

table_covariance_XSRatio_ee_PtRap0 = Table("cov matr norm xs aux 6a")
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

table_covariance_XSRatio_ee_PtRap1 = Table("cov matr norm xs aux 6b")
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

table_covariance_XSRatio_ee_PtRap2 = Table("cov matr norm xs aux 6c")
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

table_covariance_XSRatio_ee_PtRap3 = Table("cov matr norm xs aux 6d")
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

table_covariance_XSRatio_ee_PtRap4 = Table("cov matr norm xs aux 6e")
table_covariance_XSRatio_ee_PtRap4.description = "Covariance matrix for normalized cross sections using born level leptons for all bins used in bins of Z pt for the 1.6 < |y(Z)| < 2.4 bin in the dielectron final state."
table_covariance_XSRatio_ee_PtRap4.location = "Supplementary material"
for var in [x_covariance_ee_PtRap4,y_covariance_ee_PtRap4,z_covariance_ee_PtRap4]:
    table_covariance_XSRatio_ee_PtRap4.add_variable(var)
submission.add_table(table_covariance_XSRatio_ee_PtRap4)
### End covariance ee

outdir = "example_output"
submission.create_files(outdir)

