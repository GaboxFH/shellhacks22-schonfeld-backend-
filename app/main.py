from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
# import schemas, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://shellhacks22-frontend.herokuapp.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/api/securities", response_model=List[schemas.Security])
def read_securities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    securities = crud.get_securities(db, skip=skip, limit=limit)
    return securities


# @app.get("/api/securities/{security_id}", response_model=schemas.Security)
# def read_security(security_id: str, db: Session = Depends(get_db)):
#     db_security = crud.get_security(db, security_id=security_id)
#     if db_security is None:
#         raise HTTPException(status_code=404, detail="Security not found")
#     return db_security


@app.get("/api/securities/{security_id}", response_model=List[schemas.Security])
def read_security(security_id: str, db: Session = Depends(get_db), limit: int = 100):
    securities = crud.get_security(db, security_id=security_id, limit=limit)
    if securities is None:
        raise HTTPException(status_code=404, detail="Security not found")
    return securities


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items



# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}