import streamlit as st

from components.page_config import page_config
from utils.loader import load_to_session

page_config()

load_to_session()

from pages import home_page