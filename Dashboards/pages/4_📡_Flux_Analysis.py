#################################

      # Meteo Dash

     ## Flux Analysis

    ### (c) Alin Airinei, 2024

#################################


#Import the required libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go     
import numpy as np
from plotly.validators.scatter.marker import SymbolValidator

#Page setup
st.set_page_config(layout='wide',
                   page_title = "Flux Analysis",
                   page_icon = "📡"
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


# Define an RGB color (for sutitles)
title_color = (126,126,126)

# Write text with the specified styles and colors
st.write(f'<span style="color:rgb{(255, 255, 255)};font-size:36px">Meteorite Flux Tracker: Analyzing Influx by Month and Year</span>', unsafe_allow_html=True)
st.write(f'<span style="color:rgb{title_color};font-size:16px">Choose a meteorite type from the sidebar to view analysis</span>', unsafe_allow_html=True)



#Define the color palettes
chondrite_colors = ['rgb(122, 112, 108)', 'rgb(189, 91, 64)', 'rgb(199, 155, 34)', 'rgb(184, 158, 133)', 'rgb(157, 108, 132)', 
                    'rgb(166, 108, 27)', 'rgb(172, 121, 93)', 'rgb(129, 84, 76)', 'rgb(234, 149, 83)', 'rgb(173, 149, 131)', 
                    'rgb(214, 133, 98)', 'rgb(157, 104, 80)', 'rgb(155, 124, 107)', 'rgb(98, 108, 148)', 'rgb(100, 125, 109)', 
                    'rgb(187, 112, 126)', 'rgb(200, 165, 140)', 'rgb(183, 141, 42)', 'rgb(155, 152, 104)', 'rgb(149, 157, 162)', 
                    'rgb(196, 125, 94)', 'rgb(98, 107, 125)', 'rgb(131, 123, 115)', 'rgb(114, 135, 152)', 'rgb(113, 127, 138)', 
                    'rgb(229, 147, 148)', 'rgb(230, 176, 13)', 'rgb(199, 110, 44)', 'rgb(224, 169, 144)', 'rgb(121, 164, 194)', 
                    'rgb(181, 142, 78)', 'rgb(215, 112, 47)', 'rgb(216, 139, 118)', 'rgb(218, 190, 124)', 'rgb(128, 163, 164)', 
                    'rgb(132, 180, 188)', 'rgb(132, 156, 180)', 'rgb(208, 158, 122)', 'rgb(221, 164, 98)', 'rgb(205, 115, 98)', 
                    'rgb(108, 156, 156)', 'rgb(177, 175, 182)', 'rgb(192, 168, 149)', 'rgb(165, 122, 40)', 'rgb(204, 100, 76)', 
                    'rgb(145, 52, 19)', 'rgb(182, 68, 116)', 'rgb(244, 212, 52)', 'rgb(164, 173, 188)', 'rgb(158, 148, 172)', 
                    'rgb(204, 140, 122)', 'rgb(193, 146, 111)', 'rgb(194, 164, 71)', 'rgb(153, 154, 44)', 'rgb(175, 141, 100)', 
                    'rgb(142, 104, 40)', 'rgb(182, 95, 86)', 'rgb(143, 144, 148)', 'rgb(186, 87, 29)', 'rgb(173, 80, 53)', 
                    'rgb(132, 124, 164)', 'rgb(217, 165, 152)', 'rgb(205, 182, 135)', 'rgb(212, 92, 60)', 'rgb(217, 134, 78)', 
                    'rgb(189, 127, 15)', 'rgb(84, 168, 98)', 'rgb(196, 140, 174)', 'rgb(148, 133, 121)', 'rgb(169, 159, 31)', 
                    'rgb(204, 182, 98)', 'rgb(239, 163, 122)', 'rgb(174, 66, 17)', 'rgb(84, 140, 178)', 'rgb(178, 163, 155)',
                    'rgb(186, 134, 118)', 'rgb(201, 136, 4)', 'rgb(132, 184, 212)', 'rgb(199, 162, 96)', 'rgb(229, 111, 96)']

achondrite_colors = achondrite_colors = ['rgb(218, 190, 124)', 'rgb(121, 164, 194)', 'rgb(149, 157, 162)', 'rgb(196, 125, 94)', 'rgb(132, 124, 164)', 
                     'rgb(215, 112, 47)', 'rgb(145, 52, 19)', 'rgb(186, 87, 29)', 'rgb(142, 104, 40)', 'rgb(84, 168, 98)', 
                     'rgb(100, 125, 109)', 'rgb(84, 140, 178)', 'rgb(229, 111, 96)', 'rgb(244, 212, 52)', 'rgb(178, 163, 155)', 
                     'rgb(177, 175, 182)', 'rgb(205, 115, 98)', 'rgb(132, 180, 188)', 'rgb(234, 149, 83)', 'rgb(143, 144, 148)', 
                     'rgb(172, 121, 93)', 'rgb(204, 140, 122)', 'rgb(239, 163, 122)', 'rgb(182, 68, 116)', 'rgb(194, 164, 71)',
                     'rgb(201, 136, 4)', 'rgb(175, 141, 100)', 'rgb(129, 84, 76)', 'rgb(204, 100, 76)', 'rgb(187, 112, 126)',
                     'rgb(212, 92, 60)', 'rgb(173, 149, 131)', 'rgb(157, 108, 132)', 'rgb(98, 107, 125)', 'rgb(217, 165, 152)', 
                     'rgb(186, 134, 118)', 'rgb(157, 104, 80)', 'rgb(192, 168, 149)', 'rgb(169, 159, 31)', 'rgb(132, 184, 212)', 
                     'rgb(174, 66, 17)', 'rgb(204, 182, 98)', 'rgb(208, 158, 122)', 'rgb(184, 158, 133)', 'rgb(229, 147, 148)', 
                     'rgb(114, 135, 152)', 'rgb(193, 146, 111)', 'rgb(221, 164, 98)', 'rgb(199, 110, 44)', 'rgb(128, 163, 164)', 
                     'rgb(165, 122, 40)', 'rgb(196, 140, 174)', 'rgb(148, 133, 121)', 'rgb(98, 108, 148)', 'rgb(108, 156, 156)', 
                     'rgb(224, 169, 144)', 'rgb(155, 124, 107)', 'rgb(200, 165, 140)', 'rgb(155, 152, 104)', 'rgb(113, 127, 138)', 
                     'rgb(216, 139, 118)', 'rgb(122, 112, 108)', 'rgb(199, 155, 34)', 'rgb(132, 156, 180)', 'rgb(173, 80, 53)', 
                     'rgb(189, 127, 15)', 'rgb(166, 108, 27)', 'rgb(217, 134, 78)', 'rgb(183, 141, 42)', 'rgb(214, 133, 98)', 
                     'rgb(153, 154, 44)', 'rgb(131, 123, 115)', 'rgb(230, 176, 13)', 'rgb(205, 182, 135)', 'rgb(158, 148, 172)', 
                     'rgb(182, 95, 86)', 'rgb(164, 173, 188)', 'rgb(199, 162, 96)', 'rgb(189, 91, 64)', 'rgb(181, 142, 78)']

new_chondrite_colors = ['rgb(177, 175, 182)', 'rgb(200, 165, 140)', 'rgb(174, 66, 17)', 'rgb(164, 173, 188)', 'rgb(142, 104, 40)', 'rgb(215, 112, 47)', 
                        'rgb(178, 163, 155)', 'rgb(230, 176, 13)', 'rgb(184, 158, 133)', 'rgb(229, 147, 148)', 'rgb(244, 212, 52)', 'rgb(234, 149, 83)', 
                        'rgb(204, 182, 98)', 'rgb(205, 182, 135)', 'rgb(84, 168, 98)', 'rgb(157, 108, 132)', 'rgb(204, 140, 122)', 'rgb(212, 92, 60)', 
                        'rgb(175, 141, 100)', 'rgb(186, 87, 29)', 'rgb(148, 133, 121)', 'rgb(214, 133, 98)', 'rgb(186, 134, 118)', 'rgb(196, 140, 174)', 
                        'rgb(169, 159, 31)', 'rgb(121, 164, 194)', 'rgb(158, 148, 172)', 'rgb(157, 104, 80)', 'rgb(192, 168, 149)', 'rgb(153, 154, 44)', 
                        'rgb(224, 169, 144)', 'rgb(129, 84, 76)', 'rgb(100, 125, 109)', 'rgb(183, 141, 42)', 'rgb(132, 180, 188)', 'rgb(182, 68, 116)', 
                        'rgb(181, 142, 78)', 'rgb(84, 140, 178)', 'rgb(145, 52, 19)', 'rgb(194, 164, 71)', 'rgb(165, 122, 40)', 'rgb(131, 123, 115)', 
                        'rgb(182, 95, 86)', 'rgb(216, 139, 118)', 'rgb(187, 112, 126)', 'rgb(229, 111, 96)', 'rgb(173, 149, 131)', 'rgb(122, 112, 108)', 
                        'rgb(239, 163, 122)', 'rgb(132, 124, 164)', 'rgb(196, 125, 94)', 'rgb(201, 136, 4)', 'rgb(221, 164, 98)', 'rgb(143, 144, 148)', 
                        'rgb(155, 124, 107)', 'rgb(132, 156, 180)', 'rgb(217, 134, 78)', 'rgb(172, 121, 93)', 'rgb(189, 91, 64)', 'rgb(204, 100, 76)', 
                        'rgb(155, 152, 104)', 'rgb(98, 108, 148)', 'rgb(132, 184, 212)', 'rgb(173, 80, 53)', 'rgb(199, 110, 44)', 'rgb(199, 155, 34)', 
                        'rgb(217, 165, 152)', 'rgb(193, 146, 111)', 'rgb(98, 107, 125)', 'rgb(218, 190, 124)', 'rgb(108, 156, 156)', 'rgb(114, 135, 152)', 
                        'rgb(205, 115, 98)', 'rgb(149, 157, 162)', 'rgb(189, 127, 15)', 'rgb(113, 127, 138)', 'rgb(166, 108, 27)', 'rgb(208, 158, 122)', 
                        'rgb(128, 163, 164)', 'rgb(199, 162, 96)']

new_achondrite_colors = ['rgb(244, 212, 52)', 'rgb(204, 100, 76)', 'rgb(217, 165, 152)', 'rgb(230, 176, 13)', 'rgb(113, 127, 138)', 
                         'rgb(189, 91, 64)', 'rgb(131, 123, 115)', 'rgb(214, 133, 98)', 'rgb(200, 165, 140)', 'rgb(189, 127, 15)', 
                         'rgb(173, 149, 131)', 'rgb(184, 158, 133)', 'rgb(145, 52, 19)', 'rgb(98, 108, 148)', 'rgb(174, 66, 17)', 
                         'rgb(186, 87, 29)', 'rgb(108, 156, 156)', 'rgb(193, 146, 111)', 'rgb(142, 104, 40)', 'rgb(201, 136, 4)', 
                         'rgb(132, 156, 180)', 'rgb(239, 163, 122)', 'rgb(164, 173, 188)', 'rgb(205, 115, 98)', 'rgb(143, 144, 148)', 
                         'rgb(172, 121, 93)', 'rgb(194, 164, 71)', 'rgb(187, 112, 126)', 'rgb(149, 157, 162)', 'rgb(199, 162, 96)', 
                         'rgb(114, 135, 152)', 'rgb(153, 154, 44)', 'rgb(183, 141, 42)', 'rgb(132, 124, 164)', 'rgb(178, 163, 155)',
                         'rgb(98, 107, 125)', 'rgb(199, 110, 44)', 'rgb(182, 95, 86)', 'rgb(84, 140, 178)', 'rgb(217, 134, 78)', 
                         'rgb(221, 164, 98)', 'rgb(173, 80, 53)', 'rgb(234, 149, 83)', 'rgb(129, 84, 76)', 'rgb(224, 169, 144)', 
                         'rgb(169, 159, 31)', 'rgb(181, 142, 78)', 'rgb(182, 68, 116)', 'rgb(204, 182, 98)', 'rgb(204, 140, 122)', 
                         'rgb(121, 164, 194)', 'rgb(128, 163, 164)', 'rgb(100, 125, 109)', 'rgb(165, 122, 40)', 'rgb(229, 111, 96)', 
                         'rgb(177, 175, 182)', 'rgb(155, 124, 107)', 'rgb(205, 182, 135)', 'rgb(166, 108, 27)', 'rgb(199, 155, 34)', 
                         'rgb(196, 140, 174)', 'rgb(122, 112, 108)', 'rgb(132, 184, 212)', 'rgb(229, 147, 148)', 'rgb(192, 168, 149)', 
                         'rgb(215, 112, 47)', 'rgb(148, 133, 121)', 'rgb(196, 125, 94)', 'rgb(216, 139, 118)', 'rgb(84, 168, 98)', 
                         'rgb(157, 108, 132)', 'rgb(175, 141, 100)', 'rgb(212, 92, 60)', 'rgb(155, 152, 104)', 'rgb(132, 180, 188)', 
                         'rgb(158, 148, 172)', 'rgb(157, 104, 80)', 'rgb(218, 190, 124)', 'rgb(186, 134, 118)', 'rgb(208, 158, 122)']


#Import data
grouped_by_type = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/type_percentage.csv')
chondrite_groups_sorted = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/chondrite_groups_sorted.csv')
achondrite_groups_sorted = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/achondrite_groups_sorted.csv')
primitive_achondrite_groups_sorted = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/primitive_groups_sorted.csv')
unclassified_groups_sorted = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/unclassified_groups_sorted.csv')
chondrites_by_mgy = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/chondrites_by_mgy.csv')
achondrites_by_mgy = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/achondrites_by_mgy.csv')
primitives_by_mgy = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/primitives_by_mgy.csv')
unclassified_by_mgy = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/unclassified_by_mgy.csv')


#Define the sidebar selector
st.sidebar.subheader('Meteorite flux by type')
choice = st.sidebar.selectbox('Choose meteorite type', ('Chondrites', 'Achondrites', 'Primitive achondrites', 'Unclassified'), index = 0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------                                                

##SECTION 1: CHONDRITES 
        
if choice == 'Chondrites':

    #Row A
    with st.container():
                                  
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(chondrites_by_mgy['Group_x'].values, new_chondrite_colors)}

        # Create a new column with integer values representing each unique group
        chondrites_by_mgy['group_id'] = pd.factorize(chondrites_by_mgy['Group_x'])[0]

        # Create a SymbolValidator object to access the symbols
        symbol_validator = SymbolValidator()

        # Get the list of available symbols
        raw_symbols = symbol_validator.values

        # Create empty lists for name stems, name variants, and symbols
        namestems = []
        namevariants = []
        symbols = []

        # Iterate through the symbols and extract their name stems and variants
        for i in range(0, len(raw_symbols), 3):
            name = raw_symbols[i + 2]
            symbols.append(raw_symbols[i])
            namestems.append(name.replace("-open", "").replace("-dot", ""))
            namevariants.append(name[len(namestems[-1]):])


        # Assign symbols based on the group_id
        chondrites_by_mgy['symbol'] = chondrites_by_mgy['group_id'].apply(lambda x: symbols[x % len(symbols)])

        # Create the scatter 3D plot using Plotly Express
        fig = px.scatter_3d(
            chondrites_by_mgy,
            x='Year',
            y='month_no',
            z='count',
            color='Group_x',
            labels = {"Group_x": "Group"},
            color_discrete_map=color_map,
            size='count',
            size_max=24,            
            custom_data=['Group_x', 'Year', 'Month', 'count'],
        )


        fig.update_traces(hoverinfo = "text",
                          opacity = 1,
                          hovertemplate = "<br>".join([                                     
                                     "Year: %{customdata[1]}",
                                     "Month: %{customdata[2]}",
                                     "Count: %{customdata[3]}"]),
                        
                         )


         # layout
        fig.update_layout(
                          margin=dict(l=0, r=0, b=0, t=50),
                          title=dict(text='Chondrite influx by year, month, and group'),
                          title_font_color = 'rgb(126, 126, 126)',
                          title_font_size = 16,  
                          scene=dict(
                            xaxis_title='Year',
                            yaxis_title='Month',
                            zaxis_title='Count',
                            xaxis = dict(
                                 backgroundcolor='rgba(233, 181, 125, 0.8)',
                                 showgrid = True,
                                 zeroline = False,
                                 showline = False,
                                 gridcolor="rgba(153,153,153, 0.8)",
                                 gridwidth = 3,
                                 showbackground=True,
                                 linecolor = '#636363',
                                 range=[1830, chondrites_by_mgy['Year'].max()],
                                 ),
                            yaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                                
                                gridcolor="rgba(153,153,153, 0.8)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode = "linear",
                                dtick = 1,
                                range=[0, 12]
                                ),
                            zaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                               
                                gridcolor="rgba(51,51,51, 0.5)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode='linear',  # Set tick mode to linear
                                dtick=1,  # Set the tick interval to 1 (show only whole numbers)
                                range=[0, chondrites_by_mgy['count'].max()],  # Set the minimum value to 0
                                ),),
                          height = 750,
                          width = 750,
                          legend=dict(
                              itemsizing='constant',  # Use a constant item size for the legend markers
                              itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                              traceorder='normal',  # Set the trace order to normal
                              tracegroupgap=10,  # Adjust the gap between legend items        
                              itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
                            ),
                          scene_camera=dict(
                              eye=dict(x=2, y=2, z=0.7),
                              center=dict(x=-0.9, y=-0.7, z=-0.6)),
                          
                          scene_aspectratio=dict(x = 1.3, y = 1.3, z = 1.3),
                          
                        )         
        
                    
        #display the plot
        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation", expanded = True):

            st.markdown("* The main insight from the 3D visualization of the recorded landings between 1830 and 2000 is\
                            that it is considerably more likely to have single events rather than multiple events each month.")
            st.markdown("* The maximum number of recorded landings per month is represented by the rare case of 3 observed\
                            events per month. Instances of 3 events per month occured only 4 times within the given period.")
            st.markdown("* The group markers are differentiated by color. To study a particular group it can be isolated\
                            on the 3d plot by clicking on the marker coresponding to the group in the legend. To restore\
                            all the events click again on any marker in the legend.")
            st.markdown("* Meteorites in the H, L, and LL groups dominate all frequency levels, and are the only groups to\
                            populate the leves of 2 and 3 landings per month. This could either hint at a common origin or\
                            simply be a characteristic of the general distribution of all groups")


            
#----------------------------------------------------------------------------------------------------------------------                                                

##SECTION 2: ACHONDRITES                
      
elif choice == 'Achondrites':

    #Row A
    with st.container():
                                  
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(achondrites_by_mgy['Group_x'].values, new_achondrite_colors)}

        # Create a new column with integer values representing each unique group
        achondrites_by_mgy['group_id'] = pd.factorize(achondrites_by_mgy['Group_x'])[0]

        # Create a SymbolValidator object to access the symbols
        symbol_validator = SymbolValidator()

        # Get the list of available symbols
        raw_symbols = symbol_validator.values

        # Create empty lists for name stems, name variants, and symbols
        namestems = []
        namevariants = []
        symbols = []

        # Iterate through the symbols and extract their name stems and variants
        for i in range(0, len(raw_symbols), 3):
            name = raw_symbols[i + 2]
            symbols.append(raw_symbols[i])
            namestems.append(name.replace("-open", "").replace("-dot", ""))
            namevariants.append(name[len(namestems[-1]):])


        # Assign symbols based on the group_id
        achondrites_by_mgy['symbol'] = achondrites_by_mgy['group_id'].apply(lambda x: symbols[x % len(symbols)])

        # Create the scatter 3D plot using Plotly Express
        fig = px.scatter_3d(
            achondrites_by_mgy,
            x='Year',
            y='month_no',
            z='count',
            color='Group_x',
            labels = {"Group_x" : "Group"},
            color_discrete_map=color_map,
            size='count',
            size_max=24,
            opacity=1,
            custom_data=['Group_x', 'Year', 'Month', 'count'],
        )


        fig.update_traces(hoverinfo = "text",
                          opacity = 0.8,
                          hovertemplate = "<br>".join([                                     
                                     "Year: %{customdata[1]}",
                                     "Month: %{customdata[2]}",
                                     "Count: %{customdata[3]}"]),
                        
                         )

         # layout
        fig.update_layout(
                          margin=dict(l=0, r=0, b=0, t=20),
                          title=dict(text='Achondrite influx by year, month, and group'),
                          title_font_color = 'rgb(126, 126, 126)',
                          title_font_size = 16,  
                          scene=dict(
                            xaxis_title='Year',
                            yaxis_title='Month',
                            zaxis_title='Count',
                            xaxis = dict(
                                 backgroundcolor='rgba(233, 181, 125, 0.8)',
                                 showgrid = True,
                                 zeroline = False,
                                 showline = False,
                                 gridcolor="rgba(153,153,153, 0.8)",
                                 gridwidth = 3,
                                 showbackground=True,
                                 linecolor = '#636363',
                                 range=[1830, achondrites_by_mgy['Year'].max()],
                                 ),
                            yaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                                
                                gridcolor="rgba(153,153,153, 0.8)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode = "linear",
                                dtick = 1,
                                range=[0, 12]
                                ),
                            zaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                               
                                gridcolor="rgba(51,51,51, 0.5)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode='linear',  # Set tick mode to linear
                                dtick=1,  # Set the tick interval to 1 (show only whole numbers)
                                range=[0, achondrites_by_mgy['count'].max()],  # Set the minimum value to 0
                                ),),
                          height = 750,
                          width = 750,
                          legend=dict(
                              itemsizing='constant',  # Use a constant item size for the legend markers
                              itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                              traceorder='normal',  # Set the trace order to normal
                              tracegroupgap=10,  # Adjust the gap between legend items        
                              itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
                            ),
                          scene_camera=dict(
                              eye=dict(x=2, y=2, z=0.7),
                              center=dict(x=-0.9, y=-0.7, z=-0.6)),
                          
                          scene_aspectratio=dict(x = 1.3, y = 1.3, z = 1.3),
                          
                        )        
        
                   
        #display the plot
        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation", expanded = True):

            st.markdown("* Similar to the chondrites, the majority of the achondrites have arrived at the rate of 1 per\
                            month per year with only one instance of two howardites arriving during the same month (April, 1942).")            
            st.markdown("* The group markers are differentiated by color. To study a particular group it can be isolated\
                            on the 3d plot by clicking on the marker coresponding to the group in the legend. To restore\
                            all the events click again on any marker in the legend.")
            st.markdown("* The dominance of the HED (howardite, eucrite, diogenite) groups is clearly visible with instances\
                            spread almost through every month of the year but with frequent gaps between years.")
            st.markdown("* There are three martian achondrites easily identified by color and labeld as SNC (shergolite, nakhlite, chassignite).")
            st.markdown("* The iron achondrite Sikhote-Alin, the largest meteoric mass recovered so far, can be identified by month (February, 1947)\
                            and group label (IIAB), as well as the frequency of other IIAB meteorites by marker color.")
            
            


#---------------------------------------------------------------------------------------------------------------------                                                

##SECTION 3: PRIMITIVE ACHONDRITES         
   
elif choice == 'Primitive achondrites':

    #Row A
    with st.container():
                                  
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(primitives_by_mgy['Group_x'].values, new_chondrite_colors)}

        # Create a new column with integer values representing each unique group
        primitives_by_mgy['group_id'] = pd.factorize(primitives_by_mgy['Group_x'])[0]

        # Create a SymbolValidator object to access the symbols
        symbol_validator = SymbolValidator()

        # Get the list of available symbols
        raw_symbols = symbol_validator.values

        # Create empty lists for name stems, name variants, and symbols
        namestems = []
        namevariants = []
        symbols = []

        # Iterate through the symbols and extract their name stems and variants
        for i in range(0, len(raw_symbols), 3):
            name = raw_symbols[i + 2]
            symbols.append(raw_symbols[i])
            namestems.append(name.replace("-open", "").replace("-dot", ""))
            namevariants.append(name[len(namestems[-1]):])


        # Assign symbols based on the group_id
        primitives_by_mgy['symbol'] = primitives_by_mgy['group_id'].apply(lambda x: symbols[x % len(symbols)])

        # Create the scatter 3D plot using Plotly Express
        fig = px.scatter_3d(
            primitives_by_mgy,
            x='Year',
            y='month_no',
            z='count',
            color='Group_x',
            labels = {"Group_x": "Group"},
            color_discrete_map=color_map,
            size='count',
            size_max=24,            
            custom_data=['Group_x', 'Year', 'Month', 'count'],
        )


        fig.update_traces(hoverinfo = "text",
                          opacity = 1,
                          hovertemplate = "<br>".join([                                     
                                     "Year: %{customdata[1]}",
                                     "Month: %{customdata[2]}",
                                     "Count: %{customdata[3]}"]),
                        
                         )
        
        # layout
        fig.update_layout(
                          margin=dict(l=0, r=0, b=0, t=20),
                          title=dict(text='Primitive achondrite influx by year, month, and group'),
                          title_font_color = 'rgb(126,126,126)',
                          title_font_size = 16,  
                          scene=dict(
                            xaxis_title='Year',
                            yaxis_title='Month',
                            zaxis_title='Count',
                            xaxis = dict(
                                 backgroundcolor='rgba(233, 181, 125, 0.8)',
                                 showgrid = True,
                                 zeroline = False,
                                 showline = False,
                                 gridcolor="rgba(153,153,153, 0.8)",
                                 gridwidth = 3,
                                 showbackground=True,
                                 linecolor = '#636363',
                                 range=[1830, primitives_by_mgy['Year'].max()],
                                 ),
                            yaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                                
                                gridcolor="rgba(153,153,153, 0.8)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode = "linear",
                                dtick = 1,
                                range=[0, 12]
                                ),
                            zaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                               
                                gridcolor="rgba(51,51,51, 0.5)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode='linear',  # Set tick mode to linear
                                dtick=1,  # Set the tick interval to 1 (show only whole numbers)
                                range=[0, 2],  # Set the minimum value to 0
                                ),),
                          height = 750,
                          width = 750,
                          legend=dict(
                              itemsizing='constant',  # Use a constant item size for the legend markers
                              itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                              traceorder='normal',  # Set the trace order to normal
                              tracegroupgap=10,  # Adjust the gap between legend items        
                              itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
                            ),
                          scene_camera=dict(
                              eye=dict(x=2, y=2, z=0.7),
                              center=dict(x=-0.9, y=-0.7, z=-0.6)),
                          
                          scene_aspectratio=dict(x = 1.3, y = 1.3, z = 1.3),
                          
                        )                  
             
        
        #display the plot
        st.plotly_chart(fig, theme=None, use_container_width = True)

        with st.expander("See explanation"):

            st.markdown("* ")                                           



#-----------------------------------------------------------------------------------------------------------------------                                                

##SECTION 4: UNCLASSIFIED METEORITES 
           
elif choice == 'Unclassified':

    #Row A
    with st.container():
                                  
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(unclassified_by_mgy['Group_y'].values, new_chondrite_colors)}

        # Create a new column with integer values representing each unique group
        unclassified_by_mgy['group_id'] = pd.factorize(unclassified_by_mgy['Group_y'])[0]

        # Create a SymbolValidator object to access the symbols
        symbol_validator = SymbolValidator()

        # Get the list of available symbols
        raw_symbols = symbol_validator.values

        # Create empty lists for name stems, name variants, and symbols
        namestems = []
        namevariants = []
        symbols = []

        # Iterate through the symbols and extract their name stems and variants
        for i in range(0, len(raw_symbols), 3):
            name = raw_symbols[i + 2]
            symbols.append(raw_symbols[i])
            namestems.append(name.replace("-open", "").replace("-dot", ""))
            namevariants.append(name[len(namestems[-1]):])


        # Assign symbols based on the group_id
        unclassified_by_mgy['symbol'] = unclassified_by_mgy['group_id'].apply(lambda x: symbols[x % len(symbols)])

        # Create the scatter 3D plot using Plotly Express
        fig = px.scatter_3d(
            unclassified_by_mgy,
            x='Year',
            y='month_no',
            z='count',
            color='Group_y',
            labels = {"Group_y" : "Group"},
            color_discrete_map=color_map,
            size='count',
            size_max=24,
            opacity=1,
            custom_data=['Group_y', 'Year', 'Month', 'count'],
        )


        fig.update_traces(hoverinfo = "text",
                          opacity = 0.8,
                          hovertemplate = "<br>".join([                                     
                                     "Year: %{customdata[1]}",
                                     "Month: %{customdata[2]}",
                                     "Count: %{customdata[3]}"]),
                        
                         )
        # layout
        fig.update_layout(
                          margin=dict(l=0, r=0, b=0, t=20),
                          title=dict(text='Influx of unclassified meteorites by year, month, and group'),
                          title_font_color = 'rgb(126, 126, 126)',
                          title_font_size = 16,  
                          scene=dict(
                            xaxis_title='Year',
                            yaxis_title='Month',
                            zaxis_title='Count',
                            xaxis = dict(
                                 backgroundcolor='rgba(233, 181, 125, 0.8)',
                                 showgrid = True,
                                 zeroline = False,
                                 showline = False,
                                 gridcolor="rgba(153,153,153, 0.8)",
                                 gridwidth = 3,
                                 showbackground=True,
                                 linecolor = '#636363',
                                 range=[1830, unclassified_by_mgy['Year'].max()],
                                 ),
                            yaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                                
                                gridcolor="rgba(153,153,153, 0.8)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode = "linear",
                                dtick = 1,
                                range=[0, 12]
                                ),
                            zaxis = dict(
                                backgroundcolor='rgba(233, 181, 125, 0.8)',
                                showgrid = True,
                                zeroline = False,
                                showline = False,                               
                                gridcolor="rgba(51,51,51, 0.5)",
                                gridwidth = 3,
                                showbackground=True,
                                linecolor = '#636363',                                
                                tickmode='linear',  # Set tick mode to linear
                                dtick=1,  # Set the tick interval to 1 (show only whole numbers)
                                range=[0, unclassified_by_mgy['count'].max()],  # Set the minimum value to 0
                                ),),
                          height = 750,
                          width = 750,
                          legend=dict(
                              itemsizing='constant',  # Use a constant item size for the legend markers
                              itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                              traceorder='normal',  # Set the trace order to normal
                              tracegroupgap=10,  # Adjust the gap between legend items        
                              itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
                            ),
                          scene_camera=dict(
                              eye=dict(x=2, y=2, z=0.7),
                              center=dict(x=-0.9, y=-0.7, z=-0.6)),
                          
                          scene_aspectratio=dict(x = 1.3, y = 1.3, z = 1.3),
                          
                        )         
        
             
        
        #display the plot
        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):

            st.markdown("* ")                                           
            
