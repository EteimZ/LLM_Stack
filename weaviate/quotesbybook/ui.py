import streamlit as st
from client import client

"""
# QuotesByBooks
"""

query = st.text_input("Provide a query:")
limit = st.slider('Provide a limit:', 1, 10, 1)
if st.button("Search"):
    
    nearText = {"concepts": [query]}
    
    response = (
        client.query
        .get("QuotesByBook", ["author", "quote"])
        .with_near_text(nearText)
        .with_limit(limit)
        .do()
    )
    
    st.json(response)

