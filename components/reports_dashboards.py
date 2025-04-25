import streamlit as st
import pandas as pd

def display_reports_dashboards():
    st.subheader("Recommended Reports & Dashboards")
    
    st.write("""
    Based on industry standards and best practices for an online vaporization business, 
    we recommend the following reports and dashboards in Apache Superset.
    """)
    
    # Different dashboard categories
    dashboard_categories = ["Executive", "Sales & Marketing", "Inventory & Operations", "Financial", "Customer Experience", "Specialized Reports", "Future Reports", "Roadmap"]
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(dashboard_categories)
    
    with tab1:
        st.write("### Executive Dashboards")
        
        executive_dashboards = [
            {
                "name": "Executive KPI Dashboard",
                "description": "High-level overview of business performance",
                "metrics": ["Revenue (Daily/Weekly/Monthly/YTD)", "Gross Margin", "Customer Acquisition Cost", "Customer Lifetime Value", "Website Conversion Rate", "Average Order Value", "Inventory Turnover"],
                "visualization": "KPI cards, trend charts, comparison to targets",
                "refresh": "Daily"
            },
            {
                "name": "Business Health Monitor",
                "description": "Monitoring of critical business metrics across departments",
                "metrics": ["Cash Flow", "Sales by Channel", "Marketing ROI", "Inventory Health", "Customer Satisfaction", "Support Ticket Resolution"],
                "visualization": "Balanced scorecard with alerts for metrics outside acceptable ranges",
                "refresh": "Daily"
            },
            {
                "name": "Strategic Growth Dashboard",
                "description": "Long-term trends and growth indicators",
                "metrics": ["Month-over-Month Growth", "New vs Returning Customer Revenue", "Product Category Performance", "Market Share Estimates", "Channel Effectiveness"],
                "visualization": "Growth charts, heatmaps, geographic distribution",
                "refresh": "Weekly"
            }
        ]
        
        for dashboard in executive_dashboards:
            with st.expander(dashboard["name"]):
                st.write(f"**Description:** {dashboard['description']}")
                st.write("**Key Metrics:**")
                for metric in dashboard["metrics"]:
                    st.write(f"- {metric}")
                st.write(f"**Visualization Type:** {dashboard['visualization']}")
                st.write(f"**Refresh Frequency:** {dashboard['refresh']}")
    
    with tab2:
        st.write("### Sales & Marketing Dashboards")
        
        sales_dashboards = [
            {
                "name": "Sales Performance Dashboard",
                "description": "Comprehensive view of sales performance across all channels",
                "metrics": ["Sales by Product Category", "Sales by SKU", "Sales by Channel", "Sales by Geographic Region", "Sales by Customer Segment", "Promotion Performance"],
                "visualization": "Bar charts, line charts, data tables with drill-down capability",
                "refresh": "Daily"
            },
            {
                "name": "E-commerce Performance",
                "description": "Detailed analysis of online store performance",
                "metrics": ["Website Traffic", "Conversion Rate", "Cart Abandonment Rate", "Average Session Duration", "Landing Page Performance", "Top Selling Products", "Search Keyword Performance"],
                "visualization": "Funnel charts, trend lines, heatmaps",
                "refresh": "Daily"
            },
            {
                "name": "Marketing Campaign Performance",
                "description": "Evaluation of marketing campaign effectiveness",
                "metrics": ["Campaign ROI", "Email Open & Click Rates", "Social Media Engagement", "Affiliate Performance", "Ad Spend & ROAS", "Customer Acquisition Cost by Channel"],
                "visualization": "ROI comparison charts, campaign timeline, attribution modeling",
                "refresh": "Daily/Weekly"
            },
            {
                "name": "Customer Acquisition & Retention",
                "description": "Analysis of customer acquisition channels and retention metrics",
                "metrics": ["New vs Returning Customers", "Customer LTV", "Churn Rate", "Repeat Purchase Rate", "Time Between Purchases", "Customer Segmentation", "Acquisition Source Analysis"],
                "visualization": "Cohort analysis, retention curves, segment comparison",
                "refresh": "Weekly"
            }
        ]
        
        for dashboard in sales_dashboards:
            with st.expander(dashboard["name"]):
                st.write(f"**Description:** {dashboard['description']}")
                st.write("**Key Metrics:**")
                for metric in dashboard["metrics"]:
                    st.write(f"- {metric}")
                st.write(f"**Visualization Type:** {dashboard['visualization']}")
                st.write(f"**Refresh Frequency:** {dashboard['refresh']}")
    
    with tab3:
        st.write("### Inventory & Operations Dashboards")
        
        inventory_dashboards = [
            {
                "name": "Inventory Management Dashboard",
                "description": "Complete view of inventory status and movement",
                "metrics": ["Current Stock Levels", "Stock Movement History", "Days of Supply", "Stockouts", "Slow-moving Inventory", "Inventory Value", "Product Performance"],
                "visualization": "Stock level indicators, trend charts, inventory aging analysis",
                "refresh": "Daily/Real-time"
            },
            {
                "name": "Procurement & Supply Chain",
                "description": "Monitoring of supply chain performance and procurement metrics",
                "metrics": ["Purchase Orders Status", "Vendor Performance", "Lead Times", "Order Fulfillment Rate", "Shipping Cost Analysis", "Delivery Performance"],
                "visualization": "Status tracking, timeline views, performance scorecards",
                "refresh": "Daily"
            },
            {
                "name": "Product Performance Dashboard",
                "description": "Analysis of product performance across various dimensions",
                "metrics": ["Sales by Product", "Profit Margin by Product", "Returns by Product", "Stock Turnover by Product", "Cross-sell Relationships", "Product Reviews/Ratings"],
                "visualization": "Product comparison charts, profitability matrix, heatmaps",
                "refresh": "Daily/Weekly"
            },
            {
                "name": "Warehouse Operations",
                "description": "Monitoring of warehouse and fulfillment operations",
                "metrics": ["Order Processing Time", "Order Accuracy", "Shipping Times", "Returns Processing", "Order Backlog", "Fulfillment Costs"],
                "visualization": "Process flow charts, timeline tracking, efficiency metrics",
                "refresh": "Daily"
            }
        ]
        
        for dashboard in inventory_dashboards:
            with st.expander(dashboard["name"]):
                st.write(f"**Description:** {dashboard['description']}")
                st.write("**Key Metrics:**")
                for metric in dashboard["metrics"]:
                    st.write(f"- {metric}")
                st.write(f"**Visualization Type:** {dashboard['visualization']}")
                st.write(f"**Refresh Frequency:** {dashboard['refresh']}")
    
    with tab4:
        st.write("### Financial Dashboards")
        
        financial_dashboards = [
            {
                "name": "Financial Performance Dashboard",
                "description": "Comprehensive view of financial performance",
                "metrics": ["Revenue", "Cost of Goods Sold", "Gross Margin", "Operating Expenses", "Net Profit", "Cash Flow", "Accounts Receivable/Payable"],
                "visualization": "Financial statements, trend analysis, variance analysis",
                "refresh": "Daily/Weekly"
            },
            {
                "name": "Profitability Analysis",
                "description": "Detailed breakdown of profitability by various dimensions",
                "metrics": ["Profit by Product Category", "Profit by Channel", "Profit by Customer Segment", "Marketing ROI", "Customer Acquisition Cost", "Customer Lifetime Value"],
                "visualization": "Profit waterfall charts, margin analysis, breakeven analysis",
                "refresh": "Weekly/Monthly"
            },
            {
                "name": "Cash Flow Management",
                "description": "Monitoring of cash flow and forecasting",
                "metrics": ["Cash Position", "Cash Flow Forecast", "Accounts Receivable Aging", "Accounts Payable Aging", "Working Capital", "Burn Rate"],
                "visualization": "Cash flow statements, aging reports, forecast models",
                "refresh": "Daily/Weekly"
            },
            {
                "name": "Tax & Compliance Dashboard",
                "description": "Tracking of tax obligations and compliance requirements specific to vape products",
                "metrics": ["Sales Tax by Jurisdiction", "Excise Tax Liability", "Regulatory Compliance Status", "Product Registration Status", "License/Permit Status"],
                "visualization": "Compliance checklists, tax calculation tables, jurisdiction maps",
                "refresh": "Monthly/Quarterly"
            }
        ]
        
        for dashboard in financial_dashboards:
            with st.expander(dashboard["name"]):
                st.write(f"**Description:** {dashboard['description']}")
                st.write("**Key Metrics:**")
                for metric in dashboard["metrics"]:
                    st.write(f"- {metric}")
                st.write(f"**Visualization Type:** {dashboard['visualization']}")
                st.write(f"**Refresh Frequency:** {dashboard['refresh']}")
    
    with tab5:
        st.write("### Customer Experience Dashboards")
        
        customer_dashboards = [
            {
                "name": "Customer Satisfaction Dashboard",
                "description": "Monitoring of customer satisfaction metrics",
                "metrics": ["Net Promoter Score", "Customer Satisfaction Score", "Review Ratings", "Customer Feedback Analysis", "Support Ticket Analysis", "Return Rates"],
                "visualization": "Satisfaction trends, sentiment analysis, feedback word clouds",
                "refresh": "Daily/Weekly"
            },
            {
                "name": "Customer Support Performance",
                "description": "Analysis of customer support operations",
                "metrics": ["Ticket Volume", "Resolution Time", "First Response Time", "Support Channel Performance", "Customer Satisfaction by Agent", "Common Issue Categories"],
                "visualization": "Service level charts, ticket flow diagrams, response time distribution",
                "refresh": "Daily"
            },
            {
                "name": "Website User Experience",
                "description": "Analysis of website user behavior and experience",
                "metrics": ["Page Load Time", "User Flows", "Bounce Rate by Page", "Exit Pages", "Heatmap Analysis", "Form Completion Rate", "Error Rates"],
                "visualization": "User flow diagrams, heatmaps, session recordings",
                "refresh": "Daily"
            },
            {
                "name": "Customer Segmentation Dashboard",
                "description": "Deep analysis of different customer segments",
                "metrics": ["Segment Size & Growth", "Purchase Behavior by Segment", "Product Preferences by Segment", "Customer Lifetime Value by Segment", "Marketing Response by Segment"],
                "visualization": "Segment comparison charts, behavioral analysis, persona profiles",
                "refresh": "Weekly/Monthly"
            }
        ]
        
        for dashboard in customer_dashboards:
            with st.expander(dashboard["name"]):
                st.write(f"**Description:** {dashboard['description']}")
                st.write("**Key Metrics:**")
                for metric in dashboard["metrics"]:
                    st.write(f"- {metric}")
                st.write(f"**Visualization Type:** {dashboard['visualization']}")
                st.write(f"**Refresh Frequency:** {dashboard['refresh']}")
    
    with tab6:
        st.write("### Specialized Reports for Vaporization Business")
        # Specialized reports for vaporization business
        specialized_reports = [
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
    
        # Display specialized reports in a table
        specialized_df = pd.DataFrame(specialized_reports)
        st.dataframe(specialized_df[["name", "description","metrics", "importance"]], use_container_width=True)
    
    with tab7: 
    # Future AI/ML Enhanced Reports
        st.write("### Future AI/ML Enhanced Reports (Phase 2)")
    
        future_reports = [
            {
                "name": "Predictive Inventory Management",
                "description": "AI-driven forecasting of inventory needs based on historical data, seasonality, and market trends",
                "ai_features": ["Demand forecasting", "Automated reorder point calculation", "Stockout prediction", "Seasonal trend identification"]
            },
            {
                "name": "Customer Churn Prediction",
                "description": "Machine learning models to identify customers at risk of churning",
                "ai_features": ["Churn risk scoring", "Early warning indicators", "Recommended retention actions", "Churn reason prediction"]
            },
            {
                "name": "Product Recommendation Engine",
                "description": "Personalized product recommendations based on customer behavior and preferences",
                "ai_features": ["Collaborative filtering", "Product affinity analysis", "Next best product prediction", "Personalized marketing suggestions"]
            },
            {
                "name": "Sentiment Analysis Dashboard",
                "description": "Natural language processing of customer reviews, support interactions, and social media mentions",
                "ai_features": ["Sentiment scoring", "Topic extraction", "Trend analysis", "Competitive sentiment comparison"]
            },
            {
                "name": "Anomaly Detection Dashboard",
                "description": "Real-time detection of unusual patterns in sales, inventory, or customer behavior",
                "ai_features": ["Fraud detection", "Price error identification", "Unusual buying pattern alerts", "Website performance anomalies"]
            },
            {
                "name": "Customer Lifetime Value Prediction",
                "description": "Prediction of potential lifetime value for customers based on early purchase behavior",
                "ai_features": ["LTV prediction models", "High-value customer identification", "Acquisition channel evaluation", "Customer segment potential analysis"]
            }
        ]
    
        # Create columns for future reports
        col1, col2 = st.columns(2)
        
        for i, report in enumerate(future_reports):
            # Alternate between columns
            with col1 if i % 2 == 0 else col2:
                with st.expander(report["name"]):
                    st.write(f"**Description:** {report['description']}")
                    st.write("**AI/ML Features:**")
                    for feature in report["ai_features"]:
                        st.write(f"- {feature}")
    
    with tab8: 
                
        # Implementation roadmap
        st.write("### Implementation Roadmap")
        
        st.write("""
        **Phase 1: Core Dashboards (1-3 months)**
        1. Executive KPI Dashboard
        2. Sales Performance Dashboard
        3. Inventory Management Dashboard
        4. Financial Performance Dashboard
        5. Customer Satisfaction Dashboard
        
        **Phase 2: Extended Dashboards (3-6 months)**
        1. Complete all remaining standard dashboards
        2. Implement specialized vape industry reports
        3. Develop custom reports based on initial user feedback
        
        **Phase 3: AI/ML Enhanced Analytics (6-12 months)**
        1. Implement predictive inventory management
        2. Deploy customer churn prediction models
        3. Develop product recommendation engine
        4. Implement sentiment analysis of customer feedback
        5. Develop real-time anomaly detection
        """)
