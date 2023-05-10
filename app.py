from flask import Flask, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/previsao/<ar>/<info>/<horas>', methods=['GET'])
def previsao(ar: str, info: str, horas: int):
    if ar == 'comar' and info == 'tempar':
        with open('modelos/tempar/model_comar', 'rb') as f:
            modelo_salvo_comar = pickle.load(f)

        horas = int(horas)

        previsoes = modelo_salvo_comar.predict(horas)
        index_str = previsoes.index.astype('str')
        previsoes = previsoes.reindex(index_str)
        resposta = {
            'anteriores': 'anteriores',
            'previsao' : previsoes.to_dict()
            }
        return jsonify(resposta)
    if ar == 'semar' and info == 'tempar':
        with open('modelos/tempar/model_semar', 'rb') as f:
            modelo_salvo_comar = pickle.load(f)

        horas = int(horas)

        previsoes = modelo_salvo_comar.predict(horas)
        index_str = previsoes.index.astype('str')
        previsoes = previsoes.reindex(index_str)
        resposta = {
            'anteriores': 'anteriores',
            'previsao' : previsoes.to_dict()
            }
        return jsonify(resposta)
