import sys
import PIL
from PIL import Image,ImageDraw,GifImagePlugin

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
#RAM CLEANUP

os.chdir(PATH)

#INIT
SETTINGS = eval(readfile(join(PATH,"USERS/settings"))) #INITIALIZE SETTINGS

try:
    PATHFILE = eval(readfile(join(PATH,"data/PATH"))) #APP PATH FILE
except:
    try:
        PATHFILE_ERROR = readfile(join(PATH,"data/PATH"))
        print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: ", PATHFILE_ERROR)
    except:
        print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: NOT_READ. This error might likely be caused by third-party apps.")
exec(readfile(join(PATH,"scripts/core/renderFunctions.py"))) #INITIALIZE CUSTOM RENDER FUNCTIONS
exec(readfile(join(PATH,"scripts/core/text_wrapper.py"))) #INITIALIZE TEXT WRAPPER
SYSTEM_TEXTS = eval(readfile(join(PATH, "assets/text/main_"+SETTINGS["lang"])))


#Init pygame window
if SETTINGS["init_sound"]:
    pygame.mixer.pre_init(44100, channels=2)
pygame.init()
pygame.display.set_icon(ICON)
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
alertcache = False
FRAME = 0
SECOND = 0
FPS = 6
APP = "startup"
APP_CRASHED = False
data:dict = {}
TIMEOUT = SETTINGS["timeout"]
APP_CODE = ""
APP_EVENTHANDLER = ""
APP_PATH:dict = {}
ALERTS:list = []
LOADERS:list = []
APPLAUNCHER = readfile(join(PATH,"scripts/core/launcher.py"))
KEYBOARD = holo.keyboard()
exec(APPLAUNCHER) #LAUNCH HOME APP



while not CLOSE:
    if TIMEOUT > 0: #If screen timeout not reached
        if DISPLAY_BACKGROUND:
            screen.blit(STATIC_CORE["background"],(0,0))
        else:
            screen.fill([0,0,0])
        
        try:
            exec(APP_CODE) #Run the updatefile of the current app
        except Exception as e: #CRASH PROTECTION
            APP_CRASHED = True
            holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
            APP = "home"
            exec(APPLAUNCHER)
        
        #KEYBOARD UPDATE ROUTINE
        
        if KEYBOARD.visible:
            screen.blit(KEYBOARD.get_surface(),(0, SETTINGS["height"] // 2))
        
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
                    alertcache = ALERTS[-1:][0].detectClick(list(pygame.mouse.get_pos())) #Only detect most recent alert
                else:
                    alertcache = False
                if KEYBOARD.visible and list(pygame.mouse.get_pos())[1] >= SETTINGS["height"] // 2:
                    KEYBOARD.update(list(pygame.mouse.get_pos()))
            
            if not event.type == pygame.MOUSEMOTION and not alertcache: #Mousemotion is ignored for touchscreen displays. Apps need to detect mouse motion themselves
                
                try:
                    exec(APP_EVENTHANDLER) #Pass the event onto the currently active app
                except Exception as e:
                    if APP != "home":
                        APP_CRASHED = True
                        holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
                        APP = "home"
                        exec(APPLAUNCHER) #Start the home app
            
                    else: #If the HOME app crashes, exit
                        print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO HOME: ",e)
                        pygame.quit()
                        sys.exit()
        
        
        
        
        
        
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