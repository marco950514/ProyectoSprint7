#Se importan las librerias

import plotly.express as px
import pandas as pd
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write("""<h1 style="text-align:center";> Bienvenidos al Proyecto del Sprint7 </h1>""", unsafe_allow_html=True)

st.write("""
         <h3 style="text-align:justify";>
         
        En este proyecto utilizaremos herramientas de desarrollo de software vistas durante la teoria,
         estaremos utilizando Render para la gestion de nuestra aplicacion web y la libreria streamlit
         para mostrar los elementos en la página.

        </h3>
        """,unsafe_allow_html=True)

hist_button_1= st.button('Construir histograma', key="button1") # crear un botón
        
if hist_button_1: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

hist_button_2 = st.button('Construir grafica de dispersion', key="button2") # crear un botón
        
if hist_button_2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

st.header("Uso de un checkbox")
# crear una casilla de verificación
build_histogram = st.checkbox('Mostrar lo aprendido en el sprint')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write("""
             En este sprint tuvimos las siguientes lecciones:\n
             -Introduccion a las lineas de comando.\n
             -Entorno de desarrollo.\n
             -Git y Github.\n
             -Python intermedio\n
             -Entorno de desarrollo individual
            
            """)
