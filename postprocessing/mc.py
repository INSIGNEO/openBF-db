import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from SALib.util import read_param_file

P = pd.read_pickle("sharc/Pe.pkl")
A = pd.read_pickle("sharc/Ae.pkl")
c = pd.read_pickle("sharc/ce.pkl")
params = np.loadtxt("sharc/model_input.txt")

arteries = ["1_aortic_arch_I", "2_brachiocephalic_trunk", "3_subclavian_R_I",
    "4_subclavian_R_II",
  "5_radial_R", "6_ulnar_R_I", "7_ulnar_R_II", "8_common_interosseous_R", "9_vertebral_R",
  "10_common_carotid_R", "11_external_carotid_R", "12_internal_carotid_R",
  "13_aortic_arch_II", "14_common_carotid_L", "15_internal_carotid_L",
  "16_external_carotid_L", "17_aortic_arch_III", "18_subclavian_L_I", "19_vertebral_L",
  "20a_subclavian_L_II", "20b_axillary_L", "21_radial_L", "22_ulnar_L_I", "23_ulnar_L_II",
  "24_common_interosseous_L", "25_aortic_arch_IV", "26_posterior_intercostal_T6_R",
  "27_thoracic_aorta_II", "28_posterior_intercostal_T6_L", "29_thoracic_aorta_III",
  "30_posterior_intercostal_T7_R", "31_thoracic_aorta_IV",
  "32_posterior_intercostal_T7_L",
  "33_thoracic_aorta_V", "34_celiac_trunk", "35_common_hepatic", "36_splenic_I",
  "37_splenic_II", "38_left_gastric", "39_abdominal_aorta_I", "40_superior_mesenteric",
  "41_abdominal_aorta_II", "42_renal_L", "43_abdominal_aorta_III", "44_renal_R",
  "45_abdominal_aorta_IV", "46_inferior_mesenteric", "47_abdominal_aorta_V",
  "48_common_iliac_R", "49_internal_iliac_R", "50_external_iliac_R",
  "51_profunda_femoris_R",
  "52_femoral_R_II", "53_popliteal_R_II", "54_anterior_tibial_R", "55_common_iliac_L",
  "56_internal_iliac_L", "57_external_iliac_L", "58_profunda_femoris_L",
  "59_femoral_L_II",
  "60_popliteal_L_II", "61_anterior_tibial_L", "62_basilar", "63_posterior_cerebral_P1_L",
  "64_posterior_cerebral_P2_L", "65_posterior_communicating_L",
  "66_internal_carotid_II_L",
  "67_middle_cerebral_L", "68_anterior_cerebral_I_L", "69_anterior_cerebral_II_L",
  "70_anterior_communicating", "71_anterior_cerebral_II_R", "72_posterior_cerebral_P1_R",
  "73_posterior_cerebral_P2_R", "74_posterior_communicating_R",
  "75_internal_carotid_II_R",
  "76_middle_cerebral_R", "77_anterior_cerebral_I_R"]

P_aorta = P.loc[P['Artery'] == arteries[12]]
P_brachial = P.loc[P['Artery'] == arteries[3]]

A_abd = A.loc[A['Artery'] == arteries[47]]
A_il1 = A.loc[A['Artery'] == arteries[48]]
A_il2 = A.loc[A['Artery'] == arteries[55]]

c_abd = c.loc[c['Artery'] == arteries[47]]
c_il1 = c.loc[c['Artery'] == arteries[48]]
c_il2 = c.loc[c['Artery'] == arteries[55]]

DBPb = []
SBPb = []
BPPb = []
MBPb = []

DBPs = []
SBPs = []
BPPs = []
MBPs = []

DBPm = []
SBPm = []
BPPm = []
MBPm = []

DBPv = []
SBPv = []
BPPv = []
MBPv = []

Rfs = []

def reflection_coeff(Adp, Ad1, Ad2, cdp, cd1, cd2, rho):
    inv_rho = 1./(1060.*rho)
    Yabd = Adp*inv_rho/cdp
    Yil1 = Ad1*inv_rho/cd1
    Yil2 = Ad2*inv_rho/cd2

    n = Yabd - Yil1 - Yil2
    d = Yabd + Yil1 + Yil2

    return n/d

for w, wa, w1, w2, wabd, c1, c2, cabd, case in zip(P_brachial.Waveform, P_aorta.Waveform,
                                A_il1.Waveform, A_il2.Waveform, A_abd.Waveform,
                                c_il1.Waveform, c_il2.Waveform, c_abd.Waveform,
                                P_aorta.Case):
    DBP = np.min(w)/133.332
    SBP = np.max(w)/133.332
    BPP = SBP - DBP
    MBP = np.mean(w)/133.332

    rho = params[case-1,-2]

    Adp = np.min(wabd)
    Ad1 = np.min(w1)
    Ad2 = np.min(w2)

    cdp = np.min(cabd)
    cd1 = np.min(c1)
    cd2 = np.min(c2)

    Rf = reflection_coeff(Adp, Ad1, Ad2, cdp, cd1, cd2, rho)

    if DBP < 40 or SBP > 200 or BPP < 25 or BPP > 100 or np.abs(Rf) > 0.3:
        continue

    DBPa = np.min(wa)/133.332
    SBPa = np.max(wa)/133.332
    BPPa = SBPa - DBPa
    MBPa = np.mean(wa)/133.332

    DBPb.append(DBP)
    SBPb.append(SBP)
    BPPb.append(BPP)
    MBPb.append(MBP)

    DBPs.append(DBPa)
    SBPs.append(SBPa)
    BPPs.append(BPPa)
    MBPs.append(MBPa)

    DBPm.append(np.mean(DBPs))
    SBPm.append(np.mean(SBPs))
    BPPm.append(np.mean(BPPs))
    MBPm.append(np.mean(MBPs))

    DBPv.append(np.std(DBPs))
    SBPv.append(np.std(SBPs))
    BPPv.append(np.std(BPPs))
    MBPv.append(np.std(MBPs))

DBPb = np.array(DBPb)
SBPb = np.array(SBPb)
BPPb = np.array(BPPb)
MBPb = np.array(MBPb)

DBPs = np.array(DBPs)
SBPs = np.array(SBPs)
BPPs = np.array(BPPs)
MBPs = np.array(MBPs)

DBPm = np.array(DBPm)
SBPm = np.array(SBPm)
BPPm = np.array(BPPm)
MBPm = np.array(MBPm)

DBPv = np.array(DBPv)
SBPv = np.array(SBPv)
BPPv = np.array(BPPv)
MBPv = np.array(MBPv)

#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

qs = [MBPs, BPPs, DBPs, SBPs]
colors = ["mediumpurple", "seagreen", "darkturquoise", "maroon"]
labels = ["Aortic MBP (mmHg)", "Aortic PP (mmHg)", "Aortic DBP (mmHg)",
            "Aortic SBP (mmHg)"]

fig = plt.figure(1, figsize=(8, 8))
fig.clf()

i = 1
for q, color, label in zip(qs, colors, labels):
    ax = fig.add_subplot(2, 2, i)
    i += 1

    sns.distplot(q, color=color, label="Mean = {0:5.2f}".format(np.mean(q)), kde=False)
    ax.set_xlabel(label)
    # ax.set_ylim(0, 1100)
    plt.legend()
    plt.setp(ax, yticks=[])
    sns.despine(left=True)

plt.tight_layout()

#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

qs = [MBPb, BPPb, DBPb, SBPb]
colors = ["violet", "forestgreen", "steelblue", "indianred"]
labels = ["Brachial MBP (mmHg)", "Brachial PP (mmHg)", "Brachial DBP (mmHg)",
            "Brachial SBP (mmHg)"]

fig = plt.figure(4, figsize=(8, 8))
fig.clf()

i = 1
for q, color, label in zip(qs, colors, labels):
    ax = fig.add_subplot(2, 2, i)
    i += 1

    sns.distplot(q, color=color, label="Mean = {0:5.2f}".format(np.mean(q)), kde=False)
    ax.set_xlabel(label)
    # ax.set_ylim(0, 1100)
    plt.legend()
    plt.setp(ax, yticks=[])
    sns.despine(left=True)

plt.tight_layout()

#-----------------------------------------------------------------------------------------

qs = [MBPm, BPPm, DBPm, SBPm]
colors = ["mediumpurple", "seagreen", "darkturquoise", "maroon"]
labels = ["Mean aortic MBP (mmHg)", "Mean aortic PP (mmHg)", "Mean aortic DBP (mmHg)",
            "Mean aortic SBP (mmHg)"]

x = np.linspace(1, len(MBPm), len(MBPm))

fig = plt.figure(2, figsize=(8, 8))
fig.clf()

i = 1
for q, color, label in zip(qs, colors, labels):
    ax = fig.add_subplot(2, 2, i)
    i += 1

    ax.scatter(x, q, marker='.', color=color, s=2)
    ax.set_ylabel(label)
    ax.set_xlabel("N")
    sns.despine()

plt.tight_layout()

#-----------------------------------------------------------------------------------------

qs = [MBPv, BPPv, DBPv, SBPv]
colors = ["mediumpurple", "seagreen", "darkturquoise", "maroon"]
labels = ["Aortic MBP std (mmHg)", "Aortic PP std (mmHg)", "Aortic DBP std (mmHg)",
            "Aortic SBP std (mmHg)"]

x = np.linspace(1, len(MBPm), len(MBPm))

fig = plt.figure(3, figsize=(8, 8))
fig.clf()

i = 1
for q, color, label in zip(qs, colors, labels):
    ax = fig.add_subplot(2, 2, i)
    i += 1

    ax.scatter(x[1:], q[1:], marker='.', color=color, s=2)
    ax.set_ylabel(label)
    ax.set_xlabel("N")
    sns.despine()

plt.tight_layout()


plt.draw()
plt.show()
