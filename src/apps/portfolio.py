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
    #html.H3("Real Estate Scraper"),
    html.P("""I developed a structured scraper using the Scrapy-Selenium framework to collect real estate data 
           from the VivaReal website, with a focus on the city of Recife. The project faced challenges related to handling 
           dynamic websites.."""),
    html.P("""Structured data collection of real estate information in Recife. Use of the Scrapy-Selenium framework for
            interacting with dynamic websites. Implementation of a lag between requests to avoid server overload.
            Organized data manipulation and storage using pipelines and items in Scrapy. """),
    html.P("""In the Real Estate Crawler repository, you can find more details about the implementation, source code,
            and project configuration.""")])

layout = html.Div([
            dbc.Col(
                children=[html.H1('Portfolio'),
                          introduction,
                          real_estate_scraper],
                width=6)
            
])