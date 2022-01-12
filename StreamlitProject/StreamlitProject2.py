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

    #IMPORT DATA
    df_traffic_reel = pd.read_csv('C:/Users/HP/Downloads/TableRealTrafic_final.csv')
    del df_traffic_reel['Unnamed: 0']
    df_traffic_reel['TravelYear'] = pd.DatetimeIndex(df_traffic_reel['TravelDay']).year   
    df_traffic_reel['TravelMonth'] = pd.DatetimeIndex(df_traffic_reel['TravelDay']).month

    #FILTER

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

    chart_data = pd.DataFrame(df_traffic_reel[["TravelDay","PaxReel"]].groupby(['TravelDay']).sum().add_suffix('').reset_index())
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Max passengers by day", chart_data["PaxReel"].max())
    col2.metric("Min passengers by day", chart_data["PaxReel"].min())
    col3.metric("Mean passenger by day", int(chart_data["PaxReel"].mean()))

    #CHART LINE BY DAYS
    st.markdown('#### Passengers per day')
    st.markdown("This graph represents the number of passengers by day")
    #chart line by days
    chart_data = pd.DataFrame(df_traffic_reel[["TravelDay","PaxReel"]].groupby(['TravelDay']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="TravelDay", y="PaxReel",markers=True, labels=dict(TravelDay="Travel Day", PaxReel="Number of passengers"))
    st.plotly_chart(chart_data)

    #CHART LINE BY WEEKS
    st.markdown('#### Passengers per week')
    st.markdown("This graph represents the number of passengers by week")
    #chart line by weeks
    chart_data = pd.DataFrame(df_traffic_reel[["NumWeek","PaxReel"]].groupby(['NumWeek']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="NumWeek", y="PaxReel",markers=True, labels=dict(NumWeek="Week Number", PaxReel="Number of passengers"))
    chart_data = chart_data.update_xaxes(range=[1, 53])
    st.plotly_chart(chart_data)

    #CHART LINE BY MONTHS   
    st.markdown('#### Passengers per month')
    st.markdown("This graph represents the number of passengers by month")
    #chart line by months
    chart_data = pd.DataFrame(df_traffic_reel[["TravelMonth","PaxReel"]].groupby(['TravelMonth']).sum().add_suffix('').reset_index())
    chart_data = px.line(chart_data, x="TravelMonth", y="PaxReel",markers=True, labels=dict(TravelMonth="Month Number", PaxReel="Number of passengers"))
    chart_data = chart_data.update_xaxes(range=[1, 12])
    st.plotly_chart(chart_data)

    #BAR CHART AIRPORT
    st.markdown("Here, there are filter representations")
    st.markdown('#### Passengers by Airport')
    chart_data = pd.DataFrame(df_traffic_reel[["AirportName","PaxReel"]].groupby(['AirportName']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="AirportName", y="PaxReel", labels=dict(AirportName="Airports", PaxReel="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    #BAR CHART DESTINATION
    st.markdown('#### Passengers by Destination')
    chart_data = pd.DataFrame(df_traffic_reel[["Destination","PaxReel"]].groupby(['Destination']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="Destination", y="PaxReel", labels=dict(Destination="Destinations", PaxReel="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    #BAR CHART DIRECTIONALITY
    st.markdown('#### Passengers by Directinality')
    chart_data = pd.DataFrame(df_traffic_reel[["Directionality","PaxReel"]].groupby(['Directionality']).sum().add_suffix('').reset_index())
    chart_data = px.bar(chart_data, x="Directionality", y="PaxReel", labels=dict(Directionality="Directionalities", PaxReel="Number of passengers"))
    chart_data = chart_data.update_xaxes(type='category')
    st.plotly_chart(chart_data)

    st.markdown("Here, there are pie charts by events")
    st.markdown('#### Pourcentage by Holidays')


    #PIE CHART BY HOLIDYAS
    chart_data1 = pd.DataFrame(df_traffic_reel[["VacancesZoneC","PaxReel"]].groupby(['VacancesZoneC']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data1, values='PaxReel', names='VacancesZoneC')
    st.plotly_chart(fig)

    #PIE CHART BY SEASON
    st.markdown('#### Pourcentage by Season')
    chart_data2 = pd.DataFrame(df_traffic_reel[["Saison","PaxReel"]].groupby(['Saison']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data2, values='PaxReel', names='Saison')
    st.plotly_chart(fig)

    #PIE CHART BY FERIE
    st.markdown("#### Pourcentage by Public Holiday")
    chart_data3 = pd.DataFrame(df_traffic_reel[["Ferie","PaxReel"]].groupby(['Ferie']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data3, values='PaxReel', names='Ferie')
    st.plotly_chart(fig)

    ##PIE CHART BY WEEKEND
    st.markdown("#### Pourcentage by Weekend")
    chart_data4 = pd.DataFrame(df_traffic_reel[["Weekend","PaxReel"]].groupby(['Weekend']).sum().add_suffix('').reset_index())    
    df = px.data.tips()
    fig = px.pie(chart_data4, values='PaxReel', names='Weekend')
    st.plotly_chart(fig)