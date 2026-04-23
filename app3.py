# app3.py
import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Olympics Rank Predictor",
    page_icon="🏆",
    layout="wide"
)

# --------------------------
# Load Model
# --------------------------
model = pickle.load(open("model3.pkl", "rb"))

# --------------------------
# Country Flags
# --------------------------
flags = {
    "1": "🥇",
    "2": "🥈",
    "3": "🥉",
    "Top 5": "🏅",
    "Top 10": "🎖️",
    "Top 20": "⭐",
    "Other": "🌍"
}

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.big-title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#003366;
}
.sub-title {
    text-align:center;
    color:gray;
    font-size:18px;
}
.box {
    padding:20px;
    border-radius:15px;
    background:#ffffff;
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
}
.rank-box {
    text-align:center;
    font-size:34px;
    font-weight:bold;
    color:green;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# Header
# --------------------------
st.markdown('<p class="big-title">🏆 Olympics Country Rank Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Predict Country Rank using Gold, Silver & Bronze Medals</p>', unsafe_allow_html=True)

st.write("")

# --------------------------
# Inputs
# --------------------------
col1, col2, col3 = st.columns(3)

with col1:
    gold = st.number_input("🥇 Gold Medals", min_value=0, step=1)

with col2:
    silver = st.number_input("🥈 Silver Medals", min_value=0, step=1)

with col3:
    bronze = st.number_input("🥉 Bronze Medals", min_value=0, step=1)

# --------------------------
# Prediction
# --------------------------
if st.button("🔍 Predict Rank", use_container_width=True):

    rank = round(model.predict([[gold, silver, bronze]])[0])

    # Category
    if rank == 1:
        category = "1"
    elif rank == 2:
        category = "2"
    elif rank == 3:
        category = "3"
    elif rank <= 5:
        category = "Top 5"
    elif rank <= 10:
        category = "Top 10"
    elif rank <= 20:
        category = "Top 20"
    else:
        category = "Other"

    emoji = flags[category]

    st.markdown(
        f'<div class="box"><p class="rank-box">{emoji} Predicted Rank: {rank}</p></div>',
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------------
    # Charts Section
    # --------------------------
    chart1, chart2 = st.columns(2)

    with chart1:
        df1 = pd.DataFrame({
            "Medal": ["Gold", "Silver", "Bronze"],
            "Count": [gold, silver, bronze]
        })

        fig1 = px.bar(
            df1,
            x="Medal",
            y="Count",
            title="🏅 Medal Distribution",
            text="Count"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with chart2:
        fig2 = go.Figure(data=[go.Pie(
            labels=["Gold", "Silver", "Bronze"],
            values=[gold, silver, bronze],
            hole=0.45
        )])

        fig2.update_layout(title="📊 Medal Share")
        st.plotly_chart(fig2, use_container_width=True)

    # --------------------------
    # Performance Message
    # --------------------------
    st.write("")

    if rank == 1:
        st.success("🥇 Outstanding Performance! Likely Olympic Champion.")
    elif rank <= 3:
        st.success("🏆 Elite Performance! Podium Finish.")
    elif rank <= 10:
        st.info("🎖️ Strong Global Performance.")
    elif rank <= 20:
        st.warning("⭐ Competitive Performance.")
    else:
        st.error("🌍 Needs More Medals for Better Rank.")

# --------------------------
# Footer
# --------------------------
st.write("---")
st.caption("Developed by Gouri Rotte | Walchand Institute of Technology")