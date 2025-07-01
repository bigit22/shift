from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from shifttask.dependencies import ACCESS_TOKEN_EXPIRE_MINUTES
from shifttask.models import Token
from shifttask.utils import authenticate_user, create_access_token

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> dict:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
