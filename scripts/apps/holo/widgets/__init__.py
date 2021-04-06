FPS = 20

data["mouseHold"] = 0 #Number of frames the mouse has been held down

data["widgetDelete"] = ""
data["clickedObjectName"] = ""
data["clickObjectName"] = ""
data["quit"] = False

data["assets"] = {
    "overlaySurface": pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 10]),
    "home": holo_assets.buttons.home,
    "add": pygame.image.fromstring(Image.open(holo_io.path.to_absolute(join(APP_PATH["assets"], "icons/add-"+SETTINGS["theme"]+".png"))).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
    "delete": pygame.image.fromstring(Image.open(holo_io.path.to_absolute(join(APP_PATH["assets"], "icons/delete-"+SETTINGS["theme"]+".png"))).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),

}
data["assets"]["overlaySurface"].fill(holo_color.system.theme_color)
data["assets"]["overlaySurface"].set_alpha(70)

#STEP 1: Create WIDGETFILE if it doesn't exist
if not os.path.isfile(holo_io.path.to_absolute("USERS/WIDGETS")):
    with open(holo_io.path.to_absolute("USERS/WIDGETS"), "w") as f:
        f.write("{}")
        f.close()
        
#STEP 2: Read and evaluate WIDGETFILE
with open(holo_io.path.to_absolute("USERS/WIDGETS"), "r") as f:
    data["widgetfile"] = f.read()
    f.close()
    
try:
    data["widgetfile"] = eval(data["widgetfile"])
except:
    APP_CRASHED = True
    holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + SYSTEM_TEXTS["read_error"] + holo_io.path.to_absolute("USERS/WIDGETS")) #Show an alert of the exception thrown
    APP = "home"
    exec(APPLAUNCHER) #Start the home app if the WIDGETFILE could not be read

if not APP_CRASHED:
   data["widgetcode"]:dict = {} #Update code for all the widgets
   data["eventcode"]:dict = {} #Event code for all the widgets
   data["var"]:dict = {} #Variables for the widgets
   #Load the code for all widgets and execute their init 
   for i in data["widgetfile"].keys():
        if data["widgetfile"][i]["enabled"]:
            data["widgetcode"][i] = holo_io.file.read(holo_io.path.to_absolute(data["widgetfile"][i]["update"]))
            data["eventcode"][i] = holo_io.file.read(holo_io.path.to_absolute(data["widgetfile"][i]["event"]))
            
            widget = {"x": data["widgetfile"][i]["x"], "y": data["widgetfile"][i]["y"]} #Temporary variable for the widget data
            try:
                exec(holo_io.file.read(holo_io.path.to_absolute(data["widgetfile"][i]["init"])))
                data["var"][i] = widget.copy() #Move the data to its designated place
            except Exception as e:
                holo.new_alert(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", i) + str(e))
                #TODO: MEMDUMP DES WIDGETS IN DIE LOGS SCHREIBEN
                del data["widgetcode"][i]
                del data["eventcode"][i]
                data["widgetfile"][i]["enabled"] = 0
                with open(holo_io.path.to_absolute("USERS/WIDGETS"), "w") as f:
                    f.write(str(data["widgetfile"]))
                    f.close()
           
            del widget #Clean up the temporary data

#STEP 3: Load visual components

data["name_list"] = []
data["id_list"] = []
for i in data["widgetfile"]:
    if "name_" + SETTINGS["lang"] in data["widgetfile"][i]:
        data["name_list"] += [data["widgetfile"][i]["name_" + SETTINGS["lang"]]]
    elif "name" in data["widgetfile"][i]:
        data["name_list"] += [data["widgetfile"][i]["name"]]
    else:
        data["name_list"] += [i]
    data["id_list"] += [i]

data["components"] = {
    "app_selector": holo_prefabs.list_selector(pos=[int(data["assets"]["add"].get_width() * 1.5), ((SETTINGS["height"] - SETTINGS["height"] // 15) + (SETTINGS["height"] - data["assets"]["overlaySurface"].get_height())) // 2], items=data["id_list"], display_text=data["name_list"])
}

