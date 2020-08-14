FPS = 60 if SETTINGS["high_fps"] else 20

data["mouseHold"] = 0 #Number of frames the mouse has been held down

data["clickedObjectName"] = ""

data["assets"] = {
    "overlaySurface": pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 10]),
    "home": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"], "icons/home-"+SETTINGS["theme"]+".png"))).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
    "add": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"], "icons/add-"+SETTINGS["theme"]+".png"))).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
    "delete": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"], "icons/delete-"+SETTINGS["theme"]+".png"))).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),

}
data["assets"]["overlaySurface"].fill([0,0,0] if SETTINGS["theme"] == "dark" else [255,255,255])
data["assets"]["overlaySurface"].set_alpha(70)

#STEP 1: Create WIDGETFILE if it doesn't exist
if not os.path.isfile(holo.path("USERS/WIDGETS")):
    with open(holo.path("USERS/WIDGETS"), "w") as f:
        f.write("{}")
        f.close()
        
#STEP 2: Read and evaluate WIDGETFILE
with open(holo.path("USERS/WIDGETS"), "r") as f:
    data["widgetfile"] = f.read()
    f.close()
    
try:
    data["widgetfile"] = eval(data["widgetfile"])
except:
    APP_CRASHED = True
    holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + SYSTEM_TEXTS["read_error"] + holo.path("USERS/WIDGETS")) #Show an alert of the exception thrown
    APP = "home"
    exec(APPLAUNCHER) #Start the home app if the WIDGETFILE could not be read

if not APP_CRASHED:
   data["widgetcode"]:dict = {} #Update code for all the widgets
   data["eventcode"]:dict = {} #Event code for all the widgets
   data["var"]:dict = {} #Variables for the widgets
   #Load the code for all widgets and execute their init 
   for i in data["widgetfile"].keys():
        if data["widgetfile"][i]["enabled"]:
            data["widgetcode"][i] = readfile(holo.path(data["widgetfile"][i]["update"]))
            data["eventcode"][i] = readfile(holo.path(data["widgetfile"][i]["event"]))
            
            widget = {"x": data["widgetfile"][i]["x"], "y": data["widgetfile"][i]["y"]} #Temporary variable for the widget data
            try:
                exec(readfile(holo.path(data["widgetfile"][i]["init"])))
                data["var"][i] = widget.copy() #Move the data to its designated place
            except Exception as e:
                holo.new_alert(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", i) + str(e))
                #TODO: MEMDUMP DES WIDGETS IN DIE LOGS SCHREIBEN
                del data["widgetcode"][i]
                del data["eventcode"][i]
                data["widgetfile"][i]["enabled"] = 0
                with open(holo.path("USERS/WIDGETS"), "w") as f:
                    f.write(str(data["widgetfile"]))
                    f.close()
           
            del widget #Clean up the temporary data
