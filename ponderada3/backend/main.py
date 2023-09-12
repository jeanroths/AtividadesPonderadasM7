import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model
from pycaret.classification import *
from fastapi.middleware.cors import CORSMiddleware

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("modelo_ponderada3_teste")

#Create input/output pydantic models
input_model = create_model("minha_api_input", **{'trecho': 'BR-393/RJ', 'sentido': 'Norte', 'lugar_acidente': 'Rodovia do Aço', 'automovel':  0.103861, 'bicicleta': -0.10293, 'caminhao':-0.530345, 'moto': -0.422491, 'onibus':-0.422491, 'outros': -0.285399, 'tracao_animal':-0.038526, 'transporte_de_cargas_especiais':-0.046129, 'trator_maquinas':-0.027919, 'utilitarios':-0.261778, 'ilesos':-0.266837, 'levemente_feridos':-0.43087, 'moderadamente_feridos':-0.261819, 'gravemente_feridos':-0.137886, 'mortos':-0.123849, 'faixa_km': -0.896777, 'categoria_acidente':  1.150967, 'mes_ano': '01/2010'})
output_model = create_model("minha_api_output", prediction=1.0)

# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)