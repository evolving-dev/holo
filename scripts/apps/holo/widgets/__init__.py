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


for i in data["widgetfile"].keys():
    pass

APP_CRASHED = False
APP = "home"
exec(APPLAUNCHER)