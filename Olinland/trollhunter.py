import random
from npc import *

class TrollHunter (NPC):

	def __init__(self,name,loc,restlessness,strength,trolls,desc):
		NPC.__init__(self,name,loc,restlessness,10,desc)
		Player.clock.register(self.hunt,2)
		self.strength = strength
		self.trolls = trolls

	def hunt (self,time):
		targets=[]
		for troll in self.trolls:
			if Player.me.thing_named(troll.name()):
				targets.append(troll)
		if targets:
			if random.randrange(self.strength) == 0:
				victim = random.choice(targets)
				self.location().report(self.name() + ' viciously stabs ' + victim)
				victim.suffer(random.randint(1,3))
		