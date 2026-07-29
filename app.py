# ======================================================
# 🔐 AI-BASED IDS (CICIoT2023) - FULL STREAMLIT APP
# ======================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI IDS System", layout="wide")

st.title("🔐 AI-Based Intrusion Detection System (Explainable AI)")
st.write("Detect cyber attacks in IoT network traffic using Machine Learning + SHAP")

# =========================
# LOAD ARTIFACTS
# =========================
model = joblib.load("model/ids_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# load dataset for structure
df_sample = pd.read_csv("datasets/train.csv")
feature_names = df_sample.drop("label", axis=1).columns

# =========================
# SIDEBAR MODE SELECTION
# =========================
st.sidebar.title("⚙️ Mode Selection")
mode = st.sidebar.radio("Choose Input Mode:", ["Manual Input", "Upload CSV File"])

# ======================================================
# 🟢 MANUAL INPUT MODE
# ======================================================
if mode == "Manual Input":

    st.subheader("✍️ Enter Network Features")

    user_input = []

    for feature in feature_names:
        val = st.sidebar.number_input(f"{feature}", value=0.0)
        user_input.append(val)

    input_array = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    if st.button("🚀 Predict Attack"):

        prediction = model.predict(input_scaled)
        proba = model.predict_proba(input_scaled)

        label = label_encoder.inverse_transform(prediction)[0]

        st.subheader("📌 Result")

        if "Normal" in str(label):
            st.success(f"🟢 Normal Traffic Detected: {label}")
        else:
            st.error(f"🔴 Attack Detected: {label}")

        st.write("### 🔢 Confidence Scores")
        st.bar_chart(proba[0])

        # ================= SHAP =================
        st.subheader("🧠 Explainable AI (SHAP)")

        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_scaled)

        fig, ax = plt.subplots()
        shap.summary_plot(
            shap_values,
            input_scaled,
            feature_names=feature_names,
            show=False
        )

        st.pyplot(plt.gcf())

# ======================================================
# 🟡 CSV UPLOAD MODE (REAL IDS SIMULATION)
# ======================================================
elif mode == "Upload CSV File":

    st.subheader("📂 Upload Network Traffic File")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:

        data = pd.read_csv(uploaded_file)

        st.write("### 📊 Uploaded Data Preview")
        st.dataframe(data.head())

        # check missing columns
        missing_cols = set(feature_names) - set(data.columns)

        if missing_cols:
            st.error(f"Missing columns: {missing_cols}")

        else:
            X = data[feature_names]
            X_scaled = scaler.transform(X)

            preds = model.predict(X_scaled)
            labels = label_encoder.inverse_transform(preds)

            data["Prediction"] = labels

            st.write("### 🔍 Detection Results")
            st.dataframe(data)

            # ================= SUMMARY =================
            st.subheader("📊 Summary")

            normal_labels = ["Normal", "BENIGN", "Benign"]

            attack_count = sum(label not in normal_labels for label in labels)
            normal_count = sum(label in normal_labels for label in labels)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("🟢 Normal Traffic", normal_count)

            with col2:
                st.metric("🔴 Attacks Detected", attack_count)

            st.bar_chart(pd.Series(labels).value_counts())

# ======================================================
# 📌 DATASET PREVIEW
# ======================================================
if st.checkbox("📊 Show Dataset Preview"):
    st.dataframe(df_sample.head())

# ======================================================
# ℹ️ MODEL INFO
# ======================================================
if st.checkbox("ℹ️ Model Information"):
    st.write("✔ Model: Random Forest Classifier")
    st.write("✔ Dataset: CICIoT2023")
    st.write("✔ Task: Multi-class Intrusion Detection (IDS)")
    st.write("✔ Explainability: SHAP (TreeExplainer)")