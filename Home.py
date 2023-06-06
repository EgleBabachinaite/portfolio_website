import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")

content = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas.
"""
st.write(content)

st.subheader("Our Team")

df = pd.read_csv("data.csv", sep=",")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.text(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.text(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:13].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.text(row["role"])
        st.image("images/" + row["image"])
