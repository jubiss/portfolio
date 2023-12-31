import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_custom_components.my_components as c1
# Connect to main app.py file
from apps import about_me, portfolio

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                title='JubissPage'
                )
server = app.server

# Sidebar links to pages
link_list = [("01. About me", "/"),
             #("Experience", "/experience"),
             ("02. Portfolio", "/portfolio"),
             #("Contact", "/contact"),
             #("Publications", "/publications")
             ]





navbar, CONTENT_STYLE = c1.navbar(link_list=link_list, color='#000248')

#CONTENT_STYLE['backgroundColor'] = '#596854'
content = html.Div(id='page-content', style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), navbar, content],)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """
    Determines the content to display based on the current URL pathname.

    Args:
        pathname (str): Current URL pathname.

    Returns:
        str or dash.Dash: Layout of the selected page or "404 Page not found" message.
    """
    if pathname == '/':
        return about_me.layout
    if pathname == '/portfolio':
        return portfolio.layout
    else:
        return '404 Page not found'

if __name__ == '__main__':
    #app.layout = html.Div([dcc.Location(id="url"), navbar, content])
    app.run_server(debug=True)