from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox, column
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Slider, Button, RadioGroup, Dropdown, RadioButtonGroup
from bokeh.plotting import figure
import numpy as np
import pandas as pd

df = pd.read_hdf("mean_stdev.h5")

arteries = ["1-aortic_arch_I", "2-brachiocephalic_trunk", "3-subclavian_R_I", "4-subclavian_R_II",
			"5-radial_R", "6-ulnar_R_I", "7-ulnar_R_II", "8-common_interosseous_R", "9-vertebral_R",
			"10-common_carotid_R", "11-external_carotid_R", "12-internal_carotid_R", "13-aortic_arch_II",
			"14-common_carotid_L", "15-internal_carotid_L", "16-external_carotid_L", "17-aortic_arch_III",
			"18-subclavian_L_I", "19-vertebral_L", "20a-subclavian_L_II", "20b-axillary_L", "21-radial_L",
			"22-ulnar_L_I", "23-ulnar_L_II", "24-common_interosseous_L", "25-aortic_arch_IV",
			"26-posterior_intercostal_T6_R", "27-thoracic_aorta_II", "28-posterior_intercostal_T6_L",
			"29-thoracic_aorta_III", "30-posterior_intercostal_T7_R", "31-thoracic_aorta_IV",
			"32-posterior_intercostal_T7_L", "33-thoracic_aorta_V", "34-celiac_trunk", "35-common_hepatic",
			"36-splenic_I", "37-splenic_II", "38-left_gastric", "39-abdominal_aorta_I", "40-superior_mesenteric",
			"41-abdominal_aorta_II", "42-renal_L", "43-abdominal_aorta_III", "44-renal_R",
			"45-abdominal_aorta_IV", "46-inferior_mesenteric", "47-abdominal_aorta_V", "48-common_iliac_R",
			"49-internal_iliac_R", "50-external_iliac_R", "51-profunda_femoris_R", "52-femoral_R_II",
			"53-popliteal_R_II", "54-anterior_tibial_R", "55-common_iliac_L", "56-internal_iliac_L",
			"57-external_iliac_L", "58-profunda_femoris_L", "59-femoral_L_II", "60-popliteal_L_II",
			"61-anterior_tibial_L", "62-basilar", "63-posterior_cerebral_P1_L", "64-posterior_cerebral_P2_L",
			"65-posterior_communicating_L", "66-internal_carotid_II_L", "67-middle_cerebral_L",
			"68-anterior_cerebral_I_L", "69-anterior_cerebral_II_L", "70-anterior_communicating",
			"71-anterior_cerebral_II_R", "72-posterior_cerebral_P1_R", "73-posterior_cerebral_P2_R",
			"74-posterior_communicating_R", "75-internal_carotid_II_R", "76-middle_cerebral_R",
			"77-anterior_cerebral_I_R"]

arteries_labels = []
arteries_menu = []
for a in arteries:
    aa = a.split("-")
    aa[1] = aa[1].capitalize()
    lbl = ''
    for b in aa:
        lbl += b+' '
    arteries_menu.append((lbl, a))

# Set up data
a = 0
c = 0

dropdown = Dropdown(label="Select an artery and click plot",
	button_type="warning", menu=arteries_menu)

def change_dropdown_label(attr, old, new):

    if dropdown.value.split("-")[0] == "20a":
        idx = 19
    elif dropdown.value.split("-")[0] == "20b":
        idx = 20
    elif int(dropdown.value.split("-")[0]) <= 19:
        idx = int(dropdown.value.split("-")[0])-1
    else:
        idx = int(dropdown.value.split("-")[0])

    dropdown.label = arteries_menu[idx][0]
    dropdown.button_type = "default"
dropdown.on_change('value', change_dropdown_label)

x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
source = ColumnDataSource(data=dict(xs=[x, x, x], ys=[y, y+2, y-2],
	colors=["white", "white", "white"]))

# Set up plot
plot = figure(plot_height=400, plot_width=400, title=" ",
              tools="crosshair, pan, reset, save, wheel_zoom, box_zoom, hover",
              x_range=[0, 1])

plot.multi_line(xs='xs', ys='ys', source=source, color='colors')
plot.xaxis.axis_label = "time (s)"
plot.yaxis.axis_label = " "

def save_waveform():
    a = dropdown.value
    # b = int(locatn.value)
    ci = radio_group_age.active
    c = int(ages[ci])
    q = radio_group_q.active

    if q == 0:
    	iavg = df[(df["q"] == "Q") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "Q") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values
    elif q == 1:
    	iavg = df[(df["q"] == "P") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "P") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values
    elif q == 2:
    	iavg = df[(df["q"] == "u") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "u") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values

    if q == 0:
        iavg *= 1e-6
        istd *= 1e-6
    elif q == 1:
        iavg *= 133.332
        istd *= 133.332
    
    r = np.zeros((len(x), 3))
    print(x)
    print(iavg)
    print(istd)
    r[:,0] = x
    r[:,1] = iavg
    r[:,2] = istd

    qs = ["Q", "P", "u"]
    np.savetxt("{0}_waveform_{1}_age-{2}.txt".format(qs[q], a, c), r)

button_download = Button(label="Download waveform (SI units)", button_type="default")
button_download.on_click(save_waveform)

# artery = Slider(title="Artery", value=0, start=0, end=len(arteries), step=1)
# locatn = Slider(title="Location", value=1, start=1, end=5, step=1)

ages = np.array(list(set(df["Age"].values)))
r_age = Slider(title="Age", value=50, start=20,
	end=79, step=1)

ages = ["20", "30", "40", "50", "60", "70"]
radio_group_age = RadioButtonGroup(labels=["20s", "30s", "40s", "50s", "60s", "70+"], active=0)

radio_group = RadioButtonGroup(labels=["SI units", "Clinical units"], active=1)

radio_group_q = RadioButtonGroup(labels=["Flow", "Pressure", "Velocity"], active=1)

def plot_wave():
    # Get the current slider values
    a = dropdown.value
    # b = int(locatn.value)
    # c = int(r_age.value)
    ci = radio_group_age.active
    c = int(ages[ci])
    units = radio_group.active
    q = radio_group_q.active

    # Generate the new curve
    
    if q == 0:
    	iavg = df[(df["q"] == "Q") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "Q") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values
    elif q == 1:
    	iavg = df[(df["q"] == "P") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "P") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values
    elif q == 2:
    	iavg = df[(df["q"] == "u") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_mean"].values
    	istd = df[(df["q"] == "u") & (df["Artery"] == a) & (df["Age"] == c)]["inlet_std"].values

    if units == 1:
        if q == 0:
            plot.yaxis.axis_label = "Flow Q (ml/s)"
        elif q == 1: 
            plot.yaxis.axis_label = "Pressure P (mmHg)"
        elif q == 2:
            iavg *= 100
            istd *= 100
            plot.yaxis.axis_label = "Velocity P (cm/s)"
    else:
        if q == 0:
            iavg *= 1e-6
            istd *= 1e-6
            plot.yaxis.axis_label = "Flow Q (m^3/s)"
        elif q == 1:
            iavg *= 133.332
            istd *= 133.332
            plot.yaxis.axis_label = "Pressure P (kPa)"
        elif q == 2:
            plot.yaxis.axis_label = "Pressure P (m/s)"

    x = np.linspace(0, 1, len(iavg))
    source.data = dict(xs=[x, x, x], ys=[iavg-istd, iavg+istd, iavg],
    	colors=["silver", "silver", "black"])

    qs = ["Volumetric flow rate", "Transmural pressure", "Blood velocity"]

    if a.split("-")[0] == "20a":
        idx = 19
    elif a.split("-")[0] == "20b":
        idx = 20
    elif int(a.split("-")[0]) <= 19:
        idx = int(a.split("-")[0])-1
    else:
        idx = int(a.split("-")[0])

    plot.title.text = "{0} - {1}".format(arteries_menu[idx][0], qs[q])


button_plot = Button(label="Plot", button_type="success")
button_plot.on_click(plot_wave)

inputs = widgetbox(dropdown, radio_group_age, radio_group, radio_group_q, button_plot,
                    button_download)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "openBF-db"