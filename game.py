from blessed import Terminal
import time
import random


term = Terminal()

#endgame called whenever game finshes
def endscreen():
    global gamerunning
    print(term.home + term.clear)
    print(term.move_xy(gameendx,gameendy),term.blue("Gameover"))
    print(term.move_xy(gameendx + 1,gameendy + 1),term.blue("score = " + str(score)))


    while True:
        key = term.inkey()
        if key.name == "KEY_ENTER" or key == "\n":
            gamerunning = False
            break  

        





##
# def spawnenemymiddle():
#     enemy = {
#         "x": term.width // 2,
#         "y": term.height // 6,
#         "speed": random.randint(3,6)
#     }
#     enemys.append(enemy)

# def spawnenemyleft():
#     enemy = {
#         "x": term.width // 6,
#         "y": term.height // 6,
#         "speed": random.randint(3,6)
#     }
#     enemys.append(enemy)
                
# def spawnenemyright():
#     enemy = {
#         "x": term.width // 1,
#         "y": term.height // 6,
#         "speed": random.randint(3,6)
#     }
#     enemys.append(enemy)
##

###  ^ is spawners this is also spwaners 
# def enemeyspawner():
#     spawn = random.randint(1,3)
#     if spawn == 1:
#         spawnenemymiddle()
#     elif spawn == 2:
#         spawnenemyleft()
#     elif spawn == 3:
#         spawnenemyright()


def enemeyspawner():
    enemy = {
        "x": random.randint(0, term.width - 1),
        "y": random.randint(0, term.height - 1),
        "speed": random.randint(3,6)
    }
    enemys.append(enemy)





#simplified ai movement

def AImovement(enemys, player_x, player_y, framecount ):
   
    for enemy in enemys:

        if framecount % enemy["speed"] == 0:
           

                if enemy["x"] < player_x:
                    enemy["x"] += 1
                elif enemy["x"] > player_x:
                    enemy["x"] -= 1

                if enemy["y"] < player_y:
                    enemy["y"] += 1
                elif enemy["y"] > player_y:
                    enemy["y"] -= 1


def Gunsystem():
   
    for bullet in bullets:
            if not enemys:
                continue
            
            closestenemy = min(enemys, key=lambda e: (bullet["x"] - e["x"])**2 + (bullet["y"] - e["y"])**2)


            if bullet["x"] < closestenemy["x"]:
                bullet["x"] += 1  
            elif bullet["x"] > closestenemy["x"]:
                bullet["x"] -= 1  

            if bullet["y"] < closestenemy["y"]:
                bullet["y"] += 1 
            elif bullet["y"] > closestenemy["y"]:
                bullet["y"] -= 1  
                
         
def bulletspawner():
    if enemys:
        if framecount % bullettime == 0:
            bullet = {
            "x": x,
            "y": y,
        }
            bullets.append(bullet)








with term.cbreak(), term.hidden_cursor():

    #playerpos
    x, y = term.width // 2, term.height // 2  
    #endscreenpos
    gameendx, gameendy = term.width // 2, term.height // 2  
    #score
    scorex, scorey = term.width // 1, term.height // 5
    score = 0
    
   
    levelupx, levelupy = term.width // 2, term.height // 2


    bullettime = 20
    enemeyspawntime = 15

    framecount = 0
    
    bullets = []

    enemys = [
    ]

    gamerunning = True

    level = 0

    while gamerunning == True:
        #adding fraemcount for movement
        framecount += 1



        AImovement(enemys, x, y, framecount)
         #clear
        print(term.home + term.clear)  
       


        print(term.move_xy(scorex, scorey) + term.white(" score = " + str(score)))



        print(term.move_xy(x,y) + term.green("@"))

     
      
        Gunsystem()
        bulletspawner()



        for enemy in enemys:
            print(term.move_xy(enemy["x"], enemy["y"]) + "X")
        for bullet in bullets:
            print(term.move_xy(bullet["x"], bullet["y"]) + ".")

        #playercontroller#
        key = term.inkey(timeout=0.1)
        if key == 'q':
           
            endscreen()


        elif key.name == 'KEY_UP':
            y = max(0, y - 1)
        elif key.name == 'KEY_DOWN':
            y = min(term.height - 1, y + 1)
        elif key.name == 'KEY_LEFT':
            x = max(0, x - 1)
        elif key.name == 'KEY_RIGHT':
            x = min(term.width - 1, x + 1)



        
        if framecount % enemeyspawntime == 0:
            enemeyspawner()




        for bullet in bullets[:]:  # loop over a copy so we can remove safely
            for enemy in enemys[:]:
                if bullet["x"] == enemy["x"] and bullet["y"] == enemy["y"]:
                    bullets.remove(bullet)  # remove bullet
                    enemys.remove(enemy)     # remove enemy
                    score += 1               # increase score
                    break  # stop checking other enemies for this bullet


        for enemy in enemys:
            if enemy["x"] == x and enemy["y"] == y:
                endscreen()
                break
