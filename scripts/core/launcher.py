if not APP_CRASHED:
    del ALERTS
    ALERTS:list = [] #RESET ALERTS ONLY WHEN AN APP CRASHED. (keep error report)

pygame.mixer.stop()

del data
data:dict = {} #RESET APP DATA

del LOADERS
LOADERS:list = [] #RESET LOADERS

del APP_PATH
APP_PATH:dict = {}

FRAME,SECOND = 0,0 #RESET TIMERS
FPS = 6 #RESET FPS

KEYBOARD.reset()
APP_CRASHED = False

if APP == "startup":
    
    #Code to be executed at startup
    APP = "home"
    exec(APPLAUNCHER)
    
else:
    
    try:
        
        APP_PATH = PATHFILE[APP].copy()
        APP_CODE = readfile(join(PATH,join(PATHFILE[APP]['scripts'],'update.py'))) #Read the code that runs every frame
        APP_EVENTHANDLER = readfile(join(PATH,join(PATHFILE[APP]['scripts'],'event_handler.py'))) #Read the code that handles events
        
        exec(readfile(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.
        
    except Exception as e:
        
        if APP != "home": #If a third-party app crashes, return to the home screen
            
            APP_CRASHED = True
            holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
            APP = "home"
            exec(APPLAUNCHER) #Start the home app
            
        else: #If the HOME app crashes, exit
            print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO HOME: ",e)
            pygame.quit()
            sys.exit()
