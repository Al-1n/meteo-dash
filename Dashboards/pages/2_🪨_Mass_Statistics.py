#################################

      # Meteo Dash

     ## Mass Statistics

    ### (c) Alin Airinei, 2024

#################################

#Import required libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from scipy import stats
from scipy.stats import lognorm

#Page setup
st.set_page_config(layout='wide',
                   page_title = "Mass Statistics",
                   page_icon = "🪨"
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


# Define an RGB color (for subtitles)
title_color = (126, 126, 126)

# Write text with the specified style and color
st.write(f'<span style="color:rgb{(255, 255, 255)};font-size:36px">Understanding the Distribution of Observed and Recovered Meteorite Masses</span>', unsafe_allow_html=True)
st.write(f'<span style="color:rgb{title_color};font-size:16px">Choose a page from the sidebar to view analysis</span>', unsafe_allow_html=True)


#Import data
df = pd.read_csv('../Data/fell_df_known_mass_after_1830.csv', index_col = [0])

#Split the data into quantiles based on percentiles
bin_labels = ['1st_quantile', '2nd_quantile', '3rd_quantile', '4th_quantile', '5th_quantile', '6th_quantile']

df['range label'] = pd.qcut(df['mass (g)'],
                              q=[0, .025, .25, .50, .75, 0.975, 1],
                              labels=bin_labels)
df['mass range'] = pd.qcut(df['mass (g)'],
                              q=[0, .025, .25, .50, .75, 0.975, 1])

#Create subsets for each mass category
mass_cat1 = df[df["range label"] == "1st_quantile"]
mass_cat2 = df[df["range label"] == "2nd_quantile"]
mass_cat3 = df[df["range label"] == "3rd_quantile"]
mass_cat4 = df[df["range label"] == "4th_quantile"]
mass_cat5 = df[df["range label"] == "5th_quantile"]
mass_cat6 = df[df["range label"] == "6th_quantile"]

#Creating dataframes of calculated fields for each mass category

#1
cat1_grouped_by_type_and_group = mass_cat1.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat1_grouped_avg_mass = mass_cat1.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat1_grouped_min_mass = mass_cat1.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat1_grouped_max_mass = mass_cat1.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat1_grouped_by_type_and_group['min mass (g)'] = np.around(cat1_grouped_min_mass['min mass (g)'], decimals = 2)

cat1_grouped_by_type_and_group['avg mass (g)'] = np.around(cat1_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat1_grouped_by_type_and_group['max mass (g)'] = np.around(cat1_grouped_max_mass['max mass (g)'], decimals = 2)

cat1_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat1_grouped_by_type_and_group['count']  / cat1_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat1_grouped_by_type_and_group = cat1_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)

#2
cat2_grouped_by_type_and_group = mass_cat2.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat2_grouped_avg_mass = mass_cat2.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat2_grouped_min_mass = mass_cat2.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat2_grouped_max_mass = mass_cat2.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat2_grouped_by_type_and_group['min mass (g)'] = np.around(cat2_grouped_min_mass['min mass (g)'], decimals = 2)

cat2_grouped_by_type_and_group['avg mass (g)'] = np.around(cat2_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat2_grouped_by_type_and_group['max mass (g)'] = np.around(cat2_grouped_max_mass['max mass (g)'], decimals = 2)

cat2_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat2_grouped_by_type_and_group['count']  / cat2_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat2_grouped_by_type_and_group = cat2_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)

#3
cat3_grouped_by_type_and_group = mass_cat3.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat3_grouped_avg_mass = mass_cat3.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat3_grouped_min_mass = mass_cat3.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat3_grouped_max_mass = mass_cat3.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat3_grouped_by_type_and_group['min mass (g)'] = np.around(cat3_grouped_min_mass['min mass (g)'], decimals = 2)

cat3_grouped_by_type_and_group['avg mass (g)'] = np.around(cat3_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat3_grouped_by_type_and_group['max mass (g)'] = np.around(cat3_grouped_max_mass['max mass (g)'], decimals = 2)

cat3_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat3_grouped_by_type_and_group['count']  / cat3_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat3_grouped_by_type_and_group = cat3_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)

#4
cat4_grouped_by_type_and_group = mass_cat4.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat4_grouped_avg_mass = mass_cat4.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat4_grouped_min_mass = mass_cat4.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat4_grouped_max_mass = mass_cat4.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat4_grouped_by_type_and_group['min mass (g)'] = np.around(cat4_grouped_min_mass['min mass (g)'], decimals = 2)

cat4_grouped_by_type_and_group['avg mass (g)'] = np.around(cat4_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat4_grouped_by_type_and_group['max mass (g)'] = np.around(cat4_grouped_max_mass['max mass (g)'], decimals = 2)

cat4_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat4_grouped_by_type_and_group['count']  / cat4_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat4_grouped_by_type_and_group = cat4_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)

#5
cat5_grouped_by_type_and_group = mass_cat5.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat5_grouped_avg_mass = mass_cat5.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat5_grouped_min_mass = mass_cat5.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat5_grouped_max_mass = mass_cat5.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat5_grouped_by_type_and_group['min mass (g)'] = np.around(cat5_grouped_min_mass['min mass (g)'], decimals = 2)

cat5_grouped_by_type_and_group['avg mass (g)'] = np.around(cat5_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat5_grouped_by_type_and_group['max mass (g)'] = np.around(cat5_grouped_max_mass['max mass (g)'], decimals = 2)

cat5_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat5_grouped_by_type_and_group['count']  / cat5_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat5_grouped_by_type_and_group = cat5_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)

#6
cat6_grouped_by_type_and_group = mass_cat6.groupby(["Type", "group"])["name"].count().reset_index(name = 'count')

cat6_grouped_avg_mass = mass_cat6.groupby(["Type", "group"])["mass (g)"].mean().reset_index(name = 'avg mass (g)')

cat6_grouped_min_mass = mass_cat6.groupby(["Type", "group"])["mass (g)"].min().reset_index(name = 'min mass (g)')

cat6_grouped_max_mass = mass_cat6.groupby(["Type", "group"])["mass (g)"].max().reset_index(name = 'max mass (g)')

cat6_grouped_by_type_and_group['min mass (g)'] = np.around(cat6_grouped_min_mass['min mass (g)'], decimals = 2)

cat6_grouped_by_type_and_group['avg mass (g)'] = np.around(cat6_grouped_avg_mass['avg mass (g)'], decimals = 2)

cat6_grouped_by_type_and_group['max mass (g)'] = np.around(cat6_grouped_max_mass['max mass (g)'], decimals = 2)

cat6_grouped_by_type_and_group['percentage[%]'] = np.around(100 * cat6_grouped_by_type_and_group['count']  / cat6_grouped_by_type_and_group['count'].sum(), decimals = 2)

cat6_grouped_by_type_and_group = cat6_grouped_by_type_and_group.sort_values(by = "percentage[%]", ascending = False).reset_index(drop = True)


#Plot the ECDF for the mass field

#Function to generate the sorted data for ECDF
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

#Assign the mass column to an array
mass_array = df['mass (g)']

#Compute mass ecdf
x_mass, y_mass = ecdf(mass_array)

#Specify array of percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

#Compute percentiles
mass_perc = np.percentile(mass_array, percentiles)
            
#Sidebar
st.sidebar.subheader('Meteorite falls by mass')
choice = st.sidebar.selectbox('Choose Dashboard', ('Overall Distribution', 'Mass Ranges'), index = 0)
        
if choice == 'Overall Distribution':

    #Row A
    with st.container():
        cc = st.columns([70, 30], gap = "small")

        with cc[0]:                  

            fig = go.Figure()

            fig.add_trace(go.Scatter(mode = 'markers',
                                     x = x_mass,
                                     y = y_mass,
                                     name = 'ECDF',
                                     marker = dict(color = 'royalblue', size = 4, symbol = 'circle'),
                                     ))

            fig.add_trace(go.Scatter(mode = 'markers',
                                     x = mass_perc,
                                     y = percentiles/100,
                                     name = 'percentile',
                                     marker = dict(color = 'firebrick', size = 12, symbol = 'diamond'),
                                     ))
            
            fig.update_xaxes(type="log")

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='ECDF of Meteorite masses for falls observed after 1830'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,
                xaxis_title='log(mass) (g)',
                yaxis_title='ECDF',
                height = 500,
                width = 800,
                showlegend = True,
                legend=dict(
                itemsizing='constant',  # Use a constant item size for the legend markers
                itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                traceorder='normal',  # Set the trace order to normal
                tracegroupgap=1,  # Adjust the gap between legend items        
                itemdoubleclick='toggle',  # Enable double-click behavior on legend items
                font=dict(size=10)
            ),
                margin=dict(t=35, b=20, l=20, r=20),
                )
                        
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)         

              
        with cc[1]:
            
            #plot the box plot for the new dataframe 
            fig = px.box(df, y = "mass (g)", log_y = True)

            fig.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                height=500,
                width=500,          
                title=dict(text='Distribution of recovered meteorite masses'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,                              
                margin=dict(t=35, b=20, l=20, r=20),)

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
           

        with st.expander("See explanation"):
            st.markdown("* The empirical cumulative distribution function above models the probability of observing \
                a particular value or less within the given time period (183 years).")
            st.markdown("* The x-axis of the plot above uses a logarithmic scale to facilitate the visualization of the data points.")
            st.markdown("* The logarithmic scale does not convey the actual skewness of the data as it can be seen below.")
            
            st.markdown("")
                        
            with st.container():

                    col1, col2 = st.columns([50, 50])

                    with col1:
                        fig = go.Figure()

                        fig.add_trace(go.Scatter(mode = 'markers',
                                                 x = x_mass,
                                                 y = y_mass,
                                                 name = 'ECDF',
                                                 marker = dict(color = 'royalblue', size = 4, symbol = 'circle'),
                                                 ))

                        fig.add_trace(go.Scatter(mode = 'markers',
                                                 x = mass_perc,
                                                 y = percentiles/100,
                                                 name = 'percentile',
                                                 marker = dict(color = 'firebrick', size = 12, symbol = 'diamond'),
                                                 ))
                        
                        #fig.update_xaxes(type="log")

                        fig.update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                            title=dict(text='ECDF of Meteorite masses for falls observed after 1830'),
                            title_font_color='rgb(126, 126, 126)',
                            title_font_size=16,
                            title_x = 0.01,
                            xaxis_title='mass (g)',
                            yaxis_title='ECDF',            
                            height = 350,
                            #width = 800,
                            showlegend = True,
                            legend=dict(
                            itemsizing='constant',  # Use a constant item size for the legend markers
                            itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                            traceorder='normal',  # Set the trace order to normal
                            tracegroupgap=1,  # Adjust the gap between legend items        
                            itemdoubleclick='toggle',  # Enable double-click behavior on legend items
                            font=dict(size=10)
                        ),
                            margin=dict(t=50, b=20, l=20, r=20),
                            shapes=[go.layout.Shape(
                                                type='rect',
                                                xref='paper',
                                                yref='paper',
                                                x0=-0.07,
                                                y0=-0.1,
                                                x1=1.01,
                                                y1=1.02,
                                                line={'width': 1, 'color': 'rgb(89, 89, 89)'}
                                                )]
                            )
                                    
                        #display the plot
                        st.plotly_chart(fig, theme='streamlit', use_container_width = True)
                        
            st.markdown("*  In the non-logarithmic ECDF it can be clearly seen that most of the values fit almost on a straight vertical line, \
                        almost up to the 97.5 percentile.")
            st.markdown("* This suggests that very large mass values are basically outliers and have been significantly less frequent than the smaller mass values within \
                        the given time period.")

            st.write("""
                    **Note:** The amount of mass that survives a fall is not an indication of the initial meteoric mass or the destructive capacity of an impact. \
                    The Sikhote-Alin meteorite has the largest recovered mass from an observed impact yet its estimated entry mass (about 500 tons) was less  than that of the 2013 \
                    Celyabinsk bolide which had an estimated entry mass of 11000 to 13000 tons but its recovered mass was significantly smaller (about 1000Kg). Out of the estimated 500 tons \
                    of meteoric mass that entered the atmosphere at Sikhote-Alin at least 23 tons made it to the ground as meteorites. Other factors, such as entry angle, velocity, and type \
                    (and implicitly density) can play an important role in the final fragmentation and the amount of mass that survives :green[<sup>[1](https://iopscience.iop.org/article/10.1088/1757-899X/468/1/012025)</sup>].                           
                         """, unsafe_allow_html=True)                             
                        
                           
#Row B

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    with st.container():

        # write text with the specified color
        st.write(f'<span style="color:rgb{(255, 255, 255)};font-size:24px">Estimating the probability of recovering a mass within the studied interval (1830-2013)</span>', unsafe_allow_html=True)
        st.write(f'<span style="color:rgb{title_color};font-size:16px">Move the slider ends to choose a mass range in grams</span>', unsafe_allow_html=True)
                

        slider_range = st.slider("Mass range", min_value = 0.1, max_value = 212000.0, value = [0.1, 212000.0],
                                 step = 0.01)

        data = df['mass (g)']

       # Fit the lognormal distribution to the mass data
        shape, loc, scale = lognorm.fit(data, loc=0)

        # Get the mass range selected by the user
        selected_range = [0.1, 212000.0]  # Example, replace with the selected range from Streamlit slider

        # Calculate the probability of the mass falling within the selected range
        p = lognorm.cdf(slider_range[1], shape, loc, scale) - lognorm.cdf(slider_range[0], shape, loc, scale)

        prob = str(round(p * 100.0, 3)) + "%"

        range = str(slider_range[0]) + " grams" + " ➝ " + str(slider_range[1]) + " grams"

        ccp = st.columns([50, 50])

        with ccp[0]:
            st.metric("Range:",
                  value = range)
        with ccp[1]:
            st.metric("The probability of a recovered mass to be within the chosen range is:",
                  value = prob)               
        
        
        with st.expander("See explanation"):

            st.markdown("* The estimator above predicts the likelyhood of a mass that fell between 1830 and 2013 to fall within a given range.")                                           
            st.markdown("* The maximum value on the mass selector is close to the 97th percentile.")
            st.markdown("* The large gaps between the very large masses would have made the range selector difficult to use for the lower values if the maximum value was the largest mass.")
            st.markdown("* An additional estimator is included below to explore the distribution of all the masses included in the data.")
            st.markdown("* As the estimator uses a theoretical model, the estimated values might be slightly different than those predicted by the emipirical distribution function above. ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    with st.container():

        # write text with the specified color
        st.write(f'<span style="color:rgb{(255, 255, 255)};font-size:24px">Large mass estimator</span>', unsafe_allow_html=True)
        st.write(f'<span style="color:rgb{title_color};font-size:16px">Move the slider ends to choose a mass range in grams</span>', unsafe_allow_html=True)
                

        slider_range = st.slider("Mass range", min_value = 0.1, max_value = 23000000.0, value = [0.1, 23000000.0],
                                 step = 0.01)

        # Get the mass range selected by the user
        selected_range = [0.1, 23000000.0]  # Example, replace with the selected range from Streamlit slider

        # Calculate the probability of the mass falling within the selected range
        p = lognorm.cdf(slider_range[1], shape, loc, scale) - lognorm.cdf(slider_range[0], shape, loc, scale)

        prob = str(round(p * 100.0, 3)) + "%"

        range = str(slider_range[0]) + " grams" + " ➝ " + str(slider_range[1]) + " grams"

        ccp = st.columns([50, 50])

        with ccp[0]:
            st.metric("Range:",
                  value = range)
        with ccp[1]:
            st.metric("The probability of a recovered mass to be within the chosen range is:",
                  value = prob)

            
colors = ['rgb(122, 112, 108)', 'rgb(189, 91, 64)', 'rgb(199, 155, 34)', 'rgb(184, 158, 133)', 'rgb(157, 108, 132)', 
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
         'rgb(186, 134, 118)', 'rgb(201, 136, 4)', 'rgb(132, 184, 212)', 'rgb(199, 162, 96)', 'rgb(229, 111, 96)',
         'rgb(218, 190, 124)', 'rgb(121, 164, 194)', 'rgb(149, 157, 162)', 'rgb(196, 125, 94)', 'rgb(132, 124, 164)', 
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
         'rgb(182, 95, 86)', 'rgb(164, 173, 188)', 'rgb(199, 162, 96)', 'rgb(189, 91, 64)', 'rgb(181, 142, 78)',
         'rgb(177, 175, 182)', 'rgb(200, 165, 140)', 'rgb(174, 66, 17)', 'rgb(164, 173, 188)', 'rgb(142, 104, 40)', 'rgb(215, 112, 47)', 
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
         'rgb(128, 163, 164)', 'rgb(199, 162, 96)', 'rgb(145, 52, 19)', 'rgb(186, 87, 29)', 'rgb(182, 68, 116)', 'rgb(217, 134, 78)',
          'rgb(108, 156, 156)', 'rgb(178, 163, 155)', 'rgb(173, 149, 131)', 'rgb(164, 173, 188)', 'rgb(221, 164, 98)', 'rgb(84, 168, 98)',
          'rgb(194, 164, 71)', 'rgb(181, 142, 78)', 'rgb(132, 124, 164)', 'rgb(205, 182, 135)', 'rgb(158, 148, 172)', 'rgb(165, 122, 40)',
          'rgb(229, 147, 148)', 'rgb(184, 158, 133)', 'rgb(204, 100, 76)', 'rgb(218, 190, 124)', 'rgb(132, 184, 212)', 'rgb(114, 135, 152)',
          'rgb(183, 141, 42)', 'rgb(128, 163, 164)', 'rgb(157, 108, 132)', 'rgb(199, 162, 96)', 'rgb(132, 156, 180)', 'rgb(148, 133, 121)',
          'rgb(193, 146, 111)', 'rgb(153, 154, 44)', 'rgb(143, 144, 148)', 'rgb(204, 182, 98)', 'rgb(100, 125, 109)', 'rgb(192, 168, 149)',
          'rgb(169, 159, 31)', 'rgb(113, 127, 138)', 'rgb(234, 149, 83)', 'rgb(149, 157, 162)', 'rgb(129, 84, 76)', 'rgb(132, 180, 188)',
          'rgb(199, 110, 44)', 'rgb(155, 124, 107)', 'rgb(196, 140, 174)', 'rgb(199, 155, 34)', 'rgb(214, 133, 98)', 'rgb(212, 92, 60)',
          'rgb(155, 152, 104)', 'rgb(121, 164, 194)', 'rgb(189, 127, 15)', 'rgb(217, 165, 152)', 'rgb(215, 112, 47)', 'rgb(122, 112, 108)',
          'rgb(174, 66, 17)', 'rgb(224, 169, 144)', 'rgb(182, 95, 86)', 'rgb(175, 141, 100)', 'rgb(189, 91, 64)', 'rgb(166, 108, 27)',
          'rgb(196, 125, 94)', 'rgb(200, 165, 140)', 'rgb(205, 115, 98)', 'rgb(173, 80, 53)', 'rgb(229, 111, 96)', 'rgb(98, 108, 148)',
          'rgb(98, 107, 125)', 'rgb(131, 123, 115)', 'rgb(244, 212, 52)', 'rgb(239, 163, 122)', 'rgb(84, 140, 178)', 'rgb(177, 175, 182)',
          'rgb(157, 104, 80)', 'rgb(204, 140, 122)', 'rgb(208, 158, 122)', 'rgb(187, 112, 126)', 'rgb(230, 176, 13)', 'rgb(172, 121, 93)',
          'rgb(201, 136, 4)', 'rgb(186, 134, 118)', 'rgb(142, 104, 40)', 'rgb(216, 139, 118)']

type_colors = ['rgb(199, 110, 44)', 'rgb(221, 164, 98)', 'rgb(182, 95, 86)', 'rgb(199, 155, 34)', 'rgb(175, 141, 100)', 'rgb(216, 139, 118)',
               'rgb(205, 182, 135)', 'rgb(224, 169, 144)', 'rgb(189, 91, 64)', 'rgb(100, 125, 109)', 'rgb(169, 118, 88)', 'rgb(228, 158, 124)',
               'rgb(135, 148, 168)', 'rgb(173, 149, 131)', 'rgb(208, 158, 122)', 'rgb(169, 165, 166)', 'rgb(196, 140, 174)', 'rgb(212, 92, 60)',
               'rgb(186, 87, 29)', 'rgb(142, 104, 40)', 'rgb(218, 190, 124)', 'rgb(143, 144, 148)', 'rgb(155, 124, 107)', 'rgb(178, 163, 155)',
               'rgb(217, 134, 78)', 'rgb(145, 52, 19)', 'rgb(172, 121, 93)', 'rgb(181, 145, 51)', 'rgb(215, 112, 47)', 'rgb(177, 169, 173)',
               'rgb(98, 108, 148)', 'rgb(183, 176, 177)', 'rgb(98, 107, 125)', 'rgb(196, 125, 94)', 'rgb(154, 174, 191)', 'rgb(244, 212, 52)',
               'rgb(194, 164, 71)', 'rgb(184, 132, 68)', 'rgb(199, 90, 89)', 'rgb(229, 111, 96)', 'rgb(234, 149, 83)', 'rgb(157, 104, 80)',
               'rgb(192, 168, 149)', 'rgb(132, 184, 212)', 'rgb(158, 148, 172)', 'rgb(181, 142, 78)', 'rgb(201, 136, 4)', 'rgb(140, 175, 207)',
               'rgb(149, 157, 162)', 'rgb(190, 159, 92)', 'rgb(165, 122, 40)', 'rgb(122, 112, 108)', 'rgb(184, 158, 133)', 'rgb(172, 85, 57)',
               'rgb(217, 165, 152)', 'rgb(228, 140, 135)', 'rgb(185, 119, 4)', 'rgb(164, 173, 188)', 'rgb(199, 162, 96)']

if choice == 'Mass Ranges':

    st.sidebar.subheader('Meteorite mass segments')
    mass_range = st.sidebar.selectbox('Choose mass group', ('0.099➝22.0 grams', '22.0➝682.0 grams', '682.0➝2700.0 grams', '2700.0➝10322.0 grams', '10322.0➝212000.0 grams', '212000.0➝23000000.0 grams'), index = 0)

#1st mass range distribution

    #ROW A
    if mass_range == '0.099➝22.0 grams':        
        
        with st.container():            

            fig = px.bar(mass_cat1, 
                         x="year",
                         y = "mass (g)",
                         log_y = True,
                         color = "mass (g)",
                         color_continuous_scale = "peach",                                                               
                         opacity = 0.9,                                                     
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 0.1 - 22 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,                
                xaxis_title='Year',
                yaxis_title='log(Mass) (g)',
                showlegend = True,
                margin=dict(t=35, b=10, l=0, r=5)
            )                    
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("* The mass is plotted on a logarithmic scale to facilitate the visualization of small masses (1 gram or less).")                                           
            st.markdown("* 14.8% of meteorites in this range are less than 1 gram and about 52% are less than 10 grams.")
            st.markdown("* There are big gaps, ranging from 1 to 3 decades, between recoveries of meteorites in this range.")            
            st.write('''
                    &nbsp;&nbsp;&nbsp;&nbsp; Meteoroids do not need to have a high pre-atmospheric entry mass to produce an observable luminous meteor or fireball. A high velocity small meteoroid can produce a bright flash.\                    
                    But the probability that a small entry mass will be both observed and recovered on the ground in the form of a meteorite is small. As such, it may be safe to assume that \
                    meteorites in the smallest range are most likely fragments of larger impactors. Actually, when comparing the few matching events between the meteorite data and the fireball data\
                    a tendency of the recovered mass to increase with the impact energy can be observed but even some of the events with weaker energies have\
                    returned considerable fragments, that could produce damage if they hit populated areas. The survivability of an impactor depends on velocity,\
                    material strength and angle of atmospheric entry :green[<sup>[1](https://www.aanda.org/articles/aa/full_html/2021/06/aa40204-20/aa40204-20.html)</sup>] \
                    :green[<sup>[  2](https://spiral.imperial.ac.uk/bitstream/10044/1/1047/1/Survivability%20of%20meteorite%20projectiles.pdf)</sup>].  
                    ''', unsafe_allow_html=True)
            
    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat1_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat1_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat1_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 0.1 and 22 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* The general predominance of chondrites is well preserved and prominent at this mass range, with the H5 group topping the frequency list, followed by L5 and L6 chondrites.")
            st.markdown("* There are only two achondrites and two unclassified meteorites at this mass range.")
            st.markdown(" ")
            
            
#2nd mass range distribution

    #ROW A
    if mass_range == '22.0➝682.0 grams':          
        
        with st.container():            

            fig = px.bar(mass_cat2, 
                         x="year",
                         y = "mass (g)",
                         color = "mass (g)",
                         color_continuous_scale = "peach",
                         opacity = 0.9,                                                     
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 22➝682 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,     
                xaxis_title='Year',
                yaxis_title='Mass (g)',                
                margin=dict(t=35, b=10, l=0, r=5)
            )                    
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("* At this mass range, there are smaller gaps between the years with observed falls. ")                                           
            st.markdown("* The higher number of recoveries in this mass range may reflect an increase in the\
                         likelihood of locating and recovering larger impactors.")
            st.markdown("* There is a peak accumulation of mass in the given range for the year 1933.")
            st.markdown("* Years with peak accumulations seem to have at least one or more masses between the 75th\
                         percentile (about 0.5kg) and the maximum mass in the range, which might slightly suggest that on certain\
                         years there is a higher influx of large objects. Eyewitness data is not sufficient to determine\
                         if high mass impacts come in clusters. Analyzing fluctuations in impact energy from fireball\
                         data(briefly explored in the maps section) might shed further light on the subject.")
            st.markdown("* The highest mass from a single impact was recovered in 1949.")


    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat2_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat2_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat2_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 22 and 682 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* The L6 group completely dominates the count chart followed by the H5 and H6 groups.")
            st.markdown("* The top groups have maximum masses close to the upper limit of of the range and similar averages.")
            st.markdown("* There are 9 carbonaceous Mighei-like (CM) chondrites of petrologic type 2(hydrated) at this mass range.\
                        This is the highest frequency of carbonaceous meteorites across all mass ranges.")
            


#3rd mass range distribution
    if mass_range == '682.0➝2700.0 grams':    
        
        with st.container():
            
            fig = px.bar(mass_cat3,
                         x="year",
                         y = "mass (g)",
                         color = "mass (g)",
                         color_continuous_scale = "peach",                         
                         opacity = 0.9,                                                            
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 682➝2700 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,     
                xaxis_title='Year',
                yaxis_title='Mass (g)',                
                margin=dict(t=35, b=10, l=0, r=5),
                showlegend = True,
                legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
            )

            #fig.update_traces(showlegend = True)
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("* The years with the most cumulative mass in this range are 1938 and 1980 with 5 events each and a total recovered mass of 8.4kg and 9.4kg respectively")                                           
            st.markdown("* Most of the peak years have at least one or more events with recovered masses between the 75th percentile (1.9kg) and the maximum value of the range(2.7kg).")
            st.markdown("* The mass that defines the upper limit of the range was recovered twice, in the year 1880 and 1974 respectively.")


    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat3_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat3_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat3_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 0.1 and 22 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* The class limits are relatively arbitrary (based on quantiles) so it is not surprising that not much variation is observed among the top groups. It's just a reflection \
                          of the general predominance of ordinary chondrites over other types of meteorites.")
            st.markdown("* Accordingly, the primitive achondrite groups are populating the lower frequency bins.")
            st.markdown("* Masses with values above the 75th percentile are common at all frequency levels.")
           
            


#4th mass range distribution
    if mass_range == '2700.0➝10322.0 grams':
            
        with st.container():

            fig = px.bar(mass_cat4, 
                         x="year",
                         y = "mass (g)",
                         color = "mass (g)",
                         color_continuous_scale = "peach",                          
                         opacity = 0.9,                                                        
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 2700➝10322 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,     
                xaxis_title='Year',
                yaxis_title='Mass (g)',                
                margin=dict(t=35, b=10, l=0, r=5)
            )                    
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("*")                                           
            st.markdown("*")       


    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat4_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat4_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat4_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 2700 and 10322 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* The year 1933, (the year with the most falls on record) has the most recorded masses in this category.")
            st.markdown("* Other years with peaks in this category are 1843, 1910, and 2008.")
            



#5th mass range distribution
    if mass_range == '10322.0➝212000.0 grams':    
        
        with st.container():

            fig = px.bar(mass_cat5, 
                         x="year",
                         y = "mass (g)",
                         color = "mass (g)",
                         color_continuous_scale = "peach",                          
                         opacity = 0.9,                                                        
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 10322➝212000 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,     
                xaxis_title='Year',
                yaxis_title='Mass (g)',                
                margin=dict(t=35, b=10, l=0, r=5)
            )                    
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("*")                                           
            st.markdown("*")       


    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat5_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat5_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat5_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 10322 and 212000 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* .")                                           
            


#6th mass range distribution
    if mass_range == '212000.0➝23000000.0 grams':    
        
        with st.container():

            fig = px.bar(mass_cat6, 
                         x="year",
                         y = "mass (g)",
                         log_y = True,
                         color = "mass (g)",
                         color_continuous_scale = "peach",                          
                         opacity = 0.9,                                                                      
                )

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='<b>Meteorite Mass Range: 212000➝23000000 grams (Recovered 1830-2013) </b>'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=16,
                title_x = 0.01,     
                xaxis_title='Year',
                yaxis_title='log(Mass) (g)',                
                margin=dict(t=35, b=10, l=0, r=5)
            )                    
              
            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with st.expander("See explanation"):
            st.markdown("*")                                           
            st.markdown("*")       

    #ROW B
        with st.container():

            # Create a dictionary that maps the values in the column to colors.
            color_map = {value: color for value, color in zip(cat6_grouped_by_type_and_group['group'].values, type_colors)}

            fig = px.bar(cat6_grouped_by_type_and_group, x="group", y="count",
                         color_discrete_map = color_map,
                         hover_data=['group', 'Type', 'count', 'min mass (g)', 'avg mass (g)', 'max mass (g)', 'percentage[%]'],
                         labels={'group': 'Group','Type':'Type','count':'Count', 'min mass (g)': 'Minimum Mass(grams)', 
                                 'avg mass (g)': 'Average Mass(grams)', 'max mass (g)': 'Maximum Mass(grams)', 'percentage[%]':'Percentage'},
                         color = cat6_grouped_by_type_and_group["group"],
                         opacity = 0.9,             
                        )
            fig.update_xaxes(tickangle=45)

            fig.update_layout(   
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='<b>Distribution of meteorites between 212000 and 23000000 grams grouped by type and sorted by frequency </b>'),
                    title_font_color='rgb(126, 126, 126)',
                    title_font_size=16,
                    title_x = 0.01,     
                    xaxis_title='Group',
                    yaxis_title='Count',                
                    margin=dict(t=35, b=10, l=0, r=5),
                    showlegend = True,
                    legend = dict(
                        itemsizing='constant',  # Use a constant item size for the legend markers
                        itemclick='toggleothers',  # Enable toggle behavior on clicking the legend items
                        traceorder='normal',  # Set the trace order to normal
                        tracegroupgap=10,  # Adjust the gap between legend items        
                        itemdoubleclick='toggle'  # Enable double-click behavior on legend items
                        ),
                )

            #display the plot
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
        with st.expander("See explanation"):
            st.markdown("* .")                                           
            
               

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




