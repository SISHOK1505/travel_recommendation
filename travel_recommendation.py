# -*- coding: utf-8 -*-
"""travel_recommendation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nhL9hLaRbsF1UeLz6UaIlXyh0pe7X-57
"""

# Imports for clustering
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import seaborn as sns
from sklearn.cluster import KMeans

# Load the DataFrame from the specified URL
df_url = "https://raw.githubusercontent.com/SISHOK1505/travel_recommendation/24fae3460046f0862d77de0e82a9ff588a8dfe0e/locations.csv"
df = pd.read_csv(df_url)

# Perform clustering on the DataFrame
country = 'India'
city_names = df['location']

longitude = []
latitude = []
geolocator = Nominatim(user_agent="Trips")

for c in city_names.values:
    location = geolocator.geocode(c + ',' + country)
    latitude.append(location.latitude)
    longitude.append(location.longitude)

df['Latitude'] = latitude
df['Longitude'] = longitude

kmeans = KMeans(5)
l2 = df[['Latitude', 'Longitude']].values
kmeans.fit(l2)
identified_clusters = kmeans.predict(l2)
df['loc_clusters'] = identified_clusters

# Save the KMeans model as 'kmeans.h5' using joblib
import joblib
joblib.dump(kmeans, 'kmeans.h5')

# Streamlit integration
import streamlit as st
import joblib  # If your model is saved using joblib
joblib.dump(kmeans, 'kmeans.h5')

# Create a Streamlit app title
st.title("Machine Learning Model Integration")

# Create input elements for user interaction
user_input = st.text_input("Enter input data:")
prediction_button = st.button("Predict")

# Define a function to make predictions
def make_prediction(user_input):
    try:
        # Preprocess user input if necessary
        # Use the loaded machine learning model to make predictions
        prediction = model.predict([user_input])  # Replace with your model prediction logic
        return prediction
    except Exception as e:
        return str(e)

# Display the prediction result when the "Predict" button is clicked
if prediction_button:
    if user_input:
        result = make_prediction(user_input)
        st.write(f"Prediction: {result}")
    else:
        st.warning("Please enter input data.")

# Additional content or explanations can be added here

