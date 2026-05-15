from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Comment

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.get("/video/{video_id}")
def get_video_comments(video_id: int, session: Session = Depends(get_session)):
    statement = select(Comment).where(Comment.video_id == video_id)
    return session.exec(statement).all()

@router.post("/")
def post_comment(comment: Comment, session: Session = Depends(get_session)):
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, session: Session = Depends(get_session)):
    comment = session.get(Comment, comment_id)
    if comment:
        session.delete(comment)
        session.commit()
    return {"status": "deleted"}