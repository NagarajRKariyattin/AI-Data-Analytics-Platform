from preprocessing.cleaning import (
    remove_duplicates,
    fill_missing_values,
    standardize_text
)

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from preprocessing.data_loader import load_data
from preprocessing.profiling import dataset_profile


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="AI Business Analyst Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst Assistant")
st.markdown("### Upload your CSV or Excel file to begin analysis")


# ----------------------------------------------------
# File Upload
# ----------------------------------------------------
uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)


# ----------------------------------------------------
# Process Uploaded File
# ----------------------------------------------------
if uploaded_file is not None:

    try:

        # Load Data
        df = load_data(uploaded_file)

        # Profile Data
        profile = dataset_profile(df)

        st.success("✅ Dataset Loaded Successfully!")

        # ==================================================
        # Dataset Overview
        # ==================================================
        st.subheader("📌 Dataset Overview")

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("Rows", profile["Rows"])
        c2.metric("Columns", profile["Columns"])
        c3.metric("Missing Values", profile["Total Missing"])
        c4.metric("Duplicate Rows", profile["Duplicate Rows"])
        c5.metric("Quality Score", f"{profile['Quality Score']}%")

        st.divider()

        # ==================================================
        # Dataset Preview
        # ==================================================
        st.subheader("📄 Dataset Preview")

        st.dataframe(df, use_container_width=True)

        st.divider()

        # ==================================================
        # Missing Values
        # ==================================================
        st.subheader("📊 Missing Value Analysis")

        missing_df = profile["Missing Values"].reset_index()
        missing_df.columns = ["Column", "Missing Values"]

        st.dataframe(
            missing_df,
            use_container_width=True
        )

        fig = px.bar(
            missing_df,
            x="Column",
            y="Missing Values",
            text="Missing Values",
            title="Missing Values by Column"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ==================================================
        # Data Types
        # ==================================================
        st.subheader("📑 Data Types")

        dtype_df = profile["Data Types"].reset_index()
        dtype_df.columns = ["Column", "Data Type"]

        st.dataframe(
            dtype_df,
            use_container_width=True
        )

        st.divider()

        # ==================================================
        # Summary Statistics
        # ==================================================
        st.subheader("📈 Summary Statistics")

        st.dataframe(
            profile["Summary"],
            use_container_width=True
        )

        st.divider()

                # ==================================================
        # Data Cleaning Center
        # ==================================================

        st.divider()

        st.header("🧹 Data Cleaning Center")

        st.markdown("Choose how you want to clean your dataset.")

        remove_dup = st.checkbox(
            "Remove Duplicate Rows",
            value=True
        )

        standardize = st.checkbox(
            "Standardize Text Columns",
            value=True
        )

        st.markdown("### Numeric Missing Values")

        numeric_method = st.radio(
            "",
            ["mean", "median", "mode", "drop"],
            horizontal=True,
            index=1,
            key="numeric_method"
        )

        st.markdown("### Text Missing Values")

        text_method = st.radio(
            "",
            ["mode", "unknown", "drop"],
            horizontal=True,
            key="text_method"
        )

        st.divider()

        if st.button("🚀 Clean Dataset", use_container_width=True):
            ##guage----------------------------------------------------
            
#----------------------------------------------------------------------------------------------
            cleaned_df = df.copy()

            duplicates_removed = 0
            missing_filled = 0
            text_columns = 0

            # Remove Duplicates
            if remove_dup:
                cleaned_df, duplicates_removed = remove_duplicates(cleaned_df)

            # Fill Missing Values
            cleaned_df, missing_filled = fill_missing_values(
                cleaned_df,
                numeric_method=numeric_method,
                text_method=text_method
            )

            # Standardize Text
            if standardize:
                cleaned_df, text_columns = standardize_text(cleaned_df)

            st.success("✅ Dataset cleaned successfully!")
            

            st.subheader("📋 Cleaning Report")

            col1, col2, col3 = st.columns(3)

            col1.metric("Duplicates Removed", duplicates_removed)
            col2.metric("Missing Values Filled", missing_filled)
            col3.metric("Text Columns Standardized", text_columns)

            st.divider()

            st.subheader("📄 Cleaned Dataset")

            st.dataframe(
                cleaned_df,
                use_container_width=True
            )
            csv = cleaned_df.to_csv(index=False).encode("utf-8")

            st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv",
            
)

        # ==================================================
        # AI Recommendation
        # ==================================================
        st.subheader("🤖 AI Recommendation")

        recommendations = []

        if profile["Duplicate Rows"] > 0:
            recommendations.append(
                f"Remove {profile['Duplicate Rows']} duplicate rows."
            )

        if profile["Total Missing"] > 0:
            recommendations.append(
                f"Handle {profile['Total Missing']} missing values."
            )

        if profile["Quality Score"] >= 95:
            recommendations.append(
                "Dataset quality is excellent and ready for analysis."
            )

        elif profile["Quality Score"] >= 85:
            recommendations.append(
                "Dataset quality is good, but minor cleaning is recommended."
            )

        else:
            recommendations.append(
                "Dataset quality is low. Perform data cleaning before analysis."
            )

        for item in recommendations:
            st.info(item)

    except Exception as e:

        st.error(f"❌ Error : {e}")

else:

    st.info("👆 Upload a CSV or Excel file to begin.")
    
