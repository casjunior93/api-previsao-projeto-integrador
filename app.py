from flask import Flask, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

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
            'treinamento': '2023-05-21 15:50:00',
            'anteriores': ultimas_horas_com_ar,
            'previsao' : previsoes.to_dict()
            }
        response = jsonify(resposta)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
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
            'treinamento': '2023-05-21 15:50:00',
            'anteriores': ultimas_horas_sem_ar,
            'previsao' : previsoes.to_dict()
            }
        response = jsonify(resposta)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
