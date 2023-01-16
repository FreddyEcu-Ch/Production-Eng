import numpy as np
import streamlit as st
import pandas as pd
#import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt
from utiilities import j,qo_darcy,aof,Qb,qo,qo_vogel,qo_standing,qo_ipr_compuesto,IPR_curve,IPR_curve_methods, IPR_Curve

# Insert an icon
icon = Image.open("Resources/inflow.png")

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
st.title(" PRODUCTION APP :droplet:")

st.write("---")

st.markdown(
    """ This app is used to visualize the results of reservoir in Engineering of Petroleum.

*Python Libraries:* Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for software projects")

# Insert image
image = Image.open("Resources/yacimiento.jpg")
st.image(image, width=100, use_column_width=True)

# Insert video
st.subheader("*RESERVOIR ENGINEERING*")
video = open("Resources/yacimientofrancia.mp4", "rb")
st.video(video)

# Sidebar
Logo = Image.open("Resources/logo.jpg")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: *Navigation*")
# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Reservoir Potential", "Nodal Analysis (Single phase flow)"],
        icons=["house", "server", "pencil-square"],)

# Call web app sections
if options == "Reservoir Potential":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.checkbox("DARCY"):
        method="Darcy"
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter q_test value: ")
        pwf_test = st.number_input("Enter pwf_test value: ")
        pr = st.number_input("Enter pr value: ")
        pwf = st.number_input("Enter pwf value")
        pb = st.number_input("Enter pb value")
        st.subheader("*Show results*")
        Q_darcy= qo_darcy(q_test, pwf_test, pr, pwf, pb)
        st.success(f" Q_Darcy = {Q_darcy:.3f} bpd")
        IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" IP = {IP:.3f} bpd/psia")
        AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" AOF = {AOF:.3f} bpd")
        QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        st.success(f" QB = {QB:.3f} bpd")
        st.subheader("*THE IPR CURVE*")
        pwf1=st.number_input("Enter the first pwf value: ")
        pwf2=st.number_input("Enter the second pwf value: ")
        pwf3=st.number_input("Enter the third pwf value: ")
        pwf4=st.number_input("Enter the fourth pwf value: ")
        pwf5=st.number_input("Enter the fifth pwf value: ")
        list_pwf = np.array([pwf1,pwf2,pwf3,pwf4,pwf5])
        curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
        st.pyplot(curva)

    elif st.checkbox("VOGEL"):
        method = "Vogel"
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter q_test value: ")
        pwf_test = st.number_input("Enter pwf_test value: ")
        pr = st.number_input("Enter pr value: ")
        pwf = st.number_input("Enter pwf value")
        pb = st.number_input("Enter pb value")
        st.subheader("*Show results*")
        Q_Vogel= qo_vogel(q_test, pwf_test, pr, pwf, pb)
        st.success(f" Q_VOGEL = {Q_Vogel:.3f} bpd")
        IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" IP = {IP:.3f} bpd/psia")
        AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" AOF = {AOF:.3f} bpd")
        QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        st.success(f" QB = {QB:.3f} bpd")
        st.subheader("*THE IPR CURVE*")
        pwf1 = st.number_input("Enter the first pwf value: ")
        pwf2 = st.number_input("Enter the second pwf value: ")
        pwf3 = st.number_input("Enter the third pwf value: ")
        pwf4 = st.number_input("Enter the fourth pwf value: ")
        pwf5 = st.number_input("Enter the fifth pwf value: ")
        list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
        st.pyplot(curva)

    elif st.checkbox("STANDING"):
        method = "Standing"
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter q_test value: ")
        pwf_test = st.number_input("Enter pwf_test value: ")
        pr = st.number_input("Enter pr value: ")
        pwf = st.number_input("Enter pwf value")
        pb = st.number_input("Enter pb value")
        st.subheader("*Show results*")
        Q_Stand=qo_standing(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        st.success(f" Q_STANDING = {Q_Stand:.3f} bpd")
        IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" IP = {IP:.3f} bpd/psia")
        AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" AOF = {AOF:.3f} bpd")
        QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        st.success(f" Q_B = {QB:.3f} bpd")
        st.subheader("*THE IPR CURVE*")
        pwf1 = st.number_input("Enter the first pwf value: ")
        pwf2 = st.number_input("Enter the second pwf value: ")
        pwf3 = st.number_input("Enter the third pwf value: ")
        pwf4 = st.number_input("Enter the fourth pwf value: ")
        pwf5 = st.number_input("Enter the fifth pwf value: ")
        list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
        st.pyplot(curva)

    elif st.checkbox("Qo"):
        st.subheader("*Enter input values*")
        q_test = st.number_input("Enter q_test value: ")
        pwf_test = st.number_input("Enter pwf_test value: ")
        pr = st.number_input("Enter pr value: ")
        pwf = st.number_input("Enter pwf value")
        pb = st.number_input("Enter pb value")
        st.subheader("*Show results*")
        Qo=qo(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
        st.success(f" Qo = {Qo:.3f} bpd")
        IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" IP = {IP:.3f} bpd/psia")
        AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        st.success(f" AOF = {AOF:.3f} bpd")
        QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        st.success(f" QB = {QB:.3f} bpd")
        st.subheader("*THE IPR CURVE*")
        pwf1 = st.number_input("Enter the first pwf value: ")
        pwf2 = st.number_input("Enter the second pwf value: ")
        pwf3 = st.number_input("Enter the third pwf value: ")
        pwf4 = st.number_input("Enter the fourth pwf value: ")
        pwf5 = st.number_input("Enter the fifth pwf value: ")
        list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        curva=IPR_Curve(q_test,pwf_test,pr,list_pwf,pb,ef=1,ef2=None,ax=None)
        st.pyplot(curva)

