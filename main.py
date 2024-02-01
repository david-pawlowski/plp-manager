from fastapi import FastAPI

from models import Player

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/players")
async def create_player():
    player = Player(name="Messi")
    return {"message": "Hello World"}
