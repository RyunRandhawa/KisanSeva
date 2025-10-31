import os
import time
from colorama import init, Fore, Style, Back
import random

# Initialize colorama for cross-platform color support
init(autoreset=True)


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(10)]
        self.player = 1
        self.game_state = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_splash_screen(self):
        splash = f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
║{Fore.YELLOW}             WELCOME TO THE             {Fore.CYAN}║
║{Fore.MAGENTA}        ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄             {Fore.CYAN}║
║{Fore.MAGENTA}          ║   ║ ║   ║                 {Fore.CYAN}║
║{Fore.MAGENTA}          ║   ║ ║   ║                 {Fore.CYAN}║
║{Fore.RED}        ULTIMATE TIC TAC TOE            {Fore.CYAN}║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(splash)
        time.sleep(1)

    def loading_animation(self):
        print(f"\n{Fore.YELLOW}Loading game", end="")
        for _ in range(5):
            print(f"{Fore.YELLOW}.", end="", flush=True)
            time.sleep(0.2)
        print(Style.RESET_ALL)

    def get_cell_content(self, pos):
        if self.board[pos] == 'X':
            return f"{Fore.LIGHTBLUE_EX}X{Style.RESET_ALL}"
        elif self.board[pos] == 'O':
            return f"{Fore.RED}O{Style.RESET_ALL}"
        return f"{Fore.WHITE}{pos}{Style.RESET_ALL}"

    def draw_board(self):
        player_mark = 'X' if self.player % 2 != 0 else 'O'
        player_color = Fore.LIGHTBLUE_EX if self.player % 2 != 0 else Fore.RED
        current_player = "1" if self.player % 2 != 0 else "2"

        board = f"""
{player_color}Player {current_player}'s Turn ({player_mark}){Style.RESET_ALL}

{Fore.CYAN}┌─────────┬─────────┬─────────┐
│         │         │         │
│    {self.get_cell_content(1)}    │    {self.get_cell_content(2)}    │    {self.get_cell_content(3)}    │
│         │         │         │
├─────────┼─────────┼─────────┤
│         │         │         │
│    {self.get_cell_content(4)}    │    {self.get_cell_content(5)}    │    {self.get_cell_content(6)}    │
│         │         │         │
├─────────┼─────────┼─────────┤
│         │         │         │
│    {self.get_cell_content(7)}    │    {self.get_cell_content(8)}    │    {self.get_cell_content(9)}    │
│         │         │         │
└─────────┴─────────┴─────────┘{Style.RESET_ALL}

{Back.MAGENTA}{Fore.WHITE} CONTROLS {Style.RESET_ALL}
{Fore.CYAN}► Numbers (1-9):{Style.RESET_ALL} Place your mark
{Fore.CYAN}► Q:{Style.RESET_ALL} Quit game
"""
        print(board)

    def check_win(self):
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
            [1, 5, 9], [3, 5, 7]  # Diagonal
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                    self.board[combo[2]] != ' '):
                self.game_state = 1
                return

        if ' ' not in self.board[1:]:
            self.game_state = -1
        else:
            self.game_state = 0

    def celebrate_win(self, winner):
        celebration_frames = [
            "🎮  ", "🎲  ", "🎯  ", "🎪  ", "✨  ", "🏆  "
        ]

        for _ in range(3):
            for frame in celebration_frames:
                self.clear_screen()
                self.draw_board()
                color = random.choice([Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA])
                print(f"\n{color}{frame} Player {winner} WINS! {frame[::-1]}{Style.RESET_ALL}")
                time.sleep(0.2)

    def play(self):
        self.clear_screen()
        self.display_splash_screen()
        self.loading_animation()

        while self.game_state == 0:
            self.clear_screen()
            self.draw_board()

            try:
                choice = input(f"\n{Fore.CYAN}Enter your move (1-9): {Style.RESET_ALL}").lower()

                if choice == 'q':
                    print(f"\n{Fore.YELLOW}Thanks for playing! Goodbye!{Style.RESET_ALL}")
                    return

                choice = int(choice)
                if not (1 <= choice <= 9 and self.board[choice] == ' '):
                    print(f"\n{Back.RED}{Fore.WHITE} Invalid move! Try again. {Style.RESET_ALL}")
                    time.sleep(1)
                    continue

                print(f"\n{Fore.GREEN}► Making move...{Style.RESET_ALL}")
                time.sleep(0.3)

                self.board[choice] = 'X' if self.player % 2 != 0 else 'O'
                self.player += 1
                self.check_win()

            except ValueError:
                print(f"\n{Back.RED}{Fore.WHITE} Please enter a number between 1-9 {Style.RESET_ALL}")
                time.sleep(1)

        self.clear_screen()
        self.draw_board()

        if self.game_state == -1:
            print(f"\n{Fore.YELLOW}🎮 Game Draw! Well played! 🎮{Style.RESET_ALL}")
        else:
            winner = "2" if self.player % 2 != 0 else "1"
            self.celebrate_win(winner)


if __name__ == "__main__":
    try:
        game = TicTacToe()
        game.play()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Game interrupted. Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Back.RED}{Fore.WHITE} An error occurred: {e} {Style.RESET_ALL}")