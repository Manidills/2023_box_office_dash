import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt


def explore():
    antman = pd.read_csv('data/antman.csv')
    avatar = pd.read_csv('data/avatar.csv')
    bear = pd.read_csv('data/cocaine_bear.csv')
    megan = pd.read_csv('/home/dills/Downloads/papers/The_Whales_of_Near/data/megan.csv')

    option = st.radio(
    'Select to explore about recent movies',
    ('All','Avatar', 'Ant-Man', 'Cocaine-bear', 'Megan'),horizontal=True)

    if option == 'Avatar':
        st.dataframe(avatar)
        avatar.drop(avatar.index[:16], inplace=True)
        avatar["Daily"] = pd.to_numeric(avatar['Daily'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        avatar["Avg"] = pd.to_numeric(avatar['Avg'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        avatar['Date'] = avatar['Date'].apply((lambda x: str(x)[:6]))
        avatar['Date'] = avatar['Date'].str.replace('N','')
        avatar['Date'] = avatar['Date'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
        avatar["Date"] = pd.to_datetime(avatar.Date) + pd.offsets.DateOffset(years=123)

        st.markdown("##")
        st.write("""   
        ####  Daily Volume ####  """)
        st.markdown("##")   

        bar_chart = alt.Chart(avatar).mark_area(color='white').encode(
            x='Date',
            y='Daily')

        # display chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

        st.markdown('##')
        st.write("""   
        ####  DOW AVG Volume ####  """)
        st.markdown("##") 
        st.altair_chart(alt.Chart(avatar).mark_line().encode(
            x='Date',
            y='Avg',
            color='DOW',
            strokeDash='DOW',
        ),use_container_width=True)

    elif option == 'Ant-Man':
        st.dataframe(antman)
        antman["Daily"] = pd.to_numeric(antman['Daily'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        antman["Avg"] = pd.to_numeric(antman['Avg'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        antman['Date'] = antman['Date'].apply((lambda x: str(x)[:6]))
        antman['Date'] = antman['Date'].str.replace('N','')
        antman['Date'] = antman['Date'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
        antman["Date"] = pd.to_datetime(antman.Date) + pd.offsets.DateOffset(years=123)

        st.markdown("##")
        st.write("""   
        ####  Daily Volume ####  """)
        st.markdown("##")   

        bar_chart = alt.Chart(antman).mark_area(color='white').encode(
            x='Date',
            y='Daily')

        # display chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

        st.markdown('##')
        st.write("""   
        ####  DOW AVG Volume ####  """)
        st.altair_chart(alt.Chart(antman).mark_line().encode(
            x='Date',
            y='Avg',
            color='DOW',
            strokeDash='DOW',
        ),use_container_width=True)
    
    elif option == 'Cocaine-bear':
        st.dataframe(bear)
        bear["Daily"] = pd.to_numeric(bear['Daily'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        bear["Avg"] = pd.to_numeric(bear['Avg'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        bear['Date'] = bear['Date'].apply((lambda x: str(x)[:6]))
        bear['Date'] = bear['Date'].str.replace('N','')
        bear['Date'] = bear['Date'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
        bear["Date"] = pd.to_datetime(bear.Date) + pd.offsets.DateOffset(years=123)

        st.markdown("##")
        st.write("""   
        ####  Daily Volume ####  """)
        st.markdown("##")   

        bar_chart = alt.Chart(bear).mark_area(color='white').encode(
            x='Date',
            y='Daily')

        # display chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)
    
    elif option == 'Megan':
        st.dataframe(megan)
        megan["Daily"] = pd.to_numeric(megan['Daily'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        megan["Avg"] = pd.to_numeric(megan['Avg'].str.replace('[\$,-]', '', regex=True), errors='coerce')
        megan['Date'] = megan['Date'].apply((lambda x: str(x)[:6]))
        megan['Date'] = megan['Date'].str.replace('N','')
        megan['Date'] = megan['Date'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
        megan["Date"] = pd.to_datetime(megan.Date) + pd.offsets.DateOffset(years=123)

        st.markdown("##")
        st.write("""   
        ####  Daily Volume ####  """)
        st.markdown("##")   

        bar_chart = alt.Chart(megan).mark_area(color='white').encode(
            x='Date',
            y='Daily')

        # display chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

        st.markdown('##')
        st.write("""   
        ####  AVG Volume ####  """)
        st.altair_chart(alt.Chart(megan).mark_line().encode(
            x='Date',
            y='Avg',
            color='DOW',
            strokeDash='DOW',
        ),use_container_width=True)

        
    elif option == 'All':
        st.markdown("##")
        st.write("""   
            #### 2023 Box-office ####  """)
        st.markdown("##")
        st.dataframe(pd.read_csv('data/numbers_box.csv'))