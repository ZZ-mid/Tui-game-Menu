from blessed import Terminal
import time
import random
import subprocess

term = Terminal()

with term.cbreak(), term.hidden_cursor():

    #playerpos
    x, y = term.width // 2 + 7, term.height // 2 - 1, 
    game1x, game1y = term.width // 2, term.height // 2 - 1
    game2x, game2y = term.width // 2, term.height // 2  
    pos = 1

    while True:

        print(term.home + term.clear)  
       
        #plaeyer print
        print(term.move_xy(x, y) + term.green('@'))
        print(term.move_xy(game1x,game1y ) + term.blue('Game 1 '))
        print(term.move_xy(game2x,game2y ) + term.blue('Game 2 '))

        
        key = term.inkey(timeout=0.1)

        #playercontroller#
        if pos == 1:
            if key.name == 'KEY_DOWN':
                y = min(term.height // 2, y + 1)
                pos = 2
        if pos == 2:
            if key.name == 'KEY_UP':
                y = max(term.height // 2 - 1, y - 1)
                pos = 1


        if key == 'q':
            break

        if key.name == "KEY_ENTER":
            if pos == 1:
                subprocess.run(["python3", "notepaddev/Checkpoint.py"])
            if pos == 2:
                break
                



