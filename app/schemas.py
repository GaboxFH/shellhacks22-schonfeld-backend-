from typing import List, Union, Optional

from pydantic import BaseModel

from app.models import Security

class SecurityBase(BaseModel):
    security_id: Optional[str]
    cusip: Union[str, None] = None
    sedol: Union[str, None] = None
    isin: Union[str, None] = None
    ric: Union[str, None] = None
    bloomberg: Union[str, None] = None
    bbg: Union[str, None] = None
    symbol: Union[str, None] = None
    root_symbol: Union[str, None] = None
    bb_yellow: Union[str, None] = None
    spn: Union[str, None] = None
    weight: Union[float, None] = None

class SecurityCreate(SecurityBase):
    pass

class Security(SecurityBase):
    security_id: str
    # owner_id: int

    class Config:
        orm_mode = True