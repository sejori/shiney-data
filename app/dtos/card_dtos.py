from typing import Optional
from pydantic import BaseModel

class GetCardByIdRequest(BaseModel):
    card_id: int

class CreateCardRequest(BaseModel):
    content: Optional[str] = None
    deck_id: Optional[int] = None

class RepositionCardRequest(BaseModel):
    card_id: int
    preceding_card_id: int

class UpdateCardRequest(BaseModel):
    card_id: int
    content: Optional[str] = None
    deck_id: Optional[int] = None