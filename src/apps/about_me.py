from dash import html, dcc
import dash_bootstrap_components as dbc
linkedin_icon = '/assets/icons/linkedin_icon.png'
github_icon = '/assets/icons/github_icon.png'
gmail_icon = '/assets/icons/gmail_icon.png'

introduction_section = html.Div([
            html.H1('Hello! My name is José'),
            html.H5('You can also call me Zé, or Jubis'),
            html.Hr(),
            html.P(["Thank you for visiting my personal website, here you can find out about my ",
                   html.A(
                       href="/portfolio",
                       children="portfolio and personal projects"
                   ),
                   ", download my resume in ",
                   html.A(href="/assets/jose_ferreira_06_2023_en.pdf",
                          children="english",
                          target="_blank"),
                    " or ",
                    html.A(href="/assets/jose_ferreira_06_2023_pt_br.pdf",
                        children="portuguese",
                        target="_blank"), 
                        " and acess to my contacts at the bottom of the page."
                   ]),
            html.P(["Feel free to write any suggestions of improvements, bugs encountered or just to have a small talk.",
                    html.Br(),
                    "This page is made using Python Dash, deployed using dash-tools and hosted on Render."])
                   
            ])

about_me_section = html.Div([html.H3("About me"),
                          html.P(children=["I enjoy empowering people and organizations using Data Science and Machine Learning.",
                                html.Br(),
                                """I started working with Data, during my master degree research in 2019, where I was trying 
                                to understand movement patterns of animals, using Python and symbolic mathematics using Mathematica.""",
                                html.Br(),
                                "Fast-foward to today, I've had the privilege to work for a ",
                                html.A(href="https://www.grao.com.br/",
                                        children='start-up fintech',
                                        target='_blank'),
                                " a ",
                                html.A(href="https://dhauz.com/en-us/solucoes/pharma/",
                                        children=" consultancy company ",
                                        target="_blank"),
                                " where I worked in one of the 5 biggest pharmaceutical companies in the world, ",
                                html.A(href="https://bigdata.com.br/en/",
                                        children="retail start-up ",
                                        target="_blank"),
                                """ delivering recommendations for more than 500 thousands customers. 
                                Now I'm focused on creating solutions for small companies, providing bussiness and data 
                                consultancy."""])])

contact_links = html.Div([
                html.P([
                html.A(
                href="https://www.linkedin.com/in/joseferreiradata/?locale=en_US",
                target="_blank",
                children=[
                html.Img(
                    alt="Link to my Linkedin",
                    src=linkedin_icon,
                    height=35
                    ),
                    'linkedin'
                    ],
                ),
            " / ",
            html.A(
                href="https://github.com/jubiss ",
                target="_blank",
                children=[
                html.Img(
                    alt="Link to my Github",
                    src=github_icon,
                    height=35
                    ),
                    'github'
                    ],
                ),
            " / ",
            html.A(
                href="mailto:jose.edivaldo.fisica@gmail.com",
                target="_blank",
                children=[
                html.Img(
                    alt="Link to my Gmail",
                    src=gmail_icon,
                    height=35
                    ),
                    'gmail'
                    ],
            )]
            )],
            style={'margin-top': '100px',
                   'justify-content': 'center',
                   'text-align': 'center'}
            )

layout = html.Div([
            dbc.Col([introduction_section, about_me_section]),
            contact_links,
])
