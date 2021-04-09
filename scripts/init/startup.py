os.chdir(PATH)

exec(holo_io.file.read("scripts/init/cleanup_launcher.py"))#Clean up data the launcher left behind

exec(holo_io.file.read("scripts/core/holo_logging.py")) #Initialize logging functionality

SETTINGS = eval(holo_io.file.read("storage/system/settings")) #INITIALIZE SETTINGS

pygame.init()

exec(holo_io.file.read("scripts/init/fonts_main.py"))#INITIALIZE FONTS

try:
    PATHFILE = eval(holo_io.file.read("storage/system/path")) #APP PATH FILE
except:
    try:
        PATHFILE_ERROR = holo_io.file.read("storage/system/path")
        holo_logging.log_critical("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: "+ str(PATHFILE_ERROR), system=True)
    except:
        holo_logging.log_critical("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO_STARTUP: PATHFILE_READ_ERROR: NOT_FOUND.", system=True)
    pygame.quit()
    sys.exit()

SYSTEM_TEXTS = eval(holo_io.file.read("assets/text/main_"+SETTINGS["lang"]))


#Init pygame window
if SETTINGS["init_sound"]:
    pygame.mixer.pre_init(44100, channels=2)
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode([SETTINGS["width"],SETTINGS["height"]])
clock = pygame.time.Clock()
pygame.display.set_caption("HOLO")
PLATFORM = "HOLO"
AUTOSTART = eval(holo_io.file.read("storage/system/autostart"))
LOADING = pygame.image.load("assets/images/icons/startup.png").convert_alpha()
screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_1"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()


MAIN_LOOP = holo_io.file.read("scripts/core/main_loop.py")
exec(holo_io.file.read("scripts/core/text_wrapper.py")) #INITIALIZE TEXT WRAPPER
exec(holo_io.file.read("scripts/core/pass_types.py"))
exec(holo_io.file.read("scripts/core/holo_gui.py"))
exec(holo_io.file.read("scripts/core/holo_color.py"))
exec(holo_io.file.read("scripts/core/holo_prefabs.py"))
exec(holo_io.file.read("scripts/core/holo_keyboard.py"))
exec(holo_io.file.read("scripts/core/holo_launcher.py"))


screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_2"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()

exec(holo_io.file.read("scripts/init/init_static_objects.py"))#INITIALIZE STATIC OBJECTS

screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_3"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()
#GLOBAL VARIABLES (ALL CAPS VARIABLES)
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
APPLAUNCHER = holo_io.file.read("scripts/core/launcher.py")
KEYBOARD = holo_keyboard.Keyboard()
PROCESS_HANDLER = holo_io.file.read("scripts/core/process_handler.py")


screen.fill([0,0,0])
screen.blit(LOADING,(0,0))
screen.blit(FONTS["p-sans-serif-small"].render(SYSTEM_TEXTS["startup_4"], True, [150,150,150]), [0, SETTINGS["height"] - SETTINGS["width"]//30])
pygame.display.flip()

del LOADING
exec(APPLAUNCHER) #LAUNCH HOME APP

exec(MAIN_LOOP)
