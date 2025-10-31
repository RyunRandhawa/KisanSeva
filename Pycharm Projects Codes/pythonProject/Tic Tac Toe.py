import os
import time
from colorama import init, Fore, Style

# Initialize colorama and game state
init()
board = [' ' for _ in range(10)]  # 0 is not used
player = 1
Game = 0  # 0: Running, 1: Win, -1: Draw


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def DrawBoard():
    def get_cell_style(pos):
        if board[pos] == 'X':
            return f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}X{Style.RESET_ALL}"
        elif board[pos] == 'O':
            return f"{Fore.RED}{Style.BRIGHT}O{Style.RESET_ALL}"
        return f"{Fore.LIGHTBLACK_EX}{pos}{Style.RESET_ALL}"

    # Current player info
    player_mark = 'X' if player % 2 != 0 else 'O'
    player_color = Fore.LIGHTBLUE_EX if player % 2 != 0 else Fore.RED
    current_player = "1" if player % 2 != 0 else "2"

    # Board template with player info and controls
    board_display = f"""
    {Fore.LIGHTYELLOW_EX}╔══════════ TIC TAC TOE ══════════╗
    ║ X     O     X     O     X     O ║
    ╚═════════ MADE BY RYUN. ═════════╝{Style.RESET_ALL}

    {player_color}Current Player: {current_player} ({player_mark}){Style.RESET_ALL}

    {Fore.CYAN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃     ╔═════╦═════╦═════╗     ┃
    ┃     ║  {get_cell_style(1)}  ║  {get_cell_style(2)}  ║  {get_cell_style(3)}  ║     ┃
    ┃     ╠═════╬═════╬═════╣     ┃
    ┃     ║  {get_cell_style(4)}  ║  {get_cell_style(5)}  ║  {get_cell_style(6)}  ║     ┃
    ┃     ╠═════╬═════╬═════╣     ┃
    {Fore.CYAN}┃     ║  {get_cell_style(7)}  ║  {get_cell_style(8)}  ║  {get_cell_style(9)}  ║     ┃
    {Fore.CYAN}┃     ╚═════╩═════╩═════╝     ┃
    {Fore.CYAN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Style.RESET_ALL}

    {Fore.MAGENTA}[Enter 1-9 to play, 'q' to quit]{Style.RESET_ALL}
    """
    print(board_display)


def CheckPosition(x):
    return 1 <= x <= 9 and board[x] == ' '


def CheckWin():
    global Game
    # Winning combinations
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]  # Diagonal
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            Game = 1  # Win
            return

    if ' ' not in board[1:]:
        Game = -1  # Draw
    else:
        Game = 0  # Running


def play_game():
    global player, Game
    print(f"{Fore.YELLOW}\t \t  Welcome to Tic-Tac-Toe!!{Style.RESET_ALL}")
    time.sleep(1)

    while Game == 0:
        clear_screen()
        DrawBoard()

        try:
            choice = input(f"\nEnter position (1-9): ").lower()
            if choice == 'q':
                print("\nThanks for playing!")
                return

            choice = int(choice)
            if not CheckPosition(choice):
                print(f"{Fore.RED}Invalid position! Try again.{Style.RESET_ALL}")
                time.sleep(1)
                continue

            board[choice] = 'X' if player % 2 != 0 else 'O'
            player += 1
            CheckWin()

        except ValueError:
            print(f"{Fore.RED}Please enter a number between 1-9{Style.RESET_ALL}")
            time.sleep(1)

    # Game Over
    clear_screen()
    DrawBoard()

    if Game == -1:
        print(f"\n{Fore.YELLOW}Game Draw!{Style.RESET_ALL}")
    else:
        winner = "Player 1" if player % 2 == 0 else "Player 2"
        print(f"\n{Fore.GREEN}🎉 {winner} Wins! 🎉{Style.RESET_ALL}")


if __name__ == "__main__":
    play_game()