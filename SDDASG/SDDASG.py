from itertools import filterfalse
from pickle import FALSE
import random
import ctypes

# Game variables
game_vars = {
    'turn': 1, 
    'Coins': 20,      
    }

R = {'shortform' : 'R',
        'name': 'Residential'
        }

I = {'shortform': 'I',
        'name': 'Industry'
        }

C = {'shortform': 'C',
        'name': 'Commercial'
          }

O = {'shortform': 'O',
        'name': 'Park'
          }

Road = {'shortform': '*',
        'name': 'Road'
          }

#------
#Diplay main manu
#------
def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Display Highest Score")
    print("4. Exit Game")

#------
#Display Layout
#------

field = [ [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None]]

def draw_field():
    num_r=len(field)
    num_c=len(field[0])
   

    #print top line
    print(' ',end='')
    for i in range(len(field[0])):
        print('+-----',end='')
    print('+')

    for r in range(num_r):

        print(' ', end='')
        for c in field[r]:    
            print('|{:5}'.format(' ' if c is None else c['shortform']),end='')
        print('|')
        print(' ',end='')

        for c in field[r]:
            print('|{:2}{:1}{:2}'.format(' ', ' ', ' ' ),end='')
        print('|')
        print(' ',end='')

        for c in range(num_c):
            print('+-----',end='')
        print('+')  
    return

#-----------
#Initializes all the game variables for a new game
#-----------
def initialize_game():
    game_vars['turn'] = 0
    game_vars['Coins'] = 16
    
#thre = '-' * game_vars['turn']

#---------
#Purchase building
#---------
def buy_unit(field, game_vars):
    print('What building do you wish to purchase?')
    choice = {'1':R['name'],'2':I['name'], '2':I['name'], '3':C['name'], '4':O['name'], '5':Road['name'], '6':"Don't buy"}
    print('1. {}({} gold)\n2. {}({} gold\n3. {}{} gold\n4. {}{} gold\n5. {}{} gold)\n6. {}'.format(choice['1'],R['price'],choice['2'],I['price'], choice['3'],C['price'], choice['4'],O['price'], choice['5'],Road['price'], choice['6']))
    row=ord(position[0])-ord('A')
    column=int(position[1])-1
    field[row][column]=unit.copy()
    return

#---------
#Purchase building menu
#---------
def show_combat_menu(game_vars):
    print('Turn {}'.format(game_vars['turn']))
    print('Gold= {}'.format(game_vars['Coins']))
    print("1. Buy unit     2. End turn")
    print("3. Save game    4. Quit")

#----------
#Place building
#----------
def placing(field, building):
    spawn_ch=True
    while spawn_ch==True:
        row=random.randint(0,len(field)-1)
        position=chr(ord('A')+row)+'7'
        place_unit(field, position, building.copy())
        game_vars['Coins']+=1
        break

    return

def place_unit(field, position, unit_name):
    row=ord(position[0])-ord('A')
    column=int(position[1])-1
    field[row][column]=unit_name.copy()
    return True

#---------
#Alert Box
#---------

class MbConstants:
    MB_OKCANCEL = 1
    IDCANCEL = 2
    IDOK = 1

def mbox(message, title):
    return ctypes.windll.user32.MessageBoxW(0,message, title, MbConstants.MB_OKCANCEL)

#-----------
#Main Menu
#-----------

show_main_menu()
play_game=False
menu_input=int(input("Your choice?? "))
menu_ch=True

while menu_ch==True:
    if menu_input==1:
        menu_ch=False
        initialize_game()
        game_vars['turn']=1
        play_game=True
        placing(field, R)
        placing(field, C)

    elif menu_input==2:
        menu_ch=False
        play_game=True

    elif menu_input==3:
        menu_ch=False
        play_game=False
        print()
    elif menu_input==4:
        print('BYE BYE!!!!!!!!!!!')
        break
    else:
        print('Youe have entered an invalid number.')
        break

while play_game==True:
    draw_field()
    show_combat_menu(game_vars)
    menu_input=int(input("Your choice?? "))
    if menu_input==1:
        #building menu
        building_ch=True
        while building_ch==True:
            unit_num=int(input('Which building would you like to construct?\n'\
                                '1.Residential\n'\
                                '2.Industry\n'\
                                '3.Commercial\n'\
                                '4.Park\n'\
                                '5.Road\n'\
                                '6.Don\'t buy\n'\
                                'Your choice?? '))
            if unit_num!=6:
                break
                if unit_num==1:
                            break
                        #else:
                            #print('Not enough Coins.')
                elif unit_num==2:
                            break
                        #else:
                            #print('Not enough Coins.')
                elif unit_num==3:
                            break
                        #else:
                            #print('Not enough Coins.')
                elif unit_num==4:
                            break
                        #else:
                            #print('Not enough Coins.')
                elif unit_num==5:
                            break
                        #else:
                            #print('Not enough Coins.')

            else:
                print('Invalid choice.\nPlease reselect.')
                shop_ch=False

    #Turn End
    elif menu_input==2:
        print('Turn ended.')
        game_vars['turn']+=1
        break

    #Save Game
    elif menu_input==3:
        #ctypes.windll.user32.MessageBoxW(0,"Do You Want to Save your Game?", "", 3)
        rc = mbox("Do You Want to Save your Game?","title")
        if  rc == MbConstants.IDOK:
            print("Game Saved!")
            print('BYE BYE!!!!!!!!!!!!!!!!!!!!')
            break
        elif rc == MbConstants.IDCANCEL:
            continue

    #End
    else:
        #ctypes.windll.user32.MessageBoxW(0, "Do You Want to Save your Game?", "", 4)
        rc = mbox("Do You Want to Save your Game?","title")
        if  rc == MbConstants.IDOK:
            print("Game Saved!")
        print('BYE BYE!!!!!!!!!!!!!!!!!!!!')
        break