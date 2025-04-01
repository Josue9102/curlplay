import argparse
from .game import Game
from .colors import Color

def main():
    parser = argparse.ArgumentParser(description='CurlPlay - A command-line game player with colors.')
    parser.add_argument('--game', type=str, required=True, help='URL of the game file (e.g., z64 file)')

    args = parser.parse_args()
    
    game = Game(args.game)
    game.load_game()

    # For demonstration, printing color
    print(Color.get_color_code("green") + "Launch in progress..." + Color.get_color_code("reset"))

if __name__ == '__main__':
    main()
