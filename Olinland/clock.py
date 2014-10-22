
class Clock (object):

    def __init__ (self,time):
        self.funcs = []
        self.time = time

    def register (self,func,priority):
        self.funcs.append([priority,func])
        sorted(self.funcs)

    def unregister (self,func,priority):
        self.funcs.remove([priority,func])

    def tick (self):
        for func in self.funcs:
            func[1](self.time)
        self.time += 1
        return self.time
