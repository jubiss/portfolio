from dash import html, dcc
import dash_bootstrap_components as dbc


introduction = html.Div([
    html.P('''Here you will find the links to my project repositories, along with brief descriptions of each project
           and the key findings or results. If you want more detailed information, you can find it in the 
           repositories or you can send me a message.'''),
    html.P("Please note that I am still updating my old projects, so you may come across changes from time to time.")])

real_estate_scraper = html.Div([
    html.A(href="https://github.com/jubiss/real_estate_crawler",
            children=html.H3("Real Estate Scraper"),
            target="_blank"),
    html.P("""I developed a structured scraper using the Scrapy-Selenium framework to interact and collect Real Estate data from 
           dynamic websites. 
           """),
    html.P("""I implemented the scraper following good pratices for scrapping and programming.
           I created a modular code using OOP and is responsible for scraping and making an initial ETL of the data, 
           using Scrapy Pipelines.""")
])

dash_personal_web = html.Div([
    html.A(href="https://github.com/jubiss/portfolio",
           children=html.H3("Dash Portfolio"),
           target="_blank"),
    html.P("""This is the repository of this page, done using Dash and deployed with Gunicorn and Render."""),
    html.P("""Is under continuous development, since I'm still adjusting some of my old projects.""")
])

dash_components = html.Div([
    html.A(href="https://github.com/jubiss/dash_custom_components",
           children=html.H3("Dash custom components"),
           target="_blank"),
    html.P("I developed a repository to keep my custom components that I build on data visualization projects that I use Dash."),
    html.P("""Normally I use as a submodule of my projects, in this way I keep updating this repository, for each new addition
           that I need to make in other projects, and I can make other projects faster."""),
])

dash_template = html.Div([
    html.A(href="https://github.com/jubiss/dash_basic_repository",
           children=html.H3("Dash Multipage Template"),
           target="_blank"),
    html.P("""
            It's a repository template that I use to make easier to start my projects that envolve doing a dashboard with Dash.
           Beyond the repository structure I also use bat scripts to begin my project faster and in a format that is easier to deploy.""")
])

data_science_template = html.Div([
    html.A(href="https://github.com/jubiss/data_science_template",
           children=html.H3("Data Science Template"),
           target="_blank"),
    html.P("""
           It's a repository template that I use to make easier to start my projects of Data Science, and follows my personal Workflow.""")
])

layout = html.Div([
            dbc.Col(
                children=[html.H2('Portfolio'),
                          introduction,
                          real_estate_scraper,
                          html.H2('Personal Projects'),
                          dash_personal_web,
                          dash_components,
                          dash_template,
                          data_science_template
                          ],
                width=6)
            
])