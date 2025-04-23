import streamlit as st

def display_component_descriptions():
    st.subheader("Current Architecture Components")
    
    components = [
        {
            "name": "AWS (Amazon Web Services)",
            "description": "Cloud computing platform providing infrastructure services for hosting the entire BI stack. AWS offers scalability, reliability, and a wide range of integrated services.",
            "benefits": ["Scalable infrastructure", "Pay-as-you-go pricing", "High availability", "Integrated services ecosystem"],
            "considerations": ["Requires cloud expertise", "Costs need monitoring", "Proper security configuration essential"]
        },
        {
            "name": "PostgreSQL",
            "description": "Open-source relational database management system that will serve as the central data warehouse. PostgreSQL offers robust performance, reliability, and advanced features for handling complex analytical workloads.",
            "benefits": ["Open-source (cost-effective)", "Excellent SQL compliance", "Advanced analytical functions", "Robust performance", "Strong community support"],
            "considerations": ["Requires proper sizing and optimization", "Needs regular maintenance"]
        },
        {
            "name": "Apache Airflow",
            "description": "Open-source platform for programmatically authoring, scheduling, and monitoring workflows. Airflow will orchestrate the entire data pipeline, from extraction to transformation and loading processes.",
            "benefits": ["Code-based workflow definition", "Rich UI for monitoring", "Extensible through plugins", "Robust scheduling capabilities", "Large community and extensive documentation"],
            "considerations": ["Learning curve for DAG-based workflows", "Requires Python knowledge", "Needs proper resource allocation"]
        },
        {
            "name": "Apache Superset",
            "description": "Modern data exploration and visualization platform. Superset will replace DOMO as the primary BI tool, allowing users to create and share dashboards with interactive visualizations.",
            "benefits": ["Open-source (cost-effective)", "Modern, interactive visualizations", "SQL lab for ad-hoc queries", "Dashboard sharing and embedding", "Fine-grained access control"],
            "considerations": ["Less mature than commercial BI tools", "Requires SQL knowledge for advanced use", "May need customization for specific requirements"]
        },
        {
            "name": "DBT Core",
            "description": "Data transformation tool that enables analytics engineers to transform data in their warehouse more effectively. DBT Core allows for version-controlled, testable transformations using SQL.",
            "benefits": ["SQL-based transformations", "Version control integration", "Testing framework", "Documentation generation", "Modular and reusable code"],
            "considerations": ["Requires SQL knowledge", "Best practices needed for optimal use", "Integration with Airflow needs configuration"]
        }
    ]
    
    for component in components:
        with st.expander(f"{component['name']}"):
            st.write(component['description'])
            
            st.write("**Key Benefits:**")
            for benefit in component['benefits']:
                st.write(f"- {benefit}")
                
            st.write("**Considerations:**")
            for consideration in component['considerations']:
                st.write(f"- {consideration}")
    
    st.subheader("Future Phase Components")
    
    future_components = [
        {
            "name": "Apache Kafka",
            "description": "Distributed event streaming platform for high-performance data pipelines, streaming analytics, and data integration. Kafka will enable real-time data processing for customer behavior analysis.",
            "benefits": ["Real-time data streaming", "High throughput", "Fault tolerance", "Scalable architecture", "Message persistence"],
            "considerations": ["Complex to set up and manage", "Requires careful planning for topics and partitions", "Additional infrastructure resources"]
        },
        {
            "name": "Python-based AI/ML",
            "description": "Custom machine learning models developed in Python using libraries like scikit-learn, TensorFlow, or PyTorch. These models will enable predictive analytics and deeper insights into customer behavior.",
            "benefits": ["Predictive capabilities", "Custom algorithm development", "Integration with data pipeline", "Continuous improvement through retraining"],
            "considerations": ["Requires data science expertise", "Model maintenance and retraining", "Integration with existing systems", "Training and inference performance"]
        }
    ]
    
    for component in future_components:
        with st.expander(f"{component['name']}"):
            st.write(component['description'])
            
            st.write("**Key Benefits:**")
            for benefit in component['benefits']:
                st.write(f"- {benefit}")
                
            st.write("**Considerations:**")
            for consideration in component['considerations']:
                st.write(f"- {consideration}")
                
    st.subheader("Comparison with Current DOMO Solution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### DOMO")
        st.markdown("""
        **Pros:**
        - All-in-one solution (data warehouse and visualization)
        - User-friendly interface
        - Managed service (low maintenance)
        - Pre-built connectors for many data sources
        
        **Cons:**
        - Expensive licensing model
        - Limited customization
        - Vendor lock-in
        - Less suitable for AI/ML integration
        - Proprietary technology stack
        """)
    
    with col2:
        st.markdown("### Proposed AWS Architecture")
        st.markdown("""
        **Pros:**
        - Cost-effective (open-source components)
        - Highly customizable
        - Better support for AI/ML integration
        - Scalable architecture
        - No vendor lock-in
        - Full control over data and processes
        
        **Cons:**
        - Requires more technical expertise
        - Higher initial implementation effort
        - Self-managed components (more maintenance)
        - Integration complexity
        """)

