import numpy as np

from hepdata_lib import Submission
from hepdata_lib import Table
from hepdata_lib import Variable, Uncertainty

from hepdata_lib import RootFileReader

import hepdata_lib

print(hepdata_lib.__version__)

sub = Submission()


sub.comment = "A measurement"+\
" of the W W boson pair production cross section in proton-proton"+\
" collisions at $\sqrt{s}$ = 13 TeV is presented. The data used in this study were collected with"+\
" the CMS detector at the LHC and correspond to an integrated luminosity of 35.9 fb$^{-1}$."+\
" The W$^+$ W$^-$ candidate events are selected by first requiring two oppositely-charged"+\
" leptons (electrons or muons). Two methods for reducing background contributions"+\
" are employed. In the first one, a sequence of requirements on kinematic quantities"+\
" is applied allowing a measurement of the total cross section: 117.6 +/- 6.8 pb which"+\
" agrees well with the theoretical cross section. Fiducial cross sections are also reported"+\
" for events with zero jets or one jet, and the change in the zero-jet fiducial cross sec-"+\
" tion with the jet $p_T$ threshold is measured. Normalized differential cross sections"+\
" are reported within the fiducial region; these are compared to theoretical predictions"+\
" based on quantum chromodynamics at next-to-next-to-leading-order accuracy. A sec"+\
"ond method for suppressing background contributions employs two random forest"+\
" classifiers. The analysis based on this method includes a measurement of the total"+\
" cross section and also a measurement of the normalized jet multiplicity distribution"+\
" in $W$^+ W$^-$ events. Finally, a dilepton invariant mass distribution is used to probe for"+\
" physics beyond the standard model in the context of an effective field theory and"+\
" limits on the presence of dimension-6 operators are derived." 

sub.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SMP-18-004")


#########################
table5_xs =  Table("Table 5")
#TODO has this been updated
table5_xs.description = "Summary of cross sections obtained in the sequential cut analysis. The uncertainty listed is the total uncertainty obtained from the fit to the yields. Same flavor, SF, and different flavor, DF, cross sections are given."
table5_xs.location = "Data from Table 5"
table5_xs.keywords["observables"] = ["SIG", "signal strength"]


table5_data = Variable("Category", is_independent=True, is_binned=False, units="")
table5_data.values = [  "$0$-jet DF",
                        "$0$-jet SF",
                        "$1$-jet DF",
                        "$1$-jet SF",
                        "$0$-jet & 1-jet DF",
                        "$0$-jet & 1-jet SF",
                        "$0$-jet & 1-jet DF & SF",
                     ]


table5_yields0 = Variable("Cross section", is_independent=False, is_binned=False, units="pb")
table5_yields0.values = [125.2, 
                         120.1,
                         110.5,
                          89.9,
                         122.0,
                         106.0,
                         117.6,
                        ]

table5_unc0 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc0.values = [9.9,
                      19.0,
                      14.7,
                      23.8,
                      8.4,
                      18.7,
                      6.8,
                     ]
table5_yields0.add_uncertainty(table5_unc0)



table5_sigstr = Variable("Signal Strength", is_independent=False, is_binned=False, units="")
table5_sigstr.values = [ 1.054, 
                         1.011,
                         0.930,
                         0.757,
                         1.027,
                         0.892,
                         0.990,
                        ]
table5_unc1 = Uncertainty("total uncertainty", is_symmetric=True)
table5_unc1.values = [0.083,
                      0.160,
                      0.124,
                      0.200,
                      0.071,
                      0.157,
                      0.057,
                     ]
table5_sigstr.add_uncertainty(table5_unc1)


table5_xs.add_variable(table5_data)
table5_xs.add_variable(table5_yields0)
table5_xs.add_variable(table5_sigstr)

sub.add_table(table5_xs)
for table5 in sub.tables:
        table5.keywords["cmenergies"] = [13000]



table8_jetmulti = Table("Table 8")
table8_jetmulti.description = "Measured fraction of events after unfolding for $N_J = 0, 1, \geq 2$ jets. The first uncertainty is statistical and the" +\
" second combines systematic uncertainties from the response matrix and from the background" +\
" subtraction."
table8_jetmulti.keywords["observables"] = ["N"]


table8_jetmulti.location = "Data from Table 8"
table8_jetmulti_labels = Variable("Number of jets", is_independent=True, is_binned=False, units="")
table8_jetmulti_labels.values = [ str("$0$ Jet"),
                                  str("$1$ Jet"),
                                  str("$>=$ 2 Jet"),
                                ]

table8_jetmulti_0 = Variable("Fraction of events", is_independent=False, is_binned=False, units="")
table8_jetmulti_0.values = [
                            0.773,
                            0.193,
                            0.034,
                           ]


table8_0_statunc = Uncertainty("Statistical uncertainty", is_symmetric=True)
table8_0_statunc.values = [
                           0.008,
                           0.007,
                           0.006,
                          ]


table8_0_sysunc = Uncertainty("Systematic uncertainty", is_symmetric=True)
table8_0_sysunc.values = [
                          0.075,
                          0.043,
                          0.033,
                         ]


table8_jetmulti_0.add_uncertainty(table8_0_statunc)
table8_jetmulti_0.add_uncertainty(table8_0_sysunc)
table8_jetmulti.add_variable(table8_jetmulti_labels)
table8_jetmulti.add_variable(table8_jetmulti_0)



sub.add_table(table8_jetmulti)
for table in sub.tables:
        table.keywords["cmenergies"] = [13000]
############################################



table9_operators = Table("Table 9")
table9_operators.description = "Expected and observed 68% and 95% confidence intervals on the measurement of the Wilson coefficients associated with the three CP-preserving, dimension-6 operators."

table9_operators.location = "Data from Table 9"
table9_operators.keywords["observables"] = ["Limits"]

table9_data = Variable("Coefficients", is_independent=True, is_binned=False, units="")
table9_data.values = [  "$c_{WWW} / \\Lambda^2$",
                        "$c_W / \\Lambda^2$",
                        "$c_B / \\Lambda^2$",
                     ]
table9_68_interval_exp = Variable("68% CL interval expected", is_independent=False, is_binned=False, units="TeV$^{-2}$")
table9_68_interval_exp.values = [ "(-1.78, 1.82)",
                                  "(-3.67, 2.68)", 
                                  "(-9.45, 8.40)", 
                                ]
 
table9_68_interval_obs = Variable("68% CL interval observed", is_independent=False, is_binned=False, units="TeV$^{-2}$")
table9_68_interval_obs.values = [ "(-0.93, 0.99)",
                                  "(-2.03, 1.33)", 
                                  "(-5.14, 4.30)", 
                                ]
table9_95_interval_exp = Variable("95% CL interval expected", is_independent=False, is_binned=False, units="TeV$^{-2}$")
table9_95_interval_exp.values = [ "(-2.67, 2.71)",
                                  "(-5.28, 4.22)", 
                                  "(-13.9, 12.8)", 
                                ]

table9_95_interval_obs = Variable("95% CL interval observed", is_independent=False, is_binned=False, units="TeV$^{-2}$")
table9_95_interval_obs.values = [ "(-1.78, 1.84)",
                                  "(-3.56, 2.78)", 
                                  "(-9.35, 8.46)", 
                                ]

table9_operators.add_variable(table9_data)
table9_operators.add_variable(table9_68_interval_exp)
table9_operators.add_variable(table9_68_interval_obs)
table9_operators.add_variable(table9_95_interval_exp)
table9_operators.add_variable(table9_95_interval_obs)


sub.add_table(table9_operators)
##########################################################

figure6a = Table("Figure 6 top left")
figure6a.description = "Measured normalized differential cross sections with respect to the dilepton invariant mass."
figure6a.keywords["observables"] = ["DSIG/DMLL/SIG"]
figure6a.location = "Data from Figure 6"



mll_data = RootFileReader("HEPData/inputs/smp18004/unf_WWMLL_normalized1.root")
mll_data = mll_data.read_hist_1d("unfold")

fig6a_mll = Variable("$(1/\sigma) d\sigma/dm$", is_independent=False, is_binned=False, units="$GeV^{-1}$")
fig6a_mll.values = mll_data['y']

fig6a_mll_bins = Variable("dilepton invariant mass", is_independent=True, is_binned=True, units="GeV")
fig6a_mll_bins.values = mll_data["x_edges"]

mll_unc = Uncertainty("Statistical Uncertainty", is_symmetric=True)
mll_unc.values = mll_data['dy']

fig6a_mll.add_uncertainty(mll_unc)

figure6a.add_variable(fig6a_mll)
figure6a.add_variable(fig6a_mll_bins)
sub.add_table(figure6a)


#######################################
figure6b = Table("Figure 6 top right")
figure6b.description = "Measured normalized differential cross sections with respect to the leading lepton $p_T$."
figure6b.keywords["observables"] = ["DSIG/DPT/SIG"]
figure6b.location = "Data from Figure 6"

fig6b_ptmax = Variable("$(1/\sigma) d\sigma/dp_T$", is_independent=False, is_binned=False, units="$GeV^{-1}$")
ptmax_data = RootFileReader("HEPData/inputs/smp18004/unf_WWPTL1_normalized1.root")
ptmax_data = ptmax_data.read_hist_1d("unfold")  # data

fig6b_ptmax.values = ptmax_data['y']

fig6b_ptmax_unc = Uncertainty("Statistical Uncertainty", is_symmetric=True)
fig6b_ptmax_unc.values = ptmax_data['dy']

fig6b_ptmax_bins = Variable("Leading lepton $p_T$", is_independent=True, is_binned=True, units="GeV")
fig6b_ptmax_bins.values = ptmax_data["x_edges"]

fig6b_ptmax.add_uncertainty(fig6b_ptmax_unc)
figure6b.add_variable(fig6b_ptmax)
figure6b.add_variable(fig6b_ptmax_bins)
sub.add_table(figure6b)


#######################################
figure6c = Table("Figure 6 bottom left")
figure6c.description = "Measured normalized differential cross sections with respect to the trailing lepton $p_T$."
figure6c.keywords["observables"] = ["DSIG/DPT/SIG"]
figure6c.location = "Data from Figure 6"

fig6c_ptmin = Variable("$(1/\sigma) d\sigma/dp_T$", is_independent=False, is_binned=False, units="$GeV^{-1}$")

ptmin_data = RootFileReader("HEPData/inputs/smp18004/unf_WWPTL2_normalized1.root")
ptmin_data = ptmin_data.read_hist_1d("unfold")  # data

fig6c_ptmin.values = ptmin_data['y']

fig6c_ptmin_unc = Uncertainty("Statistical Uncertainty", is_symmetric=True)
fig6c_ptmin_unc.values = ptmin_data['dy']

fig6c_ptmin_bins = Variable("Trailing lepton $p_T$", is_independent=True, is_binned=True, units="GeV")
fig6c_ptmin_bins.values = ptmin_data["x_edges"]

fig6c_ptmin.add_uncertainty(fig6c_ptmin_unc)
figure6c.add_variable(fig6c_ptmin)
figure6c.add_variable(fig6c_ptmin_bins)
sub.add_table(figure6c)



#######################################
figure6d = Table("Figure 6 bottom right")
figure6d.description = "Measured normalized differential cross sections with respect to the dilepton azimuthal angular separation."
figure6d.keywords["observables"] = ["DSIG/DPHI/SIG"]
figure6d.location = "Data from Figure 6"

phill_data = RootFileReader("HEPData/inputs/smp18004/unf_WWDPHILL_normalized1.root")
phill_data = phill_data.read_hist_1d("unfold")  # data

fig6d_phill = Variable("$(1/\sigma) d\sigma/d\phi_{\ell\ell}$", is_independent=False, is_binned=False, units="")
fig6d_phill.values = phill_data['y']

fig6d_phill_unc = Uncertainty("Statistical Uncertainty", is_symmetric=True)
fig6d_phill_unc.values = phill_data['dy']
fig6d_phill.add_uncertainty(fig6d_phill_unc)

fig6d_phill_bins = Variable("$d\phi_{\ell\ell}$", is_independent=True, is_binned=True, units="")
fig6d_phill_bins.values = phill_data["x_edges"]

figure6d.add_variable(fig6d_phill)
figure6d.add_variable(fig6d_phill_bins)

sub.add_table(figure6d)


#########################################################
table6 = Table("Table 6")

table6.description = "Fiducial cross section for the production of $W^+W^-$ +0-jets as the $p_T$ threshold for jets is varied."+\
" The fiducial region is defined by two opposite-sign leptons with $p_T > 20$GeV and |$\eta$| < 2.5 excluding the products of tau lepton decay, and $m_{\ell\ell} > 20$GeV, $p_T^{\ell\ell} > 30$GeV, and"+\
" $p_T^{\mathrm{miss}} > 30$GeV."+\
" Jets must have $p_T$ above the stated threshold, |$\eta$| < 4.5, and be separated from each of the two leptons by dR > 0.4. The total uncertainty is reported."


table6.keywords["observables"] = ["SIG", "signal strength"]
table6.location = "Data from Table 6"


pt_thresholds = Variable("$p_T$ threshold", is_independent=True, is_binned=False, units="GeV")
pt_thresholds.values = [25, 30, 35, 45, 60]

cross_sections= Variable("Cross section", is_independent=False, is_binned=False, units="pb")
cross_sections.values = [0.836, 0.892, 0.932, 1.011, 1.118]

cross_sections_unc = Uncertainty("Total Uncertainty", is_symmetric=True)
cross_sections_unc.values = [0.056, 0.055, 0.055, 0.058, 0.067]
cross_sections.add_uncertainty(cross_sections_unc)

sigstrs= Variable("Signal Strength", is_independent=False, is_binned=False, units="")
sigstrs.values = [1.091, 1.054, 1.020, 0.993, 0.985]

sigstrs_unc = Uncertainty("Total Uncertainty", is_symmetric=True)
sigstrs_unc.values = [0.073, 0.065, 0.060, 0.057, 0.059]
sigstrs.add_uncertainty(sigstrs_unc)

table6.add_variable(pt_thresholds)
table6.add_variable(cross_sections)
table6.add_variable(sigstrs)

sub.add_table(table6)



#########################################################
for table in sub.tables:
        table.keywords["cmenergies"] = [13000]

outdir="./output"
sub.create_files(outdir)


import subprocess
cmd = ["zip", "-r", "output.zip", "output"]
subprocess.Popen(cmd)
