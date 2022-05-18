from pydantic import BaseModel
from typing import Optional
from src.utils import fake_mail


class ContactBodyModel(BaseModel):
    email: str = fake_mail()
    first_name: str = "test"
    last_name: Optional[str]
    phone: Optional[str]
    country: Optional[str]
    city: Optional[str]
    address: Optional[str]
