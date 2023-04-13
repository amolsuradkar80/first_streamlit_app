import pandas as pd
import json
import streamlit as st
from snowflake.snowpark import Session
import time
st.title("My Forecasting App ")

st.session_state.snowflake_connection = Session.builder.configs(**streamlit.secrets["snowflake"]).create()
session = st.session_state.snowflake_connection


st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.experimental_data_editor`.")

def get_dataset():
    # load messages df
    df = session.table("PREDICTIONS")

    return df

dataset = get_dataset()

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.experimental_data_editor(dataset, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

# if submit_button:
#     try:
#         session.write_pandas(edited, "ESG_SCORES_DEMO", overwrite=True)
#         st.success("Table updated")
#         time.sleep(5)
#     except:
#         st.warning("Error updating table")
#     #display success message for 5 seconds and update the table to reflect what is in Snowflake
#     st.experimental_rerun()
