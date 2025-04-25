import streamlit as st 
import pandas as pd

def potv_ce():
    tab1, tab2 = st.tabs(["Current Phase", "Future Phase (AI/ML & Real-time)"])
    
    with tab1:
        st.write("### Phase 1: Initial Migration from DOMO to AWS")
        current_costs =  [
            {
                "name": "Age Verification Compliance",
                "description": "Tracking of age verification processes and compliance",
                "metrics": ["Age Verification Rate", "Verification Method Used", "Failed Verifications", "Compliance by Region", "Age Verification Process Completion Rate"],
                "importance": "Critical for regulatory compliance in the vape industry"
            },
            {
                "name": "Product Regulation Tracking",
                "description": "Monitoring of product compliance with various regulations",
                "metrics": ["Product Registration Status", "Regulatory Changes by Region", "Non-compliant Products", "Required Documentation Status", "Upcoming Regulatory Deadlines"],
                "importance": "Essential for managing the complex regulatory landscape for vape products"
            },
            {
                "name": "Flavor Popularity Analysis",
                "description": "Detailed analysis of product flavors and their performance",
                "metrics": ["Sales by Flavor", "Customer Ratings by Flavor", "Flavor Trends Over Time", "Flavor Preferences by Region/Demographic", "New Flavor Performance"],
                "importance": "Critical for product development and inventory planning"
            },
            {
                "name": "Device vs. Consumable Analysis",
                "description": "Comparison of device sales versus consumable sales (e.g., vape devices vs. e-liquids)",
                "metrics": ["Device-to-Consumable Ratio", "Customer Lifetime by Device Type", "Attachment Rate", "Reorder Rate for Consumables", "Upgrade Patterns"],
                "importance": "Important for understanding the full customer lifecycle and revenue patterns"
            },
            {
                "name": "Nicotine Strength Analysis",
                "description": "Analysis of sales by nicotine strength levels",
                "metrics": ["Sales by Nicotine Strength", "Strength Preferences by Customer Segment", "Strength Trends Over Time", "Regional Strength Preferences", "Conversion Between Strengths"],
                "importance": "Valuable for product planning and understanding customer preferences"
            }
        ]
    
        # Display current costs in a table
        current_df = pd.DataFrame(current_costs)
        st.dataframe(current_df[["name", "description", "importance"]], use_container_width=True)
        
    with tab2:
        st.write("### Phase 2: Enhanced with AI/ML and Real-time Analytics")
        future_costs = [
            {
                "name": "Age Verification Compliance",
                "description": "Tracking of age verification processes and compliance",
                "metrics": ["Age Verification Rate", "Verification Method Used", "Failed Verifications", "Compliance by Region", "Age Verification Process Completion Rate"],
                "importance": "Critical for regulatory compliance in the vape industry"
            },
            {
                "name": "Product Regulation Tracking",
                "description": "Monitoring of product compliance with various regulations",
                "metrics": ["Product Registration Status", "Regulatory Changes by Region", "Non-compliant Products", "Required Documentation Status", "Upcoming Regulatory Deadlines"],
                "importance": "Essential for managing the complex regulatory landscape for vape products"
            },
            {
                "name": "Flavor Popularity Analysis",
                "description": "Detailed analysis of product flavors and their performance",
                "metrics": ["Sales by Flavor", "Customer Ratings by Flavor", "Flavor Trends Over Time", "Flavor Preferences by Region/Demographic", "New Flavor Performance"],
                "importance": "Critical for product development and inventory planning"
            },
            {
                "name": "Device vs. Consumable Analysis",
                "description": "Comparison of device sales versus consumable sales (e.g., vape devices vs. e-liquids)",
                "metrics": ["Device-to-Consumable Ratio", "Customer Lifetime by Device Type", "Attachment Rate", "Reorder Rate for Consumables", "Upgrade Patterns"],
                "importance": "Important for understanding the full customer lifecycle and revenue patterns"
            },
            {
                "name": "Nicotine Strength Analysis",
                "description": "Analysis of sales by nicotine strength levels",
                "metrics": ["Sales by Nicotine Strength", "Strength Preferences by Customer Segment", "Strength Trends Over Time", "Regional Strength Preferences", "Conversion Between Strengths"],
                "importance": "Valuable for product planning and understanding customer preferences"
            }
        ]
    
        # Display current costs in a table
        future_df = pd.DataFrame(future_costs)
        st.dataframe(future_df[["name", "description", "importance"]], use_container_width=True)

    
    
