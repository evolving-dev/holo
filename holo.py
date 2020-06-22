import pygame
import time, os
from os.path import join

def readfile(name):
    with open(name,"r") as f:
        return(f.read())

PATH = os.path.dirname(os.path.abspath(__file__))

class game:
    class options:
        dimensions = [256,256]
        frame_rate = 1
        gameTitle = "Startup - HOLO" if os.path.isdir(os.path.join(PATH,"USERS")) else "Setup - HOLO"
        pixel_size = 1
        cursorVisible = True
        #Generelle Informationen über das Spiel
    class timers:
        frame = 0
        seconds = 0
        #In dieser Klasse kann direkt auf die GameTimer zugegriffen werden.
    class state:
        done = False
        #Status des Spiels
    class storage:
        state = 1
        #Speicherort von Spieldaten oder Texturen

class engine:
    class draw:
        def refreshGameInformations():
            global screen
            screen = pygame.display.set_mode(game.options.dimensions)
            pygame.display.set_caption(game.options.gameTitle)
            game.options.pixel_count = [game.options.dimensions[0] // game.options.pixel_size, game.options.dimensions[1] // game.options.pixel_size]

ii=0

class execute:
    def gameInit():
        #game.storage.textureStorage["backgroundimage"] = pygame.image.load("menuBackground.jpg")
        pass
        #Funktion, die beim Spielstart ausgeführt wird.
    def onDrawFunction():
        screen.fill((40,60,100))
        if game.storage.state == 1:
            global ii
            for n,m in enumerate(list(STARTUP_TEXTS.keys())):
                screen.blit(STARTUP_TEXTS[m],((game.options.dimensions[0]-STARTUP_TEXTS[m].get_width())//2,(n+1)*game.options.dimensions[1]//8))
            if os.path.isdir(os.path.join(PATH,"USERS")):
                ii = 0
                pygame.display.flip()
                time.sleep(0.5)
                game.state.done = True
            elif os.path.isfile(os.path.join(PATH,"INITFILE")):
                ii = 1
                pygame.display.flip()
                time.sleep(0.5)
                game.state.done = True
            else:
                global ERRORMSG
                ERRORMSG = FONTS["big"].render("ERROR: Missing INITFILE",True,[255,0,0])
                game.storage.state = 2
        else:
            screen.blit(ERRORMSG,((game.options.dimensions[0] - ERRORMSG.get_width())//2,(game.options.dimensions[1] - ERRORMSG.get_height())//2))
        #Code, der jeden Frame ausgeführt wird. (auch Draw-Befehle)
    def onSecondFunction():
        game.storage.trueFPS = clock.get_fps()
        #Code, der jede Sekunde ausgeführt wird.
            

execute.gameInit()
pygame.init()
#programIcon = pygame.image.load('icon.png')

#pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode(game.options.dimensions)
clock = pygame.time.Clock()
pygame.display.set_caption(game.options.gameTitle)
pygame.key.set_repeat(100, 10)


exec(readfile(os.path.join(PATH, "scripts/init/initFontsFirstTimeStartup.py")))
STARTUP_LANG_FILE = eval(readfile(os.path.join(PATH,"assets/text/startup_en-US"))) if not os.path.isdir(os.path.join(PATH,"USERS")) else eval(readfile(os.path.join(PATH,"assets/text/startup_"+eval(readfile(os.path.join(PATH,"USERS/settings")))["lang"])))
STARTUP_TEXTS:dict = {}
for i in list(STARTUP_LANG_FILE.keys()):
    STARTUP_TEXTS[i] = FONTS["small"].render(STARTUP_LANG_FILE[i],True,[255]*3)



while not game.state.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state.done = True
    #Loop
    execute.onDrawFunction()
    if game.state.done:
        pygame.quit()
        break
    pygame.mouse.set_visible(game.options.cursorVisible)
    pygame.display.flip()
    
    clock.tick(game.options.frame_rate)
    
    game.timers.frame+=1
    if game.timers.frame >= game.options.frame_rate:
        game.timers.frame = 0
        game.timers.seconds+=1
        execute.onSecondFunction()
    
    
if ii:
    exec(readfile(os.path.join(PATH,"scripts/init/HOLO_INIT.py")),globals())
else:
    exec(readfile(os.path.join(PATH,"scripts/init/HOLO_START.py")),globals())


