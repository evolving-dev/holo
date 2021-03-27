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
exec(readfile(join(PATH, "scripts/core/renderFunctions.py"))) #INITIALIZE CUSTOM RENDER FUNCTIONS
exec(readfile(join(PATH, "scripts/core/text_wrapper.py"))) #INITIALIZE TEXT WRAPPER
exec(readfile(join(PATH, "scripts/core/holo_io.py"))) #Initialize I/O Functions
SYSTEM_TEXTS = eval(readfile(join(PATH, "assets/text/main_"+SETTINGS["lang"])))


#Init pygame window
if SETTINGS["init_sound"]:
    pygame.mixer.pre_init(44100, channels=2)
pygame.init()
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode([SETTINGS["width"],SETTINGS["height"]])
clock = pygame.time.Clock()
pygame.display.set_caption("HOLO")
AUTOSTART = eval(readfile(holo_io.path.to_absolute("data/AUTOSTART")))
LOADING = pygame.image.load(join(PATH,"assets/images/icons/startup.png")).convert_alpha()
screen.blit(LOADING,(0,0))
pygame.display.flip()
del LOADING

MAIN_LOOP = readfile(join(PATH, "scripts/core/main_loop.py"))

exec(readfile(join(PATH, "scripts/init/initFontsMain.py")))#INITIALIZE FONTS

exec(readfile(holo_io.path.to_absolute("scripts/core/pass_types.py")))
#exec(readfile(holo_io.path.to_absolute("scripts/core/holo_io.py"))) #MOVED TO TOP TEMPORARILY
exec(readfile(holo_io.path.to_absolute("scripts/core/holo_gui.py")))
exec(readfile(holo_io.path.to_absolute("scripts/core/holo_keyboard.py")))


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
PRIORITY_MODE_ACTIVE = 0
APP_CRASHED = False
data:dict = {}
TIMEOUT = SETTINGS["timeout"]
APP_CODE = ""
APP_EVENTHANDLER = ""
BLOCK_PROCESS_HANDLER = 0
APP_PATH:dict = {}
ALERTS:list = []
LOADERS:list = []
APPLAUNCHER = readfile(join(PATH,"scripts/core/launcher.py"))
KEYBOARD = holo_keyboard.Keyboard()
PROCESS_HANDLER = readfile(join(PATH,"scripts/core/process_handler.py"))


exec(APPLAUNCHER) #LAUNCH HOME APP

exec(MAIN_LOOP)
