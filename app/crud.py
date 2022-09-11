from operator import or_
from sqlalchemy.orm import Session
from sqlalchemy import func, or_

from . import models, schemas

def get_securities(db: Session, skip: int = 0, limit: int = 1000 ):
    return db.query(models.Security).offset(skip).limit(limit).all()


def get_security(db: Session, root_symbol : str,  limit: int = 1000):
    # return db.query(models.Security).filter(models.Security.security_id == security_id).first()
    return db.query(models.Security).filter(
        or_(
        models.Security.security_id.ilike('%{}%'.format(root_symbol)), 
        models.Security.cusip.ilike('%{}%'.format(root_symbol)),
        models.Security.sedol.ilike('%{}%'.format(root_symbol)), 
        models.Security.isin.ilike('%{}%'.format(root_symbol)), 
        models.Security.ric.ilike('%{}%'.format(root_symbol)),
        models.Security.bloomberg.ilike('%{}%'.format(root_symbol)),
        models.Security.bbg.ilike('%{}%'.format(root_symbol)),
        models.Security.symbol.ilike('%{}%'.format(root_symbol)),
        models.Security.root_symbol.ilike('%{}%'.format(root_symbol)),
        models.Security.bb_yellow.ilike('%{}%'.format(root_symbol)),
        models.Security.spn.ilike('%{}%'.format(root_symbol)),
        )
        ).limit(limit).all()