from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_custom_components import portfolio_components as pc

introduction = html.Div([
    html.P('''Here you will find the links to my project repositories, along with brief descriptions of each project
           and the key findings or results. If you want more detailed information, you can find it in the 
           repositories or you can send me a message.'''),
    html.P("Please note that I am still updating my old projects, so you may come across changes from time to time.")])

real_estate_scraper = pc.project_card(
                        title="Real Estate Scraper", 
                        description="""
                                    Scraper that interact, collect, and make the initial ETL of Real Estate data from dynamic websites, using the Scrapy-Selenium framework.  
                                    """,
                        technologies='Scrapy-Selenium | Pandas | Scraping | ETL',
                        href="https://github.com/jubiss/real_estate_crawler")

dash_personal_web = pc.project_card(
                        title="Dash Personal Website", 
                        description="""
                                    Repository used to create this page.
                                    """,
                        technologies='Dash | Html | Bootsrap | CSS',
                        href="https://github.com/jubiss/portfolio")

dash_components = pc.project_card(
                        title="Dash custom components", 
                        description="""
                                    Repository of my custom dash (html, bootstrap) components, used as a submodule for my projects.
                                    """,
                        technologies='Dash | Html | Bootsrap',
                        href="https://github.com/jubiss/dash_custom_components")

dash_template = pc.project_card(
                        title="Dash Multipage Template", 
                        description="""
                                    Repository template that I use to make easier to start and
                                    deploy my projects that envolve working with dashboards using Dash.
                                    """,
                        technologies='Dash | CSS | Batch | Gunicorn | Data Analysis',
                        href="https://github.com/jubiss/dash_basic_repository")

data_science_template = pc.project_card(
                        title='Data Science Template', 
                        description="""
                                    Repository template that I use to make easier to start my projects of Data Science, and follows my 
                                    personal Workflow.""",
                        technologies='Batch | Scikit-learn | SQL | Data Science | Machine Learning',
                        href="https://github.com/jubiss/data_science_template"
                        )

layout = html.Div([
            dbc.Col(
                children=[html.H2('Portfolio'),
                          introduction,
                          dbc.Row([dbc.Col(real_estate_scraper,width=6)]),
                          html.H2('Personal Projects'),
                          dbc.Row([
                              dbc.Col(dash_personal_web, width=6),
                              dbc.Col(dash_components, width=6),]),
                            html.Br(),
                          dbc.Row([
                              dbc.Col(dash_template, width=6),
                              dbc.Col(data_science_template, width=6)
                            ])
                          
                          ],
                )
            ])