from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def get_securities(db: Session, skip: int = 0, limit: int = 100 ):
    return db.query(models.Security).offset(skip).limit(limit).all()

def get_security(db: Session, security_id : str, limit: int = 100):
    # return db.query(models.Security).filter(models.Security.security_id == security_id).first()
    return db.query(models.Security).filter(models.Security.security_id.ilike('%{}%'.format(security_id))).limit(limit).all()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
