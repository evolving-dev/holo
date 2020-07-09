del ALERTS
ALERTS:list = [] #RESET ALERTS

del data
data:dict = {} #RESET APP DATA

del LOADERS
LOADERS:list = [] #RESET LOADERS

FRAME,SECOND = 0,0 #RESET TIMERS
FPS = 6 #RESET FPS

if APP == "startup":
    
    #Code to be executed at startup
    APP = "home"
    exec(APPLAUNCHER)
    
else:
    
    try:
        
        APP_CODE = readfile(join(PATH,join(PATHFILE[APP]['scripts'],'update.py'))) #Read the code that runs every frame
        
        exec(readfile(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.
        
    except Exception as e:
        
        if APP != "home": #If a third-party app crashes, return to the home screen
            
            holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
            APP = "home"
            exec(APPLAUNCHER) #Start the home app
            
        else: #If the HOME app crashes, exit
            print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: ",e)
            pygame.quit()
            sys.exit()
