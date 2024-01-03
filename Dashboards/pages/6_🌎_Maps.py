import streamlit as st
import pandas as pd
import plotly.express as px

##Page setup
#Set layout
st.set_page_config(layout="wide")

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


#create a function that generates custom KPI style info cards 
def info_card(title, value, icon):
    wch_colour_box = (239, 248, 247)
    wch_colour_font = (0,0,0)
    fontsize = 16
    valign = "left"
    iconname = icon
    sline = value
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.4.0/css/all.css" crossorigin="anonymous">'
    i = title

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                  {wch_colour_box[1]}, 
                                                  {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                       {wch_colour_font[1]}, 
                                       {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px;
                            padding-right: 12px;
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:45px;'>
                            <span style="color: #aaf0d1;"> <i class='fa-fw {iconname} fa-2xl'></i></span> {i}
                            </style><BR><span style='font-size: 24px; 
                            margin-top: 0; color:green;'>{sline}</style></span></p>"""

    return st.markdown(lnk + htmlstr, unsafe_allow_html=True)

#Load the data
@st.cache_data
def get_data():
    df_183 = pd.read_csv('../Data/fell_df_known_mass_after_1830.csv', index_col = [0])    
    return df_183

df_183 = get_data()

# initialise the year if not already set
if 'year' not in st.session_state:
    st.session_state['year'] = 1830

##First Row - Header Section

#Define year range
min_year = int(df_183['year'].min())
max_year = int(df_183['year'].max())

#Define columns
colh1, colh2 = st.columns((4,2), gap = "large")

with colh1:
    st.markdown("## Global Meteorite Landings")

    # get the year with a slider
    st.session_state['year'] = st.slider('Select year', min_year, max_year, key="year_slider")

with colh2:
    st.markdown("")  # this will be overwritten in the app

##Second Row - Map and Data

#Define columns
col1, col2 = st.columns ((8,4), gap = "large")

#Footer
footer = st.container()
footer.write("Meteorite Landings from 1830 to 2013")

# The first column contains the map
import plotly.graph_objs as go

# The first column contains the map
with col1:    
    # set projection
    p = 'equirectangular'   # default projection

    # Filter data based on the selected year
    filtered_df = df_183[df_183['year'] == st.session_state['year']]

    # Create a color scale for mass
    color_scale = px.colors.sequential.Plasma  # Choose a suitable color scale

    # Create scatter_geo trace with color scale and hover data
    fig = px.scatter_geo(
        filtered_df,
        lon='longitude',
        lat='latitude',
        color='Type',
        color_continuous_scale=color_scale,        
        size_max = 27,  # Adjust as needed to control the maximum marker size        
        template='plotly_dark',
        projection=p,
        scope='world',
        custom_data = [filtered_df['name'], filtered_df['country'], filtered_df['mass (g)']],
    )

    fig.update_traces(hoverinfo = "text",                          
                          opacity = 0.8,
                         hovertemplate = "<br>".join([                             
                             "Name: %{customdata[0]}",
                             "Country: %{customdata[1]}",                             
                             "Mass in grams: %{customdata[2]}"
            ]))

    # update layout
    fig.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0})  # maximize the figure size

    # plot the map
    st.plotly_chart(fig, use_container_width=True)

countries = df_183['country'].unique()

# The second column contains a selector for countries and a data table
# set the header with the new year data
landings = df_183[df_183['year']==st.session_state['year']]['name'].count()
#colh2.metric(label=f"__Total landings for {st.session_state['year']}__", value=landings)
with colh2:
    info_card(f"Total landings for {st.session_state['year']}", landings, "fa fa-globe")

with col2:
    # add/subtract from the selected countries
    st.markdown(" ")
    st.markdown(" ")
    selected_countries = st.multiselect('Add a country:', countries)

    if not selected_countries:
        # If no country is selected, find the first country with non-null entries for the given year
        default_country = df_183[df_183['year'] == st.session_state['year']]['country'].dropna().iloc[0]
        selected_countries = [default_country]

    with st.container():
        st.markdown("### Data")
        table = df_183[df_183['year'] == st.session_state['year']]
        st.dataframe(table[table['country'].isin(selected_countries)], use_container_width=True)


#DEFINE A SIDEBAR MASS UNIT CONVERTER

# Conversion factors
CONVERSION_FACTORS = {
    'mg': {
        'g': 0.001,
        'kg': 0.000001,
        'lb': 0.00000220462,
        'oz': 0.000035274,
        'ton': 1e-9,
    },
    'g': {
        'mg': 1000,
        'kg': 0.001,
        'lb': 0.00220462,
        'oz': 0.035274,
        'ton': 1e-6,
    },
    'kg': {
        'mg': 1000000,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274,
        'ton': 0.001,
    },
    'lb': {
        'mg': 453592,
        'g': 453.592,
        'kg': 0.453592,
        'oz': 16,
        'ton': 0.000453592,
    },
    'oz': {
        'mg': 28349.5,
        'g': 28.3495,
        'kg': 0.0283495,
        'lb': 0.0625,
        'ton': 2.835e-5,
    },
    'ton': {
        'mg': 1e9,
        'g': 1e6,
        'kg': 1000,
        'lb': 2204.62,
        'oz': 35274,
    },
}

def convert_mass(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factor = CONVERSION_FACTORS[from_unit][to_unit]
    return value * conversion_factor

#Horizontal line separator            
st.sidebar.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)         

# Streamlit app
st.sidebar.title("Mass Unit Converter")

# Input
value = st.sidebar.number_input("Enter the value", min_value=0.0, step=0.1, value=0.0)
from_unit = st.sidebar.selectbox("From", ['mg', 'g', 'kg', 'lb', 'oz', 'ton'], index=1)

# Output
to_unit = st.sidebar.selectbox("To", ['mg', 'g', 'kg', 'lb', 'oz', 'ton'], index=2)
converted_value = convert_mass(value, from_unit, to_unit)
st.sidebar.write(f"{value} {from_unit} = {converted_value} {to_unit}")




