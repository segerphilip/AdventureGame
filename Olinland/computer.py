from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use (self, actor):
    	doinghw = True
    	for obj in actor.inventory():
    		if obj.is_homework():
    			actor.say('I have completed ' + obj.name())
    			obj.do_homework()
    			doinghw = False
    	if doinghw:
    		actor.say('I have no homework to do!!!')