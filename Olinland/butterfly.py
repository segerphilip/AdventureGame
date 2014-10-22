import random

from npc import *
from mobile import *
from player import *

class Caterpillar (MobileThing):

    def __init__(self,name,loc,st1,st2,desc):
        MobileThing.__init__(self,'Caterpillar-'+name,loc,desc)
        self.st1 = st1
        self.st2 = st1 + st2
        Player.clock.register(self.cocoonify,2)

    def cocoonify (self,time):
        print (self.name(),self.st1)
        if time == self.st1:
            print 'This fuckers a cocoon'
            Player.clock.register(self.butterflyify,2)
            Player.clock.unregister(self.cocoonify,2)
            self._name = 'Cocoon'+self._name[11::]
            self.desc = 'A pretty cocoon. I wonder what\'s inside'

    def butterflyify (self,time):
        print (self.name(),self.st1)
        if time == self.st2:
            Player.clock.unregister(self.butterflyify,2)
            self._name = 'Butterfly'+self._name[6::]
            self.desc = 'A pretty butterfly! So magic. Much pretty!'
            Butterfly(self._name,self._location,random.randint(1,3),0,self.desc)
            self.destroy()

class Butterfly (NPC):

    def __init__(self,name,loc,restlesness,miserly,desc):
        NPC.__init__(self,name,loc,restlesness,miserly,desc)

    def move_and_take_stuff (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._restlessness) == 0:
                self.move_somewhere()