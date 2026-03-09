
from blessed import Terminal
import time
import random


term = Terminal()

#endgame called whenever game finshes
def endscreen():
    print(term.home + term.clear)
    print(term.move_xy(gameendx,gameendy),term.blue("Gameover"))
    print(term.move_xy(gameendx + 1,gameendy + 1),term.blue("time score = " + str(roundedscore)))
    print(term.move_xy(gameendx + 2,gameendy + 2),term.blue("checkpoint = " + str(checkpointscore)))

    while True:
        key = term.inkey()
        if key.name == "KEY_ENTER" or key == "\n":
            break    

        




#simplified ai movement
def AImovemnet(enemy_x,enemy_y,x,y,framecount,enemeyspeed):
   
        if framecount % enemeyspeed == 0:
            if enemy_x < x:
                enemy_x += 1
            elif enemy_x > x:
                enemy_x -= 1
        if framecount % enemeyspeed == 0:
            if enemy_y < y:
                enemy_y += 1
            elif enemy_y > y:
                enemy_y -= 1        
        return enemy_x, enemy_y



with term.cbreak(), term.hidden_cursor():

    #playerpos
    x, y = term.width // 2, term.height // 2  
    #endscreenpos
    gameendx, gameendy = term.width // 2, term.height // 2  
    #score
    scorex, scorey = term.width // 1, term.height // 5
    score = 0.00
    roundedscore = 0.00

    Checkscorex, Checkscorey = term.width // 1, term.height // 4
    #declaring enemeys#  
    enemy1_x, enemy1_y = term.width // 4, term.height // 4
    enemy2_x, enemy2_y = term.width // 1, term.height // 1
    enemy3_x, enemy3_y = term.width // 7, term.height // 1
    enemy4_x, enemy4_y = term.width // 1, term.height // 7
    #declaring enemeys#
    enemeyspeed1 = 4
    enemeyspeed2 = 5
    enemeyspeed3 = 4
    enemeyspeed4 = 6
    #enemey spedlook up
    framecount = 0
    checkx = random.randint(0, term.width - 1)
    checky = random.randint(0, term.height - 1)
    checkpointscore = 0
    



    while True:
        #adding fraemcount for movement
        framecount += 1


         #clear
        print(term.home + term.clear)  
       


        print(term.move_xy(scorex, scorey) + term.white(" score = " + str(roundedscore)))

        #plaeyer print
        print(term.move_xy(x, y) + term.green('@'))


            #checkpoint
        print(term.move_xy(Checkscorex,Checkscorey) + term.white(" Checkpoints = " + str(checkpointscore)))

        print(term.move_xy(checkx,checky) + term.green("^"))

        #eenemypprint
        print(term.move_xy(enemy1_x, enemy1_y) + term.red('1'))
        print(term.move_xy(enemy2_x, enemy2_y) + term.red('2'))
        print(term.move_xy(enemy3_x, enemy3_y) + term.red('3'))
        print(term.move_xy(enemy4_x, enemy4_y) + term.red('4'))
        #enenmey print
     
        #playercontroller#
        key = term.inkey(timeout=0.1)
        if key == 'q':
            break
        elif key.name == 'KEY_UP':
            y = max(0, y - 1)
        elif key.name == 'KEY_DOWN':
            y = min(term.height - 1, y + 1)
        elif key.name == 'KEY_LEFT':
            x = max(0, x - 1)
        elif key.name == 'KEY_RIGHT':
            x = min(term.width - 1, x + 1)


        #changing enemey positon
        enemy1_x,enemy1_y = AImovemnet(enemy1_x,enemy1_y,x,y,framecount,enemeyspeed1)
        enemy2_x,enemy2_y = AImovemnet(enemy2_x,enemy2_y,x,y,framecount,enemeyspeed2)
        enemy3_x,enemy3_y = AImovemnet(enemy3_x,enemy3_y,x,y,framecount,enemeyspeed3)
        enemy4_x,enemy4_y = AImovemnet(enemy4_x,enemy4_y,x,y,framecount,enemeyspeed4)
        #adding score evey lop and rounding it
        score += 0.01
        roundedscore = round(score, 3)

        if (x,y ) == (checkx,checky):
                checkx = random.randint(0, term.width - 1)
                checky = random.randint(0, term.height - 1)
                checkpointscore += 1

        #lowkey just expereimtnal
        #declaring enemy collisions
        if (x,y) == (enemy1_x, enemy1_y):
            endscreen()
            break
            

        if (x,y) == (enemy2_x, enemy2_y):
            endscreen()
            break



        if (x,y) == (enemy3_x, enemy3_y):
            endscreen()
            break

        if (x,y) == (enemy4_x, enemy4_y):
            endscreen()
            break
