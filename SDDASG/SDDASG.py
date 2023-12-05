﻿from asyncio.windows_events import NULL
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
    game_vars['turn'] = 1
    game_vars['Coins'] = 16
    
#thre = '-' * game_vars['turn']

#---------
#Purchase building
#---------
def buy_unit(field, game_vars, position, building):
    row = ord(position[0]) - ord('A')
    column = int(position[1]) - 1 #position = 'A7'example
    for b in buildings:
        if b['shortform'] == building:
            building = b
            break
    if field[row][column] == None:
       field[row][column] = b
       game_vars['Coins'] -= 1
       print("Building has been built successfully")
       if game_vars['Coins'] <= 0:
           return "coinRunOut"  # Run out of coin after buy building
       game_vars['turn'] += 1
       return True  # buy successfully and still have coin left
    else:
        print("The position is occupied by another building, please try again")
        return False



#---------
#Purchase building menu
#---------
def show_combat_menu(game_vars):
    print('Turn {}'.format(game_vars['turn']))
    print('Coins= {}'.format(game_vars['Coins']))
    print("1. Buy unit     2. Save game")
    print("0. Quit")

#----------
#Random Building
#----------
buildings = [R, I, C, O, Road]

def select_random_building():

    build = random.choice(buildings)    # If player proceed to next turn, they will have new randomly generated building option
    build2 = random.choice(buildings)
    while build2 == build:  #make sure that second option wont be same as first option
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


#----------
#Check if position have connected building
#----------
def is_connected(field, position):
    row = ord(position[0]) - ord('A')
    column = int(position[1]) - 1

    # Check if any adjacent positions have a building
    adjacent_positions = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
    #this will check each adjacent position and return true if there is any adjacent position which is inside the board range and have a building on it
    for r, c in adjacent_positions: #for each row and column in adjacent position
        if 0 <= r < len(field) and 0 <= c < len(field[0]) and field[r][c] is not None: 
            return True
    return False

#----------
#Get position input from user with validation
#----------
def get_user_position(field, game_vars):
    while True:
        position = input("Enter position (e.g., A1): ").capitalize()
        if len(position) == 1:
            print('Invalid input')
        else:
            if int(position[1]) <= 20 and int(position[1]) > 0 and 'A' <= position[0] <= 'T':
                if is_connected(field, position) or game_vars['turn'] == 1:
                    return position
                else:
                    print('You can only build on squares connected to existing buildings.')
            else:
                print('Please put your unit in the range of the board')


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
        print('You have entered an invalid number.')
        break

while play_game==True:
    draw_field()
    show_combat_menu(game_vars)
    in_game_menu_input = int(input('Your choice? '))
    if in_game_menu_input == 1:       # build building
        chosen_building = select_random_building()
        print(chosen_building)
        position = get_user_position(field, game_vars)
        while position == False:   # invalid input
            position = get_user_position(field, game_vars)

        print("Building:", chosen_building) # *
        print("Position:", position)        # A1
        buy_success = buy_unit(field, game_vars, position, chosen_building)  
        if buy_success == "coinRunOut":
            chosen_building = "Back"
            play_game = False   # game end cos player left no coin 
        elif buy_success == True: # player built a building successfully and the turn will end
            chosen_building = "Back"

    #Save Game
    elif menu_input==2:
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