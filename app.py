import streamlit as st
import plotly.express as px

from preprocessing.data_loader import load_data
from preprocessing.profiling import dataset_profile
from preprocessing.cleaning import (
    remove_duplicates,
    fill_missing_values,
    standardize_text,
)
from utils.quality import calculate_quality

st.set_page_config(
    page_title="AI Business Analyst Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst Assistant")
st.markdown("### Upload your CSV or Excel file to begin analysis")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
        profile = dataset_profile(df)

        st.success("✅ Dataset Loaded Successfully!")

        st.subheader("📌 Dataset Overview")
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Rows", profile["Rows"])
        c2.metric("Columns", profile["Columns"])
        c3.metric("Missing Values", profile["Total Missing"])
        c4.metric("Duplicate Rows", profile["Duplicate Rows"])
        c5.metric("Quality Score", f"{profile['Quality Score']}%")

        st.divider()

        st.subheader("📄 Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.divider()

        st.subheader("📊 Missing Value Analysis")
        missing_df = profile["Missing Values"].reset_index()
        missing_df.columns = ["Column", "Missing Values"]
        st.dataframe(missing_df, use_container_width=True)

        fig = px.bar(
            missing_df,
            x="Column",
            y="Missing Values",
            title="Missing Values by Column",
            text="Missing Values",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("📑 Data Types")
        dtype_df = profile["Data Types"].reset_index()
        dtype_df.columns = ["Column", "Data Type"]
        st.dataframe(dtype_df, use_container_width=True)

        st.divider()

        st.subheader("📈 Summary Statistics")
        st.dataframe(profile["Summary"], use_container_width=True)

        st.divider()

        # -----------------------------
        # Data Cleaning Center
        # -----------------------------
        st.subheader("🧹 Data Cleaning Center")

        remove_dup = st.checkbox("Remove Duplicate Rows")
        standardize = st.checkbox("Standardize Text")

        numeric_method = st.radio(
            "Numeric Missing Values",
            ["mean", "median", "mode", "drop"],
            horizontal=True,
        )

        text_method = st.radio(
            "Text Missing Values",
            ["mode", "unknown", "drop"],
            horizontal=True,
        )

        if st.button("🚀 Clean Dataset"):
            before = calculate_quality(df)

            cleaned_df = df.copy()

            duplicates_removed = 0
            missing_filled = 0
            text_columns = 0

            if remove_dup:
                cleaned_df, duplicates_removed = remove_duplicates(cleaned_df)

            cleaned_df, missing_filled = fill_missing_values(
                cleaned_df,
                numeric_method=numeric_method,
                text_method=text_method,
            )

            if standardize:
                cleaned_df, text_columns = standardize_text(cleaned_df)

            after = calculate_quality(cleaned_df)

            st.success("✅ Dataset cleaned successfully!")

            st.subheader("📊 Before vs After")
            b1, b2 = st.columns(2)

            with b1:
                st.markdown("### Before")
                st.metric("Rows", before["rows"])
                st.metric("Missing", before["missing"])
                st.metric("Duplicates", before["duplicates"])
                st.metric("Quality", f"{before['quality']}%")

            with b2:
                st.markdown("### After")
                st.metric("Rows", after["rows"])
                st.metric("Missing", after["missing"])
                st.metric("Duplicates", after["duplicates"])
                st.metric("Quality", f"{after['quality']}%")

            st.divider()

            st.subheader("🧹 Cleaning Report")
            r1, r2, r3 = st.columns(3)
            r1.metric("Duplicates Removed", duplicates_removed)
            r2.metric("Missing Values Filled", missing_filled)
            r3.metric("Text Columns Standardized", text_columns)

            st.subheader("🧹 Cleaned Dataset")
            st.dataframe(cleaned_df, use_container_width=True)

            csv = cleaned_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Cleaned CSV",
                data=csv,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
            )

        st.divider()

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
