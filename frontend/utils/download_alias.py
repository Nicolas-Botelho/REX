import streamlit as st
import requests

def download_json():
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    requests.get(url=f"{BACKEND_URL}/json/json_generator/")

    return {"status": 201}
  except:
    return {"status": 400}