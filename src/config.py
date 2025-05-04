class _Config:
    _cache = {}

    def __init__(self):
        try:
            with open('config.toml','r') as config_file:
                from toml import load
                self.toml = load(config_file)
        except:
            raise Exception("An error occurred when attempting to load the config.toml!")


    @staticmethod
    def to_keystr(config_path: list[str]):
        return str.join(".",config_path)
    
    def get(self,config_path:str):
        return self._get(config_path.split("."))
    
    def _get(self,config_path: list[str]):
        if _Config.to_keystr(config_path) not in self._cache.keys(): 
            current_step = self.toml
            for next_step in config_path:
                if next_step in current_step.keys():
                    current_step = current_step[next_step]
                else:
                    raise ValueError(next_step)
                
            self._cache.setdefault(_Config.to_keystr(config_path),current_step)

        return self._cache.get(_Config.to_keystr(config_path))

CONFIG_FILE = _Config()

#Window
WINDOW = {
    "size": tuple(CONFIG_FILE.get("window.size")),
    "fps": CONFIG_FILE.get("window.fps"),
    "bg_color": tuple(CONFIG_FILE.get("window.background_color"))
}

#API (for interfacing with a bot)
API = {
    "enabled": CONFIG_FILE.get("api.make_api_calls"),
    "url": CONFIG_FILE.get("api.base_url")
}

#Gameplay
TIMERS = {
    "startCountdown": CONFIG_FILE.get("timers.gamble_timer")*WINDOW["fps"],
    "gameOverCountdown": CONFIG_FILE.get("timers.game_over_timer")*WINDOW["fps"]
}

#Sprite lists
# Todo: make this part of the upcoming registry system
SPRITES = {
    "battlers": [
        "pikachu","staraptor","infernape","umbreon","mamoswine","nidoking","scizor","wigglytuff",
        "decidueye","kingdra","smeargle","marowak","quagsire","porygonz","tyranitar","metagross",
    ],
    "moves": {
        "bone","bravebird","bubble","dark","dazzling","earthquake","fire1","fire2",
        "fire3","fire4","fire5","fire6","fire7","fire8", "fist", "ironhead", "irontail", "leaf",
        "poison", "sandstorm", "shadowball", "stone", "waterfall", "zenheadbutt"
    }
}

# Debug
DEBUG = {
    "overrideBattlers": CONFIG_FILE.get("debug.override_battlers"),
    "battlerOverride": CONFIG_FILE.get("debug.battler_override"),
    "showHitboxes": CONFIG_FILE.get("debug.show_hitboxes"),
    "showCollisionBoxes": CONFIG_FILE.get("debug.show_collision_boxes"),
}