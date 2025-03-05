#Se importan las librerias

import plotly.express as px
import pandas as pd
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Bienvenidos al Proyecto del Sprint7')