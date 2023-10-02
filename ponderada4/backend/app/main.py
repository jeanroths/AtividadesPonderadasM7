from fastapi.middleware.cors import CORSMiddleware
from models import UserSchema, ModelResultSchema
from db import database, User, ModelResult
from fastapi.responses import JSONResponse, HTMLResponse
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer
from fastapi import FastAPI, Body, Depends, UploadFile, HTTPException
from pycaret.classification import *
import pandas as pd
import random
import subprocess


app = FastAPI()

model = load_model("modelo_ponderada3_teste")

async def check_user(data:UserSchema):
    if not database.is_connected:
        await database.connect()
    users = await User.objects.all()
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/users/signup", tags=["users"])
async def create_user(user: UserSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
    await User.objects.create(
        email=user.email,
        password=user.password
    )
    return signJWT(user.email)

@app.post("/users/login", tags=["users"])
async def user_login(user: UserSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Usuário ou senha inválidos"}

@app.post("/predict-and-store/", tags=["run predict"]) #dependencies=[Depends(jwtBearer())])
async def predict_and_store(model: ModelResultSchema = Body(default=None)):
    try:
        # Ler o arquivo Parquet
        #print(file.filename)
        #df = pd.read_csv(file.file)

        # Realizar a previsão usando o modelo
        #previsoes = predict_model(model, data=df)
        # Se a aplicação funcionasse corretamente, o código abaixo seria substituido pelo código acima e leria a tabela no banco de dados com o target mortes de predicted
        previsoes = round(random.uniform(0, 1), 2)
        mortes = random.randint(1, 5)
        # Armazenar o resultado no banco de dados
        #dados_para_armazenar = {"accuracy": float(previsoes), "predicted": "1 morte"}
        await ModelResult.objects.create(accuracy = float(previsoes), predicted = str(mortes) + " morto(s)" )
        #accuracy=previsoes["prediction_label"].iloc[0] 
        
        
        return JSONResponse(content=[
            {"accuracy": float(previsoes), "predicted": str(mortes) + " morto(s)"}
        ], status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.get("/model-results", tags=["resultados"])#, dependencies=[Depends(jwtBearer())])
async def get_model_results():
    try:
        # Conectar ao banco de dados
        await database.connect()

        # Consulta para obter todos os resultados do modelo
        results = await ModelResult.objects.order_by(ModelResult.id.desc()).limit(3).all()

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com", password="senha")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

origins = ["*"]  # Substitua pelo URL do seu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
