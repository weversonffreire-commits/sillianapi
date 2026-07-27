from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "API SGBR funcionando!"
    }
