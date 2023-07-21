import dash_bootstrap_components as dbc
from dash import html, dash_table, dcc
text_font_size = '18px'

def side_navbar(sidebar_name=None, sidebar_description=None, link_list=None, footer_list=None):
    """
    Ref: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/page-2
    """
    # the style arguments for the sidebar. We use position:fixed and a fixed width
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#596854",
    }
    if link_list==None:
        link_list = [("Home", "/"),
                     ("Page 1", "/Page-1"),
                     ("Page 2", "/Page-2"),]
    nav_link = []
    for link in link_list:
        nav_link.append(dbc.NavLink(link[0], href=link[1], active="exact"))

    sidebar = html.Div(
    [
        html.H2(sidebar_name, className="display-4"),
        html.Hr(),
        html.P(sidebar_description, className="lead"),
        dbc.Nav(nav_link,
                vertical=True,
                pills=True,
        ),
        html.Footer(children=footer_list,
                    style={'bottom': 0})
    ],
    style=SIDEBAR_STYLE,
    )
    # the styles for the main content position it to the right of the sidebar and
    # add some padding.
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }

    return sidebar, CONTENT_STYLE

def navbar(link_list=None, color='white'):
    """
    Creates a navigation bar component with logo and navigation links.

    Returns:
        dbc.Navbar: Navigation bar component.
    """
    if link_list==None:
        link_list = [("Home", "/"),
                     ("Page 1", "/Page-1"),
                     ("Page 2", "/Page-2"),]
    nav_link = []
    for link in link_list:
        nav_link.append(dbc.NavLink(link[0], href=link[1], active="exact", style={"color": "#F2C0A2"}))

    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        #dbc.Col(html.Img(src=logo_juliana), width=3), #Logo Column
                        dbc.Col(
                            dbc.Nav(nav_link,
                                    navbar=True,
                                    className="justify-content-end",
                            ),
                            style={'align': 'right'},
                            width=9,
                        ),
                    ],
                    #align="center",
                    #className="justify-content-between",  # Added justify-content-between class
                    style={'width': '100%'}
                ),
            ],
        fluid=True),
        color="#D96C75",
        className='mb-5',
    )

    CONTENT_STYLE = {
        #"margin-left": "18rem",
        #"margin-right": "18rem",
        #"padding": "2rem 2rem",
        "margin": "auto",
        "width": "50%",
        "align": "center",
        "color": "#0083FF"
    }

    return navbar, CONTENT_STYLE

def input_top_label(id, label, value, text_font_size=text_font_size):
    """
    Create a container with a labeled input field on top.

    Args:
        id (str): The ID of the input field.
        label (str): The label for the input field.
        value: The initial value of the input field.

    Returns:
        dbc.Container: A container with the labeled input field.
    """
    input_label = dbc.Container(
            [
            dbc.Row(dbc.Label(label, 
                              size="md",
                              style={'font-size': text_font_size}),),
            dbc.Row(dbc.Input(
                    id=id,
                    value=value,
                    type="number",
                    #min=0,
                    #max=300,
                    # className="form-control",
                    style={'width': '150px',
                           'font-size': text_font_size}))
            ]
            )
    return input_label

def centered_table(id, width, table_title=None, text_font_size=text_font_size):
    """
    Create a centered table.

    Args:
        id (str): The ID of the table.
        width (int): The width of the table.
        table_title (str, optional): The title of the table. Defaults to None.

    Returns:
        dbc.Row: A row containing the centered table.
    """
    if table_title:
        
        table = dbc.Row(
                dbc.Col([
                html.H2(table_title, style={'justify': 'center', 'alight': 'center'}),
                dash_table.DataTable(
                        id=id,
                        data=[],
                        columns=[],
                        editable=True,
                        filter_action="native",
                        sort_action="native",
                        page_action="native",
                        page_current= 0,
                        page_size= 10,
                        style_table={'height': '350px', 'overflowY': 'auto'},
                        style_data={
                                'font-family': 'Arial, sans-serif',
                                'font-size': '17px',
                                'text-align': 'left',
                                },
                        style_header={
                                'font-family': 'Arial, sans-serif',
                                'font-weight': 'bold',
                                'background-color': 'lightgray',
                                'border': '1px solid black',
                                'text-align': 'left',
                                'font-size': text_font_size
                                },
                        style_cell={
                                'border': '1px solid grey',
                                'padding': '5px',
                                },
                        
                        )],
                        width=width,
                ),
                justify='center',
                )
    else:
        table = dbc.Row(
                dbc.Col([
                dash_table.DataTable(
                        id=id,
                        data=[],
                        columns=[],
                        editable=True,
                        filter_action="native",
                        sort_action="native",
                        page_action="native",
                        page_current= 0,
                        page_size= 10,
                        style_table={'height': '350px', 'overflowY': 'auto'},
                        style_data={
                                'font-family': 'Arial, sans-serif',
                                'font-size': '17px',
                                'text-align': 'left',
                                },
                        style_header={
                                'font-weight': 'bold',
                                'background-color': 'lightgray',
                                'border': '1px solid black',
                                'text-align': 'left',
                                'font-size': text_font_size
                                },
                        style_cell={
                                'border': '1px solid grey',
                                'padding': '5px',
                                },
                        
                        )],
                        width=width,
                ),
                justify='center',
                )
    return table

def indicator_card(id, width):
    """
    Create an indicator card with a graph.

    Args:
        id (str): The ID of the graph.
        width (int): The width of the card.

    Returns:
        dbc.Col: A column containing the indicator card.
    """
    indicator= dbc.Col(
                dbc.Card(
                        dbc.CardBody(
                        dcc.Graph(figure={}, id=id),
                        className='text-center',
                        style={'padding':0}
                        ),
                        className='mb-4',
                        style={'padding':0}
                ),
                width=width,
                className="d-flex align-items-center justify-content-center"
                )
    return indicator

def create_slider(id, width, label, value, min=1, max=99, step=5,
                  text_font_size=text_font_size):
    slider = dbc.Col([
                    dbc.Label(label,
                              size='md',
                              style={'font-size': text_font_size}),
                    dcc.Slider(min=min,
                               max=max,
                               step=step,
                               value=value,
                               id=id)],
                    width=width
    )
    return slider

def radio_items(id, radio_list, default_value, width=9):
    """
    Component used to create Radio buttons for the dashboard.

    Args:
        id (str): ID of the component
        radio_list (list): Lists of dictionaries in the following format [{'label': label, 'value': value}] 
        default_value (str): Default component value

        width (int): The width of the Radio items.

    """
    radio = dbc.Col(
                dcc.RadioItems(id=id,
                               options=radio_list, 
                                value=default_value,
                                inline=True,
                                labelStyle={'display': 'inline-block', 'margin-right': '10px', 'margin-top': '5px'},
                                style = {'font-size': text_font_size}
                                ),
                            width=width,
                            )
    return radio