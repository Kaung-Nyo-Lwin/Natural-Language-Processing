# Import required libraries
import numpy as np
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import os
import pickle
import dash_bootstrap_components as dbc
from dash import Dash
import gensim
import nltk
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
nltk.download("reuters")
nltk.download('punkt')
nltk.download('punkt_tab')

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

filename = './model/glove_gensim_model_50.model'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a dash application
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    dcc.Tabs(
        [
            dcc.Tab(
                label="A1 - Search Engine",
                children=[
                    html.H2(
                        children="Search Engine",
                        style={
                            "textAlign": "center",
                            "color": "#503D36",
                            "font-size": 40,
                        },
                    ),
                    dbc.Stack(
                        dcc.Textarea(
                            id="note",
                            value="""Note : The corpus trained is about fuel. Please search like fuel price, diesel, petroleum""",
                            style={
                                "width": "100%",
                                "height": 10,
                                "whiteSpace": "pre-line",
                                "textAlign": "center",
                            },
                            readOnly=False,
                        )
                    ),                    
                    dbc.Stack(
                        dcc.Textarea(
                            id="input",
                            value="""Type Here""",
                            style={
                                "width": "100%",
                                "height": 80,
                                "whiteSpace": "pre-line",
                            },
                            readOnly=False,
                        )
                    ),
                    html.Div(
                        html.Button(
                            "Search",
                            id="search",
                            n_clicks=0,
                            style={
                                "marginRight": "10px",
                                "margin-top": "10px",
                                "width": "100%",
                                "height": 50,
                                "background-color": "white",
                                "color": "black",
                            },
                        ),
                    ),
                    html.Br(),
                    dcc.Textarea(
                        id="result",
                        value="see here",
                        style={
                            "width": "100%",
                            "height": 300,
                            "whiteSpace": "pre-line",
                            "font-size": "1.5em",
                            "textAlign": "center",
                            "color": "#503D36",
                        },
                        readOnly=True,
                    ),
                ],
            ),
        ]
    )
)

flatten = lambda l: [item for sublist in l for item in sublist]

def prepare_corpus(corpus):
    corpus = [word_tokenize(sent) for sent in corpus]
    vocab = list(set(flatten(corpus)))
    word2index = {w: i+1 for i, w in enumerate(vocab)}
    vocab.append('<UNK>')
    voc_size = len(vocab)
    word2index['<UNK>'] = 0
    index2word = {v:k for k, v in word2index.items()}
    
    return corpus, vocab, voc_size, word2index, index2word

# docs = [reuters.raw(doc) for doc in reuters.fileids(reuters.categories())]
docs = [reuters.raw(doc) for doc in reuters.fileids("fuel")]
docs_dict = {}
for i,d in enumerate(docs):
    docs_dict[i] = d
    
Corpus, _, _, _, _ = prepare_corpus(docs)

def remove_oov(corpus,model):
    for word in corpus:
        if word not in model.index_to_key:
            # print(word)
            corpus.remove(word)
    return corpus

for _ in range(10):
    Corpus_dict = {}
    for i,sublist in enumerate(Corpus):
        c_list = remove_oov(sublist,loaded_model)
        Corpus_dict[i] = c_list
        # print(c_list)
        
def Corpus_vec(Corpus_dict,query,model):
    
    Corpus_vec_dict = []
    query = remove_oov(query.split(" "),model)
    query_vec = model[query].mean(0).T
    for k,v in Corpus_dict.items():
        sim = model[v].mean(0) @ query_vec
        Corpus_vec_dict.append(sim)
    return Corpus_vec_dict

def retrieve(docs_dict,index):
    output = ""
    for i,ind in enumerate(index):
        output += f"{i+1}" + "\n-----------------------\n" + docs_dict[ind]
        
    return output

top_paras_index = np.argsort(Corpus_vec(Corpus_dict,"fuel price",loaded_model))[-11:-1]

@app.callback(
    Output(component_id="result", component_property="value"),
    [
        Input(component_id="input", component_property="value"),
        Input(component_id="search", component_property="n_clicks")
     ],
)
def search(input,n_clicks):
    if n_clicks == 0:
        global c
        c = n_clicks
        result = "see here"
    elif n_clicks != c:
        # key_words =  [word[0] for word in loaded_model.most_similar(input.split(" "))]
        top_paras_index = np.argsort(Corpus_vec(Corpus_dict,input,loaded_model))[-11:-1]
        result = retrieve(docs_dict,top_paras_index)
        # result = loaded_model[input]        
    else:
        result = "refresh"

    return result

# Run the app
if __name__ == "__main__":
    app.run_server()
