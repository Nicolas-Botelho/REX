import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer

page_config()

header()

sidebar()

st.text("A requirement management tool with a requirement from text extraction.")

footer()