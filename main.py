from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SocialBox API")

class State(BaseModel):
    world: dict
    agent: dict
    goals: list[str]

@app.get("/health")
def health(): return {"ok": True}

@app.post("/tri_decide")
def tri_decide(state: State):
    opts=[{"id":"patrol_east"},{"id":"fortify_gate"},{"id":"negotiate_bandits"}]
    return {"proposals":opts,"chosen":"fortify_gate"}
