#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px


def app():

    #import dataset
    df= pd.read_excel('C:/Users/HP/Downloads/ByWeekSearchRealTraffic.xlsx')

    #FILTER
    st.sidebar.header('FILTERS')

    #filter years
    years = list(df['Year'].drop_duplicates())
    year_choice = st.sidebar.multiselect('Choose the year(s):', years, default=years)
    df = df[df['Year'].isin(year_choice)]

    #filter destination
    destinations = list(df['Destination'].drop_duplicates())
    destination_choice = st.sidebar.multiselect('Choose the destination(s):', destinations, default=destinations)
    df = df[df['Destination'].isin(destination_choice)]

    #filter airport
    airports = list(df['Airport'].drop_duplicates())
    airport_choice = st.sidebar.multiselect('Choose the airport(s):', airports, default=airports)
    df = df[df['Airport'].isin(airport_choice)]

    #filter directionality
    directionalities = list(df['Directionality'].drop_duplicates())
    directionality_choice = st.sidebar.multiselect('Choose the directionality(ies):', directionalities, default=directionalities)
    df = df[df['Directionality'].isin(directionality_choice)]


    st.markdown('## Comparative Real Air Traffic / Skyscanner Searches')
    st.markdown("### - By weeks")
    df['diff'] = df['RealTraffic/RealTraffic2019'] - df['Searches/Searches2019']
    
    #KPIs
    st.markdown("#### Some KPIs")
    st.markdown('The percentage difference between the number of searches for a travel date and the number of passengers for that travel date')

    chart_data = pd.DataFrame(df[["NumWeek","diff"]].groupby(['NumWeek']).sum().add_suffix('').reset_index())
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean (en %)", round(chart_data["diff"].mean(),2))
    col2.metric("Max (en %)", round(chart_data["diff"].max(),2))
    col3.metric("Min (en %)", round(chart_data["diff"].min(),2))

    #chart line by weeks
    st.markdown('#### Real Air Traffic - Skyscanner Searches compared to Real Air Traffic - Skyscanner Searches 2019 ')
    #chart line by days
    chart_data = pd.DataFrame(df[["NumWeek","RealTraffic/RealTraffic2019","Searches/Searches2019","RealTraffic-Searches 2019"]].groupby(['NumWeek']).mean().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={"RealTraffic/RealTraffic2019": "Real Traffic compared to 2019 Real Air Traffic", "Searches/Searches2019": "Searches compared to 2019 Searches", "RealTraffic-Searches 2019" : "Real Traffic and Searches 2019"})
    chart_data = px.line(chart_data, x="NumWeek", y=["Real Traffic compared to 2019 Real Air Traffic","Searches compared to 2019 Searches","Real Traffic and Searches 2019"], labels=dict(NumWeek="Week Travel"))
    chart_data = chart_data.update_xaxes(range=[1, 53])
    chart_data = chart_data.update_layout(legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01))
    st.plotly_chart(chart_data)


    st.markdown("### - By months")
    df1= pd.read_excel('C:/Users/HP/Downloads/searchdirectsmonth.xlsx')

    #KPIs
    st.markdown("#### Some KPIs")
    st.markdown('The percentage difference between the number of searches for a travel date and the number of passengers for that travel date')

    df1['diff'] = df1['RealTraffic%2019ByMonth'] - df1['Searches%2019ByMonth']
    chart_data = pd.DataFrame(df1[["Month","diff"]].groupby(['Month']).sum().add_suffix('').reset_index())
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean (en %)", round(chart_data["diff"].mean(),2))
    col2.metric("Max (en %)", round(chart_data["diff"].max(),2))
    col3.metric("Min (en %)", round(chart_data["diff"].min(),2))

    #chart line by weeks
    st.markdown('#### Real Air Traffic - Skyscanner Searches compared to Real Air Traffic - Skyscanner Searches 2019 ')
    #chart line by days
    chart_data = pd.DataFrame(df1[["Month","RealTraffic%2019ByMonth","Searches%2019ByMonth","Total Real Traffic / Searches 2019"]].groupby(['Month']).mean().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={"RealTraffic%2019ByMonth": "Real Traffic compared to 2019 Real Air Traffic", "Searches%2019ByMonth": "Searches compared to 2019 Searches", "Total Real Traffic / Searches 2019" : "Real Traffic and Searches 2019"})
    chart_data = px.line(chart_data, x="Month", y=["Real Traffic compared to 2019 Real Air Traffic","Searches compared to 2019 Searches","Real Traffic and Searches 2019"], labels=dict(Month="Month Travel"))
    chart_data = chart_data.update_xaxes(range=[1, 12])
    chart_data = chart_data.update_layout(legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01))
    st.plotly_chart(chart_data)



    st.markdown("### - By holidays")

    df1= pd.read_excel('C:/Users/HP/Downloads/Searchesdirectsholidays.xlsx')
    df1['diff'] = df1['Real Traffic'] - df1['Searches']
    
    #KPIs
    st.markdown("#### Some KPIs")
    st.markdown('The percentage difference between the number of searches for a travel date and the number of passengers for that travel date')

    chart_data = pd.DataFrame(df1[["VacancesZoneC","diff"]].groupby(['VacancesZoneC']).sum().add_suffix('').reset_index()) 
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean (en %)", round(chart_data["diff"].mean(),2))
    col2.metric("Max (en %)", round(chart_data["diff"].max(),2))
    col3.metric("Min (en %)", round(chart_data["diff"].min(),2))

    #chart line by weeks
    st.markdown('#### Real Air Traffic - Skyscanner Searches compared to Real Air Traffic - Skyscanner Searches 2019 ')
    #chart line by days
    chart_data = pd.DataFrame(df1[["VacancesZoneC","Real Traffic","Searches","Total Real Traffic / Searches 2019"]].groupby(['VacancesZoneC']).mean().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={"Real Traffic": "Real Traffic compared to 2019 Real Air Traffic", "Searches": "Searches compared to 2019 Searches", "Total Real Traffic / Searches 2019" : "Real Traffic and Searches 2019"})
    chart_data = px.line(chart_data, x="VacancesZoneC", y=["Real Traffic compared to 2019 Real Air Traffic","Searches compared to 2019 Searches","Real Traffic and Searches 2019"], labels=dict(VacancesZoneC="Holidays Travel"))
    chart_data = chart_data.update_layout(legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01))
    st.plotly_chart(chart_data)
    

    






