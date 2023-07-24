import dash_bootstrap_components as dbc
from dash import html, dash_table, dcc
text_font_size = '18px'

def project_card(title, description, technologies, href):
    card = html.A(
        href=href,
        children=[dbc.Card(
                    [
                    dbc.CardHeader([
                        html.H5(title, className='card-title')
                    ]),
                    dbc.CardBody(html.P(description, className='card-text',
                                        style={'height': '4.375em',})),
                    dbc.CardFooter(html.P(technologies),
                                   style={'height': '3.5em',})
                    ]
                    , style={'width': '30.75em'}
                    )
                    ],
        style={'text-decoration': 'none'},
        target='_blank'
    )
    return card