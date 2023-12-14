import streamlit as st
from PIL import Image

st.set_page_config(layout = "wide",
    page_title="Meteo Dash",
    page_icon="☄️"
)

# define an RGB color
title_color = (89, 89, 89)

# write text with the specified color
st.write(f'<span style="color:rgb{title_color};font-size:36px">Meteorite Impact: A Comprehensive Review of Confirmed Falls between 1830 and 2013</span>', unsafe_allow_html=True)

with st.container():
        
    col1, col2, col3 = st.columns([15,30, 15])

    with col1:
        st.write("")
        st.markdown("## Welcome to Meteo Dash!")
        st.markdown(
        '''


        Use the links on the left to navigate between dashboards.


        '''
        )

    with col2:
        
        st.write("")
        image = Image.open('rdjEnhanced2.jpg')
        st.image(image, caption='Meteor Crater, Arizona')

    with col3:

        st.write("")



