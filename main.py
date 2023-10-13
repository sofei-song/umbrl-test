from typing import Union

 

from fastapi import FastAPI

from app.routes import users

 

app = FastAPI()

 

app.include_router(users.router)

 

@app.get("/")

async def root():

    return {"message": "Hello Bigger Applications!"}