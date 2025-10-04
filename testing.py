from funnyAsciiImages import play_normal_ascii, flushImage
from keyboard import read_key
from time import sleep

class gameInfo():
    def __init__(self, fps):
        self.fps = 1/fps
        self.quit = False

info = gameInfo(15)

class player():
    def __init__(self):
        self.quit = False
        self.x_pos = 1
        self.y_pos = 1
        self.blankDir = "./player-pos/blank.png"
        self.dirList = ["./player-pos/player-1pos.png", "./player-pos/player-2pos.png", "./player-pos/player-3pos.png"]

    def map(self):
        #play_normal_ascii(self.dirList[self.x_pos])

        for i in range(0, self.y_pos):
            play_normal_ascii(self.blankDir)
        play_normal_ascii(self.dirList[self.x_pos])
        for i in range(self.y_pos, 2):
            play_normal_ascii(self.blankDir)

        

    
    def userInput(self, userInput):
        if userInput in ["a", "d"]:
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
        elif userInput in ["w", "s"]:
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
        sleep(info.fps)



play = player()


while False == info.quit:
    play.map()
    play.userInput(read_key())
    flushImage()
