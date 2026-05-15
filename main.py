from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, func
from database import engine, create_db_and_tables
from models import Video, Category, Comment, User
import random
from routers import videos, users, comments

app.include_router(videos.router)
app.include_router(users.router)
app.include_router(comments.router)
app = FastAPI(title="Streaming Platform API")

# Middleware CORS (Requerimiento 3)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- ENDPOINTS VIDEOS ---
@app.get("/videos")
def get_videos(session: Session = Depends(engine)):
    return session.exec(select(Video)).all()

@app.get("/videos/{video_id}")
def get_video(video_id: int, session: Session = Depends(engine)):
    video = session.get(Video, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado")
    return video

@app.get("/videos/recommendations/{category_id}")
def get_recommendations(category_id: int, session: Session = Depends(engine)):
    # 10 recomendaciones aleatorias (Requerimiento 5)
    statement = select(Video).where(Video.category_id == category_id).limit(20)
    results = session.exec(statement).all()
    return random.sample(results, min(len(results), 10))

# --- ENDPOINTS COMENTARIOS ---
@app.post("/comments")
def create_comment(comment: Comment, session: Session = Depends(engine)):
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment