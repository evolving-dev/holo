del ALERTS
ALERTS:list = [] #DELETE RENDER PIPELINE
if APP == "startup":
    APP = "home"
    exec(APPLAUNCHER)
else:
    try:
        exec(readfile(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.
    except Exception as e:
        pass
        holo.new_alert(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e))