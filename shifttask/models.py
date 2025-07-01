from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class SalaryInfo(BaseModel):
    salary: int
    next_raise_date: str
