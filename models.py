from pydantic import BaseModel
from typing import List

class PasswordRequest(BaseModel):
    password: str

class PasswordResponse(BaseModel):
    password: str
    score: int          # 0 (very weak) to 5 (very strong)
    strength: str       # "Very Weak", "Weak", "Fair", "Strong", "Very Strong"
    feedback: List[str] # tips to improve
    is_strong: bool

class GenerateResponse(BaseModel):
    password: str
    length: int
    strength: str
    score: int