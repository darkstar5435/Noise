#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title('Noise Management - Analysis')

@st.cache
def load_data(nrows):
    data = pd.read_csv('Group_noise.csv', nrows=nrows)
    return data

noise_data = load_data(2000)
#Noise_Demand Data
st.subheader('Noise Test Data')
st.write(noise_data)    

def plot():
    
    #df = pd.read_csv('Group_noise.csv')
    df = noise_data

    clist = df["Test"].unique().tolist()

    tests = st.multiselect("Select Test Run", clist)
    #st.header("You selected: {}".format(", ".join(tests)))

    dfs = {Test: df[df["Test"] == Test] for Test in tests}

    fig = go.Figure()
    for Test, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["Frequency"], y=df["Fixtures"], name=Test))
        fig.update_layout(autosize=False, width=500, height=500)

    st.plotly_chart(fig)




plot()





