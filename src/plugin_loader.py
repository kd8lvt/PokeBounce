import importlib

from src.plugin_api.plugin.pluginhelper import PluginHelper
from src.plugin_api.registry.identifier import Identifier
from src.plugin_api.registry.registries import registries
pReg = registries.get(Identifier("vanilla","plugins"))

#This file is mainly adapted from various answers to https://stackoverflow.com/q/951124

def gather_plugins():
    res = {}
    import os
    lst = os.listdir("plugins")
    dir = []
    for d in lst:
        s = os.path.abspath("plugins")+os.sep+d
        if os.path.isdir(s) and os.path.exists(s+os.sep+"main.py"):
            dir.append(d)
        
    for d in dir:
        plugin = getattr(importlib.import_module("plugins."+d+".main"),"Plugin")
        res[len(res)] = plugin
    
    return res

def load_plugins():
    plugins = gather_plugins()
    print("Loading plugins...")
    for i in plugins:
        PluginHelper(plugins[i])
    
    def pre(plugin): plugin.pre()
    def registry(plugin): plugin.registry()
    
    pReg.foreach(pre)
    pReg.foreach(registry)

def ready():
    def ready(plugin): plugin.ready()
    pReg.foreach(ready)