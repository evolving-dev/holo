for i in range(len(data["widgetcode"])):
    try:
        data["keycache"] = list(data["widgetcode"].keys())[i]
        widget = data["var"][data["keycache"]].copy()
        exec(data["widgetcode"][data["keycache"]])
        data["var"][data["keycache"]] = widget.copy()
        
        screen.blit(widget["surface"], [widget["x"], widget["y"]])
        
        del widget
    except Exception as e:
        holo.new_alert(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", data["keycache"]) + str(e))
        #TODO: MEMDUMP DES WIGETS IN DIE LOGS SCHREIBEN
        del widget
        del data["var"][data["keycache"]]
        del data["widgetcode"][data["keycache"]]