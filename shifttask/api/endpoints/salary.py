from fastapi import Depends, APIRouter

from shifttask.models import SalaryInfo
from shifttask.utils import get_current_user

router = APIRouter()


@router.get("/salary", response_model=SalaryInfo)
async def get_salary(cur_user: dict = Depends(get_current_user)):
    return {
        "salary": cur_user["salary"],
        "next_raise_date": cur_user["next_raise_date"]
    }
