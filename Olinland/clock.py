
class Clock (object):

    def __init__ (self,time):
        self.funcs = []
        self.time = time

    def register (self,func,priority):
        self.funcs.append([priority,func])

    def tick (self):
        sorted(self.funcs)
        for func in self.funcs:
            func(self.time)
        self.time += 1
