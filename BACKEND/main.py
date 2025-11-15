from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from db import engine, get_db
from routers import auth_routes, requests, pullers, admin


app = FastAPI(title='CUET IOTRIX E-RICKSHAW AUTOMATION SYSTEM')
app.include_router(auth_routes.router)
app.include_router(requests.router)
app.include_router(pullers.router)
app.include_router(admin.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get('/')
def test():
    return {'msg': 'Hello World'}