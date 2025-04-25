import streamlit as st
from components.architecture_diagram import display_architecture_diagram
from components.component_descriptions import display_component_descriptions
from components.data_sources import display_data_sources
from components.reports_dashboards import display_reports_dashboards
from components.superset_intro import display_superset_intro

# Page configuration

st.set_page_config(
    page_title="BI Architecture Migration: DOMO to Amazon Web Services",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a section:",
    ["Architecture Overview", "Component Descriptions", "Data Sources", "Standard Reports & Dashboards","POTV - Superset intro","Architecture Cost Estimates"]
)

# Page title and intro
st.title("BI Architecture Migration: DOMO to AWS")

# Display the selected page
if page == "Architecture Overview":
    st.header("Architecture Diagram")
    st.write("""
    This diagram illustrates the proposed migration from DOMO to a modern AWS-based BI architecture 
    using PostgreSQL, Apache Airflow, and Apache Superset. It shows both the current phase and 
    future expansion to incorporate AI/ML and real-time analytics.
    """)
    display_architecture_diagram()

elif page == "Component Descriptions":
    st.header("Technology Components")
    st.write("""
    Detailed descriptions of each technology component in the proposed architecture.
    """)
    display_component_descriptions()

elif page == "Data Sources":
    st.header("Data Sources & Integration")
    st.write("""
    Overview of the various data sources and how they'll be integrated into the new architecture.
    """)
    display_data_sources()

elif page == "Standard Reports & Dashboards":
    st.header("Standard Reports & Dashboards")
    st.write("""
    Recommended standard reports and dashboards for an online vaporization business.
    """)
    display_reports_dashboards()

elif page == "POTV - Superset intro":
    st.header("POTV - Superset intro")
    st.write("""
    An inntroduction video to Superset.
    """)
    display_superset_intro()

elif page == "Architecture Cost Estimates":
    st.header("Architecture Cost Estimates")
    st.write("""
    Estimated costs for Architecture build.
    """)
    display_reports_dashboards()

# Footer
st.markdown("---")
st.markdown("BI Architecture Migration Planning Tool | Created with Streamlit")
