screen.blit(data["assets"]["overlay"], [0,0])

screen.blit(data["assets"]["bottomBar"], [0, int(SETTINGS["height"] * 0.9)])

screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])

if data["screen"] == "menu":
    for i in range(5):
        pygame.draw.line(screen, [128,128,128], [0, (i+1)*SETTINGS["height"] // 5], [SETTINGS["width"], (i+1)*SETTINGS["height"] // 5])













if data["quit"]:
    APP_CRASHED = False
    APP = "home"
    exec(APPLAUNCHER)