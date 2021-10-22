from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/anwar")
def read_root():
    return {"FastAPI sample project by Mohammed"}
