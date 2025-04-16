# Import required libraries
from dash import html
from dash import dcc
from dash import  html, Input, Output, State
import dash_bootstrap_components as dbc
from dash import Dash
from dash_chat import ChatComponent
import torch
from model import Chatbot


chatbot = Chatbot()


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


# Create a dash application
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    dcc.Tabs(
        [
            dcc.Tab(
                label="A6 - Chatbot",
                children=[
                    html.H2(
                        children="Chatbot",
                        style={
                            "textAlign": "center",
                            "color": "#503D36",
                            "font-size": 40,
                        },
                    ),
                    dbc.Stack(
                        dcc.Textarea(
                            id="note",
                            value="""Note : This chatbot knows about Kaung Nyo Lwin. You can ask me about him.""",
                            style={
                                "width": "100%",
                                "height": 15,
                                "whiteSpace": "pre-line",
                                "textAlign": "center",
                            },
                            readOnly=False,
                        )
                    ),                    
                    html.Br(),
                   ChatComponent(
        id="chat-component",
        messages=[
            {"role": "assistant", "content": "Hello!, You can ask me about Kaung Nyo Lwin."},
        ],
    ),
                ],
            ),
        ]
    )
)




@app.callback(
    Output("chat-component", "messages"),
    Input("chat-component", "new_message"),
    State("chat-component", "messages"),
    prevent_initial_call=True,
)
def handle_chat(new_message, messages):
    if not new_message:
        return messages

    updated_messages = messages + [new_message]
    
    if new_message["role"] == "user":
        response = chatbot.chat(new_message["content"])
        bot_response = {"role": "assistant", "content": response}
        chatbot.history.add_user_message(new_message["content"])
        chatbot.history.add_ai_message(response)
        return updated_messages + [bot_response]

    return updated_messages

# Run the app
if __name__ == "__main__":
    app.run_server()
