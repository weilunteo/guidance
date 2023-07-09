### EXPERIMENTING WTIH NEW CODE ### 
### ### ### ### ### ### ### ### ### 


__version__ = "1.15.0"
app_name = "Itinerary Builder"

# BOILERPLATE
from dotenv import load_dotenv
import streamlit as st
st.set_page_config(layout='wide', page_icon="🤖", page_title=f'{app_name} {__version__}')
ss = st.session_state

# LAYOUT
def main():
    load_dotenv()
    st.title("Testing Interface")
    st.write("Head to the pages")
    
if __name__ == '__main__':
    main()

