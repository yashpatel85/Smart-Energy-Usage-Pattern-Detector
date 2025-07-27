# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predict import detect_anomalies

st.set_page_config(page_title="Smart Energy Pattern Detector", layout="wide")

st.title("⚡ Smart Energy Usage Pattern Detector")

uploaded_file = st.file_uploader("📂 Upload your energy data CSV", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("🔍 Raw Uploaded Data")
        st.dataframe(df.head())

        with st.spinner("🔎 Running anomaly detection..."):
            numeric_df = df.select_dtypes(include=['float64', 'int64'])
            results = detect_anomalies(numeric_df)

        # Add timestamp back to results if it exists in original df
        if 'timestamp' in df.columns:
            results['timestamp'] = pd.to_datetime(df['timestamp'])

        st.subheader("📉 Anomaly Detection Results")
        st.dataframe(results)

        # Display metrics
        anomaly_count = results['anomaly'].value_counts().to_dict()
        st.metric("📊 Total Records", len(results))
        st.metric("✅ Normal", anomaly_count.get(1, 0))
        st.metric("🚨 Anomalies", anomaly_count.get(-1, 0))

        # Optional: Line plot with anomalies marked
        if 'timestamp' in results.columns:
            st.subheader("📍 Anomaly Visualization")

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(results['timestamp'], results['usage'], label='Usage', color='blue')

            anomalies = results[results['anomaly'] == -1]
            ax.scatter(anomalies['timestamp'], anomalies['usage'], color='red', label='Anomalies')

            ax.set_xlabel('Timestamp')
            ax.set_ylabel('Energy Usage')
            ax.legend()
            ax.grid(True)

            st.pyplot(fig)
        else:
            st.warning("⚠️ Timestamp column not found. Cannot plot anomaly timeline.")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

else:
    st.info("👈 Please upload a CSV file to proceed.")
