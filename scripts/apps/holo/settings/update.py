screen.blit(data["assets"]["overlay"], [0,0]) #Render the overlay

#Bottom bar and home button
screen.blit(data["assets"]["bar_background"], [0, int(SETTINGS["height"] * 0.9)])
screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])



if data["screen"] == "menu":
    for i in range(1, 5):
        #Render main menu
        pygame.draw.line(screen, [128,128,128], [0, i*SETTINGS["height"] // 5], [SETTINGS["width"], i*SETTINGS["height"] // 5]) #Splitting lines
        screen.blit(data["assets"][data["constants"]["menu_items"][i-1]], [0, (i - 1)*SETTINGS["height"] // 5]) #Icon
        screen.blit(data["constants"]["menu_headers"][data["constants"]["menu_items"][i-1]], [data["assets"]["general"].get_width(), (i - 0.9)*SETTINGS["height"] // 5]) #Header
        screen.blit(data["constants"]["menu_desc"][data["constants"]["menu_items"][i-1]], [data["assets"]["general"].get_width(), (i - 0.35)*SETTINGS["height"] // 5]) #Description
else:
    #Top bar to go back to the main menu
    screen.blit(data["assets"]["bar_background"], [0,0])
    screen.blit(STATIC_CORE["back"], [0,0])
    screen.blit(data["constants"]["menu_headers"][data["screen"]], [STATIC_CORE["back"].get_width(), SETTINGS["height"] // 20 - (data["constants"]["menu_headers"][data["screen"]].get_height() // 2)])

if data["screen"] == "general":
    #General settings
    screen.blit(data["general"]["language"], [SETTINGS["width"] // 10, data["general"]["languageSelector"].pos[1]])
    screen.blit(data["general"]["languageSelector"].surface, data["general"]["languageSelector"].pos)
    screen.blit(data["general"]["keyboard_layout"], [SETTINGS["width"] // 10, data["general"]["layoutSelector"].pos[1]])
    screen.blit(data["general"]["layoutSelector"].surface, data["general"]["layoutSelector"].pos)






if data["quit"]:
    APP_CRASHED = False
    APP = "home"
    exec(APPLAUNCHER)