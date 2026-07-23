from preprocessing.cleaning import (
    remove_duplicates,
    fill_missing_values,
    standardize_text
)

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.quality import calculate_quality

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
        if st.button("🚀 Clean Dataset", use_container_width=True): #-------------------------------------------------------------

            before = calculate_quality(df)
            cleaned_df = df.copy()

# Save cleaned data
            st.session_state["cleaned_df"] = cleaned_df

            duplicates_removed = 0
            missing_filled = 0
            text_columns = 0

            if remove_dup:
                cleaned_df, duplicates_removed = remove_duplicates(cleaned_df)

            cleaned_df, missing_filled = fill_missing_values(
                cleaned_df,
                numeric_method=numeric_method,
                text_method=text_method
            )

            if standardize:
                cleaned_df, text_columns = standardize_text(cleaned_df)

            after = calculate_quality(cleaned_df)

            st.success("✅ Dataset cleaned successfully!")

            st.subheader("📊 Before vs After")
            c1, c2 = st.columns(2)

            with c1:
                st.metric("Rows", before["rows"])
                st.metric("Missing", before["missing"])
                st.metric("Duplicates", before["duplicates"])
                st.metric("Quality", f"{before['quality']}%")

            with c2:
                st.metric("Rows", after["rows"])
                st.metric("Missing", after["missing"])
                st.metric("Duplicates", after["duplicates"])
                st.metric("Quality", f"{after['quality']}%")

                st.divider()
                            # ==================================================
            # Data Quality Gauge
            # ==================================================
            st.subheader("📈 Data Quality Gauge")

            g1, g2 = st.columns(2)

            with g1:
                before_fig = go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        value=before["quality"],
                        title={"text": "Before Cleaning"},
                        gauge={
                            "axis": {"range": [0, 100]},
                            "bar": {"color": "red"},
                            "steps": [
                                {"range": [0, 50], "color": "#ffcccc"},
                                {"range": [50, 80], "color": "#ffe699"},
                                {"range": [80, 100], "color": "#d9ead3"},
                            ],
                        },
                    )
                )

                before_fig.update_layout(height=300)

                st.plotly_chart(
                    before_fig,
                    use_container_width=True
                )

            with g2:
                after_fig = go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        value=after["quality"],
                        title={"text": "After Cleaning"},
                        gauge={
                            "axis": {"range": [0, 100]},
                            "bar": {"color": "green"},
                            "steps": [
                                {"range": [0, 50], "color": "#ffcccc"},
                                {"range": [50, 80], "color": "#ffe699"},
                                {"range": [80, 100], "color": "#d9ead3"},
                            ],
                        },
                    )
                )

                after_fig.update_layout(height=300)

                st.plotly_chart(
                    after_fig,
                    use_container_width=True
                )

            # ==================================================
            # Improvement
            # ==================================================
            improvement = round(
                after["quality"] - before["quality"],
                2
            )

            

            improvement = round(after["quality"]-before["quality"],2)
            st.success(f"🎉 Data Quality Improved by {improvement}%")

            st.dataframe(cleaned_df, use_container_width=True)

            csv = cleaned_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "📥 Download Cleaned CSV",
                csv,
                "cleaned_dataset.csv",
                "text/csv",
                use_container_width=True
            )



# Save the FINAL cleaned dataframe
            st.session_state["cleaned_df"] = cleaned_df
            # ==================================================
            # Interactive Dashboard
            # ==================================================
            

            if "cleaned_df" in st.session_state:

                st.header("📊 Interactive Business Dashboard")
                dashboard_df = st.session_state["cleaned_df"].copy()
            else:
                st.warning("Please clean the dataset first.")
                st.stop()
            # ==================================================
            # Sidebar Filters
            # ==================================================
            # st.sidebar.header("🎛 Dashboard Filters")

            # Category Filter
            # if "Category" in dashboard_df.columns:

            #     category = st.sidebar.selectbox(
            #         "Category",
            #         ["All"] + sorted(
            #             dashboard_df["Category"].dropna().unique().tolist()
            #         ),
            #         key="category_filter"
            #     )

                # if category != "All":
                #     dashboard_df = dashboard_df[
                #         dashboard_df["Category"] == category
                #     ]

            # State Filter
            # if "State" in dashboard_df.columns:

            #     state = st.sidebar.selectbox(
            #         "State",
            #         ["All"] + sorted(
            #             dashboard_df["State"].dropna().unique().tolist()
            #         ),
            #         key="state_filter"
            #     )

                # if state != "All":
                    # dashboard_df = dashboard_df[
                    #     dashboard_df["State"] == state
                    # ]

            st.divider()

            st.info(
                "Dashboard section moved here so 'cleaned_df' is in scope. "
                "Paste the dashboard charts, filters, KPIs and visualizations "
                "below this line, keeping the same indentation."
            )


    except Exception as e:
        st.error(f"❌ Error: {e}")

else:
    st.info("👆 Upload a CSV or Excel file to begin.")
    # ==================================================
# Interactive Dashboard
# ==================================================

if "cleaned_df" in st.session_state:

    st.header("📊 Interactive Business Dashboard")

    dashboard_df = st.session_state["cleaned_df"].copy()

    # ==================================================
    # Sidebar Filters
    # ==================================================

    st.sidebar.header("🎛 Dashboard Filters")

    # Category Filter
    if "Category" in dashboard_df.columns:

        category = st.sidebar.selectbox(
            "Category",
            ["All"] + sorted(
                dashboard_df["Category"]
                .dropna()
                .unique()
                .tolist()
            )
        )

        if category != "All":
            dashboard_df = dashboard_df[
                dashboard_df["Category"] == category
            ]

    # State Filter
    if "State" in dashboard_df.columns:

        state = st.sidebar.selectbox(
            "State",
            ["All"] + sorted(
                dashboard_df["State"]
                .dropna()
                .unique()
                .tolist()
            )
        )

        if state != "All":
            dashboard_df = dashboard_df[
                dashboard_df["State"] == state
            ]

    st.divider()

    # ==================================================
    # Paste all KPI cards below
    # ==================================================

    st.subheader("📌 Business KPIs")

    total_sales = (
        dashboard_df["Sales"].sum()
        if "Sales" in dashboard_df.columns
        else 0
    )

    total_profit = (
        dashboard_df["Profit"].sum()
        if "Profit" in dashboard_df.columns
        else 0
    )

    total_orders = len(dashboard_df)

    average_sales = (
        dashboard_df["Sales"].mean()
        if "Sales" in dashboard_df.columns
        else 0
    )

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("💰 Total Sales", f"{total_sales:,.2f}")
    k2.metric("📈 Total Profit", f"{total_profit:,.2f}")
    k3.metric("🛒 Orders", total_orders)
    k4.metric("📦 Avg Sales", f"{average_sales:,.2f}")

    st.divider()

    # Continue pasting your Category Chart,
    # State Chart,
    # Top Products,
    # Scatter Plot
    # below this line.

