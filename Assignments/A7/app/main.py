import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from transformers import pipeline

# Initialize the toxic text classification pipeline
classifier = pipeline("text-classification", model="kaung-nyo-lwin/even_student")

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Toxic Text Classifier - A7", className="text-center my-4"),
            html.Div([
                dbc.Input(
                    id="text-input",
                    placeholder="Enter text to analyze...",
                    type="text",
                    className="mb-3",
                    style={"height": "100px"}
                ),
                dbc.Button("Analyze", id="analyze-button", color="primary", className="mb-3"),
                html.Div(id="output-result", className="mt-3")
            ])
        ], width=6)
    ], justify="center")
], fluid=True)

@callback(
    Output("output-result", "children"),
    [Input("analyze-button", "n_clicks")],
    [Input("text-input", "value")]
)
def analyze_text(n_clicks, text):
    if n_clicks is None or not text:
        return ""
    
    # Get the classification result
    result = classifier(text)[0]
    print(result)
    
    # Format the output
    label = "Toxic" if result["label"] == "hate" else "Not Toxic"
    score = round(result["score"] * 100, 2)
    
    # Create color-coded output
    color = "danger" if result["label"] == "hate" else "success"
    
    return dbc.Alert([
        html.H4(f"Result: {label}", className="alert-heading"),
        html.P(f"Confidence Score: {score}%")
    ], color=color)

if __name__ == "__main__":
    app.run_server(debug=True)
