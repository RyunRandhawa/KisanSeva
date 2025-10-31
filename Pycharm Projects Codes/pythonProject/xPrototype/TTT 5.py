import os
import time
from colorama import init, Fore, Style
import random

# Initialize colorama and game state
init()
board = [' ' for _ in range(10)]
player = 1
Game = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def CheckWin():
    global Game
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]  # Diagonal
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            Game = 1
            return

    if ' ' not in board[1:]:
        Game = -1
    else:
        Game = 0

def loading_animation():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(10):
        for frame in frames:
            print(f"\r{Fore.CYAN}Loading {frame}", end="")
            time.sleep(0.1)
    print(f"\r{' ' * 20}\r")

def display_title():
    title = f"""
    {Fore.YELLOW}╔══════════════════════════════════════════╗
    ║  {Fore.CYAN}████████╗██╗ ██████╗{Fore.YELLOW}                    ║
    ║  {Fore.CYAN}╚══██╔══╝██║██╔════╝{Fore.YELLOW}                    ║
    ║     {Fore.CYAN}██║   ██║██║     {Fore.YELLOW}                    ║
    ║     {Fore.CYAN}██║   ██║██║     {Fore.YELLOW}                    ║
    ║     {Fore.CYAN}██║   ██║╚██████╗{Fore.YELLOW}                    ║
    ║     {Fore.CYAN}╚═╝   ╚═╝ ╚═════╝{Fore.YELLOW}                    ║
    ║        {Fore.RED}████████╗ █████╗  ██████╗{Fore.YELLOW}         ║
    ║        {Fore.RED}╚══██╔══╝██╔══██╗██╔════╝{Fore.YELLOW}         ║
    ║           {Fore.RED}██║   ███████║██║{Fore.YELLOW}              ║
    ║           {Fore.RED}██║   ██╔══██║██║{Fore.YELLOW}              ║
    ║           {Fore.RED}██║   ██║  ██║╚██████╗{Fore.YELLOW}         ║
    ║           {Fore.RED}╚═╝   ╚═╝  ╚═╝ ╚═════╝{Fore.YELLOW}         ║
    ║               {Fore.LIGHTBLUE_EX}████████╗ ██████╗ ███████╗{Fore.YELLOW} ║
    ║               {Fore.LIGHTBLUE_EX}╚══██╔══╝██╔═══██╗██╔════╝{Fore.YELLOW} ║
    ║                  {Fore.LIGHTBLUE_EX}██║   ██║   ██║█████╗{Fore.YELLOW}   ║
    ║                  {Fore.LIGHTBLUE_EX}██║   ██║   ██║██╔══╝{Fore.YELLOW}   ║
    ║                  {Fore.LIGHTBLUE_EX}██║   ╚██████╔╝███████╗{Fore.YELLOW} ║
    ║                  {Fore.LIGHTBLUE_EX}╚═╝    ╚═════╝ ╚══════╝{Fore.YELLOW} ║
    ╚══════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(title)

def get_cell_style(pos):
    if board[pos] == 'X':
        return f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}X{Style.RESET_ALL}"
    elif board[pos] == 'O':
        return f"{Fore.RED}{Style.BRIGHT}O{Style.RESET_ALL}"
    return f"{Fore.LIGHTBLACK_EX}{str(pos).center(1)}{Style.RESET_ALL}"

def DrawBoard():
    player_mark = 'X' if player % 2 != 0 else 'O'
    player_color = Fore.LIGHTBLUE_EX if player % 2 != 0 else Fore.RED
    current_player = "1" if player % 2 != 0 else "2"

    stars = "★ " * (player % 5 + 1)  # Dynamic star decoration

    board_display = f"""
    {Fore.YELLOW}{stars}{Style.RESET_ALL}
    {player_color}Player {current_player}'s Turn ({player_mark}){Style.RESET_ALL}
    {Fore.YELLOW}{stars}{Style.RESET_ALL}

    {Fore.CYAN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃     ╔═════╦═════╦═════╗     ┃
    ┃     ║  {get_cell_style(1)}  ║  {get_cell_style(2)}  ║  {get_cell_style(3)}  ║     ┃
    ┃     ╠═════╬═════╬═════╣     ┃
    ┃     ║  {get_cell_style(4)}  ║  {get_cell_style(5)}  ║  {get_cell_style(6)}  ║     ┃
    ┃     ╠═════╬═════╬═════╣     ┃
    {Fore.CYAN}┃     ║  {get_cell_style(7)}  ║  {get_cell_style(8)}  ║  {get_cell_style(9)}  ║     ┃
    {Fore.CYAN}┃     ╚═════╩═════╩═════╝     ┃
    {Fore.CYAN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Style.RESET_ALL}

    {Fore.MAGENTA}╭──────────── Controls ────────────╮
    │  Numbers 1-9: Place your mark    │
    │  Q: Quit game                    │
    ╰──────────────────────────────────╯{Style.RESET_ALL}
    """
    print(board_display)


def display_win_animation(winner):
    frames = ["🎮 ", "🎲 ", "🎯 ", "🎪 ", "✨ "]
    global player
    winning_player = player  # Store the winning player state

    for _ in range(3):  # Repeat animation 3 times
        for frame in frames:
            clear_screen()
            player = winning_player  # Keep the winning state during animation
            DrawBoard()
            print(f"\n{Fore.GREEN}{frame} Player {winner} WINS! {frame}{Style.RESET_ALL}")
            time.sleep(0.2)


def play_game():
    global player, Game, board
    clear_screen()
    display_title()
    loading_animation()

    while Game == 0:
        clear_screen()
        DrawBoard()

        try:
            choice = input(f"\n{Fore.CYAN}Enter your move (1-9): {Style.RESET_ALL}").lower()
            if choice == 'q':
                print(f"\n{Fore.YELLOW}Thanks for playing! See you next time!{Style.RESET_ALL}")
                return

            choice = int(choice)
            if not (1 <= choice <= 9 and board[choice] == ' '):
                print(f"\n{Fore.RED}Invalid move! Try again.{Style.RESET_ALL}")
                time.sleep(1)
                continue

            board[choice] = 'X' if player % 2 != 0 else 'O'
            player += 1  # Increment player before checking win
            CheckWin()

        except ValueError:
            print(f"\n{Fore.RED}Please enter a number between 1-9{Style.RESET_ALL}")
            time.sleep(1)

    clear_screen()
    DrawBoard()

    if Game == -1:
        print(f"\n{Fore.YELLOW}🎮 Game Draw! Well played! 🎮{Style.RESET_ALL}")
    else:
        winner = "2" if player % 2 != 0 else "1"  # Previous player is the winner
        display_win_animation(winner)

if __name__ == "__main__":
    play_game()