import streamlit as st
import requests
import datetime


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
# Input controllers
date = st.date_input("Date", datetime.date.today())
time = st.time_input("Time", datetime.datetime.now().time())
pickup_longitude = st.number_input("Pickup Longitude", value=0.0)
pickup_latitude = st.number_input("Pickup Latitude", value=0.0)
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0)
dropoff_latitude = st.number_input("Dropoff Latitude", value=0.0)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

# Convert date and time to string
pickup_datetime = f"{date} {time}"

# Build dictionary for API request
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# Call API
response = requests.get(url, params=params)
prediction = response.json()

# Display prediction
st.write(f"Predicted fare: ${prediction['fare']:.2f}")
