# Libraries
from Weekly import weekend
from Yearly import yearly
from Holidays import holiday
from explore import explore
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu


# Layout
st.set_page_config(page_title="4M",
    page_icon="chart_with_upwards_trend",layout="wide")

IMAGE = "https://media.tenor.com/eum1UC4F4nAAAAAi/hollywood-famous.gif"

a, b,c = st.columns([1,2,1])
a.image(IMAGE, width=200)
b.title("HOLLYBox\nEasy Insights to The 2023 Domestic Box office.")
c.image("https://media.tenor.com/j1YBvHkmoc4AAAAi/spesh-special.gif",width=100)
st.markdown("##")
st.markdown("##")

option = option_menu("HollyBox", ['Daily','Weekend', 'Holiday/Season','Yearly','Explore'], 
    icons=['house'], menu_icon="cast", default_index=0, orientation="horizontal")



if option == 'Daily':
    daily_df = pd.read_csv("data/convertcsv.csv")



    daily_df["Top 10 Gross"] = pd.to_numeric(daily_df['Top 10 Gross'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    daily_df["Gross"] = pd.to_numeric(daily_df['Gross'].str.replace('[\$,-]', '', regex=True), errors='coerce')
    daily_df['Date'] = daily_df['Date'].apply((lambda x: str(x)[:6]))
    daily_df['Date'] = daily_df['Date'].apply((lambda x: datetime.datetime.strptime(x, '%b %d')))
    daily_df["Date"] = pd.to_datetime(daily_df.Date) + pd.offsets.DateOffset(years=123)


    st.write("""   
    #### Daily Box Office For 2023 ####  """)
    st.dataframe(daily_df)
    st.markdown("##")

    a, b = st.columns([6,2])

    with a:
        st.write("""   
        #### #1 Release Gross ####  """)
        st.markdown("#")
        st.altair_chart(
        alt.Chart(daily_df).mark_bar().encode(
            x='Date',
            y='Gross',
            color='#1 Release'
        ),
        use_container_width=True
    )

    with b:
        #grouped = daily_df.groupby('#1 Release')['Gross'].sum().reset_index()
        st.markdown("##")
        st.markdown("##")
        st.write(
            '''
            According to the report, "Avatar" is still doing well in 2023, even with the addition of another big name ("Antman"). Ant-Man started the day with $46M and is currently on a roll. Even though the "cocaine bear" who left a footprint at 8M on opening day was a surprise find.
            
            '''
        )

    a, b = st.columns([2,6])

    with a:
        st.markdown("##")
        st.markdown("##")
        st.write(
            """
                In 2023, we can say kinda avergely 30-35 releases happing per day.
            """
        )

    with b:
        st.markdown("##")
        st.write("""   
        #### Number Of Releases ####  """)
        st.markdown("##")
        bar_chart = alt.Chart(daily_df).mark_area(
            line={'color':'darkgreen'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='black', offset=0),
                alt.GradientStop(color='yellow', offset=1)],
            x1=1,
            x2=1,
            y1=1,
            y2=0
        )).encode(
        x='Date',
        y='Releases')

        # display chart in Streamlit
        st.altair_chart(bar_chart, use_container_width=True)


    a, b = st.columns([6,2])

    with a:
        st.write("""   
        #### Top 10 Gross Based On Days ####  """)
        st.markdown("#")
        grouped_week =  daily_df.groupby('Day')['Top 10 Gross'].sum().reset_index()
        st.altair_chart(
        alt.Chart(daily_df).mark_bar(color='white').encode(
            x='Day',
            y='Top 10 Gross',
            
        ),
        use_container_width=True
    )

    with b:
        #grouped = daily_df.groupby('#1 Release')['Gross'].sum().reset_index()
        st.markdown("##")
        st.markdown("##")
        st.write(
            '''
                Friday and saturday contributes to more numbers comparing with other days, thats expected.
            
            '''
        ) 

    st.markdown("##")
    st.write("""   
    #### Top 10 Gross Based On Daily Volume ####  """)
    st.markdown("##")   

    bar_chart = alt.Chart(daily_df).mark_area(color='#ae2b29').encode(
        x='Date',
        y='Top 10 Gross')

    # display chart in Streamlit
    st.altair_chart(bar_chart, use_container_width=True)



elif option == 'Weekend':
    weekend()
elif option == 'Holiday/Season':
    holiday()
elif option == 'Yearly':
    yearly()
elif option == 'Explore':
    explore()



st.write(""" ## Sources ## """)


st.info (
    """ 
    1. Boxofficemojo
    2. The Numbers
    3. IMDB
    4. themoviedb
    """
)