from funnyAsciiImages import play_normal_ascii, flushImage
from keyboard import read_key # i could probably make this with a lot of dedication? im not going to but i could
from time import sleep # i lowk dont know how this works in this scenario (fps) but it does
from random import randint

class gameInfo(): # only exists because of how bloated the player class is
    def __init__(self, fps):
        self.fps = 1/fps
        self.quit = False

info = gameInfo(5) # Sets the game to whatever fps you give it

class player():
    def __init__(self):
        self.emptyEnemyDirList = ["./enemy-pos/enemyNP-1.png", "./enemy-pos/enemyNP-2.png", "./enemy-pos/enemyNP-3.png"]
        self.quit = False
        self.enemyPos = [1,1] # x, y
        self.x_pos = 0 # Btw these 2 positions are seperate because i wasn't planning on adding the y axis but it turned out being quite easy so i js did it anyways cuz whtv
        self.y_pos = 0
        self.blankDir = "./player-pos/blank.png"
        self.AplayerDirList = ["./player-pos/player-1pos.png", "./player-pos/player-2pos.png", "./player-pos/player-3pos.png"] # gretest idea i've ever had /srs

    def map(self): # i.. dont really know.. what i made here??
        #play_normal_ascii(self.dirList[self.x_pos])
        
        for i in range(0, self.y_pos):
            if i != self.enemyPos[1]:
                play_normal_ascii(self.blankDir)
            else:
                play_normal_ascii(self.emptyEnemyDirList[self.enemyPos[0]])

        if self.y_pos == self.enemyPos[1]:
            self.drawPlayerEnemySprites()
        else:
            play_normal_ascii(self.AplayerDirList[self.x_pos])

        if self.y_pos == 0 and self.enemyPos[1] == 2:
            play_normal_ascii(self.blankDir)
        for i in range(self.y_pos, 2):
            #play_normal_ascii(self.blankDir)
            if self.y_pos < self.enemyPos[1]:
                play_normal_ascii(self.emptyEnemyDirList[self.enemyPos[0]])
                if self.enemyPos[1] != 2:
                    play_normal_ascii(self.blankDir)
                    break
                else:
                    break
            else:
                play_normal_ascii(self.blankDir)
    
    
    def drawPlayerEnemySprites(self):
        kys = False
        if self.y_pos == self.enemyPos[1]: # Just to make sure i didn't fuck up nd use this in the wrong spot
            if self.x_pos == self.enemyPos[0]: # this is a mess
                play_normal_ascii(self.AplayerDirList[self.x_pos])
                # create new enemy
                self.enemyPos[0] = randint(0,2)
                self.enemyPos[1] = randint(0,2)
                # here to prevent 1 singular bug
                kys = True
            if kys != True:
                if self.x_pos == 0:
                    if self.enemyPos[0] == 1:
                        play_normal_ascii("./playerEnemyPos/p1-e2-pos.png")
                    elif self.enemyPos[0] == 2:
                        play_normal_ascii("./playerEnemyPos/p1-e3-pos.png")
                elif self.x_pos == 1:
                    if self.enemyPos[0] == 0:
                        play_normal_ascii("./playerEnemyPos/p2-e1-pos.png")
                    elif self.enemyPos[0] == 2:
                        play_normal_ascii("./playerEnemyPos/p2-e3-pos.png")
                elif self.x_pos == 2:
                    if self.enemyPos[0] == 0: 
                        play_normal_ascii("./playerEnemyPos/p3-e1-pos.png")
                    elif self.enemyPos[0] == 1:
                        play_normal_ascii("./playerEnemyPos/p3-e2-pos.png")

    

    
    def userInput(self, userInput): # Get the user input aand decide wht to do with it
        if userInput in ["a", "d"]: # i wanted it to loop like pacman which is why its kinda messy, i didnt focus much on this part of the code tbh
            if userInput == "a":
                if self.x_pos == 0:
                    self.x_pos = 2
                else:
                    self.x_pos -= 1
            else:
                if self.x_pos == 2:
                    self.x_pos = 0
                else:
                    self.x_pos += 1


        elif userInput in ["w", "s"]: # movement on the y axis
            if userInput == "w":
                if self.y_pos == 0:
                    self.y_pos = 2
                else:
                    self.y_pos -= 1
            else:
                if self.y_pos == 2:
                    self.y_pos = 0
                else:
                    self.y_pos += 1
        else:
            info.quit = True
        sleep(info.fps) # dont question how this works



playe = player() # making the map and player in the same class was a mistake btw, but its not that bad so im not gon bother


while False == info.quit: # i find this line kinda funny cuz it sounds goofy
    playe.map()
    playe.userInput(read_key())
    flushImage()
