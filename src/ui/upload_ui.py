import streamlit as st

from src.upload.upload_csv import load_csv
from src.database.upload_table import upload_dataframe
#from src.database.table_manager import get_table_names
from src.schema.schema_detector import get_schema


def upload_section():

    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        uploaded_df = load_csv(uploaded_file)

        st.success("✅ Dataset uploaded successfully!")

        st.write("### Preview")
        st.dataframe(uploaded_df.head())

        st.write("### Dataset Information")

        st.write(f"Rows: {uploaded_df.shape[0]}")
        st.write(f"Columns: {uploaded_df.shape[1]}")

        st.write("### Column Names")
        st.write(uploaded_df.columns.tolist())

        dtype_df = uploaded_df.dtypes.astype(str).reset_index()
        dtype_df.columns = ["Column", "Data Type"]

        st.dataframe(dtype_df)

        st.subheader("Upload Dataset to PostgreSQL")
        default_table_name = (
            uploaded_file.name
            .replace(".csv", "")
            .replace(" ", "_")
            .lower()
        )

        table_name = st.text_input(
            "Table Name",
            value=default_table_name
        )

        if st.button("Upload to PostgreSQL"):

            upload_dataframe(uploaded_df, table_name)

            # Save active table
            st.session_state["active_table"] = table_name

            st.success(f"✅ '{table_name}' uploaded successfully!")

            schema = get_schema(table_name)

            st.subheader("Detected Schema")

            st.table(schema)

        return uploaded_df, table_name

    return None, None