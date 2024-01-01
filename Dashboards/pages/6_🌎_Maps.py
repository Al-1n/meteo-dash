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

#Define columns
colh1, colh2 = st.columns((4,2))
colh1.markdown("## Global Meteorite Landings")
colh2.markdown("")  # this will be overwritten in the app

##Second Row - Map and Data

#Define columns
col1, col2 = st.columns ((8,4))

#Footer
footer = st.container()
footer.write("Meteorite Landings from 1830 to 2013")

#Define year range
min_year = int(df_183['year'].min())
max_year = int(df_183['year'].max())

# The first column contains the map
import plotly.graph_objs as go

# The first column contains the map
with col1:
    # get the year with a slider
    st.session_state['year'] = st.slider('Select year', min_year, max_year, key="year_slider")

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
        #size='mass (g)',
        size_max = 27,  # Adjust as needed to control the maximum marker size
        labels={'Type': 'Type', 'mass (g)': 'Mass (g)'},
        title='Global Meteorite Landings',
        template='plotly_dark',
        projection=p,
        scope='world',
        hover_data={'Type': True, 'mass (g)': ':,.2f'},  # Include 'Type' and 'mass (g)' in the hover box
    )

    # update layout
    fig.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0})  # maximize the figure size

    # plot the map
    st.plotly_chart(fig, use_container_width=True)


countries = df_183['country'].unique()

# The second column contains a selector for countries and a data table
# set the header with the new year data
landings = df_183[df_183['year']==st.session_state['year']]['name'].count()
colh2.metric(label=f"__Total landings for {st.session_state['year']}__", value=landings)

with col2:
    # add/subtract from the selected countries
    selected_countries = st.multiselect('Add a country:', countries)

    if not selected_countries:
        # If no country is selected, find the first country with non-null entries for the given year
        default_country = df_183[df_183['year'] == st.session_state['year']]['country'].dropna().iloc[0]
        selected_countries = [default_country]

    with st.container():
        table = df_183[df_183['year'] == st.session_state['year']]
        st.dataframe(table[table['country'].isin(selected_countries)], use_container_width=True)






