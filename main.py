import uvicorn
from fastapi import Depends, FastAPI, HTTPException
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session



models.Base.metadata.create_all(bind=engine)

app = FastAPI ()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,

)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get ("/")
def main(db: Session = Depends(get_db)):
    records = db.query(models.User).all()
    return records
