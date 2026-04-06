import streamlit as st

# show the class inside the conteiner
def class_card(dicio: dict):
  with st.container(border=True):
    st.markdown(
f"""
### {dicio.get("name")}
""")

    st.page_link(page="./pages/class_desc_page.py", label="Expand", query_params={'id' : dicio.get('id')})

def enum_card(dicio: dict):
  with st.container(border=True):
    st.markdown(
f"""
### {dicio.get("name")}
""")

    st.page_link(page="./app.py", label="Expand", query_params={'id' : dicio.get('id')})

def usecase_card(dicio: dict):
  with st.container(border=True):
    st.markdown(
f"""
### {dicio.get("name")}
""")

    st.page_link(page="./app.py", label="Expand", query_params={'id' : dicio.get('id')})

def actor_card(dicio: dict):
  with st.container(border=True):
    st.markdown(
f"""
### {dicio.get("name")}
""")

    st.page_link(page="./app.py", label="Expand", query_params={'id' : dicio.get('id')})