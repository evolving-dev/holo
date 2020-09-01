data["mousePos"] = list(pygame.mouse.get_pos())


if event.type == pygame.MOUSEBUTTONUP:
    if data["mousePos"][0] in range(SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2 + data["assets"]["home"].get_width()) and data["mousePos"][1] in range(int(SETTINGS["height"]*0.9), SETTINGS["height"]):
        pygame.draw.rect(screen, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, int(SETTINGS["height"]*0.9), data["assets"]["home"].get_width(), SETTINGS["height"] // 10 + 1])
        pygame.display.flip()
        data["quit"] = True