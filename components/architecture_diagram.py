import streamlit as st
import plotly.graph_objects as go
import networkx as nx

def display_architecture_diagram():
    # Create tabs for current and future state
    tab1, tab2 = st.tabs(["Current Phase", "Future Phase (AI/ML & Real-time)"])
    
    with tab1:
        st.write("### Phase 1: Initial Migration from DOMO to AWS")
        current_phase_diagram()
        
    with tab2:
        st.write("### Phase 2: Enhanced with AI/ML and Real-time Analytics")
        future_phase_diagram()

def current_phase_diagram():
    # Create plotly figure for the architecture diagram
    fig = go.Figure()
    
    # Define node positions
    pos = {
        # Data Sources (Layer 1)
        'Xero': (1, 8), 
        'CIN7 Core': (1, 7),
        'Shopify': (1, 6), 
        'Google Analytics': (1, 5),
        'Google Search Console': (1, 4),
        'Rakuten': (1, 3),
        'Klaviyo': (1, 2),
        'Gorgias': (1, 1),
        'Hotjar': (1, 0),
        'Refersion': (1, -1),
        
        # APIs (Layer 2)
        'APIs': (3, 4),
        
        # Data Transformation (Layer 3)
        'Data Transformation (DBT Core)': (5, 4),
        
        # Data Warehouse (Layer 4)
        'PostgreSQL': (7, 4),
        
        # Workflow Management (Layer 5)
        'Apache Airflow': (6, 7),
        
        # Reporting & Visualization (Layer 6)
        'Apache Superset': (9, 4),
        
        # AWS Environment
        'AWS': (6, -2),
    }
    
    # Add nodes (data sources)
    data_sources = ['Xero', 'CIN7 Core', 'Shopify', 'Google Analytics', 
                   'Google Search Console', 'Rakuten', 'Klaviyo', 'Gorgias', 
                   'Hotjar', 'Refersion']
    
    for source in data_sources:
        fig.add_trace(go.Scatter(
            x=[pos[source][0]],
            y=[pos[source][1]],
            mode='markers+text',
            marker=dict(size=20, color='skyblue'),
            text=[source],
            textposition="top center",
            hoverinfo='text',
            name=source
        ))
        
        # Connect data sources to APIs
        fig.add_trace(go.Scatter(
            x=[pos[source][0], pos['APIs'][0]],
            y=[pos[source][1], pos['APIs'][1]],
            mode='lines',
            line=dict(width=1, color='grey'),
            hoverinfo='none',
            showlegend=False
        ))
    
    # Add API node
    fig.add_trace(go.Scatter(
        x=[pos['APIs'][0]],
        y=[pos['APIs'][1]],
        mode='markers+text',
        marker=dict(size=30, color='lightgreen'),
        text=['APIs'],
        textposition="top center",
        hoverinfo='text',
        name='APIs'
    ))
    
    # Connect APIs to Data Transformation
    fig.add_trace(go.Scatter(
        x=[pos['APIs'][0], pos['Data Transformation (DBT Core)'][0]],
        y=[pos['APIs'][1], pos['Data Transformation (DBT Core)'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add Data Transformation node
    fig.add_trace(go.Scatter(
        x=[pos['Data Transformation (DBT Core)'][0]],
        y=[pos['Data Transformation (DBT Core)'][1]],
        mode='markers+text',
        marker=dict(size=40, color='orange'),
        text=['Data Transformation<br>(DBT Core)'],
        textposition="top center",
        hoverinfo='text',
        name='Data Transformation'
    ))
    
    # Connect Data Transformation to PostgreSQL
    fig.add_trace(go.Scatter(
        x=[pos['Data Transformation (DBT Core)'][0], pos['PostgreSQL'][0]],
        y=[pos['Data Transformation (DBT Core)'][1], pos['PostgreSQL'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add PostgreSQL node
    fig.add_trace(go.Scatter(
        x=[pos['PostgreSQL'][0]],
        y=[pos['PostgreSQL'][1]],
        mode='markers+text',
        marker=dict(size=40, color='royalblue'),
        text=['PostgreSQL<br>(Data Warehouse)'],
        textposition="top center",
        hoverinfo='text',
        name='PostgreSQL'
    ))
    
    # Connect PostgreSQL to Apache Superset
    fig.add_trace(go.Scatter(
        x=[pos['PostgreSQL'][0], pos['Apache Superset'][0]],
        y=[pos['PostgreSQL'][1], pos['Apache Superset'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add Apache Superset node
    fig.add_trace(go.Scatter(
        x=[pos['Apache Superset'][0]],
        y=[pos['Apache Superset'][1]],
        mode='markers+text',
        marker=dict(size=40, color='purple'),
        text=['Apache Superset<br>(Reporting & Visualization)'],
        textposition="top center",
        hoverinfo='text',
        name='Apache Superset'
    ))
    
    # Add Apache Airflow node
    fig.add_trace(go.Scatter(
        x=[pos['Apache Airflow'][0]],
        y=[pos['Apache Airflow'][1]],
        mode='markers+text',
        marker=dict(size=40, color='lightblue'),
        text=['Apache Airflow<br>(Workflow Management)'],
        textposition="top center",
        hoverinfo='text',
        name='Apache Airflow'
    ))
    
    # Connect Airflow to Data Transformation, PostgreSQL, and APIs
    fig.add_trace(go.Scatter(
        x=[pos['Apache Airflow'][0], pos['Data Transformation (DBT Core)'][0]],
        y=[pos['Apache Airflow'][1], pos['Data Transformation (DBT Core)'][1]],
        mode='lines',
        line=dict(width=2, color='lightblue', dash='dash'),
        hoverinfo='none',
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=[pos['Apache Airflow'][0], pos['PostgreSQL'][0]],
        y=[pos['Apache Airflow'][1], pos['PostgreSQL'][1]],
        mode='lines',
        line=dict(width=2, color='lightblue', dash='dash'),
        hoverinfo='none',
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=[pos['Apache Airflow'][0], pos['APIs'][0]],
        y=[pos['Apache Airflow'][1], pos['APIs'][1]],
        mode='lines',
        line=dict(width=2, color='lightblue', dash='dash'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add AWS node
    fig.add_trace(go.Scatter(
        x=[pos['AWS'][0]],
        y=[pos['AWS'][1]],
        mode='markers+text',
        marker=dict(size=50, color='orange', symbol='square'),
        text=['AWS Environment'],
        textposition="top center",
        hoverinfo='text',
        name='AWS'
    ))
    
    # Draw cloud boundary (AWS environment)
    cloud_x = [4, 10, 10, 4, 4]
    cloud_y = [-3, -3, 9, 9, -3]
    
    fig.add_trace(go.Scatter(
        x=cloud_x,
        y=cloud_y,
        mode='lines',
        line=dict(width=2, color='orange', dash='dot'),
        fill='toself',
        fillcolor='rgba(255, 165, 0, 0.1)',
        hoverinfo='none',
        showlegend=False
    ))
    
    # Update layout
    fig.update_layout(
        title="BI Architecture: DOMO to AWS Migration - Phase 1",
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        autosize=True,
        height=800,
        margin=dict(l=20, r=20, t=50, b=20),
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add legend/description
    with st.expander("Diagram Components Explanation"):
        st.markdown("""
        - **Data Sources**: Various business systems (Xero, Shopify, etc.) that provide raw data
        - **APIs**: Integration points for extracting data from source systems
        - **Data Transformation (DBT Core)**: Tool for transforming raw data into analytics-ready models
        - **PostgreSQL**: Central data warehouse storing transformed data
        - **Apache Airflow**: Workflow management tool orchestrating the entire data pipeline
        - **Apache Superset**: Reporting and visualization platform for business users
        - **AWS Environment**: Cloud infrastructure hosting all components except data sources
        """)

def future_phase_diagram():
    # Create plotly figure for the future architecture diagram
    fig = go.Figure()
    
    # Define node positions
    pos = {
        # Data Sources (Layer 1)
        'Xero': (1, 8), 
        'CIN7 Core': (1, 7),
        'Shopify': (1, 6), 
        'Google Analytics': (1, 5),
        'Google Search Console': (1, 4),
        'Rakuten': (1, 3),
        'Klaviyo': (1, 2),
        'Gorgias': (1, 1),
        'Hotjar': (1, 0),
        'Refersion': (1, -1),
        
        # APIs (Layer 2)
        'APIs': (3, 4),
        
        # Kafka (NEW)
        'Apache Kafka': (3, 2),
        
        # Data Transformation (Layer 3)
        'Data Transformation (DBT Core)': (5, 4),
        
        # AI/ML (NEW)
        'AI/ML (Python)': (5, 2),
        
        # Data Warehouse (Layer 4)
        'PostgreSQL': (7, 4),
        
        # Workflow Management (Layer 5)
        'Apache Airflow': (6, 7),
        
        # Reporting & Visualization (Layer 6)
        'Apache Superset': (9, 4),
        
        # AWS Environment
        'AWS': (6, -2),
    }
    
    # Add nodes (data sources)
    data_sources = ['Xero', 'CIN7 Core', 'Shopify', 'Google Analytics', 
                   'Google Search Console', 'Rakuten', 'Klaviyo', 'Gorgias', 
                   'Hotjar', 'Refersion']
    
    for source in data_sources:
        fig.add_trace(go.Scatter(
            x=[pos[source][0]],
            y=[pos[source][1]],
            mode='markers+text',
            marker=dict(size=20, color='skyblue'),
            text=[source],
            textposition="top center",
            hoverinfo='text',
            name=source
        ))
        
        # Connect data sources to APIs
        fig.add_trace(go.Scatter(
            x=[pos[source][0], pos['APIs'][0]],
            y=[pos[source][1], pos['APIs'][1]],
            mode='lines',
            line=dict(width=1, color='grey'),
            hoverinfo='none',
            showlegend=False
        ))
        
        # Connect selected sources to Kafka (real-time sources)
        if source in ['Shopify', 'Klaviyo', 'Hotjar', 'Gorgias']:
            fig.add_trace(go.Scatter(
                x=[pos[source][0], pos['Apache Kafka'][0]],
                y=[pos[source][1], pos['Apache Kafka'][1]],
                mode='lines',
                line=dict(width=1, color='red', dash='dot'),
                hoverinfo='none',
                showlegend=False
            ))
    
    # Add API node
    fig.add_trace(go.Scatter(
        x=[pos['APIs'][0]],
        y=[pos['APIs'][1]],
        mode='markers+text',
        marker=dict(size=30, color='lightgreen'),
        text=['APIs'],
        textposition="top center",
        hoverinfo='text',
        name='APIs'
    ))
    
    # Add Kafka node (NEW)
    fig.add_trace(go.Scatter(
        x=[pos['Apache Kafka'][0]],
        y=[pos['Apache Kafka'][1]],
        mode='markers+text',
        marker=dict(size=35, color='red'),
        text=['Apache Kafka<br>(Real-time Streaming)'],
        textposition="top center",
        hoverinfo='text',
        name='Apache Kafka'
    ))
    
    # Connect APIs to Data Transformation
    fig.add_trace(go.Scatter(
        x=[pos['APIs'][0], pos['Data Transformation (DBT Core)'][0]],
        y=[pos['APIs'][1], pos['Data Transformation (DBT Core)'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Connect Kafka to AI/ML
    fig.add_trace(go.Scatter(
        x=[pos['Apache Kafka'][0], pos['AI/ML (Python)'][0]],
        y=[pos['Apache Kafka'][1], pos['AI/ML (Python)'][1]],
        mode='lines',
        line=dict(width=2, color='red'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add Data Transformation node
    fig.add_trace(go.Scatter(
        x=[pos['Data Transformation (DBT Core)'][0]],
        y=[pos['Data Transformation (DBT Core)'][1]],
        mode='markers+text',
        marker=dict(size=40, color='orange'),
        text=['Data Transformation<br>(DBT Core)'],
        textposition="top center",
        hoverinfo='text',
        name='Data Transformation'
    ))
    
    # Add AI/ML node (NEW)
    fig.add_trace(go.Scatter(
        x=[pos['AI/ML (Python)'][0]],
        y=[pos['AI/ML (Python)'][1]],
        mode='markers+text',
        marker=dict(size=40, color='green'),
        text=['AI/ML Processing<br>(Python)'],
        textposition="top center",
        hoverinfo='text',
        name='AI/ML'
    ))
    
    # Connect Data Transformation to PostgreSQL
    fig.add_trace(go.Scatter(
        x=[pos['Data Transformation (DBT Core)'][0], pos['PostgreSQL'][0]],
        y=[pos['Data Transformation (DBT Core)'][1], pos['PostgreSQL'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Connect AI/ML to PostgreSQL
    fig.add_trace(go.Scatter(
        x=[pos['AI/ML (Python)'][0], pos['PostgreSQL'][0]],
        y=[pos['AI/ML (Python)'][1], pos['PostgreSQL'][1]],
        mode='lines',
        line=dict(width=2, color='green'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add PostgreSQL node
    fig.add_trace(go.Scatter(
        x=[pos['PostgreSQL'][0]],
        y=[pos['PostgreSQL'][1]],
        mode='markers+text',
        marker=dict(size=40, color='royalblue'),
        text=['PostgreSQL<br>(Data Warehouse)'],
        textposition="top center",
        hoverinfo='text',
        name='PostgreSQL'
    ))
    
    # Connect PostgreSQL to Apache Superset
    fig.add_trace(go.Scatter(
        x=[pos['PostgreSQL'][0], pos['Apache Superset'][0]],
        y=[pos['PostgreSQL'][1], pos['Apache Superset'][1]],
        mode='lines',
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add Apache Superset node
    fig.add_trace(go.Scatter(
        x=[pos['Apache Superset'][0]],
        y=[pos['Apache Superset'][1]],
        mode='markers+text',
        marker=dict(size=40, color='purple'),
        text=['Apache Superset<br>(Reporting & Visualization)'],
        textposition="top center",
        hoverinfo='text',
        name='Apache Superset'
    ))
    
    # Add Apache Airflow node
    fig.add_trace(go.Scatter(
        x=[pos['Apache Airflow'][0]],
        y=[pos['Apache Airflow'][1]],
        mode='markers+text',
        marker=dict(size=40, color='lightblue'),
        text=['Apache Airflow<br>(Workflow Management)'],
        textposition="top center",
        hoverinfo='text',
        name='Apache Airflow'
    ))
    
    # Connect Airflow to various components
    components = ['Data Transformation (DBT Core)', 'PostgreSQL', 'APIs', 'AI/ML (Python)', 'Apache Kafka']
    for component in components:
        fig.add_trace(go.Scatter(
            x=[pos['Apache Airflow'][0], pos[component][0]],
            y=[pos['Apache Airflow'][1], pos[component][1]],
            mode='lines',
            line=dict(width=2, color='lightblue', dash='dash'),
            hoverinfo='none',
            showlegend=False
        ))
    
    # Add AWS node
    fig.add_trace(go.Scatter(
        x=[pos['AWS'][0]],
        y=[pos['AWS'][1]],
        mode='markers+text',
        marker=dict(size=50, color='orange', symbol='square'),
        text=['AWS Environment'],
        textposition="top center",
        hoverinfo='text',
        name='AWS'
    ))
    
    # Draw cloud boundary (AWS environment)
    cloud_x = [4, 10, 10, 4, 4]
    cloud_y = [-3, -3, 9, 9, -3]
    
    fig.add_trace(go.Scatter(
        x=cloud_x,
        y=cloud_y,
        mode='lines',
        line=dict(width=2, color='orange', dash='dot'),
        fill='toself',
        fillcolor='rgba(255, 165, 0, 0.1)',
        hoverinfo='none',
        showlegend=False
    ))
    
    # Update layout
    fig.update_layout(
        title="BI Architecture: DOMO to AWS Migration - Phase 2 (with AI/ML & Real-time)",
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        autosize=True,
        height=800,
        margin=dict(l=20, r=20, t=50, b=20),
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add legend/description
    with st.expander("Future Phase Components Explanation"):
        st.markdown("""
        ### New Components in Phase 2:
        
        - **Apache Kafka**: Real-time data streaming platform for capturing and processing real-time events
        - **AI/ML Processing (Python)**: Custom Python-based machine learning models for predictive analytics and customer behavior analysis
        
        ### Enhanced Data Flows:
        - Direct real-time streaming from customer-facing systems (Shopify, Klaviyo, Hotjar, Gorgias)
        - AI/ML processing of both batch and streaming data
        - Enriched data warehouse with predictive models and real-time insights
        
        This future architecture enables:
        - Real-time monitoring of customer behavior
        - Predictive analytics for inventory management
        - Personalized customer experiences
        - Anomaly detection for fraud prevention
        - Dynamic pricing optimization
        """)
