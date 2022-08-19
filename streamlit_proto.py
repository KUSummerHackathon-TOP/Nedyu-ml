import streamlit as st
from main import text_similarity

strval = "Time warner profits from google investing, because google uses adtech, and tuner invested in google"
st.text_area("Article", strval)
summary = st.text_input("Summary", "")

text_similarity(summary, strval)
