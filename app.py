from flask import Flask, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/previsao/<ar>/<info>/<horas>', methods=['GET'])
def previsao(ar: str, info: str, horas: int):
    if ar == 'comar' and info == 'tempar':
        with open('modelos/tempar/model_comar', 'rb') as f:
            modelo_salvo_comar = pickle.load(f)
        with open('modelos/tempar/ultimas_horas_com_ar.p', 'rb') as f:
            ultimas_horas_com_ar = pickle.load(f)

        horas = int(horas)

        previsoes = modelo_salvo_comar.predict(horas)
        index_str = previsoes.index.astype('str')
        previsoes = previsoes.reindex(index_str)
        resposta = {
            'anteriores': ultimas_horas_com_ar,
            'previsao' : previsoes.to_dict()
            }
        return jsonify(resposta)
    if ar == 'semar' and info == 'tempar':
        with open('modelos/tempar/model_semar', 'rb') as f:
            modelo_salvo_comar = pickle.load(f)
        with open('modelos/tempar/ultimas_horas_sem_ar.p', 'rb') as f:
            ultimas_horas_sem_ar = pickle.load(f)

        horas = int(horas)

        previsoes = modelo_salvo_comar.predict(horas)
        index_str = previsoes.index.astype('str')
        previsoes = previsoes.reindex(index_str)
        resposta = {
            'anteriores': ultimas_horas_sem_ar,
            'previsao' : previsoes.to_dict()
            }
        return jsonify(resposta)
