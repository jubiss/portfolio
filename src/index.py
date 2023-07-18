from dash import html, dcc
from dash.dependencies import Input, Output
import dash_custom_components.my_components as c1
# Connect to main app.py file
from app import app
from apps import about_me #page1, page2

# Sidebar links to pages
link_list = [("About me", "/"),
             ("Experience", "/experience"),
             ("Portfolio", "/portfolio"),
             ("Contact", "/contact"),
             ("Publications", "/publications"),
             ("Resume", "/resume")]

sidebar, CONTENT_STYLE = c1.side_navbar(sidebar_name="José Ferreira", sidebar_description=None, link_list=link_list)

content = html.Div(id='page-content', style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

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
    if pathname == '/page2':
        return # page2.layout
    else:
        return '404 Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)