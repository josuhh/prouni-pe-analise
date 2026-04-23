import streamlit as st

st.set_page_config(layout="wide")

home_page = st.Page("home_page.py", title="Home", icon="🏠")
graphs_page = st.Page("graphs_page.py", title="Gráficos", icon="📊")
map_page = st.Page("map_page.py", title="Mapa", icon="🧭")

pg = st.navigation([home_page, graphs_page, map_page])

pg.run()
