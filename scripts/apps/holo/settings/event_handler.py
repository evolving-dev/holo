data["mousePos"] = list(pygame.mouse.get_pos())


if event.type == pygame.MOUSEBUTTONUP:
    if data["mousePos"][0] in range(SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2 + data["assets"]["home"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.9), SETTINGS["height"]):
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, int(SETTINGS["height"]*0.9), data["assets"]["home"].get_width(), SETTINGS["height"] // 10 + 1])
        pygame.display.flip()
        data["quit"] = True
    elif data["mousePos"][1] in range(0, int(SETTINGS["height"] *0.8)) and data["screen"] == "menu":
        data["screen"] = data["constants"]["menu_items"][int((data["mousePos"][1] / int(SETTINGS["height"] *0.8))*4)]
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [0,int((data["mousePos"][1] / int(SETTINGS["height"] *0.8))*4) * (SETTINGS["height"] // 5), SETTINGS["width"], SETTINGS["height"] // 5])
        pygame.display.flip()
    if data["screen"] == "general":
        data["general"]["languageSelector"].detect_click(data["mousePos"])