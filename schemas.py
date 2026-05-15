from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Esquemas de Usuario
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    profile_pic_url: Optional[str]

# Esquemas de Video
class VideoCreate(BaseModel):
    title: str
    description: str
    video_url: str
    thumbnail_url: str
    category_id: int

# Esquemas de Comentario
class CommentCreate(BaseModel):
    content: str
    video_id: int