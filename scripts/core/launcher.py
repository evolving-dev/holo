global ALERTS
global SETTINGS
global data
global app
global code
global LOADERS
global APP_PATH
global FRAME
global SECOND
global FPS
global KEYBOARD
global APPLAUNCHER
global PRIORITY_MODE_ACTIVE
global APP_CODE
global APP_EVENTHANDLER
global PATH
global PATHFILE

if not APP_CRASHED:
    del ALERTS
    ALERTS = [] #RESET ALERTS ONLY WHEN AN APP EXITED NORMALLY. (keep error report)

if SETTINGS["init_sound"]:
    pygame.mixer.stop()

if "data" in globals():
    del data
if "app" in globals():
    del app
if "code" in globals():
    del code

data = {} #RESET APP DATA

holo_screen.objects = {} #Reset objects

del LOADERS
LOADERS = [] #RESET LOADERS

del APP_PATH
APP_PATH = {}

FRAME,SECOND = 0,0 #RESET TIMERS
FPS = 6 #RESET FPS

holo_gui.background.show()

KEYBOARD.reset()
APP_CRASHED = False

if APP == "startup":

    #Code to be executed at startup
    APP = SETTINGS["default_home"]
    exec(APPLAUNCHER)

else:

    PRIORITY_MODE_ACTIVE = PATHFILE[APP].get("priority", 0)

    try:

        APP_PATH = PATHFILE[APP].copy()
        APP_CODE = holo_io.file.read(join(PATH,join(PATHFILE[APP]['scripts'],'update.py'))) #Read the code that runs every frame
        APP_EVENTHANDLER = holo_io.file.read(join(PATH,join(PATHFILE[APP]['scripts'],'event_handler.py'))) #Read the code that handles events

        exec(holo_io.file.read(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.

    except Exception as e:

        if APP != "home": #If a third-party app crashes, return to the home screen

            APP_CRASHED = True
            holo_prefabs.alert.new(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
            APP = "home"
            exec(APPLAUNCHER) #Start the home app

        else: #If the HOME app crashes, exit
            print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO HOME: ",e)
            pygame.quit()
            sys.exit()
