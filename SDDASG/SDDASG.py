from itertools import filterfalse
from pickle import FALSE
import random
import ctypes

# Game variables
game_vars = {
    'turn': 0, 
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

field = [ [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

def draw_field():
    num_r = len(field)
    num_c = len(field[0])

    # print top line
    print('  ', end='')
    for i in range(1, num_c+1):
        print('{:<5}'.format(i), end='')
    
    print('\n ', end='')
    for i in range(len(field[0])):
        print('+----', end='')
    print('+')

    for r in range(num_r):
        print(chr(ord('A') + r), end='')

        for c in field[r]:
            if c is None:
                print('|    ', end='')  # Print empty space for None
            elif isinstance(c, dict):
                print('|{:4}'.format(c['shortform']), end='')  # Access 'shortform' if c is a dictionary
            else:
                print('|{:4}'.format(c), end='')  # Print directly if it's not a dictionary
        print('|')

        # Print the separator line
        print(' ', end='')
        for c in field[r]:
            print('|{:4}'.format(''), end='')
        print('|')

        # Print the bottom line of each row
        print(' ', end='')
        for c in range(num_c):
            print('+----', end='')
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
    choice = {'1':R['name'],'2':I['name'], '3':C['name'], '4':O['name'], '5':Road['name'], '6':"Don't buy"}
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
#Random Building
#----------
buildings = [R, I, C, O, Road]

def select_random_building():
    build = random.choice(buildings)
    build2 = random.choice(buildings)
    print('Please choose one of the two buildings given:', build['name'], 'or', build2['name'])
    choice = input("Enter your choice: ")
    
    # Ensure the user input matches one of the randomly chosen buildings
    if choice.capitalize() == build['name'] or choice.capitalize() == build2['name']:
        chosen_building = build if choice.capitalize() == build['name'] else build2
        return chosen_building['shortform']
    else:
        print("Invalid choice. Please choose one of the two buildings.")
        return select_random_building()


def get_user_position():
    position = input("Enter position (e.g., A1): ").capitalize()
    return position

def buy_unit(field, position, building):
    row = ord(position[0]) - ord('A')
    column = int(position[1:]) - 1
    field[row][column] = building
    return


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
        play_game=True
        
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

    if menu_input == 1:       
        if (game_vars['turn']<=0):
            chosen_building = select_random_building()
            position = get_user_position()
            print("Building:", chosen_building)
            print("Position:", position)
            buy_unit(field, position, chosen_building)  
            game_vars['turn']+=1

        else:
            while True:
      
                unit_num = int(input('Which building would you like to construct?\n'
                                        '1. Residential\n'
                                        '2. Industry\n'
                                        '3. Commercial\n'
                                        '4. Park\n'
                                        '5. Road\n'
                                        '6. Don\'t buy\n'
                                        'Your choice?? '))

                if unit_num == 6:
                    print('You chose not to buy. Ending building selection.')
                    break
                elif unit_num in range(1, 6):
                    print('You chose to build option {unit_num}.')
                    break
                else:
                    print('Invalid choice.\nPlease reselect.')
                    shop_ch = False

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