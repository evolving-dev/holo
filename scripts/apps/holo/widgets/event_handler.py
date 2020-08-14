data["mousePos"] = list(pygame.mouse.get_pos())

if pygame.mouse.get_pressed()[0] and data["mouseHold"] < 6:
    data["clickedObjectFound"] = False
    try:
        for i in data["var"].keys():
            if (data["mousePos"][0] in range(data["var"][i]["x"], data["var"][i]["x"] + data["var"][i]["size"][0])) and (data["mousePos"][1] in range(data["var"][i]["y"], data["var"][i]["y"] + data["var"][i]["size"][1])):
                data["clickObjectName"] = i
                data["clickedObjectFound"] = True
                break
        if not data["clickedObjectFound"]:
            data["clickObjectName"] = ""
    except:
        pass
    
if event.type == pygame.MOUSEBUTTONUP and data["mouseHold"] < 6:
    if data["clickObjectName"] != "":
        try:
            data["mousePos"] = [data["mousePos"][0] - data["var"][data["clickObjectName"]]["x"], data["mousePos"][1] - data["var"][data["clickObjectName"]]["y"]]
            #Make mousePos relative to the widget
            
            exec(data["eventcode"][data["clickObjectName"]])
        except Exception as e:
            holo.new_alert(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", data["keycache"]) + str(e))
            #TODO: MEMDUMP DES WIDGETS IN DIE LOGS SCHREIBEN
            del widget
            del data["var"][data["keycache"]]
            del data["widgetcode"][data["keycache"]]
            del data["eventcode"][data["keycache"]]
            data["widgetfile"][data["keycache"]]["enabled"] = 0
            with open(holo.path("USERS/WIDGETS"), "w") as f:
                f.write(str(data["widgetfile"]))
                f.close()
