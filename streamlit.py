import os

import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt

tab = st.sidebar.selectbox(
    "Pipeline step",
     ('Scrape', 'Language model')
)

if tab == 'Scrape':

    st.title(tab)

    st.header("# <p> tags found")
    df = pd.read_csv("/data/log-scrape-pipeline.csv")
    fig, ax = plt.subplots()
    df['Time'] = df['Time'].astype('datetime64[s]')
    df.plot(x='Time', y='Count', ax=ax, rot=90)
    st.write(fig)

else:

    st.title(tab)
    
    confusion_path = "/data/confusion-scrape-pipeline.csv"
    examples_path = "/data/wrong-examples-scrape-pipeline.csv"

    st.header("Confusion matrix")
    df = pd.read_csv(confusion_path)
    st.write(df[["0", "1"]])

    # accuracy
    sample_count = df["0"].sum() + df["1"].sum()

    st.write("Accuracy: %.2f%%" % (((df["0"].iloc[0] + df["1"].iloc[1])/sample_count) * 100))
    
    st.header("Example misclassifications")
    df = pd.read_csv(examples_path)
    st.write(df[["Sentence", "Predicted", "Actual"]])

    
