import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* Main App */
        .stApp{
            background-color:#F5F7FA;
        }

        /* Header */
        .main-header{
            background:linear-gradient(90deg,#2563EB,#1D4ED8);
            padding:22px;
            border-radius:14px;
            color:white;
            margin-bottom:25px;
            box-shadow:0 6px 18px rgba(0,0,0,0.15);
        }

        .main-header h1{
            margin:0;
            font-size:36px;
            font-weight:700;
        }

        .main-header p{
            margin-top:8px;
            font-size:17px;
            color:#E5E7EB;
        }

        /* Section Title */
        .section-title{
            font-size:28px;
            font-weight:bold;
            color:#1F2937;
            margin-top:25px;
            margin-bottom:15px;
        }

        /* Sidebar */
        section[data-testid="stSidebar"]{
            background:#111827;
        }

        section[data-testid="stSidebar"] *{
            color:white;
        }

        /* Buttons */
        .stButton>button{
            width:100%;
            border-radius:10px;
            height:45px;
            font-weight:600;
            background:#2563EB;
            color:white;
            border:none;
        }

        .stButton>button:hover{
            background:#1D4ED8;
        }

        /* Metric Cards */
        div[data-testid="metric-container"]{
            background:white;
            border-radius:12px;
            padding:12px;
            box-shadow:0 2px 10px rgba(0,0,0,.08);
            border-left:6px solid #2563EB;
        }

        /* Charts */
        .stPlotlyChart{
            background:white;
            border-radius:12px;
            padding:12px;
            box-shadow:0 2px 10px rgba(0,0,0,.08);
        }

        </style>
        """,
        unsafe_allow_html=True
    )