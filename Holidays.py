# Libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def holiday():
    st.markdown("##")

    st.write("""   
        #### 2023 Holiday Numbers ####  """)


    holiday = pd.read_csv('data/holidays.csv')

    st.dataframe(holiday)


    season = pd.read_csv('data/season_box.csv')

    season["Average"] = pd.to_numeric(season['Average'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    season["Gross"] = pd.to_numeric(season['Gross'].str.replace('\$,-]', '', regex=True), errors='coerce')
    season["Cumulative Gross"] = pd.to_numeric(season['Cumulative Gross'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    season['Year'] = pd.to_datetime(season.Year, format='%Y')


    st.markdown("##")

    st.write("""   
        #### Yearly Seasonal Average Numbers ####  """)
    line_ = alt.Chart(season).mark_area(color='green').encode(
        x='Year',
        y='Average')


    st.altair_chart(line_, use_container_width=True)


    st.markdown("##")

    st.write("""   
        #### Yearly Seasonal Cumulative Gross ####  """)
    line_ = alt.Chart(season).mark_line(color='red').encode(
        x='Year',
        y='Cumulative Gross')


    st.altair_chart(line_, use_container_width=True)


    a, b = st.columns([2,2])

    with a:

        st.markdown("##")

        st.write("""   
            #### Top Movies By Year ####  """)

        st.dataframe(season[['Year','#1 Release']])

    with b:

        st.markdown("##")

        st.write("""   
            #### Recent Yearly Releases ####  """)

        st.dataframe(season[['Year','Releases']])