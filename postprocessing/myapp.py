from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox, column
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Slider, Button, RadioGroup, Dropdown, RadioButtonGroup
from bokeh.plotting import figure
import numpy as np
import pandas as pd

Q = pd.read_pickle("sharc/Qe.pkl")
P = pd.read_pickle("sharc/Pe.pkl")
u = pd.read_pickle("sharc/ue.pkl")
t = pd.read_pickle("sharc/t3.pkl")
# Q = Q.drop(Q[Q.Waveform == "NaN"].index)
# Q = Q.loc[Q['Artery'] == "1_aortic_arch_I"]
# Q1 = Q.loc[Q['Location']==1, 'Waveform']

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

# elastic_arteries = ["1_aortic_arch_I", "2_brachiocephalic_trunk", "3_subclavian_R_I",
#   "13_aortic_arch_II", "17_aortic_arch_III", "18_subclavian_L_I", "25_aortic_arch_IV",
#   "29_thoracic_aorta_III", "31_thoracic_aorta_IV", "33_thoracic_aorta_V"]
#
# u = u.drop(u[u.Waveform == "NaN"].index)
# u3 = u.drop(u[u.Location !=3].index)
# u3['Elastic'] = u3['Location']
# count = 0
# for i in u3.index:
#     if not count%1000: print(i)
#     count += 1
#     if u3['Artery'][i] in elastic_arteries:
#         u3.at[i, 'Elastic'] = 1
#     else:
#         u3.at[i, 'Elastic'] = 0
# u3.to_pickle("sharc/ue.pkl")

arteries_labels = []
arteries_menu = []
for a in arteries:
    aa = a.split("_")
    aa[1] = aa[1].capitalize()
    lbl = ''
    for b in aa:
        lbl += b+' '
    arteries_menu.append((lbl, a))

# Set up data
a = 0
# b = 1
c = 0

dropdown = Dropdown(label="Select an artery and click plot", button_type="warning",
                    menu=arteries_menu)
def change_dropdown_label(attr, old, new):
    dropdown.label = arteries_menu[int(dropdown.value.split("_")[0])-1][0]
    dropdown.button_type = "default"
dropdown.on_change('value', change_dropdown_label)

x = np.linspace(-1,-2,10)
y = np.linspace(0,1e-8,10)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title=" ",
              tools="crosshair, pan, reset, save, wheel_zoom, box_zoom, hover",
              x_range=[0, 1])

plot.line('x', 'y', source=source, line_width=2, line_alpha=0.6, color="black")
plot.xaxis.axis_label = "time (s)"
plot.yaxis.axis_label = " "

def save_waveform():
    artery = dropdown.value
    # b = int(locatn.value)
    c = int(r_case.value)
    q = radio_group_q.active

    if q == 0:
        Q1 = Q.loc[Q['Artery'] == artery]
        case = Q1.index[c]
        y = Q1.loc[Q1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==Q1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==Q1.Case[case], 'Waveform'][idx]
        x -= x[0]

    elif q == 1:
        P1 = P.loc[P['Artery'] == artery]
        case = P1.index[c]
        y = P1.loc[P1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==P1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==P1.Case[case], 'Waveform'][idx]
        x -= x[0]

    elif q == 2:
        u1 = u.loc[u['Artery'] == artery]
        case = u1.index[c]
        y = u1.loc[u1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==u1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==u1.Case[case], 'Waveform'][idx]
        x -= x[0]

    r = np.zeros((len(x), 2))
    r[:,0] = x
    r[:,1] = y

    qs = ["Q", "P", "u"]
    np.savetxt("{0}_waveform_{1}_case-{2}.txt".format(qs[q], artery, case), r)

button_download = Button(label="Download waveform (SI units)", button_type="default")
button_download.on_click(save_waveform)

# artery = Slider(title="Artery", value=0, start=0, end=len(arteries), step=1)
# locatn = Slider(title="Location", value=1, start=1, end=5, step=1)
Q1 = Q.loc[Q['Artery']==arteries[0]]
r_case = Slider(title="Case", value=0, start=0, end=len(Q1.index)-1, step=1)

radio_group = RadioGroup(labels=["SI units", "Clinical units"], active=0)
# radio_group_q = RadioGroup(labels=["Flow Q", "Pressure P"], active=0)

radio_group_q = RadioButtonGroup(labels=["Flow Q", "Pressure P", "Velocity u"], active=0)

def plot_wave():
    # Get the current slider values
    a = dropdown.value
    # b = int(locatn.value)
    c = int(r_case.value)
    units = radio_group.active
    q = radio_group_q.active

    # Generate the new curve

    if q == 0:
        Q1 = Q.loc[Q['Artery'] == a]
        case = Q1.index[c]
        y = Q1.loc[Q1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==Q1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==Q1.Case[case], 'Waveform'][idx]
        x -= x[0]

    elif q == 1:
        P1 = P.loc[P['Artery'] == a]
        case = P1.index[c]
        y = P1.loc[P1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==P1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==P1.Case[case], 'Waveform'][idx]
        x -= x[0]

    elif q == 2:
        u1 = u.loc[u['Artery'] == a]
        case = u1.index[c]
        y = u1.loc[u1.index == case, 'Waveform'][case]

        idx = t.loc[t.Case==u1.Case[case], 'Waveform'].index[0]
        x = t.loc[t.Case==u1.Case[case], 'Waveform'][idx]
        x -= x[0]

    if units == 1:
        if q == 0:
            yy = y*1e6
            plot.yaxis.axis_label = "Flow Q (ml/s)"
        elif q == 1:
            yy = y/133.332
            plot.yaxis.axis_label = "Pressure P (mmHg)"
        elif q == 2:
            yy = y*100
            plot.yaxis.axis_label = "Velocity P (cm/s)"
    else:
        if q == 0:
            yy = y
            plot.yaxis.axis_label = "Flow Q (m^3/s)"
        elif q == 1:
            yy = y/1e3
            plot.yaxis.axis_label = "Pressure P (kPa)"
        elif q == 2:
            yy = y
            plot.yaxis.axis_label = "Pressure P (m/s)"

    source.data = dict(x=x, y=yy)
    qs = ["Volumetric flow rate", "Transmural pressure", "Blood velocity"]
    plot.title.text = "{0} - {1}".format(arteries_menu[int(a.split('_')[0])-1][0], qs[q])


button_plot = Button(label="Plot", button_type="success")
button_plot.on_click(plot_wave)

# Set up layouts and add to document
# inputs = widgetbox(text, offset)#, amplitude, phase, freq)
inputs = widgetbox(dropdown, r_case, radio_group, radio_group_q, button_plot,
                    button_download)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "openBF-db"
