import streamlit as st
from main import text_similarity

strval = "Ad sales boost Time Warner profit  Quarterly profits at US media giant TimeWarner jumped 76% to $1.13bn (£600m) for the three months to December, from $639m year-earlier.  The firm, which is now one of the biggest investors in Google, benefited from sales of high-speed internet connections and higher advert sales. TimeWarner said fourth quarter sales rose 2% to $11.1bn from $10.9bn. Its profits were buoyed by one-off gains which offset a profit dip at Warner Bros, and less users for AOL.".replace(
    "$", "\$"
)
st.markdown(strval)

summary = st.text_input("Summary", "")
if summary:
    text_similarity(summary, strval)
