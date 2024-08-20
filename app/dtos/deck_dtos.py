from typing import Optional
from pydantic import BaseModel

class GetDeckWithCardsRequest(BaseModel):
    deck_id: Optional[int] = None