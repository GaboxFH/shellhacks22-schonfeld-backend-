from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Security(Base):
    __tablename__ = "securities"
    
    security_id = Column(String, unique=True, index=True, primary_key=True)
    cusip = Column(String)
    sedol = Column(String)
    isin = Column(String)
    ric = Column(String)
    bloomberg = Column(String)
    bbg = Column(String)
    symbol = Column(String)
    root_symbol = Column(String)
    bb_yellow = Column(String)
    spn = Column(String)