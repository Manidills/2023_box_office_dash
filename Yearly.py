# Libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt


def yearly():
    yearly_df = pd.read_csv("data/yearly_movie_box.csv")
    yearly_df_all = pd.read_csv('data/yearly_movie_box_all.csv')

    yearly_df_all['Open'] = yearly_df_all['Open'].apply((lambda x: str(x)[:6]))
    yearly_df_all["Gross"] = pd.to_numeric(yearly_df_all['Gross'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    yearly_df_all["Open Th"] = pd.to_numeric(yearly_df_all['Open Th'].str.replace('[,-]', '', regex=True), errors='coerce')
    yearly_df_all["Opening"] = pd.to_numeric(yearly_df_all['Opening'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    yearly_df_all['Open'] = yearly_df_all['Open'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
    yearly_df_all["Open"] = pd.to_datetime(yearly_df_all.Open) + pd.offsets.DateOffset(years=123)


    st.markdown("##")

    st.write("""   
        #### Yearly Numbers ####  """)
    st.dataframe(yearly_df_all)

    st.markdown("##")
    st.write("""   
        #### Yearly Gross ####  """)
    st.markdown("##")
    st.altair_chart(
            alt.Chart(yearly_df_all).mark_bar(color='blue').encode(
                x='Open:T',
                y="Gross",
                color='Release')
            ,use_container_width=True)





    a, b = st.columns([6,2])

    with a:
        st.markdown("##")
        st.write("#### Yearly Overall Gross By Distribution ####")
        pie = alt.Chart(yearly_df_all).mark_arc(innerRadius=80, color='red').encode(
        theta=alt.Theta(field="Gross",  type="quantitative"),
        color=alt.Color(field="Distributor"),
        )
        st.altair_chart(pie,use_container_width=True) 

        bar = alt.Chart(yearly_df_all).mark_bar().encode(
        x='Open',
        y='Opening'
    )

    with b:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.write(' Disney and Universal Picture starting 2023 with a BANG !!!!!. Still have time for Warner bros, Paramount and Lionsgate to take over the 2023 market bcz they have good line ups of flims. Quite rare to see "Yash Raj" doing quite well over weeks')


    st.markdown("##")
    st.write("#### 2023 Opening ####")
    st.markdown("##")

    st.altair_chart(alt.Chart(yearly_df_all).mark_bar(opacity=0.7).encode(
        x='Open',
        y=alt.Y('Opening:Q', stack=None),
        color=alt.Color('Release', legend=None),
    ),use_container_width=True) 

    a, b = st.columns([2,2])

    with a:
        st.markdown("##")
        st.write("#### 2023 TOP 5 Opening ####")
        st.markdown("##")
        st.dataframe(yearly_df_all[['Opening','Release']].head(5))

    with b:
        st.markdown("##")
        st.write("#### 2023 TOP 5 Gross ####")
        st.markdown("##")
        st.dataframe(yearly_df_all[['Gross','Release']].head(5))


    st.markdown("##")
    st.write("#### Opening Day Cinema hall Numbers ####")
    st.markdown("##")

    st.altair_chart(alt.Chart(yearly_df_all).mark_bar(opacity=0.7).encode(
        x='Open',
        y=alt.Y('Open Th:Q', stack=None),
        color='Release',
    ),use_container_width=True) 