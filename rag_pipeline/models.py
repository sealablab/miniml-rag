from pydantic import BaseModel
from typing import List

class Chunk(BaseModel):
    content: str
    id: str
