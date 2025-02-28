import streamlit as st
import pandas as pd
from plotly import express as px
def main():
    # create rows and columns
    
    st.title('Streamlit Dashboard')
    st.write('This is a Streamlit dashboard')

    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
    st.dataframe(df)
    # st.table(df)
    st.bar_chart(df, x = "continent", y = "population")


    slider = st.slider('Select a range of data', 0, len(df))
    st.write('You selected:', slider)

    filtered_df = df.iloc[:slider]
    fig = px.scatter(filtered_df, x = "gdp per capita", y = "life expectancy", size = "population", color = "continent", hover_name = "country", log_x = True, size_max = 60)
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()