from fastapi import FastAPI
from src.core.schemas import NPIExpression
from src.core.calculator import compute_npi
from src.data.csv_operations import get_stream
from src.data.mongodb import insert_operation

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/operation")
async def operation(op:NPIExpression):
    result = compute_npi(op)
    insert_operation(op, result)
    return {"operation": compute_npi(op)}


@app.get("/getCsv")
async def get_csv(op:str):
    return get_stream(op)