
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

uploaded = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if uploaded:
    ext = pl.get_file_extension(uploaded.name)
    data_frame = pl.load_file(uploaded, ext)
    column_list = pl.get_column_names(data_frame)
    
    display_columns = st.multiselect("Select columns to display", column_list, default=column_list)
    
    if st.toggle("Filter data"):
        col_filters = st.columns(3)
        string_fields = pl.get_columns_of_type(data_frame, 'object')
        filter_field = col_filters[0].selectbox("Select column to filter", string_fields)
        
        if filter_field:
            options = pl.get_unique_values(data_frame, filter_field)
            chosen_option = col_filters[1].selectbox("Select value to filter On", options)
            output = data_frame[data_frame[filter_field] == chosen_option][display_columns]
        else:
            output = data_frame[display_columns]
    else:
        output = data_frame[display_columns]

    st.dataframe(output)
    st.dataframe(output.describe())

