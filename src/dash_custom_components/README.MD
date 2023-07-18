# Dash Custom Components

This repository serves as a sub-repository for integrating customized functions for Dash components into your Dash application. If you're developing a Dash application and looking to enhance it with custom features and functionalities, this repository provides a collection of pre-built functions to simplify the customization process.

## Features

- Customized functions for various Dash components.
- Simplified implementation of common customizations.
- Easy integration into your existing Dash application.
- Examples and usage instructions for each custom function.

## Getting Started

To integrate the custom functions from this repository into your Dash application, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Pip package manager

### Installation

1. Add this repository as a sub-repository to your Dash application's project directory:

```bash
git submodule add https://github.com/jubiss/dash_custom_components.git
```

2. Change to the sub-repository directory:

```bash
cd dash_custom_components
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. In your Dash application, import the necessary Dash components and the custom functions from the sub-repository:

```python
from dash import Dash, dcc, html
import dash_custom_components.my_components as my_components
```

2. Use the custom functions within your Dash application's layout and callbacks to customize the behavior and appearance of Dash components:

```python
app = Dash(__name__)

app.layout = html.Div([
    my_components.create_slider(id='custom-slider',width=5, label=None, value=None, min=0, max=10, value=5),
    my_components.radio_items(id='custom-radio', radio_list=[{'Label': 'Option 1', 'value': 'option_1'}], default_value='option_1', width=9),
])

@app.callback(
    Output('custom-slider-output', 'children'),
    [Input('custom-slider', 'value')]
)
def update_output(value):
    return f'The selected value is: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

3. Refer to the examples and usage instructions provided within the custom functions file for detailed information on each function's parameters and functionalities.

## Contributing

Contributions to this repository are welcome! If you have any ideas, suggestions, or improvements, please submit a pull request. Make sure to follow the repository's code style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy integrating these customized Dash components into your Dash application! If you have any questions or need assistance, feel free to reach out. Happy coding!