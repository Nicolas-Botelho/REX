import streamlit as st
from pathlib import Path

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from utils.download_alias import download_json

page_config()

header()

sidebar()

st.title("Downloads")

extension = st.selectbox("Select the File Extension", ["JSON"])
generate_file_button = st.button(f"Generate {extension} File")
if generate_file_button:
  match extension.lower():
    case "json":
      download_json()
  try:
    download_button = st.download_button(
      label=f"Download {extension} File",
      data=open(f"../out/output.{extension.lower()}"),
      file_name=f"output.{extension.lower()}"
    )
  except:
    st.markdown("The selected format does not have a file")
  generate_file_button = False

footer()