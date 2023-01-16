# Import Libraries
import numpy as np
import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
import matplotlib.pyplot as plt
from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt
from utiilities import qo, Qb, qo_vogel, qo_darcy, qo_standing, j, aof, IPR_curve_methods, IPR_Curve, pwf_darcy, f_darcy, sg_oil, sg_avg, gradient_avg
# Insert an icon
icon = Image.open("Resources/2.jpg")

# State the design of the app
st.set_page_config(page_title="Production App", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title("Production Engineering App :link:")

st.write("---")

# Add information of the app
st.markdown(
    """ This app is used to visualize 3D Trajectories of directional wells, to upload csv files, 
to call data, and to realize basic calculations.

*Python Libraries:* Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for drilling projects")

# Insert image
image = Image.open("Resources/1.jpeg")
st.image(image, width=100, use_column_width=True)

# Insert video
st.subheader("*Production Fundamentals*")
video = open("Resources/production.mp4", "rb")
st.video(video)

# Add caption
st.caption("Video about Production fundamentals")

# Sidebar
Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: *Navigation*")

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Reservoir Potential", "Nodal Analysis"],
        icons=["house", "droplet half", "clipboard data"],
    )

# Call web app sections
st.set_option('deprecation.showPyplotGlobalUse', False)
if options == "Reservoir Potential":
    if st.checkbox("Darcy"):
        method = "Darcy"
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter Flow test value: ")
        pwf_test = st.number_input("Enter Bottom hole flowing pressure test value: ")
        pr = st.number_input("Enter Reservoir Pressure value: ")
        pwf = st.number_input("Enter Bottom hole flowing pressure value: ")
        pb = st.number_input("Enter Bubble point pressure value: ")
        qb = Qb(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        IP = j(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        aof = aof(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        qo = qo_darcy(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        param = ["IP", "Qb", "AOF", "Qo"]
        st.subheader("*Show results from Darcy Method*")
        st.success(f"{param[0]} -> {IP:.3f} bbl/d/psi")
        st.success(f"{param[1]} -> {qb:.3f} BPD")
        st.success(f"{param[2]} -> {aof:.3f} BPD")
        st.success(f"{param[3]} -> {qo:.3f} BPD")
        st.subheader("*Show IPR curve*")
        pwf1 = st.number_input("Enter pwf1 pressure value: ")
        pwf2 = st.number_input("Enter pwf2 pressure value: ")
        pwf3 = st.number_input("Enter pwf3 pressure value: ")
        pwf4 = st.number_input("Enter pwf4 pressure value: ")
        pwf5 = st.number_input("Enter pwf5 pressure value: ")
        pwf_list = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        ipr = IPR_curve_methods(q_test, pwf_test, pr, pwf_list, pb, method, ef = 1, ef2 = None)
        st.pyplot(ipr)

    elif st.checkbox("Voguel"):
        st.subheader("*Enter input values*")
        method = "Voguel"
        q_test = st.number_input("Enter Flow test value: ")
        pwf_test = st.number_input("Enter Bottom hole flowing pressure test value: ")
        pr = st.number_input("Enter Reservoir Pressure test value: ")
        pwf = st.number_input("Enter Bottom hole flowing pressure value: ")
        pb = st.number_input("Enter Bubble point pressure value: ")
        qb = Qb(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        IP = j(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        aof = aof(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        qo = qo_vogel(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        param = ["IP", "Qb", "AOF", "Qo"]
        st.subheader("*Show results from Voguel Method*")
        st.success(f"{param[0]} -> {IP:.3f} bbl/d/psi")
        st.success(f"{param[1]} -> {qb:.3f} BPD")
        st.success(f"{param[2]} -> {aof:.3f} BPD")
        st.success(f"{param[3]} -> {qo:.3f} BPD")
        st.subheader("*Show IPR curve*")
        pwf1 = st.number_input("Enter pwf1 pressure value: ")
        pwf2 = st.number_input("Enter pwf2 pressure value: ")
        pwf3 = st.number_input("Enter pwf3 pressure value: ")
        pwf4 = st.number_input("Enter pwf4 pressure value: ")
        pwf5 = st.number_input("Enter pwf5 pressure value: ")
        pwf_list = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        ipr = IPR_curve_methods(q_test, pwf_test, pr, pwf_list, pb, method, ef=1, ef2=None)
        st.pyplot(ipr)

    elif st.checkbox("Standing"):
        st.subheader("*Enter input values*")
        method = "Standing"
        q_test = st.number_input("Enter Flow test value: ")
        pwf_test = st.number_input("Enter Bottom hole flowing pressure test value: ")
        pr = st.number_input("Enter Reservoir Pressure test value: ")
        pwf = st.number_input("Enter Bottom hole flowing pressure value: ")
        pb = st.number_input("Enter Bubble point pressure value: ")
        qb = Qb(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        IP = j(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        aof = aof(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        param = ["J", "Qb", "AOF", "Qo"]
        st.subheader("*Show results from Standing Method*")
        st.success(f"{param[0]} -> {IP:.3f} bbl/d/psi")
        st.success(f"{param[1]} -> {qb:.3f} BPD")
        st.success(f"{param[2]} -> {aof:.3f} BPD")
        st.success(f"{param[3]} -> {qo:.3f} BPD")
        st.subheader("*Show IPR curve*")
        pwf1 = st.number_input("Enter pwf1 pressure value: ")
        pwf2 = st.number_input("Enter pwf2 pressure value: ")
        pwf3 = st.number_input("Enter pwf3 pressure value: ")
        pwf4 = st.number_input("Enter pwf4 pressure value: ")
        pwf5 = st.number_input("Enter pwf5 pressure value: ")
        pwf_list = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        ipr = IPR_curve_methods(q_test, pwf_test, pr, pwf_list, pb, method, ef=1, ef2=None)
        st.pyplot(ipr)

    elif st.checkbox("General"):
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter Flow test value: ")
        pwf_test = st.number_input("Enter Bottom hole flowing pressure test value: ")
        pr = st.number_input("Enter Reservoir Pressure test value: ")
        pwf = st.number_input("Enter Bottom hole flowing pressure value: ")
        pb = st.number_input("Enter Bubble point pressure value: ")
        qb = Qb(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        IP = j(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        aof = aof(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        qo = qo(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        param = ["J", "Qb", "AOF", "Qo"]
        st.subheader("*Show results from General Method*")
        st.success(f"{param[0]} -> {IP:.3f} bbl/d/psi")
        st.success(f"{param[1]} -> {qb:.3f} BPD")
        st.success(f"{param[2]} -> {aof:.3f} BPD")
        st.success(f"{param[3]} -> {qo:.3f} BPD")
        st.subheader("*Show IPR curve*")
        pwf1 = st.number_input("Enter pwf1 pressure value: ")
        pwf2 = st.number_input("Enter pwf2 pressure value: ")
        pwf3 = st.number_input("Enter pwf3 pressure value: ")
        pwf4 = st.number_input("Enter pwf4 pressure value: ")
        pwf5 = st.number_input("Enter pwf5 pressure value: ")
        pwf_list = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        ipr = IPR_Curve(q_test, pwf_test, pr, pwf_list, pb, ef=1, ef2=None, ax=None)
        st.pyplot(ipr)

elif options == "Nodal Analysis":
    if st.checkbox("Monophase"):
        st.subheader("*Enter input values*")
        pr = st.number_input("Enter Reservoir Pressure test value: ")
        pb = st.number_input("Enter Bubble point pressure value: ")
        q_test = st.number_input("Enter Flow test value: ")
        pwf_test = st.number_input("Enter Bottom hole flowing pressure test value: ")
        THP = st.number_input("Enter THP value: ")
        wc = st.number_input("Enter Water concentration value: ")
        sgh2o = st.number_input("Enter SGH2O concentration value: ")
        API = st.number_input("Enter Density Oil value: ")
        ID = st.number_input("Enter ID value: ")
        TVD = st.number_input("Enter TVD value: ")
        MD = st.number_input("Enter MD value: ")
        IP = j(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        #aof = aof(q_test, pwf_test, pr, pb, ef=1, ef2=None)
        sgoil = sg_oil(API)
        sgavg = sg_avg(API, wc, sgh2o)
        GradientAvg= gradient_avg(API, wc, sgh2o)
        columns = ['Q(bpd)', 'Pwf(psia)', 'THP(psia)', 'Pgravity(psia)', 'f', 'F(ft)', 'Pf(psia)', 'Po(psia)',
                   'Psys(psia)']
        df = pd.DataFrame(columns=columns)
        df[columns[0]] = np.array([0, 750, 1400, 2250, 3000, 3750, 4500, 5250, 6000, 6750, 7500])
        df[columns[1]] = df['Q(bpd)'].apply(lambda x: pwf_darcy(q_test, pwf_test, x, pr, pb))
        df[columns[2]] = THP
        df[columns[3]] = gradient_avg(API, wc, sgh2o) * TVD
        df[columns[4]] = df['Q(bpd)'].apply(lambda x: f_darcy(x, ID,C=120))
        df[columns[5]] = df['f'] * MD
        df[columns[6]] = gradient_avg(API, wc, sgh2o) * df['F(ft)']
        df[columns[7]] = df['THP(psia)'] + df['Pgravity(psia)'] + df['Pf(psia)']
        df[columns[8]] = df['Po(psia)'] - df['Pwf(psia)']
        df



