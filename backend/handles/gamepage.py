from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from templates.templates import templates


router = APIRouter()

@router.get('/gamepage', response_class=HTMLResponse)
def settings_handle(request: Request):
    return templates.TemplateResponse('gamepage.html', {'request': request})

