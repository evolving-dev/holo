from io import BytesIO
import PIL
from PIL import Image,ImageDraw
if "game" in globals():
    del game
    del execute
    del engine
    del ii
    del FONTS
    del clock
    del screen
    del event
    del STARTUP_LANG_FILE
    del STARTUP_TEXTS
    del i
    #RAM CLEANUP (START VIA LAUNCHER)
else:
    import os,pygame #DEBUG START
    PATH = "/media/pi/DOKUMENTE 3/HOLO"
    def readfile(name):
        with open(name,"r") as f:
            return(f.read())

os.chdir(PATH)

#INIT
exec(readfile(os.path.join(PATH,"scripts/core/renderFunctions.py"))) #INITIALIZE CUSTOM RENDER FUNCTIONS
SETTINGS = eval(readfile(os.path.join(PATH,"USERS/settings"))) #INITIALIZE SETTINGS
pygame.init()
#pygame.display.set_icon(pygame.image.load('icon.png')) # ICON
screen = pygame.display.set_mode([SETTINGS["width"],SETTINGS["height"]])
clock = pygame.time.Clock()
pygame.display.set_caption("HOLO")
exec(readfile(os.path.join(PATH, "scripts/init/initStaticCore.py")))#STATIC_CORE MOVED TO INITSTATICCORE.PY
exec(readfile(os.path.join(PATH, "scripts/init/initFontsMain.py")))#INITIALIZE GUI AND FONTS
STATIC:dict = {} #Static objects, such as texts, which persist until the given app was closed.
DISPLAY = [SETTINGS["width"],SETTINGS["height"]]
CLOSE = False #LOOP STATE
DISPLAY_BACKGROUND = True
FRAME = 0
SECOND = 0
FPS = 6
APP = "startup"
APP_CODE = ""
APPLAUNCHER = readfile(os.path.join(PATH,"scripts/core/launcher.py"))
exec(APPLAUNCHER)

CHECKBOX = holo.checkbox([0,0])

while not CLOSE:
    
    if DISPLAY_BACKGROUND:
        screen.blit(STATIC_CORE["background"],(0,0))
    else:
        screen.fill([0,0,0])
    screen.blit(CHECKBOX.surface,(0,0))
    clock.tick(FPS)
    pygame.display.flip()
    FRAME += 1
    if FRAME%FPS == 0:
        SECOND += 1
        FRAME = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CLOSE = True
        if event.type == pygame.MOUSEBUTTONUP:
            CHECKBOX.detectClick(list(pygame.mouse.get_pos()))
            
            
pygame.quit()