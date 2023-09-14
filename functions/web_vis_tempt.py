import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("../data_vis_tempt.txt")
print(df.columns)

figure = px.line(x=df['date'], y=df['temperature'],
				 labels={'x':'Date', 'y':'Temperature(C)'})

st.plotly_chart(figure)
