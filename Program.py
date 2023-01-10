# Import Libraries
import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt

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
    """ This app is used to visualize Reservoir potential of different wells, Nodal Analysis (Single Phase flow).

**Python Libraries:** Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for production projects")

# Insert image
image = Image.open("Resources/1.jpeg")
st.image(image, width=100, use_column_width=True)

# Insert video
st.subheader("**Drilling Fundamentals**")
video = open("Resources/production.mp4", "rb")
st.video(video)

# Add caption
st.caption("Video about production fundamentals")

# Sidebar
Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Reservoir Potential", "Nodal Analysis (Single Flow)"],
        icons=["house", "Droplet half", "Clipboard data"],
    )