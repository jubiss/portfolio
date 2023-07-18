from dash import html, dcc
import dash_bootstrap_components as dbc
linkedin_icon = '/assets/linkedin_icon.png'
layout = html.Div([
            html.H1('Hello! My name is José'),
            html.Hr(),
                dbc.Col([
                    dcc.Markdown("""
                        I enjoy empowering people and organizations using Data Science and Machine Learning. \n
                        I started working with Data, during my master degree research in 2019, where I was trying to understand movement patterns of animals, using Python and Octave and symbolic mathematics using Mathematica.
                        
                        Fast-foward to today, I've had the privilege to work for a [start-up fintech](https://www.grao.com.br/), a [consultancy company](https://dhauz.com/en-us/solucoes/pharma/) where I was allocated in a top 5 pharmaceutical company,
                        [tech-company focused on retailing](https://bigdata.com.br/en/). These days I'm focused on creating solutions for small companies, providing bussiness and data consultancy.
                        """)
                        ], width=6
                        ),
            dcc.Markdown("""
                        Feel free to write for UI/UX suggestions, ideas or bug.\n                         
                         """),
                         html.A(
                            href="https://www.linkedin.com/in/joseferreiradata/?locale=en_US",
                            children=[
                            html.Img(
                                alt="Link to my Linkedin",
                                src=linkedin_icon,
                                )
                                ]
                            ),
                         html.A(
                            href="https://github.com/jubiss ",
                            children=[
                            html.Img(
                                alt="Link to my Github",
                                src=linkedin_icon,
                                )
                                ]
                            ),
            ])
