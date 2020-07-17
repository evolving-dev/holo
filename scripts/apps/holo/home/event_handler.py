if event.type == pygame.MOUSEBUTTONUP:
    mouse_pos = list(pygame.mouse.get_pos())
    if not abs(data["cache"]["mouseposcache"] - list(pygame.mouse.get_pos())[0]) >= SETTINGS["width"] // 10:
        for i in data["apps"]["areas"].keys():
            if data["page"] == data["apps"]["areas"][i][0]: #When the app found is on the currently active page
                if mouse_pos[0] in range(data["apps"]["areas"][i][1][0],data["apps"]["areas"][i][2][0]) and mouse_pos[1] in range(data["apps"]["areas"][i][1][1], data["apps"]["areas"][i][2][1]):
                    print(i)
                    break
    else:
        if data["cache"]["mouseposcache"] - list(pygame.mouse.get_pos())[0] < 0:
            data["page"] -= 1 if data["page"] > 0 else 0
        else:
            data["page"] += 1 if data["page"] + 1 <= len(data["surfaces"]) - 1 else 0