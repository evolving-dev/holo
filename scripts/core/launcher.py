del ALERTS
ALERTS:list = [] #RESET RENDER PIPELINE
del data
data:dict = {} #RESET APP DATA
FPS = 6 #RESET FPS
if APP == "startup":
    APP = "home"
    exec(APPLAUNCHER)
else:
    try:
        exec(readfile(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.
    except Exception as e:
        if APP != "home": #If a third-party app crashes, return to the home screen
            holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e))
            APP = "home"
            exec(APPLAUNCHER)
        else: #If the HOME app crashes, exit
            print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: ",e)
            pygame.quit()
            sys.exit()
