import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Olympics Rank Predictor", page_icon="🏆")

@st.cache_resource
def train_model():
    df = pd.read_csv("Paris 2024 Olympics Medals and Sports by Country.csv", encoding="latin1")

    # If dataset has Rank column
    X = df[["Gold", "Silver", "Bronze"]]
    y = df["Rank"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

st.title("🏆 Olympics Country Rank Predictor")
st.write("Predict Country Rank using Gold, Silver & Bronze medals")

gold = st.number_input("🥇 Gold", min_value=0)
silver = st.number_input("🥈 Silver", min_value=0)
bronze = st.number_input("🥉 Bronze", min_value=0)

if st.button("Predict Rank"):
    rank = round(model.predict([[gold, silver, bronze]])[0])
    st.success(f"🏆 Predicted Rank: {rank}")
