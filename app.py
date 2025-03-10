import datetime
import streamlit as st
import requests


'''
# TaxiFareModel front
'''


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


date = st.date_input("Date")
time = st.time_input("Time (HH:MM:SS)")
pickup_longitude = st.slider("Pickup Longitude", min_value=-180.0, max_value=180.0, value=0.0)
pickup_latitude = st.slider("Pickup Latitude", min_value=-90.0, max_value=90.0, value=0.0)
dropoff_longitude = st.slider("Dropoff Longitude", min_value=-180.0, max_value=180.0, value=0.0)
dropoff_latitude = st.slider("Dropoff Latitude", min_value=-90.0, max_value=90.0, value=0.0)
passenger_count = st.slider("Passenger Count", min_value=1, max_value=8, value=1)

pickup_datetime = f"{date} {time}"
st.write(pickup_datetime)

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
st.write(response.url)
st.write(response.status_code)
st.write(f"{params}")

if response.status_code == 200:
    prediction = response.json()
    st.write(f"Predicted fare: ${prediction['fare']:.2f}")
else:
    st.write("Error: Unable to retrieve prediction. Please try again later.")
