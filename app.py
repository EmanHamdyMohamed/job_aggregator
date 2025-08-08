import streamlit as st
import pandas as pd 
import re
from scrapers.remoteok_scraper import get_remoteok_jobs


def apply_filters(df, remote_preference, selected_country,
                 min_salary, max_salary):
    """Apply filters to the job dataframe"""
    filtered_df = df.copy()
    
    # Filter by remote preference
    if remote_preference != "All":
        if remote_preference == "Remote Only":
            filtered_df = filtered_df[
                filtered_df["location"].str.contains(
                    "Remote|Anywhere|Worldwide", 
                    case=False, na=False
                )
            ]
        elif remote_preference == "On-site Only":
            filtered_df = filtered_df[
                ~filtered_df["location"].str.contains(
                    "Remote|Anywhere|Worldwide", 
                    case=False, na=False
                )
            ]
    
    # Filter by country
    if selected_country != "All Countries":
        filtered_df = filtered_df[
            filtered_df["location"].str.contains(
                selected_country, 
                case=False, na=False
            )
        ]
    
    # Filter by salary range
    def extract_salary(salary_str):
        if pd.isna(salary_str) or salary_str == 'Unknown':
            return None
        # Extract numbers from salary string
        numbers = re.findall(r'\d+', str(salary_str))
        if numbers:
            return int(numbers[0])
        return None
    
    filtered_df['salary_numeric'] = filtered_df['salary'].apply(extract_salary)
    filtered_df = filtered_df[
        (filtered_df['salary_numeric'].isna()) | 
        ((filtered_df['salary_numeric'] >= min_salary) & 
         (filtered_df['salary_numeric'] <= max_salary))
    ]
    
    return filtered_df.drop(columns=['salary_numeric'])


def show_filter_summary(remote_preference, selected_country, 
                       min_salary, max_salary):
    """Display a summary of applied filters"""
    with st.expander("🔍 Applied Filters"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Work Type:** {remote_preference}")
        with col2:
            st.write(f"**Country:** {selected_country}")
        with col3:
            st.write(f"**Salary:** ${min_salary:,} - ${max_salary:,}")



st.set_page_config(page_title="Job Aggregator", page_icon="💼", layout="wide")
st.title("💼 Job Aggregator")

# Sidebar for advanced filters
with st.sidebar:
    st.header("🔍 Advanced Filters")
    
    # Remote work preference
    remote_preference = st.selectbox(
        "Work Type",
        ["All", "Remote Only", "On-site Only", "Hybrid"]
    )
    
    # Country selection
    countries = [
        "All Countries",
        "United States", "Canada", "United Kingdom", "Germany", 
        "France", "Netherlands", "Australia", "Spain", "Italy",
        "Sweden", "Norway", "Denmark", "Switzerland", "Austria",
        "Belgium", "Ireland", "Finland", "Poland", "Portugal",
        "Czech Republic", "Hungary", "Romania", "Bulgaria",
        "India", "China", "Japan", "South Korea", "Singapore",
        "Brazil", "Mexico", "Argentina", "Chile", "Colombia",
        "South Africa", "Nigeria", "Kenya", "Egypt", "Morocco"
    ]
    
    selected_country = st.selectbox("Country", countries)
    
    # Salary range filter
    st.subheader("💰 Salary Range")
    min_salary, max_salary = st.slider(
        "Annual Salary (USD)",
        min_value=0,
        max_value=200000,
        value=(30000, 150000),
        step=5000
    )

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
                
                # Apply filters
                filtered_df = apply_filters(df, remote_preference, selected_country, min_salary, max_salary)
                
                if not filtered_df.empty:
                    # Display results
                    st.subheader(f"📊 Found {len(filtered_df)} jobs")
                    
                    # Show filter summary
                    show_filter_summary(remote_preference, selected_country, min_salary, max_salary)
                    
                    # Display the dataframe with better formatting
                    st.dataframe(
                        filtered_df,
                        use_container_width=True,
                        column_config={
                            "title": st.column_config.TextColumn("Job Title", width="medium"),
                            "company": st.column_config.TextColumn("Company", width="medium"),
                            "location": st.column_config.TextColumn("Location", width="small"),
                            "salary": st.column_config.TextColumn("Salary", width="small"),
                            "tags": st.column_config.ListColumn("Skills", width="medium"),
                            "link": st.column_config.LinkColumn("Apply", width="small")
                        }
                    )
                else:
                    st.warning("No jobs found matching your criteria.")
            else:
                st.warning("No jobs found.")
