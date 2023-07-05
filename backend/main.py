from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import os
import openai
openai.api_key=os.getenv('OPENAI_API_KEY')

class Prompt(BaseModel):
    prompt: str

app = FastAPI(
        title="FastAPI Backend ChatGPT",
        description="A base for ChatGPT apps",
        version="0.0.1",
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
            })

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/chatgpttest")
async def read_root():
    model_engine = "text-davinci-003"
    prompt = "Hello, how are you today?"
    completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
            )
    return completion

@app.post("/prompt")
async def incoming_prompt(prompt: Prompt):
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt.prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
            )
    #TODO: log incoming and outgoing data
    return completion
