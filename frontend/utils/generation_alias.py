import streamlit as st
import requests

def generate_all(input: str):
  try:
    if input == "":
      raise SyntaxError()

    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.post(url=f"{BACKEND_URL}/ai/run_all/", data={"input_text": input})

    return response.json()
  except:
    return {}