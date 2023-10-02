from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra = {
            "schema_user" : {
                "email": "teste@mail.com",
                "password":"123",
                "id": 1
            }
        }  

class ModelResultSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    accuracy: float = Field(default=None)
    predicted: str = Field(default=None)
    # Configuração criada para documentação do modelo
    class Config:
        schema_extra = {
            "post_teste" : {
                "accuracy": 1.0,
                "predicted": "1 mes"
            }
        }