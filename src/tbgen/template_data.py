'''
Created on May 17, 2022

@author: mballance
'''

class TemplateData(object):

    def __init__(self, name, path, short_desc):
        self._name = name
        self._path = path
        self._short_desc = short_desc
        
    @property
    def name(self):
        return self._name
    
    @property
    def path(self):
        return self._path
    
    @property
    def short_desc(self):
        return self._short_desc