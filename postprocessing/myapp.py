# from bokeh.plotting import figure, output_file, show
# from bokeh.layouts import widgetbox
# from bokeh.models.widgets import Button
#
# import numpy as np
# import pandas as pd
#
# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource, Slider
#
# Q = pd.read_pickle("sharc/Q.pkl")
# Q1 = Q.drop(Q[Q.Waveform == "NaN"].index)
# Q2 = Q1.loc[Q1['Artery'] == "1_aortic_arch_I"]
# Q3 = Q2.loc[Q2['Location']==3, 'Waveform']
#
# # prepare some data
# x = np.linspace(0,1,100)
# y = Q3[2]
#
# # output to static HTML file
# output_file("lines.html")
#
# # x = [x*0.005 for x in range(0, 201)]
#
# source = ColumnDataSource(data=dict(x=x, y=y))
#
# plot = figure(plot_width=400, plot_height=400)
# plot.line(x, Q3, line_width=3, line_alpha=0.6)
#
# slider = Slider(start=0, end=len(Q3.index), value=0, step=1, title="slide")
#
# update_curve = CustomJS(args=dict(source=source, slider=slider), code="""
#     var data = source.get('data');
#     var f = slider.value;
#     x = data['x']
#     y = data['y']
#     for (i = 0; i < x.length; i++) {
#         y[i] = Math.pow(x[i], f)
#     }
#     source.change.emit();
# """)
# slider.js_on_change('value', update_curve)
#
#
# show(column(slider, plot))

# from bokeh.plotting import figure, output_file, show
# from bokeh.layouts import widgetbox
# from bokeh.models.widgets import Button
#
import numpy as np
import pandas as pd
#
# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource, Slider

Q = pd.read_pickle("sharc/Q.pkl")
Q = Q.drop(Q[Q.Waveform == "NaN"].index)
# Q = Q.loc[Q['Artery'] == "1_aortic_arch_I"]
# Q1 = Q.loc[Q['Location']==1, 'Waveform']

arteries = ["1_aortic_arch_I", "2_brachiocephalic_trunk", "3_subclavian_R_I", "4_subclavian_R_II",
  "5_radial_R", "6_ulnar_R_I", "7_ulnar_R_II", "8_common_interosseous_R", "9_vertebral_R",
  "10_common_carotid_R", "11_external_carotid_R", "12_internal_carotid_R",
  "13_aortic_arch_II", "14_common_carotid_L", "15_internal_carotid_L",
  "16_external_carotid_L", "17_aortic_arch_III", "18_subclavian_L_I", "19_vertebral_L",
  "20a_subclavian_L_II", "20b_axillary_L", "21_radial_L", "22_ulnar_L_I", "23_ulnar_L_II",
  "24_common_interosseous_L", "25_aortic_arch_IV", "26_posterior_intercostal_T6_R",
  "27_thoracic_aorta_II", "28_posterior_intercostal_T6_L", "29_thoracic_aorta_III",
  "30_posterior_intercostal_T7_R", "31_thoracic_aorta_IV", "32_posterior_intercostal_T7_L",
  "33_thoracic_aorta_V", "34_celiac_trunk", "35_common_hepatic", "36_splenic_I",
  "37_splenic_II", "38_left_gastric", "39_abdominal_aorta_I", "40_superior_mesenteric",
  "41_abdominal_aorta_II", "42_renal_L", "43_abdominal_aorta_III", "44_renal_R",
  "45_abdominal_aorta_IV", "46_inferior_mesenteric", "47_abdominal_aorta_V",
  "48_common_iliac_R", "49_internal_iliac_R", "50_external_iliac_R", "51_profunda_femoris_R",
  "52_femoral_R_II", "53_popliteal_R_II", "54_anterior_tibial_R", "55_common_iliac_L",
  "56_internal_iliac_L", "57_external_iliac_L", "58_profunda_femoris_L", "59_femoral_L_II",
  "60_popliteal_L_II", "61_anterior_tibial_L", "62_basilar", "63_posterior_cerebral_P1_L",
  "64_posterior_cerebral_P2_L", "65_posterior_communicating_L", "66_internal_carotid_II_L",
  "67_middle_cerebral_L", "68_anterior_cerebral_I_L", "69_anterior_cerebral_II_L",
  "70_anterior_communicating", "71_anterior_cerebral_II_R", "72_posterior_cerebral_P1_R",
  "73_posterior_cerebral_P2_R", "74_posterior_communicating_R", "75_internal_carotid_II_R",
  "76_middle_cerebral_R", "77_anterior_cerebral_I_R"]

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, Button
from bokeh.plotting import figure

# Set up data
x = np.linspace(0, 1, 100)

a = 0
b = 1
c = 0

Q1 = Q.loc[(Q['Artery']==arteries[a]) & (Q['Location']==b)]
y = Q1.loc[Q1.index==Q1.index[c], 'Waveform'][Q1.index[c]]



source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title=arteries[a],
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 1])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
# text = TextInput(title="title", value='my sine wave')

def save_waveform():
    a = int(artery.value)
    b = int(locatn.value)
    c = int(r_case.value)
    
    Q1 = Q.loc[(Q['Artery']==arteries[a]) & (Q['Location']==b)]
    y = Q1.loc[Q1.index==Q1.index[c], 'Waveform'][Q1.index[c]]
    np.savetxt("waveform.txt", y)

button = Button(label="Download", button_type="success")
button.on_click(save_waveform)

artery = Slider(title="Artery", value=0, start=0, end=len(arteries), step=1)
locatn = Slider(title="Location", value=1, start=1, end=5, step=1)
r_case = Slider(title="Case", value=0, start=0, end=len(Q1.index), step=1)

# Set up callbacks
# def update_title(attrname, old, new):
#     plot.title.text = text.value
#
# text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a = int(artery.value)
    b = int(locatn.value)
    c = int(r_case.value)

    # Generate the new curve
    x = np.linspace(0, 1, 100)
    Q1 = Q.loc[(Q['Artery']==arteries[a]) & (Q['Location']==b)]
    y = Q1.loc[Q1.index==Q1.index[c], 'Waveform'][Q1.index[c]]

    source.data = dict(x=x, y=y)
    plot.title.text = arteries[a]



for w in [artery, locatn, r_case]:
    w.on_change('value', update_data)

# Set up layouts and add to document
# inputs = widgetbox(text, offset)#, amplitude, phase, freq)
inputs = widgetbox(artery, locatn, r_case, button)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"
