import streamlit as st
import requests

def get(module: str, cls: str, id: int):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.get(url=f"{BACKEND_URL}/{module}/{cls}/{id}")

    return response.json()
  except:
    return {}
  
def create(module: str, cls: str, body: dict):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.post(url=f"{BACKEND_URL}/{module}/{cls}", data=body)

    return response.json()
  except:
    return {}

def update(module: str, cls: str, id: int, body: dict):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.patch(url=f"{BACKEND_URL}/{module}/{cls}/{id}", data=body)

    return response.json()
  except:
    return {}

def delete(module: str, cls: str, id: int):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.delete(url=f"{BACKEND_URL}/{module}/{cls}/{id}")

    return response.json()
  except:
    return {}

# def set(module: str, cls: str, id: int, body: dict):
  # pass