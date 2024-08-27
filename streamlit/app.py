import streamlit as st
import pandas as pd
import numpy as np

# Set up the page configuration to use wide layout
st.set_page_config(page_title="Toolbar Alignment", layout="wide")

# Create the toolbar layout with columns
toolbar_columns = st.columns([1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1, 1, 1, 1, 1])

# Add label and input in the same row for each column
with toolbar_columns[0]:
    st.markdown("**UTC**")
    utc_value = st.text_input("", value="", key="utc_input")

with toolbar_columns[1]:
    st.markdown("**MOC**")
    moc_value = st.text_input("", value="", key="moc_input")

with toolbar_columns[2]:
    st.markdown("**MET**")
    met_value = st.text_input("", value="0", key="met_input")

with toolbar_columns[3]:
    st.markdown("**SLT**")
    slt_value = st.text_input("", value="0", key="slt_input")

with toolbar_columns[4]:
    st.markdown("**MJD**")
    mjd_value = st.text_input("", value="0", key="mjd_input")

with toolbar_columns[5]:
    st.markdown("**Mode**")
    mode = st.selectbox("", options=["Choose", "Option 1", "Option 2"], key="mode_select")

# Add buttons to the remaining columns
with toolbar_columns[6]:
    if st.button("Log Review", key="log_review_btn"):
        st.write("Log Review clicked!")

with toolbar_columns[7]:
    if st.button("Log Entry", key="log_entry_btn"):
        st.write("Log Entry clicked!")

with toolbar_columns[8]:
    if st.button("Log In", key="log_in_btn"):
        st.write("Log In clicked!")

with toolbar_columns[9]:
    if st.button("Log Out", key="log_out_btn"):
        st.write("Log Out clicked!")

with toolbar_columns[10]:
    if st.button("B/G Monitor", key="bg_monitor_btn"):
        st.write("B/G Monitor clicked!")

# Create a layout with two main columns for additional content
left_column, right_column = st.columns([2, 3])

# In the left column, add the slider and chart
with left_column:
    st.write("Select a value using the slider:")
    slider_value = st.slider("Choose a number", 0, 100, key="slider_input")

    st.write(f"You selected: {slider_value}")

    # Plot a simple chart
    st.write("Here is a simple line chart:")
    data = pd.DataFrame({
        'Column A': np.random.randn(10),
        'Column B': np.random.randn(10)
    })
    st.line_chart(data)

# In the right column, add additional content or widgets
with right_column:
    st.write("This is a simple example of using Streamlit.")

    # Display a sample dataframe
    st.write("Here is a sample dataframe:")
    st.dataframe(data)
