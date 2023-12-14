import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout='wide',
                   page_title = "Type Statistics",
                   page_icon = "📈📈"
                   )
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


# define an RGB color
title_color = (89, 89, 89)

# write text with the specified color
st.write(f'<span style="color:rgb{title_color};font-size:36px">Classifying Falls: Meteorite Type Analysis</span>', unsafe_allow_html=True)
st.write(f'<span style="color:rgb{title_color};font-size:16px">Choose a meteorite type from the sidebar to view analysis</span>', unsafe_allow_html=True)


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


#import data
grouped_by_type = pd.read_csv('../Data/type_percentage.csv')
chondrite_groups_sorted = pd.read_csv('../Data/chondrite_groups_sorted.csv')
achondrite_groups_sorted = pd.read_csv('../Data/achondrite_groups_sorted.csv')
primitive_achondrite_groups_sorted = pd.read_csv('../Data/primitive_groups_sorted.csv')
unclassified_groups_sorted = pd.read_csv('../Data/unclassified_groups_sorted.csv')
chondrites_by_month = pd.read_csv('../Data/chondrites_by_month.csv')
achondrites_by_month = pd.read_csv('../Data/achondrites_by_month.csv')
primitives_by_month = pd.read_csv('../Data/primitives_by_month.csv')
unclassified_by_month = pd.read_csv('../Data/unclassified_by_month.csv')
prim_dm_grouped_m_group_y = pd.read_csv('../Data/primitives_by_month_nasa_grouping.csv')


#sidebar
st.sidebar.subheader('Meteorite falls by type')
choice = st.sidebar.selectbox('Choose meteorite type', ('Chondrites', 'Achondrites', 'Primitive achondrites', 'Unclassified'), index = 0)
        
if choice == 'Chondrites':

#ROW A
    with st.container():
        cc = st.columns([70, 30], gap = "large")

        with cc[0]:
            #define custom colors
            color_discrete_sequence = new_chondrite_colors

            fig = px.bar(chondrites_by_month, x="Month", y=["C", "CI", "CK", "CM", "CO", "CR", "CV", "EH", "EL", "H", "H/L", "K", "L", "L/LL", "LL", "R", "UNGR"],
                         color_discrete_sequence = color_discrete_sequence,
                         opacity = 0.9,
                         labels={"value": "Count", "variable": "Group"}
                        )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Monthly observations of chondrites over 171 years</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x = 0.01,
                xaxis_title='Month',
                yaxis_title='Count',
                yaxis=dict(dtick = 10),
                margin=dict(t=70, b=5, l=20, r=20),
                height = 400,
                showlegend = True,
                legend=dict(
                itemsizing='constant',  # Use a constant item size for the legend markers
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=1,  # Adjust the gap between legend items        
                itemdoubleclick='toggle',  # Enable double-click behavior on legend items
                font=dict(size=10)
            ))
            
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):

                st.markdown("* The ordinary chondrites comprising the H, L and LL groups, also known collectively as the H-L-LL clan, unlike other chondrites, have been observed \
                                on every single month of the year during the time period under analysis.")                                           
                st.markdown("* The L chondrites show a higher than average frequency in the months of May, June, and September, and a lower frequency in the months of March and October.")
                st.markdown("* The H chondrites appear to have been observed more frequently in the months of May and October.")
                st.markdown("* The graph also shows that the CM (Mighei-like) chondrites are the carbonaceous chondrites most commonly observed falling.")
                st.markdown("* The graph shows that the months when CM chondrites are most likely to arive are April, June and September.")
                st.markdown("* The CM chondrites have been related to a possible cometary origin, in particular after the analysis of samples returned by Nasa's Stardust \
                                mission :green[<sup>[1](https://doi.org/10.1038/s41598-021-82320-2)</sup>].", unsafe_allow_html=True)
                st.write("")
                st.write("""
                        &nbsp;&nbsp;&nbsp;&nbsp; **Note:** The monthly analysis illustrated here does not take into account periodicity. The fact that over the years more sightings accumulate \
                        over certain months does not imply that every single year there will be a higher frequency of observed impacts during the same months. The actual influx rate has its own variation and there are years \
                        when no falls are being observed from the ground level during the same high-accumulation months. Indeed, the most common count for each type of meteorite is one per month. Ground observations are only \
                        one piece of the puzzle for determining the influx rate of space material on Earth :green[<sup>[2](https://www.lpi.usra.edu/books/MESSII/9021.pdf)</sup>]. For more information follow the link to the \
                        flux analysis page from the sidebar.
                         """, unsafe_allow_html=True)         
                st.write("")
                st.write("""
                        &nbsp;&nbsp;&nbsp;&nbsp; The monthly statistics are limited to 171 years due to the availability of dates. \
                        In an effort to focus on a time period with consistent record keeping this analysis does not take into account events recorded prior to 1830. \
                        The observation dates are sourced from the NHM Meteorite Catalogue(:green[https://doi.org/10.5519/qd.vgkhb1y1]).    
                         """)           
                
               
        with cc[1]:

            #create a pie chart to display the four meteorite types and their percentages
            fig = go.Figure(data=[go.Pie(labels=grouped_by_type['Type'], 
                                 values=grouped_by_type['percentage[%]'], 
                                 hole=.4,
                                 textposition = 'outside', 
                                 marker=dict(colors=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)'], 
                                             line=dict(color='rgb(89, 89, 89)', width=1)),
                                 opacity=0.9,
                                 pull=[0.4, 0.0, 0.0, 0.0])])
            
            fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  )
            
            #customize the plot
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Percentage of observed meteorite falls by type</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x=0.01,
                margin=dict(l=20, r=20, b=5, t = 70),
                autosize = False,
                height = 400,
                width = 400,
                showlegend=True,  # Enable the legend
                xaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                yaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                legend=dict(
                orientation='h',  # Set the orientation to horizontal
                #yanchor='bottom',  # Set the anchor point to the bottom
               # y= -0.1,  # Adjust the y position to move the legend below the chart
               # xanchor='left',  # Set the anchor point to the right
              #  x=0.2,  # Adjust the x position to align the legend to the right
                itemsizing='constant',  # Use a constant item size for the legend markers
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=10,  # Adjust the gap between legend items        
                itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
            )
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):

                st.markdown("* Chondrites are the most common type of meteorite observed falling.:green[] ")                                           
                st.markdown("* Chondrites originate from undifferentiated asteroids and comets. \
                            :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)&nbsp;[2](https://www.nature.com/articles/s41598-021-82320-2)</sup>]. ", unsafe_allow_html=True)
                st.markdown('* The classification method used throughout the pages of this app are based on \
                            :green[["Systematics and Evaluation of Meteorite Classification"](https://www.lpi.usra.edu/books/MESSII/9014.pdf)] \
                            by Michael K. Weisberg, Timothy J. McCoy and Alexander N. Krot ')
                st.markdown("* Some studies might quote different percentage values based on \
                            the sample data and classification methods used.:green[<sup>[3](https://en.wikipedia.org/wiki/Meteorite_fall_statistics)</sup>]. ", unsafe_allow_html=True)
                st.markdown("")
                           
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)                
    
# ROW B
    with st.container():        
                
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(chondrite_groups_sorted['group'].values, chondrite_colors)}

        # Create the treemap figure
        fig = px.treemap(chondrite_groups_sorted, 
                         path=[px.Constant('Chondrites'), 'group'], 
                         values='count', 
                         color='group', 
                         color_discrete_map = color_map,
                         custom_data = [chondrite_groups_sorted['count'], chondrite_groups_sorted['percentage[%]'], chondrite_groups_sorted['max_mass_grams']],
                         hover_data=["count"]
                                          
                        )

        fig.update_traces(hoverinfo = "text", 
                          marker=dict(cornerradius=5),
                          opacity = 0.8,
                         hovertemplate = "<br>".join([
                             "%{label}",
                             "<br>",
                             "Count: %{customdata[0]}",
                             "Percent: %{customdata[1]}",
                             "Maximum Mass in grams: %{customdata[2]}"
            ]))
        fig.data[0].customdata[79] = [838, 100, 4000000.0, 'Chondrites']
        #customize the plot
        fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
            title=dict(text='<b>Observed chondrite falls sorted by group and frequency</b>'),
            title_font_color='rgb(89, 89, 89)',
            title_font_size=16,
            title_x = 0.01,
            margin=dict(l=35, r=35, b=45, t = 50),
            height = 300
            )
             
        # Show the figure
        st.plotly_chart(fig, theme=None, use_container_width = True)
        
        with st.expander("See explanation"):

            st.markdown("* The treemap graph above confirms the abundance of the oridinary chondrite class comprised of the groups L, H, and LL. ")                                           
            st.markdown("* The  most common carbonaceous meteorites are the CM group.")
            st.markdown("* Some of the highest masses recorded belong to the H5 group followed by the CV group.")
            st.markdown("* The most common petrologic types for the H, L, and LL groups are 4, 5, and 6 respectively.")
            st.markdown("* None of the H, L, and LL groups have petrologic types lower than 3.")
            st.markdown("* None of the observed CM, CI and CR meteorites have a petrologic type higher than 2.")
            st.write(" ")
            st.write("""                       
                        &nbsp;&nbsp;&nbsp;&nbsp; Petrologic types higher than 3 are ordered according to their degree of thermal alteration, with 7 being the highest, \
                        while those lower than 3 are ordered according to their degree of aqueous alteration, with type 1 having the highest degree of alteration. \
                        Meteorites of petrologic type 3 are considered pristine, or unaltered. There is also a spectrum of subtypes going from type 3.0 to 3.9 determined by \
                        thermoluminiscence :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>].                           
                         """, unsafe_allow_html=True)            
                
                

elif choice == 'Achondrites':

#ROW A
    with st.container():
        cc = st.columns([70, 30], gap = "large")

        with cc[0]:
            color_discrete_sequence2 = new_achondrite_colors

            fig = px.bar(achondrites_by_month, x="Month", y=["ANGR", "AUB", "DIO", "EUC", "HOW", "IIAB", "IID", "IIE", "IIF", "IIIAB", "IVA", "MES", "PAL", "SNC"],
                         color_discrete_sequence = color_discrete_sequence2,
                         opacity = 0.9, 
                         labels={"value": "Count", "variable": "Group"}
                        )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Monthly observations of achondrites over 171 years</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x = 0.01,
                xaxis_title='Month',
                yaxis_title='Count',
                yaxis=dict(dtick = 10),
                margin=dict(t=70, b=5, l=20, r=20),
                height = 400,
                showlegend = True)

            # Show the figure
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):
                
                st.markdown("* There is an increase in the frequency of observed :green[HED] (howardite, eucrite and diogenite) \
                                meteorites in the months of April, June, August and October. ")                                           
                st.markdown("* The :green[HED] meteorites, are hypothesized to originate from the region of the asteroid Vesta in the main asteroid belt between  \
                                Jupiter and Mars as a result of massive impacts :green[<sup>[1](https://doi.org/10.1016/j.chemer.2014.08.002)</sup>].", unsafe_allow_html=True)
                st.markdown("* Vesta is thought to be the largest surviving protoplanet from the early solar system \
                                :green[<sup>[2](https://science.nasa.gov/science-news/science-at-nasa/2011/29mar_vesta)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* There are estimates that about :green[6%] \
                                of all meteorites found on Earth are \
                                'Vestoids':green[<sup>[3](https://solarsystem.nasa.gov/missions/dawn/science/vesta/)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* Based on the current data, the HEDs also represent about :green[5%] of the reported falls for the given time period.")
                st.write("")
                st.write("""
                        &nbsp;&nbsp;&nbsp;&nbsp; The monthly statistics are limited to 171 years due to the availability of dates. \
                        In an effort to focus on a time period with consistent record keeping this analysis does not take into account events recorded prior to 1830. \
                        The observation dates are sourced from the NHM Meteorite Catalogue(:green[https://doi.org/10.5519/qd.vgkhb1y1]).                           
                         """, unsafe_allow_html=True)       
                
            
            
        with cc[1]:

            #create a pie chart to display the four meteorite types and their percentages
            fig = go.Figure(data=[go.Pie(labels=grouped_by_type['Type'], 
                                 values=grouped_by_type['percentage[%]'], 
                                 hole=.4,
                                 textposition = 'outside',textinfo = 'percent',
                                 marker=dict(colors=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)'], 
                                             line=dict(color='rgb(89, 89, 89)', width=1)),
                                 opacity=0.9,
                                 pull=[0.0, 0.4, 0.0, 0.0])])
            
            fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  )
            
            #customize the plot
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Percentage of observed meteorite falls by type</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x=0.01,
                margin=dict(l=20, r=20, b=5, t = 70),
                autosize = False,
                height = 400,
                width = 400,
                showlegend=True,  # Enable the legend
                xaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                yaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                legend=dict(
                orientation='h',  # Set the orientation to horizontal
                #yanchor='bottom',  # Set the anchor point to the bottom
               # y= -0.1,  # Adjust the y position to move the legend below the chart
                #xanchor='left',  # Set the anchor point to the right
                #x=0.2,  # Adjust the x position to align the legend to the right
                itemsizing='constant',  # Use a constant item size for the legend markers
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=10,  # Adjust the gap between legend items        
                itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
            )
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):

                st.markdown("* Achondrites are formed either by recrystalization or breccias of recrystalzed igneous rock \
                            (rocks differentiated from the solar-like consistency of chondrites by parent body processes such \
                            as volcanism or impact melting) :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>]. ", unsafe_allow_html=True)                                          
                st.markdown("* Some studies might quote different percentage values based on \
                            the sample data and classification methods used.:green[<sup>[2](https://en.wikipedia.org/wiki/Meteorite_fall_statistics)</sup>]. ", unsafe_allow_html=True)
                st.markdown("")
                
  
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)
                    
# ROW B
    with st.container():        
                
       # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(achondrite_groups_sorted['group'].values, achondrite_colors)}

        # Create the treemap figure
        fig = px.treemap(achondrite_groups_sorted, 
                         path=[px.Constant('Achondrites'), 'group'], 
                         values='count', 
                         color='group',
                         color_discrete_sequence=['rgb(196, 76, 92)'],
                         color_discrete_map = color_map,
                         custom_data = [achondrite_groups_sorted['count'], achondrite_groups_sorted['percentage[%]'], achondrite_groups_sorted['max_mass_grams']],
                         hover_data=["count"]
                                          
                        )

        fig.update_traces(hoverinfo = "text", 
                          marker=dict(cornerradius=5),
                          opacity = 0.9,
                         hovertemplate = "<br>".join([
                             "%{label}",
                             "<br>",
                             "Count: %{customdata[0]}",
                             "Percent: %{customdata[1]}",
                             "Maximum Mass in grams: %{customdata[2]}"
            ]))
        fig.data[0].customdata[28] = [104, 100, 23000000.00, 'Achondrites']
        
        #customize the plot
        fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
            title=dict(text='<b>Observed achondrite falls sorted by group and frequency</b>'),
            title_font_color='rgb(89, 89, 89)',
            title_font_size=16,
            title_x = 0.01,
            margin=dict(l=35, r=35, b=45, t = 50),
            height = 300
            )
        
        # Show the figure
        st.plotly_chart(fig, theme=None, use_container_width = True)

        with st.expander("See explanation"):
                
                st.markdown("* The Eucrite-mmict(monomict breccia) are the the most observed achondrites followed closely by Howardites. ")                                           
                st.markdown("* While the HED types have the highest frequency, the highest masses belong to the Iron and Aubrite types. ")
                st.markdown("* :green[Sikhote-Alin], of the Iron-IIAB type, is the largest mass recovered from an observed fall with a cumulative fragmentary mass of at least 23 metric tons.\
                            :green[<sup>[1](https://web.archive.org/web/20100612144717/http://meteoritemag.uark.edu/604.htm)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* There is one Martian (nakhlite) meteorite that was observed falling on June 28, 1911, in Egypt, having a recovered mass of 10-Kg (22 lb)\
                            :green[<sup>[2](https://web.archive.org/web/20160527132206/https://www.minersoc.org/pages/Archive-MM/Volume_16/16-76-274.pdf)</sup>]. ", unsafe_allow_html=True)
        
   
elif choice == 'Primitive achondrites':

    #Row A
    with st.container():
        cc = st.columns([70, 30], gap = "large")

        with cc[0]:
            #define custom colors
            color_discrete_sequence3 = achondrite_colors

            fig = px.bar(primitives_by_month, x="Month", y=["ACAP", "IAB", "IIICD", "LOD", "UNGR", "URE", "WIN"],
                         color_discrete_sequence = color_discrete_sequence3,
                         opacity = 0.9,
                         labels={"value": "Count", "variable": "Group"}
                        )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Monthly observations of primitive achondrites over 171 years</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x = 0.01,
                xaxis_title='Month',
                yaxis_title='Count',
                yaxis=dict(dtick = 10),
                margin=dict(t=70, b=5, l=20, r=20),
                height = 400,
                showlegend = True)

            # Show the figure
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):
                
                st.markdown("* The data for primitive achondrites is to sparse to draw definitive conclusions about their monthly landings.")
                st.markdown("* The Urelites have the most available landing dates and the only group to have been observed to arrive more than once on the same month.")
                st.markdown("* The Winonaites, IAB and IIICD iron meteorites form a clan hypothesisized to originate from a common  parent body.")
                st.markdown("* Only one Winonaite and one IIICD have ever been observed falling while the IABs are almost as common as the urelites.")
                st.markdown("* The months of April and November have each two observeations of the WIN-IAB-IIICD clan.")
                st.markdown("* Another clan, the Acapulcoite-Lodranite, have an observation of one of each of the member groups in August and October.")
                st.markdown("* There were no primitive achondrites observed falling in June or December.")
                st.write("""
                        &nbsp;&nbsp;&nbsp;&nbsp; The monthly statistics are limited to 171 years due to the availability of dates. \
                        In an effort to focus on a time period with consistent record keeping this analysis does not take into account events recorded prior to 1830. \
                        The observation dates are sourced from the NHM Meteorite Catalogue(:green[https://doi.org/10.5519/qd.vgkhb1y1]).                           
                         """, unsafe_allow_html=True)       
            
            
        with cc[1]:

            #create a pie chart to display the four meteorite types and their percentages
            fig = go.Figure(data=[go.Pie(labels=grouped_by_type['Type'], 
                                 values=grouped_by_type['percentage[%]'], 
                                 hole=.4,
                                 textposition = 'outside',textinfo = 'percent',
                                 marker=dict(colors=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)'], 
                                             line=dict(color='rgb(89, 89, 89)', width=1)),
                                 opacity=0.9,
                                 pull=[0.0, 0.0, 0.4, 0.0])])
            
            fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  )
            
            #customize the plot
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Percentage of observed meteorite falls by type</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x=0.01,
                margin=dict(l=50, r=50, b=5, t = 70),
                autosize = False,
                height = 400,
                width = 400,
                showlegend=True,  # Enable the legend
                xaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                yaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                legend=dict(
                orientation='h',  # Set the orientation to horizontal               
                itemsizing='constant',  # Use a constant item size for the legend markers
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=10,  # Adjust the gap between legend items        
                itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
            )
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):

                st.markdown("* The primitive achondrites represent the smallest classified group of meteorites.")                                           
                st.markdown("* Primitive achondrites present characteristics of recrystalization from a molten state but preserve some of the chemistry of  \
                                their undifferentiated(chondritic) state :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* As such, some classification methods identify them as achondrites even though they are considered to be closer to \
                                their chondritic parent :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* Some studies might quote different percentage values based on the sample data and classification methods used.:green[<sup>[2](https://en.wikipedia.org/wiki/Meteorite_fall_statistics)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* The current classification is based on the meteorite landings data available from NASA and includes only falls observed after 1830.")
                     
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)
    
# Row B
    with st.container():        
                
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(primitive_achondrite_groups_sorted['group'].values, achondrite_colors)}



        # Create the treemap figure
        fig = px.treemap(primitive_achondrite_groups_sorted, 
                         path=[px.Constant('Primitive Achondrites'), 'group'], 
                         values='count', 
                         color='group',
                         color_discrete_sequence=['rgb(185, 148, 174)'],
                         color_discrete_map = color_map,
                         custom_data = [primitive_achondrite_groups_sorted['count'], primitive_achondrite_groups_sorted['percentage[%]'], primitive_achondrite_groups_sorted['max_mass_grams']],
                         hover_data=["count"]
                                          
                        )

        fig.update_traces(hoverinfo = "text", 
                          marker=dict(cornerradius=5),
                          opacity = 0.9,
                         hovertemplate = "<br>".join([
                             "%{label}",
                             "<br>",
                             "Count: %{customdata[0]}",
                             "Percent: %{customdata[1]}",
                             "Maximum Mass in grams: %{customdata[2]}"
            ]))
        fig.data[0].customdata[10] = [19, 100, 150200.0, 'Primitive Achondrites']

        #customize the plot
        fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
            title=dict(text='<b>Observed primitive achondrite falls sorted by group and frequency</b>'),
            title_font_color='rgb(89, 89, 89)',
            title_font_size=16,
            title_x = 0.01,
            margin=dict(l=35, r=35, b=45, t = 50),
            height = 300
            )
                
        # Show the figure
        st.plotly_chart(fig, theme=None, use_container_width = True)

        with st.expander("See explanation"):
                
                st.markdown("* The Irons are the most frequently observed falling primitive achondrites.")                                           
                st.markdown('* A few discrepancies can be observed when comparing the monthly observations above (based on the Meteorite Catalogue \
                            from NHM) with the treemap of all observations of primitive achondrites (based on the NASA dataset):')
                cce = st.columns([3, 97])

                with cce[1]:
                    st.markdown('&nbsp; - The NHM catalogue does not include the denomination of \"primitive achondrite\" which leads to primitive \
                            achondrites being classified as achondrites or as unclassified irons or stones.')
                    st.markdown("&nbsp; - The Yardymly meteorite is classified as a group 3 iron (IIICD) in the NHM catalogue \
                            and as a group 1 iron (IAB complex) in the NASA catalogue.")
                    st.markdown("&nbsp; - The Muzaffarpur meteorite is classified as an IAB-sHL iron in the NASA dataset \
                            and is unclassified in the NHM dataset.")
                    st.markdown("&nbsp; - Similarly, the Quesa meteorite is unclassified in the NHM dataset while classified as an \
                            ungrouped group 1 iron (IAB) in the NASA dataset.")
                    st.markdown("&nbsp; - The NASA dataset also includes records that do not have information regarding the month of observation \
                            which increases the count for types that do not have that information.")
                    st.markdown("&nbsp; - If the monthly predilections where based on the alternative (NASA) classification the graph \
                            of landings by month would look like the graph below.")

                    ccg = st.columns([65, 35])

                    with ccg[0]:

                        #define custom colors
                        color_discrete_sequence3 = achondrite_colors

                        fig = px.bar(prim_dm_grouped_m_group_y, x="Month", y=['Acapulcoite', 'Iron, IAB complex', 'Iron, IAB-MG', 'Iron, IAB-sHL',
                               'Iron, IAB-sLL', 'Iron, IAB-ung', 'Lodranite', 'Ureilite', 'Winonaite'],
                                     color_discrete_sequence = color_discrete_sequence3,
                                     opacity = 0.9,
                                     labels={"value": "Count", "variable": "Group"}
                                                )

                        fig.update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                            title=dict(text='<b>Monthly observations of primitive achondrites over 171 years (based on alternative classification)</b>'),
                            title_font_color='rgb(89, 89, 89)',
                            title_font_size=16,
                            title_x = 0.01,
                            xaxis_title='Month',
                            yaxis_title='Count',
                            yaxis=dict(dtick = 10),
                            margin=dict(t=50, b=30, l=50, r=70),
                            height = 400,
                            showlegend = True)

                        # Show the figure
                        st.plotly_chart(fig, theme='streamlit', use_container_width = True)
                                   
                st.markdown("* The only primitive achondrite group that has no observed falls are the Brachinites.")
                st.markdown("")
                    

elif choice == 'Unclassified':

    #Row A
    with st.container():
        cc = st.columns([70, 30], gap = "large")

        with cc[0]:
             #define custom colors
            color_discrete_sequence4 = new_achondrite_colors

            fig = px.bar(unclassified_by_month, x="Month", y=['Stone-uncl', 'Iron', 'Unknown'],
                         color_discrete_sequence = color_discrete_sequence4,
                         opacity = 0.9,
                         labels={"value": "Count", "variable": "Group"}
                        )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Monthly observations of unclassified meteorites over 171 years</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x = 0.01,
                xaxis_title='Month',
                yaxis_title='Count',
                yaxis=dict(dtick = 1),
                margin=dict(t=70, b=5, l=20, r=20),
                height = 400,
                showlegend = True
            )

            # Show the figure
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):
                
                st.markdown("* In the graph above, the unclassified meteorites have been roughly grouped into stones and irons. ")                                           
                st.markdown("* There is only one observed fall that is not described by one of the terms mentioned above. ")
                st.markdown("* The nomenclature described is used as an initial description of the material :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* Further analysis of the recovered fragments might eventually place them in one of the known groups and classes.")
                st.markdown("* Comparing the monthly frequency based and their initial description with the monthly frequency of known groups over the years\
                        might give a clue as to what their types might be.")
                st.markdown("* For example there is a higher frequency of L and LL chondrites that have arrived in June and also a high frequency of unclassified stony meteorites that have arrived in June.\
                        This might suggest that the unclassified stones could be parts of the L and LL groups.")
                st.markdown("* Similarly, there is a higher frequency of IIIAB achondrites that have arrived in April as well as a higher number of unclassified irons that arrived \
                            during the same month over the years. ")
                st.markdown("")
                st.markdown('**Under the principle of "correlation does not imply causation" these similarities should not be treated as conclusive proof of their appartenance to the aforementioned groups**.')
                st.write("")
                st.write("""
                        &nbsp;&nbsp;&nbsp;&nbsp; The monthly statistics are limited to 171 years due to the availability of dates. \
                        This analysis does not take into account events recorded prior to 1830 in an effort to focus on a time period with consistent record keeping. \
                        The observation dates are sourced from the NHM Meteorite Catalogue(:green[https://doi.org/10.5519/qd.vgkhb1y1]).    
                         """)             
            
        with cc[1]:

            #create a pie chart to display the four meteorite types and their percentages
            fig = go.Figure(data=[go.Pie(labels=grouped_by_type['Type'], 
                                 values=grouped_by_type['percentage[%]'], 
                                 hole=.4,
                                 textposition = 'outside',textinfo = 'percent',
                                 marker=dict(colors=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)'], 
                                             line=dict(color='rgb(89, 89, 89)', width=1)),
                                 opacity=0.9,
                                 pull=[0.0, 0.0, 0.0, 0.4])])
            
            fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  )
            
            #customize the plot
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Percentage of observed meteorite falls by type</b>'),
                title_font_color='rgb(89, 89, 89)',
                title_font_size=16,
                title_x=0.01,
                margin=dict(l=50, r=50, b=5, t = 70),
                autosize = True,
                height = 400,
                width = 400,
                showlegend=True,  # Enable the legend
                xaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                yaxis = dict(showgrid = False, zeroline = False, showticklabels = True),
                legend=dict(
                orientation='h',  # Set the orientation to horizontal                
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=10,  # Adjust the gap between legend items        
                itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                
            )
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with st.expander("See explanation"):
                
                st.markdown('* A small percentage of observed falls have not been placed into any of the known groups and \
                        classes. These are labeled in our current scheme as "unclassified". ')
                st.markdown("* The Meteoritical Society updates its database as new findings are confirmed.")
                st.markdown("* Values such as names, location and mass could change over time.")
                st.markdown("* Work might be under way to fit the unclassified meteorites into a \
                        known group or a new category ")
                st.markdown("* Also, the classification methods are not definitive and changes in how the categories are defined might be required in the future. :green[<sup>[1](https://www.lpi.usra.edu/books/MESSII/9014.pdf)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* Some studies might quote different percentage values based on the sample data and classification methods used.:green[<sup>[2](https://en.wikipedia.org/wiki/Meteorite_fall_statistics)</sup>]. ", unsafe_allow_html=True)
                st.markdown("* The current classification is based on the meteorite landings data available from NASA and includes only falls observed after 1830.")
                st.markdown("")
                
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)
    
    # Row B
    with st.container():        
                
        # Create a dictionary that maps the values in the column to colors.
        color_map = {value: color for value, color in zip(unclassified_groups_sorted['group'].values, achondrite_colors)}



        # Create the treemap figure
        fig = px.treemap(unclassified_groups_sorted, 
                         path=[px.Constant('Unclassified'), 'group'], 
                         values='count', 
                         color='group',
                         color_discrete_sequence=['rgb(241, 132, 76)'],
                         color_discrete_map = color_map,
                         custom_data = [unclassified_groups_sorted['count'], unclassified_groups_sorted['percentage[%]'], unclassified_groups_sorted['max_mass_grams']],
                         hover_data=["count"]
                                          
                        )

        fig.update_traces(hoverinfo = "text", 
                          marker=dict(cornerradius=5),
                          opacity = 0.9,
                          hovertemplate = "<br>".join([
                             "%{label}",
                             "<br>",
                             "Count: %{customdata[0]}",
                             "Percent: %{customdata[1]}",
                             "Maximum Mass in grams: %{customdata[2]}"
            ]))

        #customize the plot
        fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
            title=dict(text='<b>Unclassified observed falls sorted by group and frequency</b>'),
            title_font_color='rgb(89, 89, 89)',
            title_font_size=16,
            title_x = 0.01,
            margin=dict(l=35, r=35, b=45, t = 50),
            height = 300
            )

        
        fig.data[0].customdata[3] = [32, 100, 37500.00, 'Unclassified']
        fig.data[0].customdata[2] = [1, 3.12, 'Unknown', 'Unknown']
                
        # Show the figure
        st.plotly_chart(fig, theme=None, use_container_width = True)

        with st.expander("See explanation"):
                
                st.markdown("* The large proportion of stone to iron unclassifieds might possibly reflect their chondritic or achondritic type. ")                                           
                st.markdown("* This is true particularly in the case of irons, as irons are always achondrites or primitive achondrites. ")
                st.markdown("* This is not as clear cut for stones, which can be either chondrites or achondrites. Only further research can establish their appartenence to one group or another. :green[] ")
                st.markdown("")
                

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




                
