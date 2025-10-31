import os
import time
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init()

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

########Win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'

# This Function Draws Game Board

def DrawBoard():
    # Colors for X and O
    def colored_mark(pos):
        if board[pos] == 'X':
            return f"{Fore.BLUE}{board[pos]}{Style.RESET_ALL}"
        elif board[pos] == 'O':
            return f"{Fore.RED}{board[pos]}{Style.RESET_ALL}"
        else:
            return f"{Fore.LIGHTBLACK_EX}{pos}{Style.RESET_ALL}"

    print("\n")
    print(f"     ╔═════╦═════╦═════╗")
    print(f"     ║  {colored_mark(1)}  ║  {colored_mark(2)}  ║  {colored_mark(3)}  ║")
    print(f"     ╠═════╬═════╬═════╣")
    print(f"     ║  {colored_mark(4)}  ║  {colored_mark(5)}  ║  {colored_mark(6)}  ║")
    print(f"     ╠═════╬═════╬═════╣")
    print(f"     ║  {colored_mark(7)}  ║  {colored_mark(8)}  ║  {colored_mark(9)}  ║")
    print(f"     ╚═════╩═════╩═════╝{Style.RESET_ALL}")
    print("\n")


# This Function Checks position is empty or not
def CheckPosition(x):
    if (board[x] == ' '):
        return True
    else:
        return False

    # This Function Checks player has won or not


def CheckWin():
    global Game
    # Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
        # Vertical Winning Condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
        # Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game Designed By Ryun Randhawa")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)
while (Game == Running):
    os.system('cls')
    DrawBoard()
    if (player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if (CheckPosition(choice)):
        board[choice] = Mark
        player += 1
        CheckWin()

os.system('cls')
DrawBoard()
if (Game == Draw):
    print("\nGame Draw")
elif (Game == Win):
    player -= 1
    if (player % 2 != 0):
        print("\nPlayer 1 Won")
    else:
        print("\nPlayer 2 Won")