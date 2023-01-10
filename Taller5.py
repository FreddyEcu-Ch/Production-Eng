import streamlit as st
import pandas as pd
#import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt

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
st.title(" Reservoir App :link:")

st.write("---")

st.markdown(
    """ This app is used to visualize the results of reservoir in Engineering of Petroleum.

**Python Libraries:** Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for software projects")

# Insert image
image = Image.open("Resources/yacimiento.jpg")
st.image(image, width=100, use_column_width=True)

# Insert video
st.subheader("**RESERVOIR ENGINEERING**")
video = open("Resources/yacimientofrancia.mp4", "rb")
st.video(video)

# Sidebar
Logo = Image.open("Resources/logo.jpg")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: **Navigation**")
# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Reservoir Potential", "Nodal Analysis (Single phase flow)"],
        icons=["house", "fuel-pump", "box"],)


