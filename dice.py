import random

  
#print face
base   = '+-------+         +-------+'
sep    = '         '
blank  = '|       |'
left   = '| *     |'
middle = '|   *   |'
right  = '|     * |'
both   = '| *   * |'

dice = [(blank, middle, blank),
        (left,  blank,  right),
        (left,  middle, right),
        (both,  blank,  both ),
        (both,  middle, both ),
        (both,  both,   both )]

def print_dice(a, b):
    print(base)
    print('\n'.join(a + sep + b for a, b in zip(dice[a-1], dice[b-1])))
    print(base)
    
    
#roll dice
def roll():
  roll = input("Type y to roll the die: ")
  while roll=="y":
    print_dice(random.randint(1,6),random.randint(1,6))
    roll = input("Type y to roll the die: ")
  else:
    print("Thank you for playing!")  
    
roll()  

  


