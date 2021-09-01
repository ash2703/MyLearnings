from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel   #for data handling

"""
How to run: uvicorn main:app --reload
"""

# create a FastAPI instance
app = FastAPI()


@app.get('/')
def index():
    """
    Hello World
    Simple GET request
    """
    return {'Hello' : 'World'}

# Simulate a database for API calls
db = []

@app.post('/scities')
def create_city(city : str):
    """
    Simple POST request
    Add name of city in database and return the item
    """
    db.append(city)
    return db[-1]

@app.get('/cities')
def get_cities():
    """
    Fetch all contents of the database
    """
    return db

class City(BaseModel):
    # Define the expected input data for your api calls
    name: str
    timezone: Optional[str]  # Optional field
    houses: int = Query(..., gt = 0, le = 100) # Query item with constraints on min and max value


@app.post('/cities')
def create_city(city : City):
    """
    Perform more complex additions in the database
    Expected input is a json object
    """
    db.append(city.dict())
    return db[-1]

@app.get('/cities/{id}')
def get_city(id : int):
    return db[id - 1]

@app.delete('/cities/{id}')
def delete_city(id: int):
    db.pop(id-1)
    return {}

# @app.get("/cities/{id}/{name}")
# def get_city_id_name(id: int, name: str):
#     return {"id": id, "query param":name}

# The second param nae is called query param  ex: http://127.0.0.1:8000/cities/1?name=aayush
# @app.get("/cities/{id_name}")
# def get_city_id(id_name: int, name: str = None):
#     return {"id": id_name, "query param":name}
