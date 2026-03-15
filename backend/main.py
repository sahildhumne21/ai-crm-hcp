from fastapi import FastAPI
from database import engine
from models import Base
from agents.langgraph_agent import run_agent

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI CRM HCP backend running"}

@app.post("/chat")
def chat(message: str):

    response = run_agent(message)

    return response