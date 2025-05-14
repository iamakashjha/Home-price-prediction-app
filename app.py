import streamlit as st
import pickle
import json
import numpy as np

# Load artifacts
with open('server/artifacts/columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]  # assuming first 3 are sqft, bath, bhk

with open('server/artifacts/bengaluru_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

# Streamlit UI
st.set_page_config(page_title="Bangalore Home Price Predictor", layout="centered")
st.title("Bangalore Home Price Prediction")

sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000, step=10)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bath = st.selectbox("Bathrooms", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
location = st.selectbox("Location", sorted(locations))

if st.button("Estimate Price"):
    result = predict_price(location, sqft, bath, bhk)
    st.success(f"Estimated Price: ₹ {result} Lakhs")
