import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from utils.generation_alias import generate_all

page_config()

header()

sidebar()

input = st.text_area("Enter the system text")

gen_all_button = st.button("Generate All Artifacts")
if gen_all_button:
  if input == None or input == "":
    st.error("Empty Input")
  else:
    generate_all(input)
  gen_all_button = False

# if st.button("Create Use Cases"):
#   st.text(f"Use Cases Created with {input}")
# if st.button("Create Classes"):
#   st.text(f"Classes Created with {input}")
# if st.button("Create Non Functional Requirements"):
#   st.text("WIP")
# if st.button("Create Business Rules"):
#   st.text("WIP")
