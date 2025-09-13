#################################

      # Meteo Dash

     ## Time Series

    ### (c) Alin Airinei, 2024

#################################

#Import required libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#Page setup
st.set_page_config(layout='wide',
                   page_title = "Historical Summaries",
                   page_icon = "📈"
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
  
# Define an RGB color 
title_color = (255, 255, 255)

# Write text with the specified style and color
st.write(f'<span style="color:rgb{title_color};font-size:36px">Observed Meteorite Landings between 1830 and 2013</span>', unsafe_allow_html=True)

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

cc = st.columns(4)

with cc[0]:
     st.write("")
    

with cc[1]:
    st.write("")
    
with cc[2]:
    info_card("Average sightings per year", 5, 'fa fa-chart-simple')

with cc[3]:
    info_card("Year w/ maximum No. of obs.", 1933, 'fa fa-calendar')                  

#import data
grouped_by_decade_200 = pd.read_csv('https://raw.githubusercontent.com/Al-1n/meteo-dash/main/Data/grouped_by_decade_200.csv')
freq_by_year_200 = pd.read_csv('https://raw.githubusercontent.com/Al-1n/meteo-dash/main/Data/freq_by_year_200.csv')
grouped_by_decade_year_avg = pd.read_csv('https://raw.githubusercontent.com/Al-1n/meteo-dash/main/Data/grouped_by_decade_year_avg.csv')

#Tableau 20
colors1 = ['rgb(140, 86, 75)', 'rgb(197, 176, 213)', 'rgb(196, 156, 148)', 'rgb(247, 182, 210)',
          'rgb(199, 199, 199)', 'rgb(255, 152, 150)', 'rgb(127, 127, 127)']
#Tableau 20
colors2 = ['rgb(140, 86, 75)', 'rgb(255, 152, 150)', 'rgb(196, 156, 148)', 'rgb(247, 182, 210)', 
          'rgb(127, 127, 127)', 'rgb(148, 103, 189)', 'rgb(199, 199, 199)', 'rgb(197, 176, 213)',  
          'rgb(255, 188, 121)', 'rgb(137, 137, 137)'] 

# Row B
with st.container():
    
    c3, c4 = st.columns(2, gap="large")
    
    with c3:       

        # create a bar plot
        fig = go.Figure(
            go.Bar(
                x=grouped_by_decade_200["decade"],
                y=grouped_by_decade_200["count"],
                customdata=[
                    [
                        f"Decade: {decade}<br>Count: {count}<br>Avg Per Year: {avg_per_year:.0f}"
                    ]
                    for decade, count, avg_per_year in zip(
                        grouped_by_decade_200["decade"],
                        grouped_by_decade_200["count"],
                        grouped_by_decade_200["avg_per_year"],
                    )
                ],
                marker=dict(
                    color=grouped_by_decade_200["avg_per_year"],
                    colorbar=dict(
                        title="Avg Per Year",
                        len=0.75,
                        y=0.5,
                        yanchor="middle",
                        tickvals=[
                            grouped_by_decade_200["avg_per_year"].min(),
                            grouped_by_decade_200["avg_per_year"].max(),
                        ],
                    ),
                    showscale=False,
                    colorscale="Tealgrn",
                ),
                hovertemplate="%{customdata[0]}<extra></extra>",
            )
        )

        # Set the layout
        fig.update_layout(
            plot_bgcolor="rgba(0, 0, 0, 0)",
            title=dict(text="Variation in the frequency of observations by decade"),
            title_font_color="rgb(126, 126, 126)",
            title_font_size=20,
            xaxis_title='Decade',
            yaxis_title='Count',
            margin=dict(l=0, r=20, b=20, t = 30),
            height = 350
        )

        st.plotly_chart(fig, use_container_width = True)



    with c4:

        fig = go.Figure()

        # define the plot
        fig.add_trace(go.Scatter(x=freq_by_year_200['year'], y=freq_by_year_200['count'], mode='lines', 
                                 line=dict(width=1.5),
                                 hovertemplate='<b>Year:</b> %{x}<br>' +
                                               '<b>Count:</b> %{y}<br><extra></extra>'
                                ))

        # set the title
        fig.update_layout(title=dict(text='Variation in the annual frequency of observed events'),
                          title_font_color = 'rgb(126, 126, 126)',
                          title_font_size = 20,
                          font=dict(size=16),
                          xaxis_title='Year',
                          yaxis_title='Count',
                          margin=dict(l=0, r=20, b=20, t = 30),
                          height = 350
                          )                           

        # format the ticks to match each decade and rotate the labels
        fig.update_xaxes(tickmode='linear', tick0=1830, dtick=10)
        fig.update_xaxes(tickangle=45)

        st.plotly_chart(fig, use_container_width = True)

with st.expander("See explanation", expanded = True):
                st.markdown("* The decade of the 1930s has the highest number of observations with a total of :green[91] sightings.")                                           
                st.markdown("* The graph on the right shows a noticeable spike corresponding to the year :green[1933].")
                st.write("""
                            &nbsp;&nbsp;&nbsp;&nbsp;While there is a slight variation in the number of events between the 1940s and the early 2000s, \
                            the yearly average goes in a straight line as it can be seen in the graph below. This is not a definite \
                            sign that the apparent dips prior and after the 1860s are a consequence of underreporting as there \
                            may be additional underlying factors pushing the average up, such as the fact that the world population quadrupled during the 20th century. \
                            As such, the spike of the 1860s might suggest an actual increase in the number of events, in particular around the year 1868(as seen in the graph on the right above).
                            """)
                with st.container():

                    col1, col2 = st.columns([30, 5])

                    with col1:
                        

                        fig = go.Figure()

                        # define the plot
                        fig.add_trace(go.Scatter(x=grouped_by_decade_year_avg['decade'], y=grouped_by_decade_year_avg['avg/year'], mode='lines', 
                                                 line=dict(width=1.5),
                                                 hovertemplate='<b>Year:</b> %{x}<br>' +
                                                               '<b>Count:</b> %{y}<br><extra></extra>'
                                                ))

                        # set the title
                        fig.update_layout(title=dict(text='<b style="text-align:center">Average yearly observations per decade</b>'),
                                          title_font_color = 'green',
                                          title_font_size = 16,
                                          title_x = 0.1,
                                          title_y = 0.8,
                                          font=dict(size=16),
                                          xaxis_title='Year',
                                          yaxis_title='Count',
                                          margin=dict(l=20, r=0, b=20, t = 30),
                                          autosize=True,
                                          height = 250,
                                          width = 400,
                                          shapes=[go.layout.Shape(
                                                type='rect',
                                                xref='paper',
                                                yref='paper',
                                                x0=-0.03,
                                                y0=-0.3,
                                                x1=1.01,
                                                y1=1.02,
                                                line={'width': 1, 'color': 'rgb(89, 89, 89)'}
                                                )]
                                          )                           

                        # format the ticks to match each decade and rotate the labels
                        fig.update_xaxes(tickmode='linear', tick0=1830, dtick=10)
                        fig.update_xaxes(tickangle=45)

                        st.plotly_chart(fig, use_container_width = True)
                        
                                                     

              
