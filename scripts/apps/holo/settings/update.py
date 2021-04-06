screen.blit(holo_assets.overlays.main, [0,0]) #Render the overlay

#Bottom bar and home button
if not KEYBOARD.visible:
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
    screen.blit(holo_assets.buttons.back, [0,0])
    screen.blit(data["constants"]["menu_headers"][data["screen"]], [holo_assets.buttons.back.get_width(), SETTINGS["height"] // 20 - (data["constants"]["menu_headers"][data["screen"]].get_height() // 2)])

if data["screen"] == "general":
    #General settings
    screen.blit(data["general"]["language"], [SETTINGS["width"] // 10, data["general"]["languageSelector"].pos[1]])
    screen.blit(data["general"]["languageSelector"].surface, data["general"]["languageSelector"].pos)
    screen.blit(data["general"]["sound_checkbox"].surface, data["general"]["sound_checkbox"].pos)
    screen.blit(data["general"]["keyboard_layout"], [SETTINGS["width"] // 10, data["general"]["layoutSelector"].pos[1]])
    screen.blit(data["general"]["layoutSelector"].surface, data["general"]["layoutSelector"].pos)
    screen.blit(data["general"]["date_format"], [SETTINGS["width"] // 10, int(SETTINGS["height"]*0.35)])
    screen.blit(data["general"]["time_format"], [SETTINGS["width"] // 10, int(SETTINGS["height"]*0.45)])
    screen.blit(data["general"]["autostart"], [SETTINGS["width"] // 10, int(SETTINGS["height"]*0.55)])
    screen.blit(data["general"]["use_sound"], [SETTINGS["width"] // 10, int(SETTINGS["height"]*0.65)])
    screen.blit(data["assets"]["button_change"], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.35)])
    screen.blit(data["assets"]["button_change"], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.45)])
    screen.blit(data["assets"]["button_change"], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.55)])

if data["screen"] in ["time_format", "date_format"]:
    while len(KEYBOARD.text) > 32:
        KEYBOARD.text = KEYBOARD.text[:-1]

    screen.blit(data["assets"]["textbox"], [SETTINGS["width"] // 10,int((SETTINGS["height"] // 10)*1.1)])
    data["input_text"] = FONTS["p-sans-serif"].render(KEYBOARD.text, True, holo_color.system.text_color)
    screen.blit(data["input_text"], [SETTINGS["width"] // 10,int((SETTINGS["height"] // 10)*1.1) + (data["assets"]["textbox"].get_height() // 2 - data["input_text"].get_height() // 2)])
    screen.blit(data["time_surface"] if data["screen"] == "time_format" else data["date_surface"], [0,0])

    try:
        data["time_date_example"] = SYSTEM_TEXTS["settings"]["general"]["example"] + time.strftime(KEYBOARD.text)
    except:
        data["time_date_example"] = SYSTEM_TEXTS["settings"]["general"]["example"] + SYSTEM_TEXTS["error"]

    data["time_date_example"] = FONTS["p-sans-serif"].render(data["time_date_example"], True, holo_color.system.text_color)
    screen.blit(data["time_date_example"], [SETTINGS["width"] // 2, (SETTINGS["height"] // 2 - data["time_date_example"].get_height()) // 2])



if data["screen"] == "display":
    screen.blit(data["display"]["theme_text"], [SETTINGS["width"] // 10, data["display"]["theme_selector"].pos[1]])
    screen.blit(data["display"]["theme_selector"].surface, data["display"]["theme_selector"].pos)


if data["screen"] == "autostart":
    data["autostart"]["process_list"] = list(data["autostart"]["processes"].keys())
    screen.blit(data["autostart"]["description"], [0, int((SETTINGS["height"] // 10) * 1.02)])
    if (len(data["autostart"]["process_list"]) == 0):
        screen.blit(data["autostart"]["empty"], [SETTINGS["width"] // 2 - data["autostart"]["empty"].get_width() // 2, int((SETTINGS["height"] // 3)*1.05)])
    else:
        screen.blit(holo_assets.arrows.left, [0, SETTINGS["height"] // 3])
        screen.blit(holo_assets.arrows.right, [SETTINGS["width"] - holo_assets.arrows.right.get_width(), int((SETTINGS["height"] // 3)*1.05)])
        screen.blit(data["autostart"]["processes"][data["autostart"]["active"]]["main"], [0,SETTINGS["height"] // 3])
        screen.blit(data["autostart"]["processes"][data["autostart"]["active"]]["checkbox"].surface, data["autostart"]["processes"]["test"]["checkbox"].pos)


if data["quit"]:
    APP_CRASHED = False
    APP = "home"
    exec(APPLAUNCHER)
