import logging
from typing import List

from fastapi import APIRouter, HTTPException

from app.models.sneakers import Sneaker

logger = logging.getLogger()
router = APIRouter()

sneakers: List = []


@router.post("/sneakers", response_model=Sneaker)
async def add_sneaker(sneaker: Sneaker):
    """
    Add a new sneaker to the list of sneakers.

    Args:
        sneaker (Sneaker): The details of the sneaker to be added.

    Returns:
        Sneaker: The details of the added sneaker.
    """
    sneaker.id = len(sneakers) + 1
    sneakers.append(sneaker)
    return sneaker


@router.get("/sneakers", response_model=List[Sneaker])
async def get_sneakers():
    """
    Retrieve the list of all sneakers.

    Returns:
        List[Sneaker]: The list of all sneakers.
    """
    return sneakers


@router.get("/sneakers/{sneaker_id}", response_model=Sneaker)
async def get_sneaker(sneaker_id: int):
    """
    Retrieve the details of a specific sneaker by its ID.

    Args:
        sneaker_id (int): The ID of the sneaker to retrieve.

    Returns:
        Sneaker: The details of the requested sneaker.

    Raises:
        HTTPException: If the sneaker with the given ID is not found.
    """
    sneaker = next((s for s in sneakers if s.id == sneaker_id), None)
    if sneaker is None:
        raise HTTPException(status_code=404, detail="Sneaker not found")
    return sneaker


@router.put("/sneakers/{sneaker_id}", response_model=Sneaker)
async def update_sneaker(sneaker_id: int, sneaker_update: Sneaker):
    """
    Update the details of a specific sneaker.

    Args:
        sneaker_id (int): The ID of the sneaker to update.
        sneaker_update (Sneaker): The updated details of the sneaker.

    Returns:
        Sneaker: The updated details of the sneaker.

    Raises:
        HTTPException: If the sneaker with the given ID is not found.
    """
    sneaker = next((s for s in sneakers if s.id == sneaker_id), None)
    if sneaker is None:
        raise HTTPException(status_code=404, detail="Sneaker not found")
    sneaker.model = sneaker_update.model
    sneaker.brand = sneaker_update.brand
    sneaker.size = sneaker_update.size
    sneaker.color = sneaker_update.color
    return sneaker


@router.delete("/sneakers/{sneaker_id}", response_model=Sneaker)
async def delete_sneaker(sneaker_id: int):
    """
    Delete a specific sneaker by its ID.

    Args:
        sneaker_id (int): The ID of the sneaker to delete.

    Returns:
        dict: A message indicating that the sneaker has been deleted.

    Raises:
        HTTPException: If the sneaker with the given ID is not found.
    """
    global sneakers  # pylint: disable=global-statement
    sneakers = [s for s in sneakers if s.id != sneaker_id]
    return {"message": "Sneaker deleted"}
