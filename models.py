from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True)
    password_hash: str
    profile_pic_url: Optional[str] = None
    videos: List["Video"] = Relationship(back_populates="owner")
    comments: List["Comment"] = Relationship(back_populates="user")

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    videos: List["Video"] = Relationship(back_populates="category")

class Video(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    video_url: str  # URL de S3
    thumbnail_url: str  # URL de S3
    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")
    
    owner: User = Relationship(back_populates="videos")
    category: Category = Relationship(back_populates="videos")
    comments: List["Comment"] = Relationship(back_populates="video")

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    video_id: int = Field(foreign_key="video.id")
    user_id: int = Field(foreign_key="user.id")
    
    video: Video = Relationship(back_populates="comments")
    user: User = Relationship(back_populates="comments")