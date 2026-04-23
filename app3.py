import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Olympics Rank Predictor", page_icon="🏆", layout="wide")

# Load model
@st.cache_resource
def load_model():
    with open("model3.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# Title
st.title("🏆 Olympics Country Rank Predictor")
st.write("Predict Country Rank using Gold, Silver & Bronze Medals")

# Inputs
col1, col2, col3 = st.columns(3)

with col1:
    gold = st.number_input("🥇 Gold", min_value=0)

with col2:
    silver = st.number_input("🥈 Silver", min_value=0)

with col3:
    bronze = st.number_input("🥉 Bronze", min_value=0)

# Predict
if st.button("🔍 Predict Rank"):
    rank = round(model.predict([[gold, silver, bronze]])[0])

    st.success(f"🏆 Predicted Country Rank: {rank}")

    if rank == 1:
        st.balloons()
        st.success("🥇 Olympic Champion!")
    elif rank <= 3:
        st.success("🏅 Podium Finish")
    elif rank <= 10:
        st.info("🎖️ Top 10 Country")
    elif rank <= 20:
        st.warning("⭐ Competitive Rank")
    else:
        st.error("🌍 Lower Rank")

st.write("---")
st.caption("Developed by Gouri Rotte")
