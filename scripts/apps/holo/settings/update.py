screen.blit(data["assets"]["overlay"], [0,0])
screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])















if data["quit"]:
    APP_CRASHED = False
    APP = "home"
    exec(APPLAUNCHER)