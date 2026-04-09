import streamlit as st
import requests

def load_class():
  loaded_classes = load("classes", "class")
  # size = len(loaded_classes)
  return loaded_classes

def load_enum():
  loaded_enums = load("classes", "enum")
  # size = len(loaded_enums)
  return loaded_enums

def load_usecases():
  loaded_ucs = load("use_cases", "usecase")
  # size = len(loaded_ucs)
  return loaded_ucs

def load_usecase_actor():
  loaded_actors =  load("use_cases", "actor")
  # size = len(loaded_actors)
  return loaded_actors

def load(module: str, cls: str):
  BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

  response = requests.get(url=f"{BACKEND_URL}/{module}/{cls}/")  

  return response.json()

def load_to_session():
  classes = load_class()
  enums = load_enum()
  ucs = load_usecases()
  actors = load_usecase_actor()

  st.session_state = {
      "classes" : classes,
      "enums" : enums,
      "ucs" : ucs,
      "actors" : actors,
      "prim_attrs": [],
      "enum_attrs": [],
      "relations": []
    }