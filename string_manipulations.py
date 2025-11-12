from fastapi import FastAPI
from pydantic import BaseModel
from string_ops import reverse_str,to_upper,without_vowels

app = FastAPI()

@app.get("/")
def hello():
    return "hello from string"

@app.get("/reverse")
def reverse_word(text:str):
    reversed_str = reverse_str(text)
    return {"orignal":text,"reversed":reversed_str}

@app.get("/uppercase/{text}")
def reverse_word(text:str):
    upper_str = to_upper(text)
    return {"orignal":text,"reversed":upper_str}

@app.post("/remove-vowels")
def remove_vowels(body:dict):
    clean_str = without_vowels(body.get("string"))
    return clean_str
    