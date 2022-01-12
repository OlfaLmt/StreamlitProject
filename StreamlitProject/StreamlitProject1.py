#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px


df_traffic_reel = pd.read_csv('C:/Users/HP/Downloads/TableRealTrafic_final.csv')
del df_traffic_reel['Unnamed: 0']

dataset = st.container()

def app():
    st.markdown('## Application of parisian air trafic analysis 🛪')
    st.markdown('#### Data visualisation of parisian air traffic (CDG and ORY) and searches done with the Skyscanner flight comparator.  ')
    st.markdown('We will study in this project the air traffic data of Parisian airports to and from destinations such as: North Africa, Central and South America, North America, Other Africa, Other Europe, Dom-Tom, Far East, France, Middle East, Schengen and EU')
    st.markdown('In parallel we will study the searches made with the flight comparator Skyscanner on Paris airports to and from destinations such as North Africa, Central and South America, North America, Other Africa, Other Europe, Dom-Tom, Far East, France, Middle East, Schengen and EU')
    st.markdown('This study focuses on data from the beginning of 2019 until the end of 2021.')
    st.markdown('We will then analyze this data to verify that actual traffic correlates with searches made on Skyscanner.')

    df_traffic_reel = pd.read_csv('C:/Users/HP/Downloads/TableRealTrafic_final.csv')
    del df_traffic_reel['Unnamed: 0']
    st.markdown('#### Real Traffic')
    st.markdown("Here are the first 5 rows of the dataset representing the trafic made for a travel date according to the airport, the direction and the destination. We will have information such as the weekend, a holiday, the season for each date of travel.")
    st.write(df_traffic_reel.head())

    df_traffic_redirects = pd.read_csv('C:/Users/HP/Downloads/TableRedirects_final.csv')
    del df_traffic_redirects['Unnamed: 0']
    st.markdown('#### Skyscanner Searches')
    st.markdown("Here are the first 5 rows of the dataset representing the searches made for a travel date according to the airport, the direction and the destination. We will have information such as the weekend, a holiday, the season for each date of travel. We will know here the number of searches that there were according to the date of search and the date of travel.")
    st.write(df_traffic_redirects.head())