print("Welcome to Tic Tac Toe ")

occupied = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

board =   "\n   |   |   \n"  \
          " {} | {} | {} \n"  \
          "___|___|___\n"  \
          "   |   |   \n"  \
          " {} | {} | {} \n"  \
          "___|___|___\n"  \
          "   |   |   \n"  \
          " {} | {} | {} \n"  \
          "   |   |   \n"  \

def print_board(pozition, value):
    global occupied
    if pozition < 0 or pozition > 9:
        occupied = 9 * ' '
        print("Out of range position.")
    else:
        occupied[pozition - 1] = value
    print(board.format(occupied[0], occupied[1], occupied[2], occupied[3], occupied[4], occupied[5], occupied[6], occupied[7], occupied[8]))


def start_game():
    player_one = input("Enter first player name: ")
    player_two = input("Enter second player name: ")
    run_game(player_one, player_two)

def run_game(player_one, player_two):
  print("Game started...")
  replay(player_one, player_two)




def replay(player_one, player_two):
    turn = 1
    while ' ' in occupied:
        if turn == 1:
            input_one = '"' + input("Player {} chose from 1 to 9: ".format(player_one)) + '"'
            while occupied[int(input_one)] == ' ':
              input_one = "" + input("Pozition is occupied chose another one {} : ".format(player_one))
            print_board(int(input_one), 'x')
            turn = 0
        else:
            input_two = "" + input("Player {} chose from 1 to 9: ".format(player_two))
            while occupied[int(input_two)] == ' ':
              input_two = "" + input("Pozition is occupied chose another one {} : ".format(player_two))
            print_board(int(input_two), '0')
            turn = 1

start_game()
player_one = input("Enter first player name: ")
