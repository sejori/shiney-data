from typing import Optional
from pydantic import BaseModel

class CreateCardRequest(BaseModel):
    content: Optional[str] = None
    deck_id: Optional[int] = None
    