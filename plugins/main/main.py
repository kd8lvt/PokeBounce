from src.plugin_api.registry.identifier import Identifier
from src.plugin_api.plugin.plugin import Plugin as _Plugin
import plugins.main.moves as moves

class Plugin(_Plugin):
    id = Identifier("kd8lvt","vanilla")
    namespace = "main"

    def pre(self):
        print("Vanilla plugin preload!")

    def registry(self):
        print("Vanilla plugin registry!")
        print("Moves...")
        moves.registerAll(self.helper.get_registry(Identifier.from_string("vanilla:moves")))