import streamlit as st

title = st.title("Weather Forecast for the NExt Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
subhead = st.subheader(f"{option} for the next {days} days in {place}")