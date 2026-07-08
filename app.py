import streamlit as st

home = st.Page("home.py", title="메인 페이지", icon="❤️" )
page1 =  st.Page("page_1.py", title="1페이지", icon="💕")
page2 =  st.Page("page_2.py", title="2페이지",icon="😍")
page3 =  st.Page("page_3.py", title="3페이지",icon="😒")

pages = st.navigation([home,page1,page2,page3],position="sidebar")
st.sidebar.button("눌러눌러")

pages.run()