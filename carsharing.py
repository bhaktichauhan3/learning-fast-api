from datetime import datetime
from typing import Optional, List

import uvicorn
from fastapi import FastAPI, HTTPException

from schemas import load_db

app = FastAPI()
db = load_db()


@app.get("/")
def welcome():
    """Returns a friendly welcome message."""
    return {'message': "Welcome to the car sharing service!"}


@app.get("/date")
def get_current_datetime():
    """Returns the current date/time"""
    return {'date': datetime.now()}


@app.get("/api/cars")
def get_cars(size: Optional[str] = None, doors: Optional[int] = None) -> List:
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)
