from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self.done = False

    def is_homework (self):
        return True

    def do_homework (self):
    	self.done = True
    	self._name = 'DONE-' + self._name

    # FIX ME
