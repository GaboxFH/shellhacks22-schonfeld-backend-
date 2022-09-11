from typing import List
from difflib import SequenceMatcher
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
# import schemas, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://shellhacks22-frontend.herokuapp.com/*",
    
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
    return {"Hello": "Schonfeld"}

def weight_results(securities, query):
    query = query.upper()

    for record in securities:
        weight_security_id = SequenceMatcher(None, str(record.security_id or ''), query).ratio()
        weight_cusip = SequenceMatcher(None, str(record.cusip or ''), query).ratio()
        weight_sedol = SequenceMatcher(None, str(record.sedol or ''), query).ratio()
        weight_isin = SequenceMatcher(None, str(record.isin or ''), query).ratio()
        weight_ric = SequenceMatcher(None, str(record.ric or ''), query).ratio()
        weight_bloomberg = SequenceMatcher(None, str(record.bloomberg or ''), query).ratio()
        weight_bbg = SequenceMatcher(None, str(record.bbg or ''), query).ratio()
        weight_symbol = SequenceMatcher(None, str(record.symbol or ''), query).ratio()
        weight_root_symbol = SequenceMatcher(None, str(record.root_symbol or ''), query).ratio()
        weight_bb_yellow = SequenceMatcher(None, str(record.bb_yellow or ''), query).ratio()
        weight_spn = SequenceMatcher(None, str(record.spn or ''), query).ratio()

        weight_total = weight_security_id + weight_cusip + weight_sedol + weight_isin + weight_ric + weight_bloomberg + weight_bbg + weight_symbol + weight_root_symbol + weight_bb_yellow + weight_spn
        record.weight = weight_total
    return securities

@app.get("/api/securities", response_model=List[schemas.Security])
def read_securities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    securities = crud.get_securities(db, skip=skip, limit=limit)
    return securities


@app.get("/api/securities/{root_symbol}", response_model=List[schemas.Security])
def read_security(root_symbol: str, db: Session = Depends(get_db), limit: int = 500):
    securities = crud.get_security(db, root_symbol=root_symbol, limit=limit)
    print (len(securities))
    if securities is None:
        raise HTTPException(status_code=404, detail="Security not found")
    securities = weight_results(securities, root_symbol)
    securities.sort(key=lambda x: x.weight, reverse = True)
    return securities