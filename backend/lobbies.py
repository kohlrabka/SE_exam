from pydantic import BaseModel

class Lobby(BaseModel):
    code: str
    turn: int
    players: list[str]
    rolls: list[None]


lobbies = {}


