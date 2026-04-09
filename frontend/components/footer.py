import streamlit as st

def footer():
#   footer=f"""
# <style>
#   a:link , a:visited {{
#     color: {st.get_option('theme.blueTextColor')};
#     background-color: {st.get_option('theme.backgroundColor')};
#   }}

#   a:hover,  a:active {{
#     color: {st.get_option('theme.redTextColor')};
#     background-color: {st.get_option('theme.backgroundColor')};
#   }}

#   .footer {{
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: {st.get_option('theme.backgroundColor')};
#     color: {st.get_option('theme.textColor')};
#     text-align: center;
#   }}
# </style>
# <div class="footer">
#   <p>Developed with ❤ by <a href="https://github.com/Nicolas-Botelho">N. D. Botelho</a></p>
# </div>
#   """

  footer = "Developed with ❤ by [N. D. Botelho](https://github.com/Nicolas-Botelho)"

  st.markdown(footer, text_alignment="center")