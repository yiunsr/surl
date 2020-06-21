from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/", tags=["items"])
async def read_items():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]


@router.get("/{item_id}", tags=["items"])
async def read_item(item_id: str):
    return {"name": "Fake Specific Item", "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["items"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(status_code=403, detail="You can only update the item: foo")
    return {"item_id": item_id, "name": "The Fighters"}
