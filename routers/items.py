"""
APIRouter for item endpoints. Demonstrates FastAPI router usage.
"""
from fastapi import APIRouter, HTTPException, Query, Path, Body, Depends, BackgroundTasks
from typing import List
from models import Item, ItemModel, get_data_source, log_action

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[ItemModel])
def list_items(data=Depends(get_data_source)):
    """List all items."""
    return [item.to_model() for item in data]

@router.get("/{item_id}", response_model=ItemModel)
def get_item(item_id: int = Path(..., ge=1), data=Depends(get_data_source)):
    """Get item by ID."""
    for item in data:
        if item.id == item_id:
            return item.to_model()
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/", response_model=ItemModel)
def create_item(item: ItemModel = Body(...), data=Depends(get_data_source)):
    """Create a new item."""
    new_id = max([i.id for i in data], default=0) + 1
    new_item = Item(id=new_id, name=item.name, description=item.description)
    data.append(new_item)
    return new_item.to_model()

@router.put("/{item_id}", response_model=ItemModel)
def update_item(item_id: int, item: ItemModel, data=Depends(get_data_source)):
    """Update an item."""
    for i in data:
        if i.id == item_id:
            i.update(name=item.name, description=item.description)
            return i.to_model()
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/{item_id}")
def delete_item(item_id: int, data=Depends(get_data_source)):
    """Delete an item."""
    for i, item in enumerate(data):
        if item.id == item_id:
            del data[i]
            return {"detail": f"Item {item_id} deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/{item_id}/log")
def log_item_action(item_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_action, f"Item {item_id} accessed")
    return {"detail": "Action will be logged in background."}

@router.get("/{item_id}/action")
def item_action(item_id: int, action: str = Query(...)):
    action_type = action.removeprefix("do_")
    if action_type == "view":
        return {"action": "view", "item_id": item_id}
    elif action_type == "edit":
        return {"action": "edit", "item_id": item_id}
    else:
        raise HTTPException(status_code=400, detail=f"Unknown action: {action}")
