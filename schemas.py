import json
from typing import List, Optional
from pydantic import BaseModel


class Car(BaseModel):
    id: int
    size: str
    fuel: str
    doors: int
    transmission: str


def load_db() -> list:
    with open("cars.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]
