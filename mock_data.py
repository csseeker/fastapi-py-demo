"""
Mocked data source for FastAPI demo.
"""
from typing import List
from models import Item

# Initial mocked data
DATA: List[Item] = [
    Item(id=1, name="Apple", description="A juicy fruit"),
    Item(id=2, name="Banana", description="A yellow fruit"),
    Item(id=3, name="Carrot", description="A crunchy vegetable"),
]
