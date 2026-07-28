import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

/* Background */

.stApp{

background:#f5f7fb;

}

/* Card */

.dashboard-card{

background:white;

padding:22px;

border-radius:18px;

box-shadow:0px 8px 24px rgba(0,0,0,.08);

margin-bottom:20px;

transition:.3s;

}

.dashboard-card:hover{

transform:translateY(-4px);

box-shadow:0px 12px 30px rgba(0,0,0,.12);

}

/* KPI */

.metric-card{

background:linear-gradient(135deg,#2563eb,#3b82f6);

padding:20px;

border-radius:16px;

color:white;

text-align:center;

}

/* Buttons */

.stButton>button{

width:100%;

border-radius:12px;

height:45px;

border:none;

background:#2563eb;

color:white;

font-weight:600;

}

.stButton>button:hover{

background:#1d4ed8;

}

/* Inputs */

.stTextInput input{

border-radius:10px;

}

/* Sidebar */

[data-testid="stSidebar"]{

background:#ffffff;

border-right:1px solid #e5e7eb;

}

</style>
""",
        unsafe_allow_html=True,
    )