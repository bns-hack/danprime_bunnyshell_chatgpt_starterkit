from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str

app = FastAPI(
        title="FastAPI Backend ChatGPT with Docs",
        description="Use it to manage context and documents",
        version="0.0.1",
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
            })

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q":q}

@app.post("/prompt")
async def incoming_prompt(prompt: Prompt):
    #TODO: log incoming and outgoing data
    return prompt
