 
import streamlit as st
import json
import os

HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.json")
def initialize_history():
    if "history" not in st.session_state:

        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                st.session_state.history = json.load(f)
        else:
            st.session_state.history = []


def add_query(query):

    history = st.session_state.history

    if query in history:
        history.remove(query)

    history.insert(0, query)

    history = history[:10]       

    st.session_state.history = history

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def get_history():
    """
    Return query history.
    """
    return st.session_state.history


def clear_history():
  if st.sidebar.button("🗑 Clear History"):

    st.session_state.history = []

    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

    st.rerun()


def show_history():
    st.sidebar.subheader("📝 Query History")

    history = st.session_state.history

    for query in history:

        if st.sidebar.button(
            query,
            key=f"history_{query}",
            use_container_width=True
        ):
            st.session_state.selected_query = query
            st.rerun()

    if st.sidebar.button("🗑 Clear History"):
        st.session_state.history = []

        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

        st.rerun()
def select_query(query):
    st.session_state.selected_query = query