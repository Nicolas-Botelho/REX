import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from components.card import usecase_card

from utils.loader import load_usecases

page_config()

header()

sidebar()

st.title("Use Cases")

for ucs in st.session_state.get("ucs"):
  usecase_card(ucs)

footer()