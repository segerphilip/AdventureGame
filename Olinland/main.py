
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *


REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():
    radarInfo=[]

    mh353 = Room('Riccardo Office', 'The place where Riccardo lives')
    mh3rd = Room('Milas Hall Third Floor', 'Third floor of Milas hall')
    mh2nd = Room('Milas Hall Second Floor', 'Second floor of Milas hall')
    mh1st = Room('Milas Hall First Floor', 'First floor of Milas hall')
    oval = Room('Oval', 'It\'s not a circle')
    ac1st = Room('Academic Center First Floor', 'A place for learning')
    ac113 = Room('Academic Center 113', 'Where we learn to learn programming')
    cc1st = Room('Campus Center First Floor', 'FOOOOOD')
    easth = Room('East Hall', 'Watch out for gross upperclassmen')
    babson = Room('Babson College', 'Even worse than East hall')
    wh1st = Room('West Hall 1', 'The abandoned lounge. Watch out, a wild Chelsea patrols these lands.')
    wh2nd = Room('West Hall 2', 'Chill homework lounge')
    wh3rd = Room('West Hall 3', 'Sophomore homework lounge and Korra')
    wh4th = Room('West Hall 4', 'Drank.')
    whktchn = Room('West Hall Kitchen', 'Don\'t pull a Greg')
    wh101 = Room('Chelsea\'s Room', 'The land of candy and condoms')
    wh411 = Room('Philip\'s Room', 'The land of chill and loft')

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  wh1st)
    biconnect(wh2nd, 'down', wh1st)
    biconnect(wh3rd, 'down', wh2nd)
    biconnect(wh4th, 'down', wh3rd)
    biconnect(wh1st, 'west', wh101)
    biconnect(wh4th, 'east', wh411)
    biconnect(wh1st, 'north', whktchn)
    biconnect(wh1st, 'east',  easth)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    # The player is the first 'thing' that has to be created

    radarInfo.append(Player('Blubbering-Fool', oval, ''))

    
    radarInfo.append(Thing('blackboard', ac113, 'You wrong on it.'))
    radarInfo.append(Thing('lovely-trees', oval, 'They are very lovely.'))
    radarInfo.append(Thing('leather couch', wh101, 'Plop right down and have a chat.'))
    radarInfo.append(Thing('foosball table', wh1st, 'Such foos, much ball.'))
    radarInfo.append(MobileThing('cs-book', oval, 'Sounds like you\'re a NERD!!!!'))
    radarInfo.append(MobileThing('math-book', oval, 'Sounds like you\'re a NERD!!!!'))
    radarInfo.append(MobileThing('kettle', whktchn, 'Keep this away from Greg.'))
    radarInfo.append(MobileThing('Canada flag', wh411, 'No other flags are needed.'))
    radarInfo.append(MobileThing('nerf gun', wh1st, 'Point away from eyes.'))

    radarInfo.append(Computer('hal-9000', ac113, 'Super smart.'))
    radarInfo.append(Computer('johnny-5', easth, 'Super smart.'))

    radarInfo.append(Professor('Riccardo',mh353,random.randint(1,5),2,''))
    
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        radarInfo.append(Homework(homework,
                 random.choice(Room.rooms),
                 'Ew, homework!'))

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        radarInfo.append(NPC(student,
            random.choice(Room.rooms),
            random.randint(1,5),
            random.randint(1,5),'These are friends, not food.'))

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      radarInfo.append(Troll(troll,
            random.choice(Room.rooms),
            random.randint(1,3),
            random.randint(1,3),'These are trolls, and food!'))

    Radar('handy radar',mh353, 'Oh hey look, a radar!',radarInfo) 


VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
