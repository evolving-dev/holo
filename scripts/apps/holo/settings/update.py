screen.blit(data["assets"]["overlay"], [0,0])

screen.blit(data["assets"]["bottomBar"], [0, int(SETTINGS["height"] * 0.9)])

screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])



if data["screen"] == "menu":
    for i in range(1, 5):
        pygame.draw.line(screen, [128,128,128], [0, i*SETTINGS["height"] // 5], [SETTINGS["width"], i*SETTINGS["height"] // 5])
        screen.blit(data["assets"][data["constants"]["menu_items"][i-1]], [0, (i - 1)*SETTINGS["height"] // 5])
        screen.blit(data["constants"]["menu_headers"][data["constants"]["menu_items"][i-1]], [data["assets"]["general"].get_width(), (i - 0.9)*SETTINGS["height"] // 5])
        screen.blit(data["constants"]["menu_desc"][data["constants"]["menu_items"][i-1]], [data["assets"]["general"].get_width(), (i - 0.35)*SETTINGS["height"] // 5])




if data["screen"] == "general":
    pass






if data["quit"]:
    APP_CRASHED = False
    APP = "home"
    exec(APPLAUNCHER)