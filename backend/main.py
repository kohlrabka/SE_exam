from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.handles import homepage
from backend.handles import gamepage


app = APIRouter()

app.mount("/static", StaticFiles(directory="./static"), name="static")

app.include_router(homepage.router)
app.include_router(gamepage.router)