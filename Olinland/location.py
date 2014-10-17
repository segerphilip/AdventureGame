from wobject import *

class Location (WObject):

    def __init__ (self,name):
        WObject.__init__(self,name)
        self._contents = []

    def contents (self):
        return self._contents

    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]