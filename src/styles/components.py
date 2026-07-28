import streamlit as st


def section_title(icon, title):
    st.markdown(
        f"""
        <div style="
            margin-top:20px;
            margin-bottom:15px;
            font-size:30px;
            font-weight:700;
            color:#1f2937;
        ">
            {icon} {title}
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, value):
    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:18px;
            padding:22px;
            box-shadow:0 8px 20px rgba(0,0,0,.08);
            text-align:center;
            height:140px;
        ">

        <div style="
            color:#6b7280;
            font-size:16px;
            font-weight:600;
        ">
        {title}
        </div>

        <div style="
            margin-top:18px;
            font-size:34px;
            font-weight:700;
            color:#2563eb;
        ">
        {value}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )