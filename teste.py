import pandas as pd
import pickle

with open('modelos/tempar/model_comar', 'rb') as f:
  modelo_salvo_comar = pickle.load(f)

previsoes = modelo_salvo_comar.predict(12)
index_str = previsoes.index.astype('str')
previsoes = previsoes.reindex(index_str)
res = {'oi' : previsoes}

print(previsoes.to_dict())