from fastapi import FastAPI
import uvicorn
from app.routers import v1

app = FastAPI()

app.include_router(
    v1.router,
    prefix = "/api"
)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8000)