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

st.title("Classes")

st.page_link(page="./pages/class_new.py", label="Create New Class")

for cls in st.session_state.get("classes"):
  class_card(cls)

# data dict with the response
# list of cards with the classes
# each card opens all the details
# cards can be changed clicking on the card links
# classes, attributes, relations can be CRUDed from the cards

footer()