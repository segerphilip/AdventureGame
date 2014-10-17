from wobject import *
from player import *
from location import *


class Room (Location): #,Container):

    rooms = []

    def __init__ (self,name,desc):
        Location.__init__(self,name)
        self.desc = desc 
        self._exits = {}
        Room.rooms.append(self)

    def exits (self):
        return self._exits

    def report (self,msg):
        if Player.me.location() is self:
            print msg
        elif Player.god_mode:
            print '(At', self.name(), msg+')'

    def broadcast (self,msg):
        print msg

    def is_room (self):
        return True
