import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hi Streamlit")

## Display a Simple Text
st.write("Welcome to the Streamlit Tutorial")

## Display a DataFrame
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here is the Dataframe")
st.write(df)

## Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)