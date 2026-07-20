import streamlit as st
import plotly.express as px

from preprocessing.data_loader import load_data
from preprocessing.profiling import dataset_profile


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Business Analyst Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst Assistant")
st.markdown("### Upload your CSV or Excel file to begin analysis")


# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)


# -----------------------------
# Process Uploaded File
# -----------------------------
if uploaded_file is not None:

    try:
        # Load dataset
        df = load_data(uploaded_file)

        # Generate profile
        profile = dataset_profile(df)

        st.success("✅ Dataset Loaded Successfully!")

        # =============================
        # KPI SECTION
        # =============================
        st.subheader("📌 Dataset Overview")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Rows", profile["Rows"])
        col2.metric("Columns", profile["Columns"])
        col3.metric("Missing Values", profile["Total Missing"])
        col4.metric("Duplicate Rows", profile["Duplicate Rows"])
        col5.metric("Quality Score", f"{profile['Quality Score']}%")

        st.divider()

        # =============================
        # Dataset Preview
        # =============================
        st.subheader("📄 Dataset Preview")

        st.dataframe(df, use_container_width=True)

        st.divider()

        # =============================
        # Missing Values
        # =============================
        st.subheader("📊 Missing Value Analysis")

        missing_df = profile["Missing Values"].reset_index()
        missing_df.columns = ["Column", "Missing Values"]

        st.dataframe(missing_df, use_container_width=True)

        fig = px.bar(
            missing_df,
            x="Column",
            y="Missing Values",
            title="Missing Values by Column",
            text="Missing Values"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # =============================
        # Data Types
        # =============================
        st.subheader("📑 Data Types")

        dtype_df = profile["Data Types"].reset_index()
        dtype_df.columns = ["Column", "Data Type"]

        st.dataframe(dtype_df, use_container_width=True)

        st.divider()

        # =============================
        # Summary Statistics
        # =============================
        st.subheader("📈 Summary Statistics")

        st.dataframe(profile["Summary"], use_container_width=True)

        st.divider()

        # =============================
        # AI Recommendation
        # =============================
        st.subheader("🤖 AI Recommendation")

        recommendations = []

        if profile["Duplicate Rows"] > 0:
            recommendations.append(
                f"• Remove {profile['Duplicate Rows']} duplicate rows."
            )

        if profile["Total Missing"] > 0:
            recommendations.append(
                f"• Handle {profile['Total Missing']} missing values."
            )

        if profile["Quality Score"] >= 95:
            recommendations.append(
                "• Dataset quality is excellent and ready for analysis."
            )
        elif profile["Quality Score"] >= 85:
            recommendations.append(
                "• Dataset quality is good, but minor cleaning is recommended."
            )
        else:
            recommendations.append(
                "• Dataset quality is low. Perform data cleaning before analysis."
            )

        for recommendation in recommendations:
            st.info(recommendation)

    except Exception as e:
        st.error(f"Error while processing file: {e}")

else:
    st.info("👆 Upload a CSV or Excel file to get started.")
    print("-")