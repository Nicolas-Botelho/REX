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

footer()

st.title("Use Cases")

usecases = load_usecases()

if len(usecases) == 0:
  st.markdown("No Use Cases in the System")
elif usecases[0].get("error") != None:
  st.error("Erro Interno")
else:
  for ucs in usecases:
    usecase_card(ucs)