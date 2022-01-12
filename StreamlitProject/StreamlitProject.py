#!/usr/bin/env python
# coding: utf-8

#app.py
import StreamlitProject1
import StreamlitProject2
import StreamlitProject3
import StreamlitProject4
import streamlit as st

PAGES = {
    "Homepage": StreamlitProject1,
    "Real Air Traffic": StreamlitProject2,
    "Skyscanner Searches": StreamlitProject3,
    "Real Traffic vs Searches ": StreamlitProject4
}

st.sidebar.markdown('### MSc Data Management | Olfa LAMTI')
st.sidebar.markdown('###### GitHub | https://github.com/OlfaLmt')
st.sidebar.markdown('###### LinkedIn | https://linkedin.com/in/olfa-lamti-334b95160')

st.sidebar.header('CONTENTS')
selection = st.sidebar.selectbox("", list(PAGES.keys()))
page = PAGES[selection]
page.app()