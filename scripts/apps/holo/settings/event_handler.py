data["mousePos"] = list(pygame.mouse.get_pos())


if event.type == pygame.MOUSEBUTTONUP:
    if data["screen"] != "menu" and data["mousePos"][0] in range(0, SYSTEM_ASSETS["back"].get_width()) and data["mousePos"][1] in range(0, SYSTEM_ASSETS["back"].get_height()):
        #Back button
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [0,0,SYSTEM_ASSETS["back"].get_width(),SYSTEM_ASSETS["back"].get_height()])
        pygame.display.flip()
        data["screen"] = "menu"
        KEYBOARD.reset()
    else:
        if data["mousePos"][0] in range(SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2 + data["assets"]["home"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.9), SETTINGS["height"]):
            #Home button
            if not KEYBOARD.visible:
                pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, int(SETTINGS["height"]*0.9), data["assets"]["home"].get_width(), SETTINGS["height"] // 10 + 1])
                pygame.display.flip()
                data["quit"] = True
                KEYBOARD.reset()
        elif data["mousePos"][1] in range(0, int(SETTINGS["height"] *0.8)) and data["screen"] == "menu":
            #Main menu click
            data["screen"] = data["constants"]["menu_items"][int((data["mousePos"][1] / int(SETTINGS["height"] *0.8))*4)]
            pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [0,int((data["mousePos"][1] / int(SETTINGS["height"] *0.8))*4) * (SETTINGS["height"] // 5), SETTINGS["width"], SETTINGS["height"] // 5])
            pygame.display.flip()

        if data["screen"] == "general" and len(ALERTS) == 0:
            #General settings
            data["general"]["languageSelector"].detect_click(data["mousePos"])
            data["general"]["layoutSelector"].detect_click(data["mousePos"])
            if data["general"]["sound_checkbox"].detect_click(data["mousePos"]):
                if data["general"]["sound_checkbox"].isChecked:
                    holo.new_alert(SYSTEM_TEXTS["settings"]["general"]["sound_warning"])

            if (data["mousePos"][0] in range(SETTINGS["width"] // 2, SETTINGS["width"] // 2 + data["assets"]["button_change"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.35), int(SETTINGS["height"]*0.35) + data["assets"]["button_change"].get_height())):
                pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.35), data["assets"]["button_change"].get_width(), data["assets"]["button_change"].get_height()])
                pygame.display.flip()
                data["screen"] = "date_format"
                KEYBOARD.show()
                KEYBOARD.text = SETTINGS["dateformat"]

            if (data["mousePos"][0] in range(SETTINGS["width"] // 2, SETTINGS["width"] // 2 + data["assets"]["button_change"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.45), int(SETTINGS["height"]*0.45) + data["assets"]["button_change"].get_height())):
                pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.45), data["assets"]["button_change"].get_width(), data["assets"]["button_change"].get_height()])
                pygame.display.flip()
                data["screen"] = "time_format"
                KEYBOARD.show()
                KEYBOARD.text = SETTINGS["timeformat"]

            if (data["mousePos"][0] in range(SETTINGS["width"] // 2, SETTINGS["width"] // 2 + data["assets"]["button_change"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.55), int(SETTINGS["height"]*0.55) + data["assets"]["button_change"].get_height())):
                pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2, int(SETTINGS["height"]*0.55), data["assets"]["button_change"].get_width(), data["assets"]["button_change"].get_height()])
                pygame.display.flip()
                data["screen"] = "autostart"


        if data["screen"] == "display":
            #display settings
            data["display"]["theme_selector"].detect_click(data["mousePos"])

        if data["screen"] == "autostart":
            if len(data["autostart"]["process_list"]) != 0:
                data["autostart"]["processes"][data["autostart"]["active"]]["checkbox"].detect_click(data["mousePos"])
            if data["mousePos"][0] in range(0, SYSTEM_ASSETS["arrows"]["left"].get_width()) and data["mousePos"][1] in range(SETTINGS["height"] // 3, SETTINGS["height"] // 3 + SYSTEM_ASSETS["arrows"]["left"].get_height()):
                try:
                    data["autostart"]["active"] = data["autostart"]["process_list"][data["autostart"]["process_list"].index(data["autostart"]["active"]) - 1]
                except:
                    if len(data["autostart"]["process_list"]) != 0:
                        data["autostart"]["active"] = data["autostart"]["process_list"][0]
            if data["mousePos"][0] in range(SETTINGS["width"] - SYSTEM_ASSETS["arrows"]["left"].get_width(), SETTINGS["width"]) and data["mousePos"][1] in range(SETTINGS["height"] // 3, SETTINGS["height"] // 3 + SYSTEM_ASSETS["arrows"]["left"].get_height()):
                try:
                    data["autostart"]["active"] = data["autostart"]["process_list"][data["autostart"]["process_list"].index(data["autostart"]["active"]) + 1]
                except:
                    if len(data["autostart"]["process_list"]) != 0:
                        data["autostart"]["active"] = data["autostart"]["process_list"][0]
