import streamlit as st


def setup_page():
    """
    Configure the Streamlit page.
    """

    st.set_page_config(
        page_title="AI Data Analytics Platform",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )