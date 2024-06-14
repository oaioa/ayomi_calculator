from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.getenv("MONGO_URL"))
db = client["calculator_database"]
collection = db["operations_history"]

def insert_operation(operation: str, result: float)-> None:
    collection.insert_one({
        "operation": operation,
        "result": result,
        "date": datetime.now()
    })

def query_operation(operation: str)-> list[dict]:
    return list(collection.find({"operation": operation}))

