from asyncio.windows_events import NULL
from itertools import filterfalse
from pickle import FALSE
import random
import ctypes

# Game variables
game_vars = {
    'turn': 1, 
    'Coins': 20,
    'points': 0,
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
    print("4. Score Rules")
    print("0. Exit Game")


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

def initialize_field():
    global field
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
        print('{:<4}'.format(i), end='')
    
    print('\n ', end='')
    for i in range(len(field[0])):
        print('+---', end='')
    print('+')

    for r in range(num_r):
        print(chr(ord('A') + r), end='')

        for c in field[r]:
            if c != None:
                print('|{:^3}'.format(c['shortform']),end = '')
            else:
                print('|{:^3}'.format(' '),end = '')
        print('|')



        # Print the bottom line of each row
        print(' ', end='')
        for c in range(num_c):
            print('+---', end='')
        print('+')


    print('  ', end='')
    for i in range(1, num_c+1):
        print('{:<4}'.format(i), end='')

    print('\n')
    return


#-----------
#Initializes all the game variables for a new game
#-----------
def initialize_game():
    game_vars['turn'] = 1
    game_vars['Coins'] = 16
    
#thre = '-' * game_vars['turn']


#-----------
#Initializes all the game variables for a new game
#-----------
def show_legends():
    print('Shortform Legends: \nR = Residential \nI = Industry \nC = Commercial \nO = Park \n* = Road\n')

#-----------
#Score Rules
#-----------
def score_rules():
    print('\nThere are 5 types of buildings: \n')
    print('Residential (R): \nIf it is next to an industry (1), then it scores 1 point only.\nOtherwise, it scores 1 point for each adjacent residential (R) or commercial (C), \nand 2 points for each adjacent park (O).\n')
    print('Industry (I): \nScores 1 point per industry in the city. \nEach industry generates 1 coin per residential building adjacent to it.\n')
    print('Commercial (C): \nScores 1 point per commercial adjacent to it. \nEach commercial generates 1 coin per residential adjacent to it.\n')
    print('Park (O): \nScores 1 point per park adjacent to it.\n')
    print('Road (*): \nScores 1 point per connected road () in the same row.\n')

#---------
#Purchase building
#---------
def buy_unit(field, game_vars, position, building):
    row = ord(position[0]) - ord('A')
    column = int(position[1:]) - 1 #position = 'A7'example
    for b in buildings:
        if b['shortform'] == building:
            building = b
            break
    if field[row][column] == None:
       field[row][column] = b
       game_vars['Coins'] -= 1
       print("Building has been built successfully")
       if b['shortform'] == 'I':
           update_industry_coins(field, row,column)
       elif b['shortform'] == 'C':
           update_commercial_coins(field, row,column)
       elif b['shortform'] == 'R':
           update_residential_coins(field, row,column)
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
    print("3. Score Rules  0. Quit")

#----------
#Random Building
#----------
buildings = [R, I, C, O, Road]

def select_random_building(build=None, build2=None):
    if build is None:
        build = random.choice(buildings)    # If player proceed to next turn, they will have new randomly generated building option
        build2 = random.choice(buildings)
        while build2 == build:  #make sure that second option wont be same as first option
            build2 = random.choice(buildings)

    print('Please choose one of the two buildings given:\n' + '[1] ' + build['name'] +'\n[2] ' + build2['name'])
    choice = input("Enter your choice: ")
    # Ensure the user input matches one of the randomly chosen buildings
    if choice == '1' or choice == '2':
        chosen_building = build if choice == '1' else build2
        return chosen_building['shortform']
    else:
        print("Invalid choice. Please choose one of the two buildings.")
        return select_random_building(build,build2)


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
        if len(position) == 1 or not position[1].isdigit() or (len(position) == 3 and not position[2].isdigit()) or (len(position) > 3) or not (position[0].isalpha()):
            print('Invalid input. Please try again')
        else:
            if len(position) == 3:
                if int(position[1]) == 2 and ('A' <= position[0] <= 'T') and int(position[2]) == 0:
                    if is_connected(field, position) or game_vars['turn'] == 1:
                        return position
                    else:
                        print('You can only build on squares connected to existing buildings.')
                elif int(position[1]) == 1 and ('A' <= position[0] <= 'T'):
                    if is_connected(field, position) or game_vars['turn'] == 1:
                        return position
                    else:
                        print('You can only build on squares connected to existing buildings.')
                else:
                    print('Please put your unit in the range of the board')
            elif len(position) == 2:
                if 'A' <= position[0] <= 'T':
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


#---------
#Calculate Score
#---------


def calculate_points(field):
    points = 0

    for r in range(len(field)):
        for c in range(len(field[0])):
            building = field[r][c]

            if building is not None:
                if building['shortform'] == 'R':
                    points += calculate_residential_points(field, r, c)
                elif building['shortform'] == 'I':
                    points += 1  
                elif building['shortform'] == 'C':
                    points += calculate_commercial_points(field, r, c)
                elif building['shortform'] == 'O':
                    points += calculate_park_points(field, r, c)
                elif building['shortform'] == '*':
                    points += calculate_road_points(field, r)

    return points

def calculate_residential_points(field, row, col):
    adjacent_buildings = get_adjacent_buildings(field, row, col)
    industry_adjacent = any(building['shortform'] == 'I' for building in adjacent_buildings)
    non_road_adjacent = [building for building in adjacent_buildings if building['shortform'] != '*']
    residential_adjacent = sum(1 for building in non_road_adjacent if building['shortform'] == 'R')
    commercial_adjacent = sum(1 for building in non_road_adjacent if building['shortform'] == 'C')
    park_adjacent = sum(1 for building in non_road_adjacent if building['shortform'] == 'O')

    if industry_adjacent:
        return 1  
    else:
        return residential_adjacent + 2 * park_adjacent + commercial_adjacent


def calculate_industry_points(field, row, col):
    industry_count = sum(1 for r in range(len(field)) for c in range(len(field[0])) if field[r][c] and field[r][c]['shortform'] == 'I')
    return industry_count


# calculate number of residential building adjacent to the industry and add coin
def update_industry_coins(field, row, col):
    adjacent_buildings = get_adjacent_buildings(field, row, col)
    residential_adjacent = sum(1 for building in adjacent_buildings if building['shortform'] == 'R')
    if residential_adjacent:
        game_vars['Coins'] += residential_adjacent

# check got industry adjacent to new built residential or not and add coin if have
def update_residential_coins(field, row, col):
    adjacent_buildings = get_adjacent_buildings(field, row, col)
    industry_adjacent = sum(1 for building in adjacent_buildings if building['shortform'] == 'I')
    if industry_adjacent:
        game_vars['Coins'] += industry_adjacent
    
    commercial_adjacent = sum(1 for building in adjacent_buildings if building['shortform'] == 'C')
    if commercial_adjacent:
        game_vars['Coins'] += commercial_adjacent

def calculate_commercial_points(field, row, col):
    adjacent_buildings = get_adjacent_buildings(field, row, col)
    non_road_adjacent = [building for building in get_adjacent_buildings(field, row, col) if building['shortform'] != '*']
    commercial_adjacent = sum(1 for building in non_road_adjacent if building['shortform'] == 'C')
    return commercial_adjacent


# calculate number of residential building adjacent to the commercial and add coin
def update_commercial_coins(field, row, col):
    adjacent_buildings = get_adjacent_buildings(field, row, col)
    residential_adjacent = sum(1 for building in adjacent_buildings if building['shortform'] == 'R')
    if residential_adjacent:
        game_vars['Coins'] += residential_adjacent

def calculate_park_points(field, row, col):
    adjacent_positions = [
        (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
        (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
    ]
    park_adjacent = sum(1 for r, c in adjacent_positions if 0 <= r < len(field) and 0 <= c < len(field[0]) and field[r][c] and field[r][c]['shortform'] == 'O')

    return park_adjacent



def calculate_road_points(field, row):
    connected_roads = 0
    current_road_length = 0
    for building in field[row]:
        if building and building['shortform'] == '*':
            current_road_length += 1
        else:
            connected_roads += current_road_length // 2  
            current_road_length = 0
    connected_roads += current_road_length // 2  
    return connected_roads


def get_adjacent_buildings(field, row, col):
    adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    adjacent_buildings = [field[r][c] for r, c in adjacent_positions if 0 <= r < len(field) and 0 <= c < len(field[0]) and field[r][c] is not None]
    return adjacent_buildings

def display_current_score():
    game_vars['points'] = calculate_points(field)
    print(f"Current Points: {game_vars['points']}")

def is_game_over():
    if game_vars['Coins'] == 0:
        print("Game Over! You ran out of coins.")
        display_final_score()
        return True

    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] is None:
                return False

    print("Game Over! No empty grids left on the board.")
    display_final_score()
    return True

def display_final_score():
    game_vars['points'] = calculate_points(field)
    print(f"Final Score: {game_vars['points']}")

#-------------
# save_game()
#
#-------------
def save_game():
    with open('save_variable.txt', 'w') as save_file:
        # Save game variables
        save_file.write('Coins={}\n'.format(game_vars['Coins']))
        save_file.write('turn={}\n'.format(game_vars['turn']))
        save_file.write('points={}\n'.format(game_vars['points']))

    with open('save_field.txt', 'w') as save_file:
        # Save game field
        for row in range(len(field)):
            for column in range(len(field[row])):
                if field[row][column] is not None:
                    save_file.write(
                        '{},{},{},{}\n'.format(row, column, field[row][column]['shortform'], field[row][column]['name'])
                    )


#-----------------------------------------
# load_game()
#
#    Loads the game from 'save.txt'
#-----------------------------------------
def load_game(game_vars):
    initialize_field()
    config_file = open('save_variable.txt','r')
    for line in config_file:
        info = line.strip('\n')
        temp_list = info.split('=')
        game_vars[temp_list[0]] = int(temp_list[1]) # Replace the original new data with the previous stored data
    config_file.close()
    fieldfile = open('save_field.txt', 'r')
    for line in fieldfile:
        line = line.strip('\n')
        line_list = line.split(',')
        if line_list[2] == '*':
            field[int(line_list[0])][int(line_list[1])] = Road
        elif line_list[2] == 'R':
            field[int(line_list[0])][int(line_list[1])] = R
        elif line_list[2] == 'I':
            field[int(line_list[0])][int(line_list[1])] = I
        elif line_list[2] == 'C':
            field[int(line_list[0])][int(line_list[1])] = C
        elif line_list[2] == 'O':
            field[int(line_list[0])][int(line_list[1])] = O       
                    
    return


#-----------
#Main Menu
#-----------
running = True

while running == True:

    show_main_menu()
    
    menu_validation = False
    menu_ch=True
    while menu_validation == False:
        validation = True   #Check the validation of input for combat menu
        try:
            menu_input=int(input("Your choice?? "))
        except:         # It will keep prompt user for choice as long as his choice is invalid
            print('Invalid input')
            validation = False
        else:
            if menu_input > 4:
                print('Invalid input')
                validation = False
        if validation == True:
            while menu_ch==True:

                if menu_input==1:
                    menu_ch=False
                    initialize_game()
                    initialize_field()
                    play_game=True
                    menu_validation = True
        
                elif menu_input==2:
                    load_game(game_vars)
                    menu_ch=False
                    play_game=True
                    menu_validation = True

                elif menu_input==3:
                    menu_ch=False
                    play_game=False
                    print()
                    menu_validation = True

                elif menu_input==4:
                    menu_ch=False
                    play_game=False
                    score_rules()
                    menu_validation = True

                elif menu_input==0:
                    print('BYE BYE!!!!!!!!!!!')
                    menu_validation = True
                    running = False
                    break
                else:
                    print('You have entered an invalid number.')
                    menu_ch = False


    while play_game==True:
        draw_field()
        show_legends()
        while True:
            display_current_score()
            show_combat_menu(game_vars)
            validation = True   #Check the validation of input for combat menu
            try:
                in_game_menu_input = int(input('Your choice? '))
            except:         # It will keep prompt user for choice as long as his choice is invalid
                print('Invalid input')
                validation = False
            else:
                if in_game_menu_input > 3:
                    print('Invalid input')
                    validation = False
            if validation == True:
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
                        play_game = False   # game end cos player left no coin 
                        break
                    elif buy_success == True: # player built a building successfully and the turn will end
                        break

                # Save Game
                elif in_game_menu_input == 2:
                    rc = mbox("Do You Want to Save your Game?", "title")
                    if rc == MbConstants.IDOK:
                        save_game()
                        print("Game Saved!")

                    elif rc == MbConstants.IDCANCEL:
                        continue

                elif in_game_menu_input == 3:
                    score_rules()
                    validation == True

                # Quit
                elif in_game_menu_input == 0:
                    rc = mbox("Do You Want to Save your Game?", "title")
                    if rc == MbConstants.IDOK:
                        save_game()
                        print("Game Saved!")
                        play_game = False
                        break
                    
                    elif rc == MbConstants.IDCANCEL:
                        play_game = False
                        break
                    
        if is_game_over():
            while True:
                try:
                    back_to_menu = int(input("Enter '0' to go back to the main menu: "))
                except ValueError:
                    print("Invalid input. Please enter '0' to go back to the main menu.")
                    continue
                
                if back_to_menu == 0:
                    break
                else:
                    print("Invalid input. Please enter '0' to go back to the main menu.")

            

#-------------------
#Score System Guide
#-------------------       
## Game Over

#def is_board_full(field):
#    # Check if there are no empty grids on the board
#    return all(all(cell is not None for cell in row) for row in field)

#while play_game:
#    draw_field()
#    show_combat_menu(game_vars)
#    display_current_score()
#    in_game_menu_input = int(input('Your choice? '))
#    if in_game_menu_input == 1:  # build building
#        chosen_building = select_random_building()
#        print(chosen_building)
#        position = get_user_position(field, game_vars)
#        while position == False:   # invalid input
#            position = get_user_position(field, game_vars)
        
#        print("Building:", chosen_building)  # *
#        print("Position:", position)         # A1
#        buy_success = buy_unit(field, game_vars, position, chosen_building)  
#        if buy_success == "coinRunOut":
#            print("Game Over! You ran out of coins.")
#            play_game = False  # game end because the player has no coin left
#        elif buy_success == True:  # player built a building successfully and the turn will end
#            chosen_building = "Back"

#        # Check for game over based on no empty grids
#        if is_board_full(field):
#            print("Game Over! No empty grids left on the board.")
#            play_game = False

#    # Save Game
#    elif in_game_menu_input == 2:
#        rc = mbox("Do You Want to Save your Game?", "title")
#        if rc == MbConstants.IDOK:
#            print("Game Saved!")
#        elif rc == MbConstants.IDCANCEL:
#            continue

#    # Quit
#    elif in_game_menu_input == 0:
#        rc = mbox("Do You Want to Save your Game?", "title")
#        if rc == MbConstants.IDOK:
#            print("Game Saved!")
#        print('BYE BYE!!!!!!!!!!!!!!!!!!!!')
#        break

#    # Check for Game Over
#    if is_game_over(game_vars):
#        print("Game Over! You ran out of coins.")
#        play_game = False

#    # Check for game over based on no empty grids
#    if is_board_full(field):
#        print("Game Over! No empty grids left on the board.")
#        play_game = False

#    #Save Game
#    elif menu_input==2:
#        #ctypes.windll.user32.MessageBoxW(0,"Do You Want to Save your Game?", "", 3)
#        rc = mbox("Do You Want to Save your Game?","title")
#        if  rc == MbConstants.IDOK:
#            save_game()
#            print("Game Saved!")
#            print('BYE BYE!!!!!!!!!!!!!!!!!!!!')
#            break
#        elif rc == MbConstants.IDCANCEL:
#            continue

#    #End
#    else:
#        #ctypes.windll.user32.MessageBoxW(0, "Do You Want to Save your Game?", "", 4)
#        rc = mbox("Do You Want to Save your Game?","title")
#        if  rc == MbConstants.IDOK:
#            save_game()
#            print("Game Saved!")            
#        print('BYE BYE!!!!!!!!!!!!!!!!!!!!')
#        break

    

    
