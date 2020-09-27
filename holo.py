import pygame
import time, os, math
from os.path import join
try:
    import _thread
except ImportError:
    import _dummy_thread as _thread
    print("[HOLO:STARTUP/WARNING]: The threading module could not be loaded, background processes might not work as expected.")

def readfile(name):
    with open(name,"rb") as f:
        return(f.read().decode("utf-8"))
def readbinary(name):
    with open(name,"rb") as f:
        return(f.read())

PATH = os.path.dirname(os.path.abspath(__file__))

class game:
    class options:
        dimensions = [256,256]
        frame_rate = 1
        gameTitle = "Startup - HOLO" if os.path.isdir(os.path.join(PATH,"USERS")) else "Setup - HOLO"
        cursorVisible = True
    class timers:
        frame = 0
        seconds = 0
    class state:
        done = False
    class storage:
        state = 1

class engine:
    class draw:
        def refreshGameInformations():
            global screen
            screen = pygame.display.set_mode(game.options.dimensions)
            pygame.display.set_caption(game.options.gameTitle)
            game.options.pixel_count = [game.options.dimensions[0] // game.options.pixel_size, game.options.dimensions[1] // game.options.pixel_size]

ii=0

class execute:
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
    def onSecondFunction():
        game.storage.trueFPS = clock.get_fps()
            
pygame.mixer.pre_init(44100, channels=2)
pygame.init()
ICON = pygame.image.load(join(PATH,'assets/images/icons/icon.png'))

pygame.display.set_icon(ICON)
screen = pygame.display.set_mode(game.options.dimensions)
clock = pygame.time.Clock()
pygame.display.set_caption(game.options.gameTitle)
pygame.key.set_repeat(100, 10)

exec(readfile(join(PATH, "scripts/init/initFontsFirstTimeStartup.py")))
STARTUP_LANG_FILE = eval(readfile(os.path.join(PATH,"assets/text/startup_en-US"))) if not os.path.isdir(os.path.join(PATH,"USERS")) else eval(readfile(os.path.join(PATH,"assets/text/startup_"+eval(readfile(os.path.join(PATH,"USERS/settings")))["lang"])))
STARTUP_TEXTS:dict = {}
for i in list(STARTUP_LANG_FILE.keys()):
    STARTUP_TEXTS[i] = FONTS["small"].render(STARTUP_LANG_FILE[i],True,[255]*3)

while not game.state.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state.done = True
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


