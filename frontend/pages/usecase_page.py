import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from components.card import usecase_card

page_config()

header()

sidebar()

st.title("Use Cases")

usecases = st.session_state.get("ucs")

if len(usecases) == 0:
  st.markdown("No Use Cases in the System")
elif usecases[0].get("error") != None:
  st.error("Erro Interno")
else:
  for ucs in usecases:
    usecase_card(ucs)

footer()
