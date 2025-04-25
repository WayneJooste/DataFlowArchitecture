import streamlit as st

def display_superset_intro():
    # --- Superset Video Section ---
    video_path = 'assets/superset.mp4'
    st.video(video_path, format="video/mp4", start_time=0)

