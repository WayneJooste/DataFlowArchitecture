import streamlit as st 
import pandas as pd

def display_potv_ce():
    tab1, tab2 = st.tabs(["Current Phase", "Future Phase (AI/ML & Real-time)"])
    
    with tab1:
        st.write("### Phase 1: Initial Migration from DOMO to AWS")
        current_costs =  [
            {
                "Service Name": "Amazon EC2",
                "Description": "Dedicted cloud hosting service",
                "Occurance": "Monthly",
                "Cost (USD)": "949.25"
            },
            {
                "Service Name": "Cloud storage",
                "Description": "Storage and data ingress and egress - intial estimates of 1Tb but could increase",
                "Occurance": "Monthly",
                "Cost (USD)": "224.75"
            },
            {
                "Service Name": "Firewall",
                "Description": "Server firewalls for data protection",
                "Occurance": "Monthly",
                "Cost (USD)": "235.00"
            },
            {
                "Service Name": "Load balancer",
                "Description": "Ensures network traffic is directed to the most available resources to prevent bottlenecks",
                "Occurance": "Monthly",
                "Cost (USD)": "380.50"
            },
            {
                "Service Name": "TOTAL MONTHLY",
                "Description": "",
                "Occurance": "Monthly",
                "Cost (USD)": "1 789.5"
            },
            {
                "Service Name": "Development acceleration fee",
                "Description": "This fee is charged for the accelarated development (API's and infastructure) committment to the project",
                "Occurance": "Once-off",
                "Cost (USD)": "15 000"
            }
        ]
    
        # Display current costs in a table
        current_df = pd.DataFrame(current_costs)
        st.dataframe(current_df[["Service Name", "Description", "Occurance", "Cost (USD)"]], use_container_width=True)
        
    with tab2:
        st.write("### Phase 2: Enhanced with AI/ML and Real-time Analytics")
        
        st.write("""
        1. All monthly costs associated with the Current (initial architecture) will continue
        2. Additional infastrcuture will be required but can onnly be estimated once requirements are fully specified
        """)

    
    
