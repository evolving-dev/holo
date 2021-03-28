os.chdir(PATH)

exec(holo_io.file.read("scripts/init/cleanup_launcher.py"))#Clean up data the launcher left behind

exec(holo_io.file.read("scripts/core/holo_logging.py")) #Initialize logging functionality

SETTINGS = eval(holo_io.file.read(join(PATH,"USERS/settings"))) #INITIALIZE SETTINGS

pygame.init()

exec(holo_io.file.read(join(PATH, "scripts/init/fonts_main.py")))#INITIALIZE FONTS

try:
    PATHFILE = eval(holo_io.file.read(join(PATH,"data/PATH"))) #APP PATH FILE
except:
    try:
        PATHFILE_ERROR = holo_io.file.read(join(PATH,"data/PATH"))
        holo_logging.log_critical("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: "+ str(PATHFILE_ERROR), system=True)
    except:
        holo_logging.log_critical("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: NOT_FOUND.", system=True)
    pygame.quit()
    sys.exit()

SYSTEM_TEXTS = eval(holo_io.file.read(join(PATH, "assets/text/main_"+SETTINGS["lang"])))


#Init pygame window
if SETTINGS["init_sound"]:
    pygame.mixer.pre_init(44100, channels=2)
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode([SETTINGS["width"],SETTINGS["height"]])
clock = pygame.time.Clock()
pygame.display.set_caption("HOLO")
PLATFORM = "HOLO"
AUTOSTART = eval(holo_io.file.read(holo_io.path.to_absolute("data/AUTOSTART")))
LOADING = pygame.image.load(join(PATH,"assets/images/icons/startup.png")).convert_alpha()
screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_1"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()


MAIN_LOOP = holo_io.file.read(join(PATH, "scripts/core/main_loop.py"))
exec(holo_io.file.read(join(PATH, "scripts/core/renderFunctions.py"))) #INITIALIZE LEGACY CUSTOM RENDER FUNCTIONS (WILL GET REMOVED SOON)
exec(holo_io.file.read(join(PATH, "scripts/core/text_wrapper.py"))) #INITIALIZE TEXT WRAPPER
exec(holo_io.file.read(holo_io.path.to_absolute("scripts/core/pass_types.py")))
exec(holo_io.file.read(holo_io.path.to_absolute("scripts/core/holo_gui.py")))
exec(holo_io.file.read(holo_io.path.to_absolute("scripts/core/holo_keyboard.py")))

screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_2"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()

exec(holo_io.file.read(join(PATH, "scripts/init/initStaticCore.py")))#INITIALIZE STATIC OBJECTS

screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_3"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()
#GLOBAL VARIABLES (ALL CAPS VARIABLES)
STATIC:dict = {} #Static objects, such as texts, which persist until the given app was closed.
DISPLAY = [SETTINGS["width"],SETTINGS["height"]]
CLOSE = False #LOOP STATE
DISPLAY_BACKGROUND = True
ALERT_CLICKED = False
FRAME = 0
SECOND = 0
FPS = 6
APP = "startup"
PRIORITY_MODE_ACTIVE = 0
APP_CRASHED = False
TIMEOUT = SETTINGS["timeout"]
APP_CODE = ""
APP_EVENTHANDLER = ""
BLOCK_PROCESS_HANDLER = 0
APP_PATH:dict = {}
ALERTS:list = []
LOADERS:list = []
APPLAUNCHER = holo_io.file.read(join(PATH,"scripts/core/launcher.py"))
KEYBOARD = holo_keyboard.Keyboard()
PROCESS_HANDLER = holo_io.file.read(join(PATH,"scripts/core/process_handler.py"))


screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_4"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()

del LOADING
exec(APPLAUNCHER) #LAUNCH HOME APP

exec(MAIN_LOOP)
