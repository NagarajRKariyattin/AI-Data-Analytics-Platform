import streamlit as st


def app_header():

    st.markdown(
        """
        <div class="main-header">

        <h1>📊 AI Data Analytics Platform</h1>

        <p>
        Upload • Analyze • Visualize • Generate AI Insights
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )