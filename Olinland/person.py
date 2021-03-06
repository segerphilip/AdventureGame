from mobile import *

class Person (MobileThing):    # Container...

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._max_health = 3
        self._health = self._max_health

    def health (self):
        return self._health

    def reset_health (self):
        self._health = self._maxHealth

    def say (self,msg):
        loc = self.location()
        loc.report(self.name()+' says -- '+msg)

    def have_fit (self):
        self.say('Yaaaaah! I am upset!')

    def people_around (self):
        return [x for x in self.location().contents()
                    if x.is_person() and x is not self]

    def stuff_around (self):
        stuff = []
        peek_around = self.peek_around()
        if peek_around:
            for peek in peek_around:
                stuff.append(peek)
        for x in self.location().contents():
            if not x.is_person():
                stuff.append(x)
        return [x for x in stuff]

    def inventory (self):
        return [x for x in self._contents]

    def peek_around (self):
        objects = []
        npcs = self.people_around()
        for npc in npcs:
            inventory = npc.inventory()
            for obj in inventory:
                objects.append(obj)
        return [x for x in objects]

    def lose (self,t,loseto):
        self.say('I lose ' + t.name())
        self.have_fit()
        t.move(loseto)
    
    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            return True
        else:
            print 'No exit in direction', direction
            return False


    def suffer (self,hits):
        self.say('Ouch! '+str(hits)+' hits is more than I want!')
        self._health -= hits
        if (self.health() < 0):
            self.die()
        else:
            self.say('My health is now '+str(self.health()))

    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')
        inventory = self.inventory()
        for pos in inventory:
                pos.move(self._location)
        self.say('I drop everything and die!')
        self.destroy()

    def enter_room (self):
        people = self.people_around()
        if people:
            self.say('Hi ' + ', '.join([x.name() for x in people]))

    def leave_room (self):
        pass   # do nothing to reduce verbiage

    def take (self,actor):
        actor.say('I am not strong enough to just take '+self.name())

    def drop (self,actor):
        print actor.name(),'is not carrying',self.name()

    def give (self,actor,target):
        print actor.name(),'is not carrying',self.name()
        
    def accept (self,obj,source):
        self.say('Thanks, ' + source.name())

    def is_person (self):
        return True
