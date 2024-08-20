from typing import Optional
from pydantic import BaseModel

class GetDeckByIdRequest(BaseModel):
    deck_id: int

class GetDeckWithCardsRequest(BaseModel):
    deck_id: Optional[int] = None

class CreateDeckRequest(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[int] = None

class RepositionDeckRequest(BaseModel):
    deck_id: int
    preceding_deck_id: int

class UpdateDeckRequest(BaseModel):
    deck_id: int
    name: Optional[str] = None
    parent_id: Optional[int] = None