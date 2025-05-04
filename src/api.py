import requests
from src.config import CONFIG_FILE

def post(args: list[any]):
    if CONFIG_FILE.API.enabled == True:
        newargs = args.copy()
        newargs[0] = CONFIG_FILE.API.url + newargs[0]
        return requests.post(*args)
    return None

def set_winner(winner):
    post("/setwinner", json = {"winner" : winner})

def draw():
    set_winner("Nobody")

def set_fighters(fighterList):
    post("/setfighters", json = {"fighters" : fighterList})

def set_gameid(gameId):
    post("/setgameid", json = {"id" : gameId})

def set_gambling(gambling):
    post("/setgambling", json = {"openGambling" : gambling})