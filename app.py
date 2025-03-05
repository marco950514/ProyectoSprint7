#Se importan las librerias

import plotly.express as px
import pandas as pd
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Bienvenidos al Proyecto del Sprint7')

hist_button_1= st.button('Construir histograma') # crear un botón
        
if hist_button_1: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

hist_button_2 = st.button('Construir histograma') # crear un botón
        
if hist_button_2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)