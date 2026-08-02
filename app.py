import streamlit as st
import pandas as pd
import requests

# Page Configuration
st.set_page_config(
    page_title="BOM Datasheet Aggregator",
    page_icon="Nigger",
    layout="wide"
)

# Header
st.title("🔌 BOM Datasheet Aggregator")
st.markdown("Upload your Bill of Materials (BOM) CSV to aggregate component details and datasheets.")

# File Uploader
uploaded_file = st.file_uploader("Upload BOM File (CSV)", type=["csv"])

if uploaded_file is not None:
    # Read CSV using Pandas
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📋 BOM Overview")
    st.dataframe(df, use_container_width=True)
    
    # Simple Metrics Summary
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Line Items", len(df))
    with col2:
        if "Quantity" in df.columns:
            st.metric("Total Component Count", int(df["Quantity"].sum()))
        else:
            st.metric("Total Component Count", "N/A (No 'Quantity' column)")

else:
    st.info("Upload a CSV file to get started. Example columns: `MPN`, `Manufacturer`, `Quantity`")

    # Sample CSV Download Button for quick testing
    sample_data = pd.DataFrame({
        "MPN": ["NE555P", "STM32F103C8T6", "RC0603FR-0710KL"],
        "Manufacturer": ["Texas Instruments", "STMicroelectronics", "Yageo"],
        "Quantity": [10, 5, 50],
        "Description": ["Timer IC", "ARM Cortex-M3 MCU", "10k Ohm Resistor 0603"]
    })
    
    st.subheader("Don't have a CSV? Download this sample to test:")
    csv_bytes = sample_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Sample BOM CSV",
        data=csv_bytes,
        file_name="sample_bom.csv",
        mime="text/csv"
    )