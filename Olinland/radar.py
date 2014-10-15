from mobile import *
from room import *
from thing import *

class Radar (MobileThing):

    def __init__ (self,name,loc,desc,info):
        MobileThing.__init__(self,name,loc,desc)
        self.info=info

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        for thing in self.info:
        	actor.say('I detect ' + thing.name() + ' in ' + thing._location.name())
