import streamlit as st
import pandas as pd
import requests

# Page Configuration
st.set_page_config(
    page_title="BOM Datasheet Aggregator",
    page_icon="",
    layout="wide"
)

# Header
st.title("BOM Datasheet Aggregator")

# Search Bar UI
search_query = st.text_input(
    label="Search Components",
    placeholder="Search for a component (e.g., Resistor, Capacitor, IC)",
)

#
if st.button("Search", type="primary"):
    if search_query.strip():
        # Step A: Pass UI input into parser function
        data = run_component_parser(search_query.strip())
        # Step B: Save output in session state
        st.session_state["results_df"] = data
    else:
        st.warning("Please enter a valid search term.")

if st.session_state["results_df"] is not None:
    # TODO: Render the component details and datasheet download links
    pass