#################################

      # Meteo Dash

     ## World Data

    ### (c) Alin Airinei, 2024

#################################

#Import the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats
from PIL import Image

#Page setup
st.set_page_config(layout="wide",
                   page_title = "World Data",
                   page_icon = "🗺️")

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

#Define info cards for worldwide data
def info_card(title, value, icon):
        wch_colour_box = (239, 248, 247)
        wch_colour_font = (0,0,0)
        fontsize = 15
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


#Load data
fell_df = pd.read_csv('../Data/df183_with_country_area.csv', index_col = [0])
grouped_by_region = fell_df.groupby(['country', "area(sq Km)", 'continent'])['name'].count().sort_values(ascending = False).reset_index(name = 'count')
freq_by_continent = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/freq_by_continent.csv')
most_frequent_by_country = pd.read_csv('/home/a/Data Projects/Meteorite_landings/Data/most_frequent_by_country.csv')

#Define continental subsets grouped by the number of observations
europe = grouped_by_region[grouped_by_region['continent'] == 'Europe'].sort_values(by='count', ascending=False)
asia = grouped_by_region[grouped_by_region['continent'] == 'Asia'].sort_values(by='count', ascending=False)
north_america = grouped_by_region[grouped_by_region['continent'] == 'North America'].sort_values(by='count', ascending=False)
africa = grouped_by_region[grouped_by_region['continent'] == 'Africa'].sort_values(by='count', ascending=False)
south_america = grouped_by_region[grouped_by_region['continent'] == 'South America'].sort_values(by='count', ascending=False)
oceania = grouped_by_region[grouped_by_region['continent'] == 'Oceania'].sort_values(by='count', ascending=False)
antarctica = grouped_by_region[grouped_by_region['continent'] == 'Antarctica'].sort_values(by='count', ascending=False)

#Define continental subsets grouped by country area
europe_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'Europe'].sort_values(by='area(sq Km)', ascending=False)
asia_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'Asia'].sort_values(by='area(sq Km)', ascending=False)
north_america_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'North America'].sort_values(by='area(sq Km)', ascending=False)
africa_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'Africa'].sort_values(by='area(sq Km)', ascending=False)
south_america_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'South America'].sort_values(by='area(sq Km)', ascending=False)
oceania_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'Oceania'].sort_values(by='area(sq Km)', ascending=False)
antarctica_sorted_by_area = grouped_by_region[grouped_by_region['continent'] == 'Antarctica'].sort_values(by='area(sq Km)', ascending=False)

#Define continental subsets that compare fall count and area side by side
european_countries = np.column_stack((europe['country'], europe_sorted_by_area['country']))
european_countries = pd.DataFrame(european_countries)
european_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)

asian_countries = np.column_stack((asia['country'], asia_sorted_by_area['country']))
asian_countries = pd.DataFrame(asian_countries)
asian_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)

north_american_countries = np.column_stack((north_america['country'], north_america_sorted_by_area['country']))
north_american_countries = pd.DataFrame(north_american_countries)
north_american_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)

african_countries = np.column_stack((africa['country'], africa_sorted_by_area['country']))
african_countries = pd.DataFrame(african_countries)
african_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)

south_american_countries = np.column_stack((south_america['country'], south_america_sorted_by_area['country']))
south_american_countries = pd.DataFrame(south_american_countries)
south_american_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)

oceanic_countries = np.column_stack((oceania['country'], oceania_sorted_by_area['country']))
oceanic_countries = pd.DataFrame(oceanic_countries)
oceanic_countries.rename(columns={0:"sorted by count", 1: "sorted by area"}, inplace = True)


#Create a select box to choose the continent
st.sidebar.markdown('### Countries with confirmed observations grouped by region and sorted by frequency')
select = st.sidebar.selectbox('Select continent', ['Europe', 'Asia', 'North America', 'Africa', 'South America', 'Oceania', 'Antarctica', 'Worldwide'], key = '0', label_visibility="visible")


#Tableau 20
colors = ['rgb(140, 86, 75)', 'rgb(255, 152, 150)', 'rgb(196, 156, 148)', 'rgb(247, 182, 210)', 
          'rgb(127, 127, 127)', 'rgb(148, 103, 189)', 'rgb(199, 199, 199)', 'rgb(197, 176, 213)',  
          'rgb(255, 188, 121)', 'rgb(137, 137, 137)']
colors1 = ['rgb(140, 86, 75)', 'rgb(197, 176, 213)', 'rgb(196, 156, 148)', 'rgb(247, 182, 210)',
              'rgb(199, 199, 199)', 'rgb(255, 152, 150)', 'rgb(127, 127, 127)']

colors2 = ['rgb(140, 86, 75)', 'rgb(255, 152, 150)', 'rgb(196, 156, 148)', 'rgb(247, 182, 210)', 
          'rgb(127, 127, 127)', 'rgb(148, 103, 189)', 'rgb(199, 199, 199)', 'rgb(197, 176, 213)',  
          'rgb(255, 188, 121)', 'rgb(137, 137, 137)']

#Create a function to generate a color scale with enough shades for all the bars (see the 'Africa' chart)
def generate_colorscale(start_color, end_color, n, alpha=1.0):
    """
    Generates a list of colors in RGBA format, varying the color intensity
    from a base color to white. The number of colors is specified by n.

    :param base_color: The base color in RGB format, as a tuple.
    :param n: The number of colors to generate.
    :param alpha: The alpha value for the colors. Must be between 0 and 1.
    :return: A list of colors in RGBA format.
    """
    if alpha < 0 or alpha > 1:
        raise ValueError("alpha must be between 0 and 1.")

    start_color = start_color
    end_color = end_color

    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color

    r_step = (r_end - r_start) / n
    g_step = (g_end - g_start) / n
    b_step = (b_end - b_start) / n

    color_list = []
    for i in range(n):
        r_value = int(r_start + r_step * i)
        g_value = int(g_start + g_step * i)
        b_value = int(b_start + b_step * i)
        color = (r_value, g_value, b_value, alpha)
        color_list.append("rgba" + str(color))

    return color_list

colorscale0 = px.colors.sequential.Tealgrn
colorscale1 = generate_colorscale((176, 242, 188), (37, 125, 152), 50, alpha=1)
colorscale2 = generate_colorscale((226, 114, 91), (217, 206, 193), 50, alpha=1)

# Define an RGB color (for subtitles)
title_color = (126, 126, 126)

# Write text with the specified style and color
st.write(f'<span style="color:rgb{(255, 255, 255)};font-size:36px">Global Insights: Number of Observations across Countries and Regions</span>', unsafe_allow_html=True)
st.write(f'<span style="color:rgb{title_color};font-size:16px">Choose a continent from the sidebar to view analysis</span>', unsafe_allow_html=True)

#Page I --------------------------------------------------------------------
if select == 'Europe':
    with st.container():

        cc = st.columns(2, gap = "large")

        with cc[0]:
        
            fig = go.Figure(go.Bar(x=europe['count'],
                                   y=europe['country'],
                                   orientation='h',
                                   marker={"color": list(range(len(europe['country']))), "colorscale": colorscale0},
                                   ), layout=go.Layout(yaxis=go.layout.YAxis(tickmode="linear")),
                            )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Top Countries with Confirmed Observations in Europe'),
                title_font_color = 'rgb(126, 126, 126)',
                xaxis_title='Count',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=0.01, r=50, b=20, t = 50),
                height = 500
             )
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with cc[1]:

            import plotly.graph_objects as go
            fig = go.Figure(go.Bar(x=europe_sorted_by_area['area(sq Km)'],
                                           y=europe_sorted_by_area['country'],
                                           orientation='h',
                                           marker=dict(color=europe_sorted_by_area['country'].map(dict(zip(europe_sorted_by_area['country'].unique(), colorscale2)))),
                                           ), layout=go.Layout(yaxis=go.layout.YAxis(tickmode="linear")),
                                    )
                    
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='European countries sorted by area'),
                title_font_color = 'rgb(126, 126, 126)',
                xaxis_title='Area(sq Km)',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=50, r=20, b=20, t = 50),
                #width=1000,
                height = 500
             )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)
            

    with st.container():

        # Calculate the trendline data
        x = np.log10(europe_sorted_by_area["area(sq Km)"])
        y = europe_sorted_by_area["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        # Create the scatter plot
        fig = px.scatter(
            europe_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(                        
                        title=dict(text='Correlation between country area and number of observations in Europe'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=0.01, t = 50),
                        height = 300
                        
        )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {                       
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])
        
#Expander 1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
        with st.expander("See explanation", expanded = True):

                cce = st.columns([60, 15, 25])

                with cce[0]:
                        st.markdown("* In Europe, the trend between surface area and count is positive, indicating a correlation between a country's size and\
                                the number of observed meteorite falls.")
                        st.markdown("* Countries such as Russia, France and Ukraine are among the largest and also have some of the largest numbers of reportet events.")
                        st.markdown("### Data")
                        st.dataframe(european_countries, hide_index = True, use_container_width = False)
                        st.markdown("* Population density plays a crucial role in certain instances. For example, when comparing Russia and France, despite Russia being \
                                approximately 30 times larger than France, both countries have an equal number of reported observations within the given time period. \
                                This equality is likely due to the sparse population spread across Russia's extensive territory.")
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")
                
                st.markdown("")
                st.markdown("**Note:** This analysis includes only countries with reported falls, which means that several countries in Europe are not included in this study.")
                  
                 
#Page II -------------------------------------------------------------------   
elif select == 'Asia':
    with st.container():

        cc = st.columns(2, gap = "large")

        with cc[0]:
        
            fig = go.Figure(go.Bar(x=asia['count'],
                                   y=asia['country'],
                                   orientation='h',
                                   marker={"color": list(range(len(asia['country']))), "colorscale": colorscale0},
                                   )
                            )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Top Countries with Confirmed Observations in Asia'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Count',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=0.01, r=50, b=20, t = 50),
                #width=1000,
                height = 500
             )
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with cc[1]:

            import plotly.graph_objects as go
            fig = go.Figure(go.Bar(x=asia_sorted_by_area['area(sq Km)'],
                                           y=asia_sorted_by_area['country'],
                                           orientation='h',
                                           marker=dict(color=asia_sorted_by_area['country'].map(dict(zip(asia_sorted_by_area['country'].unique(), colorscale2)))),
                                           )
                                    )
                    
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Asian countries sorted by area'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Area(sq Km)',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=50, r=20, b=20, t = 50),
                #width=1000,
                height = 500
             )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)
            
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)

    with st.container():

        # Calculate the trendline data
        x = np.log10(asia_sorted_by_area["area(sq Km)"])
        y = asia_sorted_by_area["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        # Create the scatter plot
        fig = px.scatter(
            asia_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(                        
                        title=dict(text='Correlation between country area and number of observations in Asia'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=5, t = 50),
                        height = 300
                        
        )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {             
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])

       
    #Expander 2

        with st.expander("See explanation", expanded = True):
                
                cce = st.columns([60, 15, 25])
                with cce[0]:
                        st.markdown("* Just as in the case of Europe, there seems to be a correlation between the size of a country and the number of observed falls for the Asian countries.")
                        st.markdown("* The frequency of observations seems to be influenced by population density as well. As an example, Japan, despite being the 14th largest country, \
                                occupies the third position in terms of the number of observations. This trend can be partly attributed to Japan's exceptional population density, \
                                which stands among the highest globally.")
                        st.markdown("### Data")
                        st.dataframe(asian_countries, hide_index = True)
                        
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                                        
                
                st.markdown("")
                st.markdown("**Note:** This analysis includes only countries with reported falls, which means that several countries in Asia are not included in this study.")

                
#Page III ------------------------------------------------------------------       
elif select == 'North America':
    with st.container():

        cc = st.columns(2, gap = "large")

        with cc[0]:
        
            fig = go.Figure(go.Bar(x=north_america['count'],
                                   y=north_america['country'],
                                   orientation='h',
                                   marker={"color": list(range(len(north_america['country']))), "colorscale": colorscale0},
                                   )
                            )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Top Countries with Confirmed Observations in North America'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Count',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=0.01, r=50, b=20, t = 50),
                #width=1000,
                height = 400
             )
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with cc[1]:

            import plotly.graph_objects as go
            fig = go.Figure(go.Bar(x=north_america_sorted_by_area['area(sq Km)'],
                                           y=north_america_sorted_by_area['country'],
                                           orientation='h',
                                           marker=dict(color=north_america_sorted_by_area['country'].map(dict(zip(north_america_sorted_by_area['country'].unique(), colorscale2)))),
                                           )
                                    )
                    
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='North American countries sorted by area'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Area(sq Km)',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=50, r=20, b=20, t = 50),
                #width=1000,
                height = 400
             )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            
#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)

    with st.container():

        # Calculate the trendline data
        x = np.log10(north_america_sorted_by_area["area(sq Km)"])
        y = north_america_sorted_by_area["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        # Create the scatter plot
        fig = px.scatter(
            north_america_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(                        
                        title=dict(text='Correlation between country area and number of observations in North America'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=5, t = 50),
                        height = 300
                        
        )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {            
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])


    #Expander 3

        with st.expander("See explanation", expanded = True):

                

                
                cce = st.columns([60, 15, 25])
                with cce[0]:
                        st.markdown("* The correlation strength between country size and number of observations in North America is positive but weak compared to Europe for example. The correlation strength is likely affected by the small number of countries with reported landings.")
                        st.markdown("* A significant amount of teritory is represented by the 4 out of 23 countries included but there are still 19 countries with no reported falls.")
                        st.markdown("* This makes the results difficult to interpret which prompts for further investigations.")
                        st.markdown("### Data")
                        st.dataframe(north_american_countries, hide_index = True)
                        st.markdown("* In this case, population density is clearly a factor in determining the lack of correlation, as Mexico has approximately three times the population \
                                of Canada. Similar to the situation in Russia, the low population density in Canada leads to a lower frequency of observations, despite its vast territory.")
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")                
                

#Page IV--------------------------------------------------------------------        
elif select == 'Africa':
        with st.container():

            cc = st.columns(2, gap = "large")

            with cc[0]:
            
                fig = go.Figure(go.Bar(x=africa['count'],
                                       y=africa['country'],
                                       orientation='h',
                                       marker=dict(color=africa_sorted_by_area['country'].map(dict(zip(africa_sorted_by_area['country'].unique(), colorscale1)))),
                                       )
                                )
                
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='Top Countries with Confirmed Observations in Africa'),
                    title_font_color = 'rgb(126, 126, 126)',
                    xaxis_title='Count',
                    yaxis_title='Country',
                    yaxis=dict(autorange="reversed"),
                    bargap=0.3,
                    margin=dict(l=0.01, r=50, b=20, t = 50),
                    #width=1000,
                    height = 500
                 )
                st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            with cc[1]:

                import plotly.graph_objects as go
                fig = go.Figure(go.Bar(x=africa_sorted_by_area['area(sq Km)'],
                                               y=africa_sorted_by_area['country'],
                                               orientation='h',
                                               marker=dict(color=africa_sorted_by_area['country'].map(dict(zip(africa_sorted_by_area['country'].unique(), colorscale2)))),
                                               )
                                        )
                        
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                    title=dict(text='African countries sorted by area'),
                    title_font_color = 'rgb(126, 126, 126)',
                    xaxis_title='Area(sq Km)',
                    yaxis_title='Country',
                    yaxis=dict(autorange="reversed"),
                    bargap=0.3,
                    margin=dict(l=50, r=20, b=20, t = 50),
                    #width=1000,
                    height = 500
                 )

                st.plotly_chart(fig, theme='streamlit', use_container_width = True)

#Horizontal line separator            
        st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)
                

        with st.container():

            # Calculate the trendline data
            x = np.log10(africa_sorted_by_area["area(sq Km)"])
            y = africa_sorted_by_area["count"]
            coefficients = np.polyfit(x, y, 1)
            trendline_y = np.polyval(coefficients, x) 

            # Create the scatter plot
            fig = px.scatter(
                africa_sorted_by_area,
                x="area(sq Km)",
                y="count",
                color='country',
                log_x=True

            )

            # Add the trendline as a line trace
            fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

            fig.update_traces(marker={'size': 12})

            fig.update_layout(                            
                            title=dict(text='Correlation between country area and number of observations in Africa'),
                            title_font_color = 'rgb(126, 126, 126)',
                            title_font_size=18,
                            title_x=0.02,
                            xaxis_title='Area(sq Km)',
                            yaxis_title='Count',
                            margin=dict(l=0.01, r=50, b=5, t = 50),
                            height = 300
                            
            )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

            # Fit the linear regression model

            slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

            # Calculate additional statistical summaries
            if r_value != 1.0:
                    f_value = r_value**2 / (1 - r_value**2)
            else:
                    f_value = np.inf

            statistical_summaries = {                    
                    "r-squared": r_value**2,
                    "pearson-r": r_value
                }

            statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])
            

    #Expander 4

        with st.expander("See explanation", expanded = True):

                
                cce = st.columns([60, 15, 25])
                with cce[0]:
                        st.markdown("* There seems to be no correlation between country size and number of observations in Africa.")
                        st.markdown("* Indeed, some of the largest countries have a high number of observations, but many of the largest have very few while some \
                                        midsized countries like Morroco and Burkina Faso have an above average number of observations.")
                        st.markdown("* Morocco is famous for its meteorite trade.")
                        st.markdown("* One of the reasons for the high frequency of recovered fragments in Morroco is the ease of spotting them in the desert environment.")
                        st.markdown("### Data")
                        st.dataframe(african_countries, hide_index = True)
                        st.markdown("* Based on the available data, it is not entirely clear which combination of factors contributes to the lack of correlation \
                                between country size and the number of observations in Africa. Additional factors could include population density, geography, \
                                economic and political factors, underreporting, and unregulated trade.")
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")                
                

#Page V --------------------------------------------------------------------
elif select == 'South America':
    with st.container():
                
        cc = st.columns(2, gap = "large")

        with cc[0]:
        
            fig = go.Figure(go.Bar(x=south_america['count'],
                                   y=south_america['country'],
                                   orientation='h',
                                   marker={"color": list(range(len(south_america['country']))), "colorscale": colorscale0},
                                   )
                            )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Top Countries with Confirmed Observations in South America'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Count',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=0.01, r=50, b=20, t = 50),
                #width=1000,
                height = 400
             )
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with cc[1]:
        
            
            fig = go.Figure(go.Bar(x=south_america_sorted_by_area['area(sq Km)'],                                       
                                   y=south_america_sorted_by_area['country'],
                                   orientation='h',
                                   marker=dict(color=south_america_sorted_by_area['country'].map(dict(zip(south_america_sorted_by_area['country'].unique(), colorscale2)))),
                                   )
                            )
                    
            fig.update_layout(                
                title=dict(text='South American countries sorted by area'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Area(sq Km)',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=50, r=20, b=20, t = 50),
                #width=1000,
                height = 400
             )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)

    with st.container():

        # Calculate the trendline data
        x = np.log10(south_america_sorted_by_area["area(sq Km)"])
        y = south_america_sorted_by_area["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        # Create the scatter plot
        fig = px.scatter(
            south_america_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(                        
                        title=dict(text='Correlation between country area and number of observations in South America'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=5, t = 50),
                        height = 300
                        
        )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {            
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])
        

    #Expander 5

        with st.expander("See explanation", expanded = True):
                
                cce = st.columns([60, 15, 25])
                with cce[0]:
                        st.markdown("* There is a correlation between country size and number of observations in South America.")
                        st.markdown("* Brazil has both a larger area and higher population density than Argentina, yet the number \
                                        of observations for both countries is similar.")
                        st.markdown("* Therefore, there may be some yet undetermined reasons for Brazil not having a higher number of reported events.")
                        st.markdown("### Data")
                        st.dataframe(south_american_countries, hide_index = True)
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")                     
                                           

#Page VI--------------------------------------------------------------------    
elif select == 'Oceania':
    with st.container():

        cc = st.columns(2, gap = "large")

        with cc[0]:
        
            fig = go.Figure(go.Bar(x=oceania['count'],
                                   y=oceania['country'],
                                   orientation='h',
                                   marker={"color": list(range(len(oceania['country']))), "colorscale": colorscale0},
                                   )
                            )
            
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Top Countries with Confirmed Observations in Oceania'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Count',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=0.01, r=50, b=20, t = 50),
                #width=1000,
                height = 300
             )
            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        with cc[1]:

            import plotly.graph_objects as go
            fig = go.Figure(go.Bar(x=oceania_sorted_by_area['area(sq Km)'],
                                   y=oceania_sorted_by_area['country'],
                                   orientation='h',
                                   marker=dict(color=oceania_sorted_by_area['country'].map(dict(zip(oceania_sorted_by_area['country'].unique(), colorscale2)))),
                                   )
                            )
                    
            fig.update_layout(                
                title=dict(text='Oceanic countries sorted by area'),
                title_font_color = 'rgb(126, 126, 126)',
                title_x=0.01,
                xaxis_title='Area(sq Km)',
                yaxis_title='Country',
                yaxis=dict(autorange="reversed"),
                bargap=0.3,
                margin=dict(l=50, r=20, b=20, t = 50),
                #width=1000,
                height = 300
             )

            st.plotly_chart(fig, theme='streamlit', use_container_width = True)

#Horizontal line separator            
    st.markdown("""<hr style="height:5px;border:none;color:#EEDD6B;background-color:#EEDD6B;" /> """, unsafe_allow_html=True)

    with st.container():

        # Calculate the trendline data
        x = np.log10(oceania_sorted_by_area["area(sq Km)"])
        y = oceania_sorted_by_area["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        # Create the scatter plot
        fig = px.scatter(
            oceania_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(
                        {'plot_bgcolor': 'rgba(174, 202, 220, 0.8)'},
                        title=dict(text='Correlation between country area and number of observations in Oceania'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=5, t = 50),
                        height = 300
                        
        )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {            
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])

     #Expander 6

        with st.expander("See explanation", expanded = True):
                
                cce = st.columns([60, 15, 25])

                with cce[0]:
                        st.markdown("* The correlation between country size and number of observations seems to be very strong in Oceania.")
                        st.markdown("* The number of countries is also small but they comprise the majority of the land area.")
                        st.markdown("### Data")
                        st.dataframe(oceanic_countries, hide_index = True)
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")                     
                
#Page VII ------------------------------------------------------------------       
elif select == 'Antarctica':

    with st.container():
            

            antarctica = {"continent": "Antarctica", "count": 0}

            antarctica = pd.DataFrame(antarctica, index = [0])

            st.dataframe(antarctica, hide_index = True, height = 50, width = 400) #use_container_width = True)

#Expander 7
    with st.container():
            with st.expander("See explanation", expanded = True):
                    st.markdown("* Antarctica does not have any permanent human settlements and thus no observations have been documented yet.")
                    st.markdown("* Nonetheless, Antarctica is a real hotspot for finding already fallen meteorites\
                                :green[<sup>[1](https://earthobservatory.nasa.gov/images/149554/finding-meteorite-hotspots-in-antarctica)</sup>].", unsafe_allow_html = True )
                    
    with st.container():
            cc_img = st.columns([15, 20, 15])

            with cc_img[0]:
                    st.write("")
            with cc_img[1]:
                    image = Image.open('static/antarctic_meteorites_2022.png')
                    st.image(image)
                    st.write("")
            with cc_img[2]:
                    st.write("")

#Page VIII -----------------------------------------------------------------
elif select == "Worldwide":

    #Row A
    with st.container():
    
        cc = st.columns(4)

        with cc[0]:
                st.write("")
                
            # cc[0].markdown()

        with cc[1]:
                st.write("")
                            
        with cc[2]:
                info_card("Countries w/data", 108, 'fa fa-globe')                
            
            #info_card("Average sightings per year", 5, 'fa fa-chart-simple')
                

        with cc[3]:
                info_card("Countries w/less than 3 obs.", 51, 'fa fa-map-location-dot')
            #info_card("Year w/ maximum No. of obs.", 1933, 'fa fa-calendar')
    with st.container():

            cce = st.columns([50, 50])

            with cce[0]:
                    st.write("")
            with cce[1]:
                    with st.expander("See explanation"):
                        
                        st.markdown("* Only :green[55.4%], or roughly half of world countries have contributed data of meteorite sightings.")                                           
                        st.markdown("* :green[47.2%] of the countries with data, or roughly half, have less than 3 reported observations.")
                        st.markdown("")
                        st.write("""
                                \n
                                &nbsp;&nbsp;&nbsp;&nbsp; Given the information above, the consistency of meteorite databases might be affected by
                                significant under-reporting, in particular with regard to observed landings.
                                As such, the current selection of records from the NASA/Meteoritical Society database and the NHM Meteorite Catalogue \
                                could be non-representative and certain insights need to be evaluated carefully. \n
                                &nbsp;&nbsp;&nbsp;&nbsp; For a more comprehensive inquiry, additional data is required. Further investigations
                                and comparisons of the current results will include an analysis of the Fireball data reported by U.S. Government sensors.  
                                 """)                                                  

    # Row B
    with st.container():
        
        c1, c2 = st.columns(2, gap="large")
        with c1:

            fig = go.Figure(go.Bar(
                x=freq_by_continent['count'],
                y=freq_by_continent['continent'],
                orientation='h',
                marker=dict(color=freq_by_continent['continent'].map(dict(zip(freq_by_continent['continent'].unique(), colors1)))),
                hovertemplate='Continent: %{y}<br>Count: %{x}<extra></extra>'
            ))

            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
                title=dict(text='Number of confirmed observations by continent'),
                title_font_color='rgb(126, 126, 126)',
                title_font_size=18,
                xaxis_title='Count',
                yaxis_title='Continent',
                yaxis=dict(autorange="reversed"),
                margin=dict(l=0, r=20, b=20, t = 30),
                height = 300
            )

            st.plotly_chart(fig, use_container_width = True)


        with c2:
            fig = go.Figure(go.Bar(
                    x=most_frequent_by_country['count'],
                    y=most_frequent_by_country['country'],
                    orientation='h',
                    marker=dict(color=most_frequent_by_country['country'].map(dict(zip(most_frequent_by_country['country'].unique(), colors2)))),
                    hovertemplate='Country: %{y}<br>Count: %{x}<extra></extra>'
                ))

            fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)'},
            title=dict(text='Top 10 countries with confirmed observations'),
            title_font_color = 'rgb(126, 126, 126)',
            title_font_size = 18, 
            xaxis_title='Count',
            yaxis_title='Country',
            yaxis=dict(autorange="reversed"),
            margin=dict(l=10, r=10, b=20, t = 30),
            height = 300
            )
            st.plotly_chart(fig, use_container_width = True)
            
        with st.expander("See explanation"):
                        st.markdown("* At continental level Europe is leading by number of observations followed by Asia and North America.")                                           
                        st.markdown("* Even though Europe has the highest number of observations, at country level the United States has the highest number of observed falls, followed by India.")
                        st.markdown("")   
                        st.write("""
                            Since reporting inconsistencies are possibly corelated to population size and fraction of populated surface area per country, \
                            one possible workaround might be to create a subset of countries that are similar in both population and fraction of developed surface area \
                            as well as a documented history of consistent record keeping and observations. This will still not compensate for events that occur in less \
                            populated areas or over the ocean but it might give a better perspective over the frequency of landing events.
                            """)                

    with st.container():

        # Calculate the trendline data
        x = np.log10(grouped_by_region["area(sq Km)"])
        y = grouped_by_region["count"]
        coefficients = np.polyfit(x, y, 1)
        trendline_y = np.polyval(coefficients, x) 

        grouped_by_region_sorted_by_area = grouped_by_region.sort_values(by='area(sq Km)', ascending=False)

        # Create the scatter plot
        fig = px.scatter(
            grouped_by_region_sorted_by_area,
            x="area(sq Km)",
            y="count",
            color='country',
            log_x=True

        )

        # Add the trendline as a line trace
        fig.add_trace(go.Scatter(x=10**x, y=trendline_y, mode='lines', name='Trendline', line={"width":3, "color": '#f2c15d'}))  

        fig.update_traces(marker={'size': 12})

        fig.update_layout(
                        {'plot_bgcolor': '#aecadc'},
                        title=dict(text='Worldwide correlation between country area and number of observations'),
                        title_font_color = 'rgb(126, 126, 126)',
                        title_font_size=18,
                        title_x=0.02,
                        xaxis_title='Area(sq Km)',
                        yaxis_title='Count',
                        margin=dict(l=0.01, r=50, b=5, t = 50),
                        height = 300
                )

        st.plotly_chart(fig, theme='streamlit', use_container_width = True)

        # Fit the linear regression model
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

        # Calculate additional statistical summaries
        if r_value != 1.0:
            f_value = r_value**2 / (1 - r_value**2)
        else:
            f_value = np.inf

        statistical_summaries = {            
            "r-squared": r_value**2,
            "pearson-r": r_value
        }

        statistical_summaries = pd.DataFrame(statistical_summaries, index = [0])      

    #Expander 2

        with st.expander("See explanation", expanded = True):

                cce = st.columns([60, 15, 25])

                with cce[0]:
                        st.markdown("* At world level the correlation between country size and number of observations is positive.")
                        st.markdown("* The countries with the largest areas are clearly at the top of the list for meteorite fall reporting frequency.")
                        st.markdown("* An interesting topic of research would be to determine if the history of economic development and the variation in population density through the years \
                                        have influenced the variation in the frequencey of observations.")
                        st.markdown("")
                        st.markdown("**Note:** Only countries with reported falls are included in this analysis.")                        
                with cce[1]:
                        st.write("")
                with cce[2]:
                        st.dataframe(statistical_summaries, hide_index = True, use_container_width = True)
                        st.write("")                     



