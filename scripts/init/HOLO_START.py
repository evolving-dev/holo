import sys
import PIL
from PIL import Image,ImageDraw,GifImagePlugin
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
    import os,pygame,time,math #DEBUG START
    from os.path import join
    PATH = "/media/pi/DOKUMENTE 3/HOLO"
    def readfile(name):
        with open(name,"r") as f:
            return(f.read())

os.chdir(PATH)

#INIT
PATHFILE = eval(readfile(join(PATH,"data/PATH"))) #APP PATH FILE
exec(readfile(join(PATH,"scripts/core/renderFunctions.py"))) #INITIALIZE CUSTOM RENDER FUNCTIONS
exec(readfile(join(PATH,"scripts/core/text_wrapper.py"))) #INITIALIZE TEXT WRAPPER
SETTINGS = eval(readfile(join(PATH,"USERS/settings"))) #INITIALIZE SETTINGS
SYSTEM_TEXTS = eval(readfile(join(PATH, "assets/text/main_"+SETTINGS["lang"])))


#Init pygame window
pygame.init()
#pygame.display.set_icon(pygame.image.load('icon.png')) # ICON
screen = pygame.display.set_mode([SETTINGS["width"],SETTINGS["height"]])
clock = pygame.time.Clock()
pygame.display.set_caption("HOLO")
LOADING = pygame.image.load(join(PATH,"assets/images/icons/startup.png")).convert_alpha()
screen.blit(LOADING,(0,0))
pygame.display.flip()
del LOADING


exec(readfile(join(PATH, "scripts/init/initFontsMain.py")))#INITIALIZE FONTS
exec(readfile(join(PATH, "scripts/init/initStaticCore.py")))#INITIALIZE STATIC OBJECTS


#GLOBAL VARIABLES (ALL CAPS VARIABLES)
STATIC:dict = {} #Static objects, such as texts, which persist until the given app was closed.
DISPLAY = [SETTINGS["width"],SETTINGS["height"]]
CLOSE = False #LOOP STATE
DISPLAY_BACKGROUND = True
FRAME = 0
SECOND = 0
FPS = 6
APP = "startup"
data:dict = {}
TIMEOUT = SETTINGS["timeout"]
APP_CODE = ""
ALERTS:list = []
LOADERS:list = []
APPLAUNCHER = readfile(join(PATH,"scripts/core/launcher.py"))
exec(APPLAUNCHER)

holo.new_alert("testalert")

CHECKBOX = holo.checkbox([0,0])

holo.new_loader()

while not CLOSE:
    if TIMEOUT > 0: #If screen timeout not reached
        if DISPLAY_BACKGROUND:
            screen.blit(STATIC_CORE["background"],(0,0))
        else:
            screen.fill([0,0,0])
        
        #DEBUG DRAWINGS (WILL BE REMOVED SOON)
        screen.blit(CHECKBOX.surface,(0,0))
        
        #END DEBUG
        
        
        #ALERT UPDATE ROUTINE
        for index,alert in enumerate(ALERTS):
            if not alert.visible:
                del ALERTS[index]
        for alert in ALERTS:
            screen.blit(alert.surface,(SETTINGS["width"] // 2 - alert.width // 2, SETTINGS["height"] // 2 - alert.height // 2))
        ###
        
        #LOADER UPDATE ROUTINE
        for index,loader in enumerate(LOADERS):
            if loader.finished:
                del LOADERS[index]
        for loader in LOADERS:
            if not (FRAME % math.ceil(FPS / 6)):
                loader.update()
            screen.blit(loader.surface,tuple(loader.pos))
        
        clock.tick(FPS)
        pygame.display.flip()
        FRAME += 1
        if FRAME%FPS == 0:
            SECOND += 1
            FRAME = 0
            if TIMEOUT:
                TIMEOUT -= 1
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLOSE = True
            else:
                TIMEOUT = SETTINGS["timeout"]
            if event.type == pygame.MOUSEBUTTONUP:
                if len(ALERTS) >= 1:
                    ALERTS[-1:][0].detectClick(list(pygame.mouse.get_pos())) #Only detect most recent alert
                CHECKBOX.detectClick(list(pygame.mouse.get_pos()))
                
        
        
        
        
        
        
    else: #If screen timeout reached
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    CLOSE = True
                    TIMEOUT = SETTINGS["timeout"] #End timeout loop either through closing or clicking/tapping
                if event.type == pygame.MOUSEBUTTONUP:
                    TIMEOUT = SETTINGS["timeout"]
            if TIMEOUT > 0:
                break
            else:
                clock.tick(1)
                screen.fill([0,0,0])
                pygame.display.flip()
            
            
pygame.quit()