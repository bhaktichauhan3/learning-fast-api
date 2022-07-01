import json
from typing import List, Optional
from pydantic import BaseModel


class CarInput(BaseModel):
    size: str
    fuel: str
    doors: int
    transmission: str

    class Config:
        schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel": "hybrid"
            }
        }


class CarOutput(CarInput):
    id: int


def load_db() -> type([CarOutput]):
    with open("cars.json") as f:
        return [CarInput.parse_obj(obj) for obj in json.load(f)]


def save_db(cars: type([CarInput])):
    with open("cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)
