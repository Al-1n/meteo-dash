import streamlit as st
from PIL import Image

#Page setup
st.set_page_config(layout = "wide",
    page_title="Meteo Dash",
    page_icon="☄️"
)

#Remove blank space
st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top=1, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )

#Remove underlining from links
st.markdown(
        """
            <style type="text/css">
             a {text-decoration:none;}
            </style>""",
        unsafe_allow_html=True,
    )

# define an RGB color
text_color = (126, 126, 126)

image = Image.open('static/rdjEnhanced2.jpg')
st.image(image)

# write title and subtitle
st.write("")
st.markdown("# Welcome to Meteo Dash!")

st.write(f'<span style="color:rgb{text_color};font-size:18px">Meteorite Impact: A Comprehensive Review of Observed and Recovered Falls between 1830 and 2013</span>', unsafe_allow_html=True)
st.markdown(" ")
st.markdown(" ")
# Create columns
col1, col2, col3, col4 = st.columns([17, 17, 17, 49], gap="small")
col5, col6, col7, col8 = st.columns([17, 17, 17, 49], gap="small")

# Define image paths
image_paths = {
    "Type_Statistics": "./app/static/type.jpeg",
    "World_Data": "./app/static/world.jpeg",
    "Time_Series": "./app/static/time.jpeg",
    "Flux_Analysis": "./app/static/flux.jpeg",
    "Mass_Statistics": "./app/static/mass.jpeg",    
    "Maps": "./app/static/maps.jpeg"    
}

# Function to create clickable image links with centered captions
def create_image_link(column, page_name, image_path, page_caption):
    # Set max_height as a percentage of column height
    max_height_percent = 80
    max_height = f"{max_height_percent}%"
    
    # Image
    column.markdown(
        f'<a href="{page_name}" target="_self"><img src="{image_path}" style="max-height: {max_height}; width: 100%; border: 1px"></a>',
        unsafe_allow_html=True,
    )
    
    # Caption as a centered text link with reduced space
    caption = f'<div style="text-align: center; margin-top: -10px; margin-bottom: 20px;"><a href="{page_name}" target="_self">{page_caption}</a></div>'
    column.markdown(caption, unsafe_allow_html=True)

# Main content layout
with st.container():
    create_image_link(col1, "Type_Statistics", image_paths["Type_Statistics"], "Type Statistics")
    create_image_link(col2, "World_Data", image_paths["World_Data"], "World Data")    
    create_image_link(col3, "Time_Series", image_paths["Time_Series"], "Time Series")
    col4.empty()

with st.container():
    create_image_link(col5, "Flux_Analysis", image_paths["Flux_Analysis"], "Flux Analysis")
    create_image_link(col6, "Mass_Statistics", image_paths["Mass_Statistics"], "Mass Statistics")
    create_image_link(col7, "Maps", image_paths["Maps"], "Maps")
    col8.empty()
