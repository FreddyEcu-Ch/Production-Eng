import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import plotly_express as px

#Titulo de la aplicación
st.title("Production Engineering App")

# insertar icono
icon=Image.open("Resources/Nodal.png")

#Insertar logo
logo=Image.open("Resources/logo.jpg")

#Descripción
st.write("aplicación para calcular las curvas IPR, usadas en ingeniería de producción petrolera")

#Video
video=open("Resources/video.mp4")
st.video(video)
#Menu de opciones
st.sidebar.title("Menu de opciones")
with st.sidebar:
    options=option_menu(menu_title="Menu",
                        options=["Home","Reservoir Potential","Nodal Analysis (Single phase flow)"],
                        icons=["menu-app","bar-chart-line-fill","clipboard2-data-fill"])

