from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from frontend.templates.templates import templates
from backend.lobbies import lobbies, Lobby
import uuid


router = APIRouter()

@router.get('/homepage', response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse('homepage.html', {'request': request})


@router.get('/homepage/create_lobby', response_class=HTMLResponse)
def homepage_create_lobby(player_name: str):
    lobby_code = str(uuid.uuid4())[:8] 
    lobbies[lobby_code] = Lobby(code=lobby_code, players=[player_name], turn=0, rolls=[None, None])
    print(lobbies)
    return lobby_code


@router.get('/homepage/join_lobby', response_class=HTMLResponse)
def homepage_join_lobby(code, player_name):

    if code in lobbies:
        lobby =  lobbies[code]
        lobby.players.append(player_name)
        lobby.rolls[player_name] = None

        return JSONResponse(
            content={
                'is_valid_code': True
            }
        )

    return JSONResponse(content={
        'is_valid_code': False
    })