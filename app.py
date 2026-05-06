import streamlit as st
import joblib
import pandas as pd
from datetime import datetime

# Load model
model = joblib.load("mg_model.pkl")

LIME_RATIO = 4.8

st.title("Hot Metal Mg Prediction Model")

# Inputs
hm_wt = st.number_input("HM Weight (tons)", value=160.0)
hm_temp = st.number_input("HM Temperature", value=1350.0)
hm_s = st.number_input("HM Sulfur (%)", value=0.020, format="%.3f")
hm_si = st.number_input("HM Silicon (%)", value=0.500, format="%.3f")
aim_s = st.number_input("Target Sulfur (%)", value=0.003, format="%.3f")

if st.button("Predict"):
    s_removal = hm_s - aim_s
    now = datetime.now()

    data = pd.DataFrame([{
        "HM_WT": hm_wt,
        "HM_TEMP": hm_temp,
        "HM_S": hm_s,
        "HM_SI": hm_si,
        "AIM_S": aim_s,
        "S_REMOVAL": s_removal,
        "HOUR": now.hour,
        "DAY": now.day,
        "MONTH": now.month,
        "S_REMOVAL_PER_TON": s_removal / hm_wt
    }])

    pred_mg = model.predict(data)[0]
    pred_lime = pred_mg * LIME_RATIO
    cost = pred_mg * 300

    st.success(f"Predicted Mg: {pred_mg:.2f} kg")
    st.success(f"Predicted Lime: {pred_lime:.2f} kg")
    st.info(f"Estimated Mg Cost: ₹{cost:,.0f}")