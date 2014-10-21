from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def take (self,actor):
    	self.move(actor)
    	actor.say('I pick up ' +self.name())

    def drop (self,actor):
    	self.move(actor._location)
    	actor.say('I drop ' +self.name())

    def give (self,actor,target):
    	self.move(target)
        actor.say('I give ' + self.name() + ' to ' + target.name())
        target.accept(self,actor)
        print self._location.name()

    def is_mobile_thing (self):
        return True
