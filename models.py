"""
Shared models and dependencies for FastAPI demo.
"""
from typing import Optional, List
from pydantic import BaseModel, Field
from dataclasses import dataclass, asdict

# Response model using Pydantic
class ItemModel(BaseModel):
    id: int = Field(..., description="Item ID")
    name: str = Field(..., description="Item name")
    description: Optional[str] = Field(None, description="Item description")

# Python 3.13: dataclass with Self type
@dataclass
class Item:
    id: int
    name: str
    description: Optional[str] = None
    def to_model(self) -> ItemModel:
        return ItemModel(**asdict(self))
    def update(self, name: Optional[str] = None, description: Optional[str] = None) -> "Item":
        if name:
            self.name = name
        if description:
            self.description = description
        return self

# Dependency example
def get_data_source():
    import mock_data
    return mock_data.DATA

# Background task example
def log_action(action: str):
    print(f"Action logged: {action}")
