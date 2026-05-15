from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Video

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.get("/")
def list_videos(session: Session = Depends(get_session)):
    return session.exec(select(Video)).all()

@router.get("/search")
def search_videos(title: str, session: Session = Depends(get_session)):
    statement = select(Video).where(Video.title.contains(title))
    return session.exec(statement).all()

@router.get("/category/{cat_id}")
def filter_by_category(cat_id: int, session: Session = Depends(get_session)):
    statement = select(Video).where(Video.category_id == cat_id)
    return session.exec(statement).all()

@router.post("/")
def upload_video(video_data: Video, session: Session = Depends(get_session)):
    session.add(video_data)
    session.commit()
    session.refresh(video_data)
    return video_data