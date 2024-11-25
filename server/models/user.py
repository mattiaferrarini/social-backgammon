from pydantic import BaseModel, Field, EmailStr
from services.database import default_id
from services.rating import DEFAULT_RATING

class UserInDB(BaseModel):
    id: str = Field(default_factory=default_id, alias="_id")
    username: str
    email: EmailStr
    password: str
    rating: int = DEFAULT_RATING

class UserInLeaderboard(UserInDB):
    position: int = 0

class UserOnline(BaseModel):
    id: str = Field(default_factory=default_id, alias="_id")
    username: str
    online: bool = False

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str