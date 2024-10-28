from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from frontend.templates.templates import templates
from backend.lobbies import lobbies
from backend.dice import *


router = APIRouter()

@router.get('/gamepage', response_class=HTMLResponse)
def gamepage(request: Request):
    return templates.TemplateResponse('gamepage.html', {'request': request})




@router.get('/gamepage/roll', response_class=HTMLResponse)
def gamepage_roll(code: str, player_name: str):


    lobby = lobbies[code]

    if lobby.players[lobby.turn] != player_name:
        return 

    if len(lobby.players) != 2:
        return

    if lobby.turn % 2 == 0:
        lobby.rolls[0] = get_dices()
        lobby.turn += 1

        return JSONResponse(
            content={
                "roll1": lobby.rolls[0],
                "roll2": None,
                "winner": None
            }
        )
    else:
        lobby.rolls[1] = get_dices()
        r1 = get_score(dices=lobby.rolls[0])
        r2 = get_score(dices=lobby.rolls[0])
    
        lobby.turn += 1

        return JSONResponse(
            content={
                "roll1": lobby.rolls[0],
                "roll2": lobby.rolls[1],
                "winner": lobby.players[0] if r1 > r2 else "draw" if r1 < r2 else lobby.players[1]
            }
        )



