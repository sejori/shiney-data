from pydantic import BaseModel

class GetDeckWithCardsRequest(BaseModel):
    deck_id: int