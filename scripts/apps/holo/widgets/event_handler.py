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
    
