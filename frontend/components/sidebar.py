import streamlit as st

def sidebar():
  with st.sidebar:
    st.page_link("./app.py", label="Home")
    st.page_link("./pages/generation_page.py", label="Generation")
    st.page_link("./pages/download_page.py", label="Download")
    st.page_link("./pages/usecase_page.py", label="Use Cases")
    st.page_link("./pages/class_page.py", label="Classes")
    # st.page_link("./pages/nrf_page.py", label="Non Functional Requirements")
    # st.page_link("./pages/br_pages.py", label="Business Rules")