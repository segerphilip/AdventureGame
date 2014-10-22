from player import *
from npc import *
import random

class Professor (NPC):

    def __init__ (self,name,loc,restlessness,professorial,desc):
        NPC.__init__(self,name,loc,restlessness,100,desc)
        self._professorial = professorial
        Player.clock.register(self.lecture,3)

    _topics = ['Turing machines',
                'the lambda calculus',
                'Godel']

    def lecture (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._professorial) == 0:
                if self.people_around():
                    self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
                else:
                    self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

    def accept (self,obj,source):
        if obj.is_homework:
            self.say('Thanks for the homework, ' + source.name())
            if source.name() == 'Blubbering-Fool':
                self.say('Man, you did a great job on the homework. What a champ!')
                print 'You win. Game over.'
                sys.exit(0)
        else:
            self.say('Thanks, ' + source.name())