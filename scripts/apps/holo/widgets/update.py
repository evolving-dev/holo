if pygame.mouse.get_pressed()[0]:
    data["mouseHold"] += 1
else:
    data["mouseHold"] = 0

for i in range(len(data["widgetcode"])):
    try:
        data["keycache"] = list(data["widgetcode"].keys())[i]
        widget = data["var"][data["keycache"]].copy()
        exec(data["widgetcode"][data["keycache"]])
        data["var"][data["keycache"]] = widget.copy()

        screen.blit(widget["surface"], [widget["x"], widget["y"]])
    except Exception as e:
        holo_prefabs.alert.new(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", data["keycache"]) + str(e))
        #TODO: MEMDUMP DES WIDGETS IN DIE LOGS SCHREIBEN
        del data["var"][data["keycache"]]
        del data["widgetcode"][data["keycache"]]
        del data["eventcode"][data["keycache"]]
        data["widgetfile"][data["keycache"]]["enabled"] = 0
        with open(holo_io.path.to_absolute("storage/system/widgets"), "w") as f:
            f.write(str(data["widgetfile"]))
            f.close()

try:
    if pygame.mouse.get_pressed()[0] and data["mouseHold"] >= 6:
        data["mousePos"] = list(pygame.mouse.get_pos())
        if data["mouseHold"] == 6:
            for i in data["var"].keys():
                if (data["mousePos"][0] in range(data["var"][i]["x"], data["var"][i]["x"] + data["var"][i]["size"][0])) and (data["mousePos"][1] in range(data["var"][i]["y"], data["var"][i]["y"] + data["var"][i]["size"][1])):
                    data["moveObjectName"] = i
                    break
        else:
            data["var"][data["moveObjectName"]]["x"] = data["mousePos"][0] - (data["var"][data["moveObjectName"]]["size"][0] // 2)
            data["var"][data["moveObjectName"]]["y"] = data["mousePos"][1] - (data["var"][data["moveObjectName"]]["size"][1] // 2)

    else:
        data["moveObjectName"] = ""
except:
    pass

data["widgetDelete"] = ""

for i in data["var"]:
    if data["var"][i]["y"] + int(data["var"][i]["size"][1] * 0.7) >= int(SETTINGS["height"] * 0.9) and data["var"][i]["x"] >= SETTINGS["width"] // 2:
        data["widgetDelete"] = i
if data["widgetDelete"] != "":
    data["assets"]["overlaySurface"].fill([255,0,0])
else:
    data["assets"]["overlaySurface"].fill(holo_color.system.theme_color)


#OVERLAY
screen.blit(data["assets"]["overlaySurface"], [0, SETTINGS["height"] - data["assets"]["overlaySurface"].get_height()])
screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
screen.blit(data["assets"]["add"], [int(SETTINGS["width"]*0.01), SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
screen.blit(data["assets"]["delete"], [SETTINGS["width"] - data["assets"]["home"].get_width(), SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
screen.blit(data["components"]["app_selector"].surface, [int(data["assets"]["add"].get_width() * 1.5), ((SETTINGS["height"] - SETTINGS["height"] // 15) + (SETTINGS["height"] - data["assets"]["overlaySurface"].get_height())) // 2])

if data["quit"]:

    for i in data["var"].keys():
        data["widgetfile"][i]["x"] = data["var"][i]["x"]
        data["widgetfile"][i]["y"] = data["var"][i]["y"]

    with open(holo_io.path.to_absolute("storage/system/widgets"), "r") as f:
        data["widgetfile_OLD"] = f.read()
        f.close()

    try:
        data["widgetfile_OLD"] = eval(data["widgetfile_OLD"])
    except:
        holo_prefabs.alert.new(APP + SYSTEM_TEXTS["crash"] + "\n" + SYSTEM_TEXTS["read_error"] + holo_io.path.to_absolute("storage/system/widgets")) #Show an alert of the exception thrown
        holo_launcher.to_home(crash=True) #Start the home app if the WIDGETFILE could not be read

    if data["widgetfile"] != data["widgetfile_OLD"]:
        with open(holo_io.path.to_absolute("storage/system/widgets"), "w") as f:
            f.write(str(data["widgetfile"]))
            f.close()

    holo_launcher.to_home(crash=True)
