#!/usr/bin/env python
# coding: utf-8

#app.py
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def app():

    #import data
    df_traffic_reel = pd.read_csv('C:/Users/HP/Downloads/TableRedirects_final.csv')
    del df_traffic_reel['Unnamed: 0']
    df_traffic_reel['TravelYear'] = pd.DatetimeIndex(df_traffic_reel['TravelDay']).year   
    df_traffic_reel['TravelMonth'] = pd.DatetimeIndex(df_traffic_reel['TravelDay']).month

    #filter on sidebar
    st.sidebar.header('FILTERS')

    #filter years
    years = list(df_traffic_reel['TravelYear'].drop_duplicates())
    year_choice = st.sidebar.multiselect('Choose the year(s):', years, default=years)
    df_traffic_reel = df_traffic_reel[df_traffic_reel['TravelYear'].isin(year_choice)]

    #filter destination
    destinations = list(df_traffic_reel['Destination'].drop_duplicates())
    destination_choice = st.sidebar.multiselect('Choose the destination(s):', destinations, default=destinations)
    df_traffic_reel = df_traffic_reel[df_traffic_reel['Destination'].isin(destination_choice)]

    #filter airport
    airports = list(df_traffic_reel['AirportName'].drop_duplicates())
    airport_choice = st.sidebar.multiselect('Choose the airport(s):', airports, default=airports)
    df_traffic_reel = df_traffic_reel[df_traffic_reel['AirportName'].isin(airport_choice)]

    #filter directionality
    directionalities = list(df_traffic_reel['Directionality'].drop_duplicates())
    directionality_choice = st.sidebar.multiselect('Choose the directionality(ies):', directionalities, default=directionalities)
    df_traffic_reel = df_traffic_reel[df_traffic_reel['Directionality'].isin(directionality_choice)]

    st.markdown('## Real Traffic')

    #KPIs
    st.markdown("#### Some KPIs")

    chart_data = pd.DataFrame(df_traffic_reel[["TravelDay","Pax"]].groupby(['TravelDay']).sum().add_suffix('').reset_index())
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Max researches for a day", chart_data["Pax"].max())
    col2.metric("Min researches for a day", chart_data["Pax"].min())
    col3.metric("Mean researches for a day", int(chart_data["Pax"].mean()))

    #chart line by weeks
    st.markdown('#### Researches per day')
    st.markdown("This graph represents the number of ressearches for a day")
    #chart line by days
    chart_data = pd.DataFrame(df_traffic_reel[["TravelDay","Pax"]].groupby(['TravelDay']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="TravelDay", y="Pax",markers=True, labels=dict(TravelDay="Travel Day", Pax="Number of passengers"))
    st.plotly_chart(chart_data)

    #chart line by weeks
    st.markdown('#### Researches per week')
    st.markdown("This graph represents the number of ressearches for a week")
    #chart line by weeks
    chart_data = pd.DataFrame(df_traffic_reel[["NumWeek","Pax"]].groupby(['NumWeek']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="NumWeek", y="Pax",markers=True, labels=dict(NumWeek="Week Number", Pax="Number of passengers"))
    chart_data = chart_data.update_xaxes(range=[1, 53])
    st.plotly_chart(chart_data)

    #chart line by months    
    st.markdown('#### Ressearches per month')
    st.markdown("This graph represents the number of ressearches for a month")
    #chart line by months
    chart_data = pd.DataFrame(df_traffic_reel[["TravelMonth","Pax"]].groupby(['TravelMonth']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="TravelMonth", y="Pax",markers=True, labels=dict(TravelMonth="Month Number", Pax="Number of passengers"))
    chart_data = chart_data.update_xaxes(range=[1, 12])
    st.plotly_chart(chart_data)

    #bar chart airport
    st.markdown("Here, there are filter representations")
    st.markdown('#### Ressearches by Airport')
    chart_data = pd.DataFrame(df_traffic_reel[["AirportName","Pax"]].groupby(['AirportName']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="AirportName", y="Pax", labels=dict(AirportName="Airports", Pax="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    #bar chart destination
    st.markdown('#### Ressearches by Destination')
    chart_data = pd.DataFrame(df_traffic_reel[["Destination","Pax"]].groupby(['Destination']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="Destination", y="Pax", labels=dict(Destination="Destinations", Pax="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    #bar chart directionality
    st.markdown('#### Ressearches by Directinality')
    chart_data = pd.DataFrame(df_traffic_reel[["Directionality","Pax"]].groupby(['Directionality']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="Directionality", y="Pax", labels=dict(Directionality="Directionalities", Pax="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    st.markdown("Here, there are pie charts by events")
    st.markdown('#### Pourcentage by Holidays')

    chart_data1 = pd.DataFrame(df_traffic_reel[["VacancesZoneC","Pax"]].groupby(['VacancesZoneC']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data1, values='Pax', names='VacancesZoneC')
    st.plotly_chart(fig)

    #pie chart by evenent season
    st.markdown('#### Pourcentage by Season')
    chart_data2 = pd.DataFrame(df_traffic_reel[["Saison","Pax"]].groupby(['Saison']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data2, values='Pax', names='Saison')
    st.plotly_chart(fig)

    #pie chart by evenent ferie
    st.markdown("#### Pourcentage by Public Holiday")
    chart_data3 = pd.DataFrame(df_traffic_reel[["Ferie","Pax"]].groupby(['Ferie']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data3, values='Pax', names='Ferie')
    st.plotly_chart(fig)

    #pie chart by evenent weekend
    st.markdown("#### Pourcentage by Weekend")
    chart_data4 = pd.DataFrame(df_traffic_reel[["Weekend","Pax"]].groupby(['Weekend']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data4, values='Pax', names='Weekend')
    st.plotly_chart(fig)