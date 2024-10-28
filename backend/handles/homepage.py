from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from frontend.templates.templates import templates


router = APIRouter()

@router.get('/homepage', response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse('homepage.html', {'request': request})


@router.get('/homepage/create_lobby', response_class=HTMLResponse)
def homepage_create_lobby(request: Request):
    print("clicked")
    return "459hvdf5n9"
