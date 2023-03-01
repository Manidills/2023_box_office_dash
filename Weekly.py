# Libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt



# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def weekend():
    weekend_df = pd.read_csv("data/weekly_box.csv")
    weekly_df = pd.read_csv('data/weekend_box.csv')

    weekend_df['Dates'] = weekend_df['Dates'].apply((lambda x: str(x)[:9]))
    weekend_df["Overall Gross"] = pd.to_numeric(weekend_df['Overall Gross'].str.replace('[\$,-]', '', regex=True), errors='coerce')

    st.markdown("##")

    st.write("""   
        #### Weekend Numbers ####  """)
    st.dataframe(weekend_df)
    a, b = st.columns([6,2])

    with a:
        st.markdown("##")
        st.write("#### Weekend Overall Gross Distribution ####")
        pie = alt.Chart(weekend_df).mark_arc(innerRadius=80, color='red').encode(
        theta=alt.Theta(field="Overall Gross",  type="quantitative"),
        color=alt.Color(field="Dates"),
        )
        st.altair_chart(pie,use_container_width=True)

        

    with b:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.write(' It shows there is high volume happened between FEB 17 - 23 ( ANTMAN ) ')


    st.markdown("#")
    st.write("#### #1 Releases Overall Weekend Gross ####")
    st.markdown("#")

    bars = alt.Chart(weekend_df).mark_bar(color='blue').encode(
    x='Dates',
    y="Overall Gross",
    color='#1 Release')
    st.altair_chart(bars, use_container_width=True)

    st.markdown("#")
    st.write("#### Weekly Report ####")
    st.markdown("#")

    st.dataframe(weekly_df)