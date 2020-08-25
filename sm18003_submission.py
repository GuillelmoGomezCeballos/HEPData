
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

outdir = "smp18003_output"
submission.create_files(outdir)
