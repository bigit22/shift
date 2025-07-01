import uvicorn
from fastapi import FastAPI

from shifttask.api.endpoints import auth_router, salary_router

app = FastAPI()
app.include_router(salary_router)
app.include_router(auth_router)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
