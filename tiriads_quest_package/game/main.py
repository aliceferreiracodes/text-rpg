import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import new_game

def main():
  home_screen()



def home_screen():
  print(
        '''
          === Tiriad's Quest ===

New game
Load 
Exit 
        '''
  )
  while True:
    option = input("Enter your option:\n> ").capitalize()
    if not (option == "New game" or option == "Load" or option == "Exit"):
      print("Enter a valid option.\n")
    else:
      break

  match option:
    case "New game":
      new_game.create()
    case "Load":
      load_screen()
    case "Exit":
      exit()


def load_screen():
  pass


if __name__ == "__main__":
  main()