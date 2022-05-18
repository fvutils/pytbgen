'''
Created on May 17, 2022

@author: mballance
'''
import pkgutil
import importlib

class TemplateRgy(object):
    
    _inst = None
    
    def __init__(self):
        self._template_m = {}
    
    def _discoverTemplates(self):
        for finder, name, ispkg in pkgutil.iter_modules():
            if name.startswith("tbgen_templates_"):
                print("Loading templates %s" % name)
                importlib.import_module(name)
        
    def addTemplate(self, data):
        self._template_m[data.name] = data

    @property        
    def templates(self):
        ret = list(self._template_m.values())
        ret.sort(key=lambda item: item.name)
        return ret
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = cls()
            cls._inst._discoverTemplates()
        return cls._inst
    