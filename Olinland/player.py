from person import *
from clock import *

import sys
import random

class Player (Person):

    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False
    # static field representing the clock
    clock = Clock(0)
    follower = None

    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)
        Player.me = self

    # Grab any kind of thing from player's location, 
    # given its name.  The thing may be in the possession of
    # the place, or in the possession of a person at the place.
   
    def thing_named (self,name):
        for x in self.location().contents():
            if x.name() == name:
                return x
        for x in self.peek_around():
            if x.name() == name:
                return x
        for x in self.inventory():
            if x.name() == name:
                return x
        return None

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()
        inventory = self.inventory()

        print '------------------------------------------------------------'
        print 'You are in', loc.name()
        print loc.desc

        if all_stuff:
            print 'You see:', names(all_stuff)
        else: 
            print 'The room is empty'

        if inventory:
            print 'You have:', names(inventory)
        else:
            print 'You aren\'t carrying anything'

        if people:
            print 'You see:', names(people)
        else:
            print 'You see no one around'

        if exits:
            print 'Exits:', ', '.join([x for x in exits])
        else:
            print 'There are no exits'

    def sing (self):
        self.say('\nMy Anaconda don\'t...\nMy Anaconda don\'t... \nMy Anaconda don\'t want none unless you got buns hun')
        people = self.people_around()
        if people:
            for victim in people:
                if victim == self.follower:
                    victim.say('Your voice is BEAUTIFUL!!!')
                else:
                    victim.say('Your voice, it\'s TERRIBLE!!!')
                    victim.suffer(1)                

    def twerk (self):
        if self.follower == None:
            people = self.people_around()
            if people:
                friend = random.choice(people)
                friend.say('Those Bunnnns, Hun! I\'m yours forever')
                friend.follower()
        else:
            self.follower.say('How dare you to try to replace me.')

    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            if self.follower != None:
                t = exits[direction]
                self.follower.leave_room()
                t.report(self.follower.name()+' follows '+ self.name()+' to '+t.name())
                self.follower.move(t)
                self.follower.enter_room()
            return True
        else:
            print 'No exit in direction', direction
            return False

    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print 'This game for you is now over...'
        sys.exit(0)
