import sys
import os

from ui.main_menu import MainMenu

def main() -> int:
    states = [MainMenu()]
    while len(states) > 0:
        os.system('clear')
        states[-1].render()
        result = states[-1].input()
        if result is not None:
            states.append(result)
        else:
            states.pop()
    return 0

if __name__ == '__main__':
    sys.exit(main())