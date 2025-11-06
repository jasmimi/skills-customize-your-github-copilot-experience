from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Demo - Items")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# In-memory "database"
items_db = {
    1: Item(id=1, name="Widget", description="A useful widget", price=9.99),
    2: Item(id=2, name="Gadget", description="A fancy gadget", price=19.99),
}
next_id = max(items_db.keys()) + 1


@app.get("/items", response_model=List[Item])
def list_items():
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global next_id
    item.id = next_id
    items_db[next_id] = item
    next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated.id = item_id
    items_db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None
