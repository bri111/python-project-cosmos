import streamlit as st

def grid_layout():
    # Add custom CSS to stretch the sections and add borders
    st.markdown(
        """
        <style>
        .stBlock {
            border: 2px solid #ff6347;  /* Border color (tomato) */
            padding: 20px;
            margin: 10px;
            height: 100%;  /* Stretch height */
        }
        .stColumn {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the first row with two grid cells
    row1_col1, row1_col2 = st.columns([2, 1])

    # First row, first cell
    with row1_col1:
        st.markdown('<div class="stBlock">Globe</div>', unsafe_allow_html=True)

    # First row, second cell
    with row1_col2:
        st.markdown('<div class="stBlock">Table:</div>', unsafe_allow_html=True)
        st.write("B | A | C | D | E")
        st.write("------------")
        for _ in range(4):  # Simulate table rows
            st.write("Data | Data | Data | Data | Data")

    # Create the second row with two grid cells (bottom part of the grid)
    row2_col1, row2_col2 = st.columns(2)

    # Second row, first cell
    with row2_col1:
        st.markdown('<div class="stBlock">Bottom Left Content</div>', unsafe_allow_html=True)

    # Second row, second cell
    with row2_col2:
        st.markdown('<div class="stBlock">Bottom Right Content</div>', unsafe_allow_html=True)

# Run the layout
grid_layout()
