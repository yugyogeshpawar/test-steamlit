import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'Name': ['Yogesh', 'Raj', 'Tushar'],
    'Score': [85, 92, 98]
})

styled_df = data.style.highlight_max(axis=0)
st.dataframe(styled_df)

st.dataframe(data)
