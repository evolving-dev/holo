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
    data["components"]["app_selector"].detect_click(data["mousePos"])
    
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
    if data["mousePos"][0] in range(SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2 + data["assets"]["home"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.9), SETTINGS["height"]):
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, int(SETTINGS["height"]*0.9), data["assets"]["home"].get_width(), SETTINGS["height"] // 10 + 1])
        pygame.display.flip()
        data["quit"] = True
    if data["mousePos"][0] in range(0, data["assets"]["add"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.9), SETTINGS["height"]):
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [int(SETTINGS["width"]*0.01), int(SETTINGS["height"]*0.9), data["assets"]["add"].get_width(), SETTINGS["height"] // 10 + 1])
        pygame.display.flip()
        
        i = data["components"]["app_selector"].items[data["components"]["app_selector"].selected]
        
        widget = {"x": data["widgetfile"][i]["x"], "y": data["widgetfile"][i]["y"]} #Temporary variable for the widget data
        
        data["widgetfile"][i]["enabled"] = 1
        
        with open(holo.path("USERS/WIDGETS"), "w") as f:
            f.write(str(data["widgetfile"]))
            f.close()
        data["widgetcode"][i] = readfile(holo.path(data["widgetfile"][i]["update"]))
        data["eventcode"][i] = readfile(holo.path(data["widgetfile"][i]["event"]))
        
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
    

if event.type == pygame.MOUSEBUTTONUP:
    if data["widgetDelete"] != "":
        data["widgetfile"][data["widgetDelete"]]["enabled"] = 0
        del data["var"][data["widgetDelete"]]
        del data["widgetcode"][data["widgetDelete"]]
        del data["eventcode"][data["widgetDelete"]]
        with open(holo.path("USERS/WIDGETS"), "w") as f:
            f.write(str(data["widgetfile"]))
            f.close()
        data["widgetDelete"] = ""