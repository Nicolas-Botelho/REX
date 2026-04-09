import streamlit as st
import requests

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from components.card import class_card

from utils.loader import load_class

page_config()

header()

sidebar()

footer()

st.title("Classes")

classes = load_class()

if len(classes) == 0:
  st.markdown("No Classes in the System")
elif classes[0].get("error") != None:
  st.error("Erro Interno")
else:
  for cls in classes:
    class_card(cls)

# data dict with the response
# list of cards with the classes
# each card opens all the details
# cards can be changed clicking on the card links
# classes, attributes, relations can be CRUDed from the cards