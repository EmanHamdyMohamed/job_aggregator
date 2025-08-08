import streamlit as st
import pandas as pd 
from scrapers.remoteok_scraper import get_remoteok_jobs

st.set_page_config(page_title="Job Aggregator", page_icon="💼", layout="wide")
st.title("💼 Job Aggregator")

# Create a container for better alignment
with st.container():
    # Create two columns for the search interface
    col1, col2 = st.columns([3, 1])

    search_keyword = col1.text_input(
        "Enter Job Title or Keyword",
        key="search_keyword"
    )

    # Use CSS to align the button with the input field
    col2.markdown(
        """
        <style>
        .stButton > button {
            margin-top: 11px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    search_button = col2.button('Search')
    if search_button:
        # Call the function to get the jobs
        with st.spinner("Fetching jobs..."):
            jobs = get_remoteok_jobs(search_keyword)
            if jobs:
                df = pd.DataFrame(jobs)
                st.dataframe(df)
            else:
                st.warning("No jobs found.")
