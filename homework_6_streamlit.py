import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import plotly.express as px
import time




page = st.sidebar.selectbox('Zakładki',['Ankieta','Staty']) 

if page == 'Ankieta':
## Ankieta
    firstname = st.text_input("Podaj imię", "Wpisz tutaj...")
    if st.button("Zapisz imię"):
        result = "Zapisano"
        st.success(result)

    surname = st.text_input("Podaj nazwisko", "Wpisz tutaj...")
    if st.button("Zapisz nazwisko"):
        result = "Zapisano"
        st.success(result)
else:
  data = st.file_uploader("Wczytaj dane csv", type=['csv'])
  if data is not None:
     df = pd.read_csv(data)
     with st.spinner("Jeszcze moment..."):
         time.sleep(3)
     st.success("Gotowe!")
     
     wykres = st.selectbox("Wybierz wykres do wyświetlenia", ("Rozkład zamówień według płci", "Rozkład zamówień według aplikacji klienckiej"))
     st.write("Wybrałeś: ", wykres)
     if wykres == "Rozkład zamówień według płci":
        histogram = px.histogram(df, "gender", labels={"gender": "Gender"}, title="Rozkład zamówień według płci")
        histogram.show()
     else:
        histogram2 = px.histogram(df, "user_agent", labels={"user_agent": "User agent"}, title="Rozkład zamówień według aplikacji klienckiej")
        histogram2.show()
