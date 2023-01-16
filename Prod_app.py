import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import plotly_express as px
from utiilities import j_darcy,j,aof,Qb,qo_darcy,qo_vogel,qo_ipr_compuesto,qo_standing,qo,IPR_curve_methods, IPR_curve, sg_avg,gradient_avg,inflow,fig
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt
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
if options== "Reservoir Potential":
    if st.checkbox("Darcy"):
        Seleccion=st.selectbox("Select",("Qo","IPR"))
        if Seleccion=="Qo":
            st.subheader("Enter input")
            q_test=st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr= st.number_input("Ingrese Presion de reservorio Pr")
            pwf=st.number_input("Ingrese pwf")
            pb= st.number_input("Ingrese Presion de burbuja Pb")
            qod=qo_darcy(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
            q="Qo Darcy"
            st.success(f"{q} -> {qod:.3f} degrees")
        elif Seleccion=="IPR":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            #numero = int(st.number_input("Ingrese cuanto pwf hay:"))
            pwf = [4000,3500,3000,2500,1000,0]
            curva = IPR_curve_methods(q_test, pwf_test, pr, pwf, pb, 'Darcy')
            st.pyplot(curva)



    elif st.checkbox("Vogel"):
        Seleccion = st.selectbox("Select", ("Qo", "IPR"))
        if Seleccion == "Qo":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pwf = st.number_input("Ingrese pwf")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            qod = qo_vogel(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
            q = "Qo Vogel"
            st.success(f"{q} -> {qod:.3f} degrees")
        elif Seleccion=="IPR":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            #numero = int(st.number_input("Ingrese cuanto pwf hay:"))
            pwf = [4000,3500,3000,2500,1000,0]
            curva = IPR_curve_methods(q_test, pwf_test, pr, pwf, pb, 'Vogel')
            st.pyplot(curva)

    elif st.checkbox("Standing"):
        Seleccion = st.selectbox("Select", ("Qo", "IPR"))
        if Seleccion == "Qo":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pwf = st.number_input("Ingrese pwf")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            qod = qo_standing(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
            q = "Qo Standing"
            st.success(f"{q} -> {qod:.3f} degrees")
        elif Seleccion=="IPR":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            #numero = int(st.number_input("Ingrese cuanto pwf hay:"))
            pwf = [4000,3500,3000,2500,1000,0]
            curva = IPR_curve_methods(q_test, pwf_test, pr, pwf, pb, 'Standing')
            st.pyplot(curva)
    elif st.checkbox("IPR Compuesto"):
        Seleccion = st.selectbox("Select", ("Qo", "IPR"))
        if Seleccion == "Qo":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pwf = st.number_input("Ingrese pwf")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            ef = st.number_input("Inrese EF1")
            ef2 = st.number_input("Inrese EF2")
            qod = qo_ipr_compuesto(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
            q = "Qo IPR compuesto"
            st.success(f"{q} -> {qod:.3f} degrees")
        elif Seleccion == "IPR":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            # numero = int(st.number_input("Ingrese cuanto pwf hay:"))
            pwf = [4000, 3500, 3000, 2500, 1000, 0]
            curva = IPR_curve_methods(q_test, pwf_test, pr, pwf, pb, 'IPR_compuesto')
            st.pyplot(curva)

    elif st.checkbox("Todas las condiciones"):
        Seleccion = st.selectbox("Select", ("Qo", "IPR"))
        if Seleccion == "Qo":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pwf = st.number_input("Ingrese pwf")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            ef=st.number_input("Inrese EF1")
            ef2 = st.number_input("Inrese EF2")
            qod = qo(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
            q = "Qo all conditions"
            st.success(f"{q} -> {qod:.3f} degrees")
        elif Seleccion=="IPR":
            st.subheader("Enter input")
            q_test = st.number_input("Ingrese caudal de prueba Qtest")
            pwf_test = st.number_input("Ingrese Pwf de prueba Pwftest")
            pr = st.number_input("Ingrese Presion de reservorio Pr")
            pb = st.number_input("Ingrese Presion de burbuja Pb")
            #numero = int(st.number_input("Ingrese cuanto pwf hay:"))
            pwf = [4000,3500,3000,2500,1000,0]
            curva = IPR_curve(q_test, pwf_test, pr, pwf, pb)
            st.pyplot(curva)
elif options== "Nodal Analysis (Single phase flow)":
    if st.checkbox("Monofasico"):
        opcion=st.selectbox("Select",("GEprom fluid","Gradienteprom fluid","Dataframe Inflow"))
        if opcion=="GEprom fluid":
            API=st.number_input("Ingrese API")
            wcut=st.number_input("Ingrese wc")
            sg_h2o=st.number_input("Ingrese gravedad especifica h2o")
            ge=sg_avg(API, wcut, sg_h2o)
            g = "Gravedad especifica del fluido"
            st.success(f"{g} -> {ge:.3f} degrees")

        elif opcion=="Gradienteprom fluid":
            API=st.number_input("Ingrese API")
            wcut=st.number_input("Ingrese wcut")
            sg_h2o=st.number_input("Ingrese gravedad especifica h2o")
            ge=gradient_avg(API, wcut, sg_h2o)
            g = "Gradiente promedio del fluido"
            st.success(f"{g} -> {ge:.3f} degrees")

        elif opcion=="Dataframe Inflow":
            Qt=st.number_input("Ingrese Qt")
            Pwft=st.number_input("Ingrese Pwft")
            Pr=st.number_input("Ingrese Pr")
            Pb = st.number_input("Ingrese Pb")
            THP = st.number_input("Ingrese THP")
            API = st.number_input("Ingrese API")
            wcut = st.number_input("Ingrese wcut")
            sg_h2o = st.number_input("Ingrese sg_h2o")
            tvd = st.number_input("Ingrese tvd")
            ID = st.number_input("Ingrese ID")
            C = st.number_input("Ingrese C")
            md = st.number_input("Ingrese md")
            df=inflow(Qt,Pwft,Pr,Pb,THP,API,wcut,sg_h2o,tvd,ID,C,md)
            st.write(df)
            curva=fig(df)
            st.pyplot(curva)
