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




    # items = relationship("Item", back_populates="owner")


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
