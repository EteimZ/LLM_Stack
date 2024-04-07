import streamlit as st
from client import client

"""
# QuotesByBooks
"""

query = st.text_input("Provide a query:")

with st.sidebar:
    """
    # Query config
    """
    limit = st.slider('limit:', 1, 10, 1, help="Provide a limit to how much data you want returned.")

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

