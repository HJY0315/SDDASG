import random

#------
#Diplay main manu
#------
def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Display Highest Score")
    print("3. Exit Game")

#------
#Display Layout
#------
def draw_field():
    num_r=len(field)
    num_c=len(field[0])
    print(' '*3,'1',' '*3,'2',' '*3,'3')

    #print top line
    print(' ',end='')
    for i in range(len(field[0])):
        print('+-----',end='')
    print('+')

    for r in range(num_r):

        print(chr(ord('A')+r),end='')
        for c in field[r]:    
            print('|{:5}'.format(' ' if c is None else c['shortform']),end='')
        print('|')
        print(' ',end='')

        for c in field[r]:
            print('|{:2}{:1}{:2}'.format(' ' if c is None else c['maxHP'] ,' ' if c is None else '/',' ' if c is None else c['maxHP']),end='')
        print('|')
        print(' ',end='')

        for c in range(num_c):
            print('+-----',end='')
        print('+')  
    return

