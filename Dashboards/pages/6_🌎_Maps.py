#################################

      # Meteo Dash

     ## Maps

    ### (c) Alin Airinei, 2024

#################################

#Import the required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

##Page setup
#Set layout
st.set_page_config(layout="wide",
                   page_title = "Maps",
                   page_icon = "🌎")

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


#Create a function that generates custom KPI style info cards 
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
    df_183 = pd.read_csv('../Data/df183.csv', index_col = [0])

    fireball_df = pd.read_csv("../Data/fireball_data.csv", index_col = [0])  
  
    return df_183, fireball_df

df_183, fireball_df = get_data()


#Define the sidebar map selector
st.sidebar.subheader('Meteorite and Fireball Maps')
choice = st.sidebar.selectbox('Choose map', ('Observed Landings', 'Fireball Events'), index = 0)


                                        ### SECTION I ###

#------------------------------------------------------------------------------------------------------------

###########################
   # Observed Landings #
###########################
        
if choice == 'Observed Landings':

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
        st.session_state['year'] = st.slider('Select year', min_year, max_year, value = 1921, key="year_slider")

    with colh2:
        st.markdown("")  # this will be overwritten in the app

    ##Second Row - Map and Data

    #Define columns
    col1, col2 = st.columns ((8,4), gap = "large")

    # The first column contains the map
    import plotly.graph_objs as go

    # The first column contains the map
    with col1:    
        # set projection
        p = 'equirectangular'   # default projection

        #create a column of mass in kilograms for better marker size assignment
        df_183['mass (g)'].fillna(df_183['mass (g)'].min(), inplace = True) #even when the mass is unknown there must be some mass for it 
        df_183['mass (kg)'] = df_183['mass (g)'] / 1000.0

        # Filter data based on the selected year
        filtered_df = df_183[df_183['year'] == st.session_state['year']]
        
        # Create a color scale for mass
        color_scale = px.colors.sequential.Oryel  # Choose a suitable color scale

        # Create scatter_geo trace with color scale and hover data
        fig = px.scatter_geo(
            filtered_df,
            lon='longitude',
            lat='latitude',
            color='Type',
            color_continuous_scale=color_scale,
            size = 'mass (kg)',
            size_max = 10,  # Adjust as needed to control the maximum marker size        
            template='plotly_dark',
            projection=p,
            scope='world',
            custom_data = [filtered_df['name'], filtered_df['country'], filtered_df['mass (g)']],
        )

        fig.update_traces(hoverinfo = "text",                          
                              opacity = 0.8,
                          marker_sizemin = 4,
                             hovertemplate = "<br>".join([                             
                                 "Name: %{customdata[0]}",
                                 "Country: %{customdata[1]}",                             
                                 "Mass in grams: %{customdata[2]}"
                ]))

        # update layout
        fig.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0})  # maximize the figure size

        # plot the map
        st.plotly_chart(fig, use_container_width=True)

        #add explanations
        with st.expander("See explanation", expanded = True):

                    st.markdown("* Move the slider to select a year and display the map of observed impacts for the \
                                selected year.")                                           
                    st.markdown("* The yearly landing locations are sourced from the NASA meteorite landing \
                                :green[[dataset](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data)] \
                                based on The Meteoritical Society catalogue of meteorites.", unsafe_allow_html=True)
                    st.markdown("* No map will be displayed for the years with no catalogued landings and the metric box \
                                in the top right corner will display a total of zero landings (e.g. there are zero \
                                recorded landings for the year 2005).")
                    st.markdown("* If the number of markers on the map and the total count displayed in the metric box do \
                                not coincide it may be that \
                                the default zoom level is causing markers that are close to each other to overlap \
                                (e.g. see the map for the year 1925). Use the zoom in function to identify the overlaping \
                                markers.")
                    st.markdown("* The fact that there are years with few to no observations it does not indicate \
                                a decrease of the influx of material from space. For example, while there are no recorded\
                                meteorite landings for the year 2005, the fireball data from the US Government Sensors\
                                shows peak activity for the same year. For more information choose\
                                **Fireball Events** from the sidebar to explore the fireball data.")

    countries = df_183['country'].unique()

    # The second column contains a selector for countries and a data table
    # set the header with the new year data    
    landings = df_183[df_183['year']==st.session_state['year']]['name'].count()

    with colh2:
        info_card(f"Total landings for {st.session_state['year']}", landings, "fa fa-globe")

    with col2:
        # add/subtract from the selected countries
        st.markdown(" ")
        st.markdown(" ")
        selected_countries = st.multiselect('Add a country:', countries)

        if not selected_countries:
            # If no country is selected, find the first country with non-null entries for the given year
            filtered_df = df_183[df_183['year'] == st.session_state['year']]
            non_null_countries = filtered_df['country'].dropna()
            
            if not non_null_countries.empty:
                default_country = non_null_countries.iloc[0]
                selected_countries = [default_country]
            else:
                selected_countries = []  # No non-null entries found

        with st.container():
            st.markdown("### Landing Data")
            table = df_183[df_183['year'] == st.session_state['year']]
            st.dataframe(table[table['country'].isin(selected_countries)], use_container_width=True)

            #add explanations
            with st.expander("See explanation", expanded = True):

                    st.markdown("* The country selector above will default to the first entry with non-null values.")                                           
                    st.markdown("* To display data for additional regions or specific events add the coresponding country.")
                    st.markdown("* Country names are included in the hover info displayed on the map.")
                    

                                        ### SECTION II ###

#---------------------------------------------------------------------------------------------------------------------------

###########################
    # Fireball Maps #
###########################

elif choice == 'Fireball Events':
       
    # initialise the year if not already set
    if 'year' not in st.session_state:
        st.session_state['year'] = 1988

    ##First Row - Header Section

    #Define year range
    min_year = int(fireball_df['year'].min())
    max_year = int(fireball_df['year'].max())

    #Define columns
    colh1, colh2 = st.columns((4,2), gap = "large")

    with colh1:
        st.markdown("## Fireball Events")

        # get the year with a slider
        st.session_state['year'] = st.slider('Select year', min_year, max_year, value = 2005, key="year_slider")

    with colh2:
        st.markdown("")  # this will be overwritten in the app

    ##Second Row - Map and Data

    #Define columns
    col1, col2 = st.columns ((8,4), gap = "large")
       
    # The first column contains the map
    with col1:    
        # set projection
        p = 'equirectangular'   # default projection

        # Filter data based on the selected year
        filtered_fireball_df = fireball_df[fireball_df['year'] == st.session_state['year']]

        #Create a "frequency by year" subset
        freq_by_year = fireball_df.groupby(['year'])['Latitude (deg.)'].nunique().reset_index(name = 'count')

        # Create a color scale for mass
        color_scale = px.colors.sequential.Oryel  # Choose a suitable color scale

        # Create scatter_geo trace with color scale and hover data
        fig = px.scatter_geo(
            filtered_fireball_df,
            lon='longitude_decimal',
            lat='latitude_decimal',
            color='Calculated Total Impact Energy (kt)',
            color_continuous_scale=color_scale,
            size = 'Calculated Total Impact Energy (kt)',
            size_max = 27,  # Adjust as needed to control the maximum marker size        
            template='plotly_dark',
            projection=p,
            scope='world',
            custom_data = [filtered_fireball_df['country'], filtered_fireball_df['Calculated Total Impact Energy (kt)']],
        )

        fig.update_traces(hoverinfo = "text",
                          opacity = 0.8,
                          marker_sizemin = 3,
                          hovertemplate = "<br>".join([
                                 "Country/Region: %{customdata[0]}",
                                 "Impact Energy (kt): %{customdata[1]}"
                ]))

        # update layout
        fig.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0},
                          coloraxis_colorbar_title_text = 'Energy (kt)')  # maximize the figure size

        #figt.update_layout(coloraxis_colorbar_title_text = 'your title')

        # plot the map
        st.plotly_chart(fig, use_container_width=True)        

        #add explanations
        with st.expander("See explanation", expanded = True):
                                                            
                    st.markdown("* The fireball data was collected by the United States Department of Defense and \
                                made publicaly available through NASA's Center for Near Earth Object Studies\
                                (:green[[cneos](https://cneos.jpl.nasa.gov/fireballs/)])\
                                .", unsafe_allow_html=True)
                    st.markdown("* The frequency of the recorded events has been increasing over the years with 2015\
                                having the highest number of events.")
                    with st.container():

                        col_graph1, col_graph12 = st.columns([34, 1])

                        with col_graph1:
                            

                            fig = go.Figure()

                            # define the plot
                            fig.add_trace(go.Scatter(x = freq_by_year['year'], y= freq_by_year['count'], mode='lines', 
                                                     line=dict(width=1.5),
                                                     hovertemplate='<b>Year:</b> %{x}<br>' +
                                                                   '<b>Count:</b> %{y}<br><extra></extra>'
                                                    ))

                            # set the title
                            fig.update_layout(title=dict(text='<b style="text-align:center">Frequency of fireball events by year</b>'),
                                              title_font_color = 'green',
                                              title_font_size = 16,
                                              title_x = 0.1,
                                              title_y = 0.85,
                                              font=dict(size=16),
                                              xaxis_title='Year',
                                              yaxis_title='Count',
                                              margin=dict(l=0, r=0, b=20, t = 30),
                                              height = 256                                              
                                              )                           

                            # format the ticks to match each decade and rotate the labels
                            fig.update_xaxes(tickmode='linear', tick0=1830, dtick=10)
                            fig.update_xaxes(tickangle=45)

                            st.plotly_chart(fig, use_container_width = True)

                    st.markdown("* The much higher density of fireball events compared to the ground observations should not\
                                automatically lead to the conclusion that there are an enormous amount of unaccounted\
                                meteorite landings even though it may often be the case.")
                    st.markdown("* The survivability of meteorites from preatmospheric masses depends on a number of factors such as\
                                material strength, angle of entry and velocity. While objects with a variety of combinations\
                                of this factors can produce fireballs, many will only land as micrometeorites and spherules\
                                :green[[<sup>1</sup>](https://cneos.jpl.nasa.gov/fireballs/intro.html)]\
                                .", unsafe_allow_html = True)
                    st.markdown("* Furthermore, as the NASA cneos website specifies, the dataset is not a complete list of fireballs\
                                and includes only some of the brightest events. Other sources such as the\
                                :green[[Geostationary Lightning Mapper](https://neo-bolide.ndc.nasa.gov/#/)] (GLM) might show more\
                                events but don't cover as an extensive an area.", unsafe_allow_html=True)
                    st.markdown("* Other sources of fireball data such as ground based camera networks go back to the 1960's but also\
                                do not cover such an extensive area as the USG Sensors and the GLM data\
                                :green[[<sup>2</sup>](https://www.researchgate.net/publication/241238899_Flux_of_Extraterrestrial_Materials)]\
                                .", unsafe_allow_html = True)
                    st.markdown("* The cneos dataset from USG Sensors has made the headlines as it was the basis for detecting the\
                                first known interstellar object(:green[[IM1](https://iopscience.iop.org/article/10.3847/1538-4357/ac8eac/pdf)])\
                                to have crashed into the Earth which led to\
                                :green[[the expedition](https://avi-loeb.medium.com/the-im1-spherules-from-the-pacific-ocean-have-extrasolar-composition-f025cb03dec6)]\
                                by :green[[Galileo Project](https://projects.iq.harvard.edu/galileo/)] in search for spherules around\
                                the impact region.", unsafe_allow_html=True)
                    st.markdown("* To find IM1 on the maps move the slider to the year 2014 and zoom in on the off the coast region\
                                on the right side of Papua New Guinea. One of the fireballs in the region has a calculated impact\
                                energy of 0.11kt. If you identify the same object in the data table on the right, you will notice\
                                that it had a velocity of 44.8 km/s at an altitude of 18.7 km, which is faster than any other object\
                                at similar altitudes with most of the velocity in the vertical direction. Congratulations, you detected the impact\
                                of an object that originated outside the solar system!")

    countries = fireball_df['country'].unique()

    # The second column contains a selector for countries and a data table
    # set the header with the new year data
    landings = fireball_df[fireball_df['year']==st.session_state['year']]['Latitude (deg.)'].count()
    
    with colh2:
        info_card(f"Total fireballs for {st.session_state['year']}", landings, "fa fa-globe")

    with col2:
        # add/subtract from the selected countries
        st.markdown(" ")
        st.markdown(" ")
        selected_countries = st.multiselect('Add a country:', countries)

        if not selected_countries:
            # If no country is selected, find the first country with non-null entries for the given year
            filtered_fireball_df = fireball_df[fireball_df['year'] == st.session_state['year']]
            non_null_countries = filtered_fireball_df['country'].dropna()
            
            if not non_null_countries.empty:
                default_country = non_null_countries.iloc[0]
                selected_countries = [default_country]
            else:
                selected_countries = []  # No non-null entries found

        with st.container():
            st.markdown("### Fireball Data")
            table = fireball_df[fireball_df['year'] == st.session_state['year']]
            st.dataframe(table[table['country'].isin(selected_countries)], use_container_width=True)

            #add explanations
            with st.expander("See explanation", expanded = True):

                    st.markdown("* The country selector above will default to the first entry with non-null values.")                                           
                    st.markdown("* To display data for additional regions or specific events add the coresponding country.")
                    st.markdown("* Country names are included in the hover info displayed on the map.")
                    st.markdown("* Unclaimed regions such as terra nullis and international waters are jointly labeled as\
                                *International*.")

                                        ### ADDITIONAL COMPONENTS ###
                
#---------------------------------------------------------------------------------------------------------------------------

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




