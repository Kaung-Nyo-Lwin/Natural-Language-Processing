import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from transformers import pipeline
from datetime import datetime

# Initialize the Dash app with a modern theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Initialize the text generation pipeline
model_name = "kaung-nyo-lwin/dpo_gpt2_nlp_a5"  # You can change this to any other GPT model
generator = pipeline('text-generation', 
                    model=model_name,
                    device=-1)  # device=-1 for CPU, device=0 for GPU

def generate_response(prompt, max_length=100):
    # Generate response using the pipeline
    response = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        do_sample=True,
        pad_token_id=50256  # EOS token ID for GPT-2
    )
    
    # Extract the generated text and remove the prompt
    generated_text = response[0]['generated_text']
    return generated_text[len(prompt):].strip()

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("GPT2_DPO Chat App", className="text-center my-4"),
            html.Hr(),
        ])
    ]),
    
    # Chat display area
    dbc.Row([
        dbc.Col([
            html.Div(id="chat-display", style={
                "height": "400px",
                "overflowY": "auto",
                "border": "1px solid #ddd",
                "borderRadius": "5px",
                "padding": "10px",
                "backgroundColor": "#f8f9fa"
            })
        ])
    ]),
    
    # Input area
    dbc.Row([
        dbc.Col([
            dbc.Input(
                id="user-input",
                type="text",
                placeholder="Type your message here...",
                className="my-3"
            ),
            dbc.Button(
                "Send",
                id="send-button",
                color="primary",
                className="float-end"
            ),
            # Store for chat history
            dcc.Store(id='chat-history', data=[]),
            # Loading spinner
            dbc.Spinner(html.Div(id="loading-output"))
        ])
    ])
], fluid=True)

@app.callback(
    [Output('chat-display', 'children'),
     Output('chat-history', 'data'),
     Output('user-input', 'value')],
    [Input('send-button', 'n_clicks'),
     Input('user-input', 'n_submit')],
    [State('user-input', 'value'),
     State('chat-history', 'data')],
    prevent_initial_call=True
)
def update_chat(n_clicks, n_submit, user_input, chat_history):
    if not user_input:
        return dash.no_update, dash.no_update, dash.no_update
    
    # Add user message to chat history
    timestamp = datetime.now().strftime("%H:%M")
    chat_history.append({
        'sender': 'user',
        'message': user_input,
        'time': timestamp
    })
    
    # Generate bot response
    bot_response = generate_response(user_input)
    
    # Add bot response to chat history
    chat_history.append({
        'sender': 'bot',
        'message': bot_response,
        'time': timestamp
    })
    
    # Create chat display
    chat_display = []
    for msg in chat_history:
        if msg['sender'] == 'user':
            chat_display.append(
                dbc.Card(
                    dbc.CardBody([
                        html.P(msg['message'], className="mb-0"),
                        html.Small(msg['time'], className="text-muted")
                    ]),
                    className="mb-2 float-end",
                    style={"maxWidth": "70%", "backgroundColor": "#007bff", "color": "white"}
                )
            )
        else:
            chat_display.append(
                dbc.Card(
                    dbc.CardBody([
                        html.P(msg['message'], className="mb-0"),
                        html.Small(msg['time'], className="text-muted")
                    ]),
                    className="mb-2",
                    style={"maxWidth": "70%", "backgroundColor": "#f8f9fa"}
                )
            )
        chat_display.append(html.Br())
    
    return chat_display, chat_history, ''

if __name__ == '__main__':
    app.run_server(debug=True)
