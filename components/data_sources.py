import streamlit as st
import pandas as pd

def display_data_sources():
    st.subheader("Data Sources Overview")
    
    st.write("""
    The following data sources will be integrated into the new BI architecture. Each source provides 
    different business data that will be combined to create a comprehensive view of the business operations.
    """)
    
    # Create data source details
    data_sources = [
        {
            "name": "Xero",
            "category": "Financial",
            "data_type": "Accounting & Financial",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily",
            "key_data_elements": "Invoices, Bills, Chart of Accounts, General Ledger, Balance Sheet",
            "integration_complexity": "Medium"
        },
        {
            "name": "CIN7 Core",
            "category": "Inventory",
            "data_type": "Inventory & Order Management",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily (hourly for critical data)",
            "key_data_elements": "Inventory levels, Product data, Purchase orders, Stock movements",
            "integration_complexity": "Medium-High"
        },
        {
            "name": "Shopify",
            "category": "E-commerce",
            "data_type": "Sales & Customer",
            "api_availability": "Yes - REST & GraphQL API",
            "refresh_frequency": "Real-time (via webhooks) & Hourly",
            "key_data_elements": "Orders, Customers, Products, Collections, Inventory, Abandoned carts",
            "integration_complexity": "Low-Medium"
        },
        {
            "name": "Google Analytics",
            "category": "Web Analytics",
            "data_type": "Customer Behavior",
            "api_availability": "Yes - API v4",
            "refresh_frequency": "Daily",
            "key_data_elements": "Page views, Sessions, Conversion events, Traffic sources, User demographics",
            "integration_complexity": "Medium"
        },
        {
            "name": "Google Search Console",
            "category": "SEO",
            "data_type": "Search Performance",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily",
            "key_data_elements": "Search queries, Click-through rates, Impressions, Positions",
            "integration_complexity": "Low"
        },
        {
            "name": "ShipNetwork",
            "category": "Warehousing and Fulfillment",
            "data_type": "Logistics and Order Fulfillment Data",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily",
            "key_data_elements": "Inventory levels, Order statuses, Shipping tracking, Warehouse locations",
            "integration_complexity": "Medium"
        },
        {
            "name": "Klaviyo",
            "category": "Email Marketing",
            "data_type": "Customer Engagement",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily (real-time for events)",
            "key_data_elements": "Email campaigns, Open rates, Click rates, Subscriber data, Event tracking",
            "integration_complexity": "Medium"
        },
        {
            "name": "Gorgias",
            "category": "Customer Support",
            "data_type": "Support Interactions",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily (hourly for critical data)",
            "key_data_elements": "Tickets, Customer interactions, Resolution times, Support agent performance",
            "integration_complexity": "Medium"
        },
        {
            "name": "Hotjar",
            "category": "User Experience",
            "data_type": "Customer Behavior",
            "api_availability": "Limited API",
            "refresh_frequency": "Daily",
            "key_data_elements": "Heatmaps, Session recordings, Survey responses",
            "integration_complexity": "High (limited API capabilities)"
        },
        {
            "name": "Refersion",
            "category": "Affiliate Marketing",
            "data_type": "Performance Marketing",
            "api_availability": "Yes - REST API",
            "refresh_frequency": "Daily",
            "key_data_elements": "Affiliate data, Commissions, Orders, Conversions",
            "integration_complexity": "Medium"
        }
    ]
    
    # Convert to DataFrame for display
    df = pd.DataFrame(data_sources)
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Table View", "Integration Details", "Data Models"])
    
    with tab1:
        st.dataframe(df, use_container_width=True)
    
    with tab2:
        for source in data_sources:
            with st.expander(f"{source['name']} Integration"):
                st.write(f"**Category:** {source['category']}")
                st.write(f"**Data Type:** {source['data_type']}")
                st.write(f"**API Availability:** {source['api_availability']}")
                st.write(f"**Refresh Frequency:** {source['refresh_frequency']}")
                st.write(f"**Key Data Elements:** {source['key_data_elements']}")
                st.write(f"**Integration Complexity:** {source['integration_complexity']}")
                
                # Show integration approach
                st.write("**Integration Approach:**")
                st.write(f"Data from {source['name']} will be extracted via its API and loaded into staging tables in AlcheSanctum. The data will then be transformed using DBT Core into analytics-ready models.")
                
                # Show sample data model
                if source['name'] in ["Shopify", "Xero", "Klaviyo"]:
                    st.write("**Sample Data Model:**")
                    if source['name'] == "Shopify":
                        st.code("""
-- Fact table
fact_orders (
    order_id,
    customer_id,
    order_date,
    total_amount,
    tax_amount,
    shipping_amount,
    discount_amount,
    status,
    source
)

-- Dimension tables
dim_customers (
    customer_id,
    first_name,
    last_name,
    email,
    city,
    state,
    country,
    customer_since
)

dim_products (
    product_id,
    sku,
    title,
    description,
    category,
    vendor,
    cost,
    price
)

-- Bridge table
order_items (
    order_id,
    product_id,
    quantity,
    price,
    discount
)
                        """, language="sql")
                    elif source['name'] == "Xero":
                        st.code("""
-- Fact tables
fact_invoices (
    invoice_id,
    customer_id,
    invoice_date,
    due_date,
    total_amount,
    tax_amount,
    status
)

fact_bills (
    bill_id,
    vendor_id,
    bill_date,
    due_date,
    total_amount,
    tax_amount,
    status
)

-- Dimension tables
dim_accounts (
    account_id,
    account_name,
    account_type,
    account_code,
    tax_type
)

-- Ledger transactions
ledger_entries (
    transaction_id,
    account_id,
    document_id,
    document_type,
    transaction_date,
    amount,
    description
)
                        """, language="sql")
                    elif source['name'] == "Klaviyo":
                        st.code("""
-- Fact tables
fact_email_campaigns (
    campaign_id,
    name,
    subject,
    send_date,
    list_id,
    sends,
    opens,
    clicks,
    unsubscribes,
    bounces
)

fact_email_events (
    event_id,
    customer_id,
    campaign_id,
    event_type,
    event_date,
    email,
    device_type,
    os,
    browser
)

-- Dimension tables
dim_lists (
    list_id,
    name,
    created_date,
    subscriber_count,
    active
)
                        """, language="sql")
    
    with tab3:
        st.write("### Data Models & Warehouse Schema")
        
        st.write("""
        The data from various sources will be organized into a dimensional model following the Kimball methodology. 
        This includes fact tables for transactional data and dimension tables for descriptive attributes.
        """)
        
        st.write("#### Core Data Models:")
        
        data_models = [
            {
                "model": "Sales & Orders",
                "fact_tables": "fact_orders, fact_order_items",
                "dimension_tables": "dim_customers, dim_products, dim_dates, dim_locations",
                "data_sources": "Shopify, CIN7 Core"
            },
            {
                "model": "Inventory",
                "fact_tables": "fact_inventory_movements, fact_stock_levels",
                "dimension_tables": "dim_products, dim_locations, dim_dates",
                "data_sources": "CIN7 Core, Shopify, ShipNetwork"
            },
            {
                "model": "Financial",
                "fact_tables": "fact_invoices, fact_bills, fact_gl_entries",
                "dimension_tables": "dim_accounts, dim_vendors, dim_customers, dim_dates",
                "data_sources": "Xero"
            },
            {
                "model": "Marketing",
                "fact_tables": "fact_marketing_campaigns, fact_marketing_events, fact_affiliate_sales",
                "dimension_tables": "dim_campaigns, dim_channels, dim_affiliates, dim_dates",
                "data_sources": "Klaviyo, Refersion, Google Analytics"
            },
            {
                "model": "Customer Support",
                "fact_tables": "fact_support_tickets, fact_interactions",
                "dimension_tables": "dim_customers, dim_agents, dim_ticket_types, dim_dates",
                "data_sources": "Gorgias"
            },
            {
                "model": "Website Performance",
                "fact_tables": "fact_pageviews, fact_sessions, fact_search_performance",
                "dimension_tables": "dim_pages, dim_traffic_sources, dim_devices, dim_dates",
                "data_sources": "Google Analytics, Google Search Console, Hotjar"
            }
        ]
        
        # Display data models
        df_models = pd.DataFrame(data_models)
        st.dataframe(df_models, use_container_width=True)
        
        # Show database schema diagram
        st.write("#### Sample Schema Diagram (Sales & Orders)")
        
        # Use text-based diagram as placeholder
        st.code("""
+-------------------+       +-------------------+       +-------------------+
| dim_customers     |       | fact_orders       |       | dim_products      |
+-------------------+       +-------------------+       +-------------------+
| customer_id (PK)  |<----->| order_id (PK)     |       | product_id (PK)   |
| first_name        |       | customer_id (FK)  |       | sku               |
| last_name         |       | order_date        |       | title             |
| email             |       | total_amount      |       | description       |
| address           |       | tax_amount        |       | category          |
| city              |       | shipping_amount   |       | vendor            |
| state             |       | discount_amount   |       | cost              |
| country           |       | status            |       | price             |
| customer_since    |       | source            |       | created_date      |
+-------------------+       +-------------------+       +-------------------+
                                    |
                                    |
                                    v
                            +-------------------+
                            | fact_order_items  |
                            +-------------------+
                            | order_id (FK)     |
                            | product_id (FK)   |
                            | quantity          |
                            | price             |
                            | discount          |
                            +-------------------+
        """)
        
        st.write("### Data Integration Process")
        
        st.write("""
        The data integration process follows an ELT (Extract, Load, Transform) approach:
        
        1. **Extract**: Data is extracted from source systems via APIs and loaded into staging tables
        2. **Load**: Raw data is loaded into the data warehouse
        3. **Transform**: DBT Core transforms raw data into analytics-ready models
        
        AlcheFlow orchestrates this entire process, with the following workflow:
        
        1. Extract data from source systems
        2. Load raw data into staging area in AlcheSanctum
        3. Run DBT transformations to create analytics models
        4. Validate data quality
        5. Refresh Superset dashboards
        """)
