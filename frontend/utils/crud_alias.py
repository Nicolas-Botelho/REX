import streamlit as st
import requests

def get(module: str, cls: str, id: int):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.get(url=f"{BACKEND_URL}/{module}/{cls}/{id}")

    return response.json()
  except:
    return {}
  
def create(module: str, cls: str, id: int, body: dict):
  pass

def update(module: str, cls: str, id: int, body: dict):
  pass

def delete(module: str, cls: str, id: int):
  pass

def set(module: str, cls: str, id: int, body: dict):
  pass