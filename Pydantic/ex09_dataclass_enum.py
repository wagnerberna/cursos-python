from click import style
from pydantic.dataclasses import dataclass
from typing import Tuple
from enum import Enum

# Toppings enumera opções para os dois valores da tupla
class Topping(str, Enum):
    mozzarella = "mozzarella"
    tomato_sauce = "tomato sauce"
    prosciutto = "prosciutto"
    basil = "basil"
    rucola = "rucola"


@dataclass
class Pizza:
    style: str
    toppings: Tuple[Topping, ...]


p1 = Pizza(style="Vegan", toppings=("rucola", "mozzarella"))
print(p1)

p1 = Pizza(style="Vegan", toppings=("ricota", "teste"))
print(p1)
