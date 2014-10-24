from npc import *

class BadNinja (NPC):

	def __init__ (self,name,loc,restlessness,chance,desc):
		NPC.__init__(self,name,loc,restlessness,10,desc)
		Player.clock.register(self.burn, 2)
		self.chance = chance

	def burn (self,time):
		if not self.is_in_limbo():
			homework = []
			stuff_around = self.stuff_around()
			if stuff_around:
				for stuff in stuff_around:
					if stuff.is_homework():
						if stuff.done:
							homework.append(stuff)
			if homework:
				if random.randrange(self.chance) == 0:
					target = random.choice(homework)
					target.take(self)
					target.say('I will burn your stupid homework!')
					target.destroy()
