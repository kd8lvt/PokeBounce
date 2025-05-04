import requests
import src.config as config

def post(endpoint,value):
    if config.API["enabled"] == True:
        endpoint = config.API["url"] + endpoint
        return requests.post(endpoint, json=value)
    return None

def set_winner(winner):
    post("/setwinner", {"winner" : winner})

def draw():
    set_winner("Nobody")

def set_fighters(fighterList):
    post("/setfighters", {"fighters" : fighterList})

def set_gameid(gameId):
    post("/setgameid", {"id" : gameId})

def set_gambling(gambling):
    post("/setgambling", {"openGambling" : gambling})