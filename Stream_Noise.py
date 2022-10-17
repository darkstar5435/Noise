#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def plot():
    
    df = pd.read_csv('Group_noise.csv')

    clist = df["Test"].unique().tolist()

    tests = st.multiselect("Select Test Run", clist)
    #st.header("You selected: {}".format(", ".join(tests)))

    dfs = {Test: df[df["Test"] == Test] for Test in tests}

    fig = go.Figure()
    for Test, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["Frequency"], y=df["Fixtures"], name=Test))

    st.plotly_chart(fig)


plot()






