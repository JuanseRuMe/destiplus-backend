from pydantic import BaseModel
from typing import Dict, Optional, List

class UserVerify(BaseModel):
    email: str

class UserResponse(BaseModel):
    exists: bool
    type: str
    message: str

class UserRegister(BaseModel):
    email: str
    type: str