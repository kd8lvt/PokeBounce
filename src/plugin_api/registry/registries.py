from src.plugin_api.registry.identifier import Identifier
from src.plugin_api.registry.registry import Registry

registries = Registry("registries")
registries.register(Identifier.from_string("vanilla:plugins"),Registry("plugins"))
registries.register(Identifier.from_string("vanilla:moves"),Registry("moves"))
registries.register(Identifier.from_string("vanilla:battlers"),Registry("battlers"))