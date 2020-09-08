if event.type == pygame.MOUSEBUTTONUP: #When the mousebutton is released
    mouse_pos = list(pygame.mouse.get_pos())
    if len(ALERTS) == 0: #When there are no alerts open
        if not abs(data["cache"]["mouseposcache"] - list(pygame.mouse.get_pos())[0]) >= SETTINGS["width"] // 20: #When the mouse / finger has not been significantly moved on the x-axis
            for i in data["apps"]["areas"].keys(): #Search for apps that might have been clicked
                if data["page"] == data["apps"]["areas"][i][0]: #When the app found is on the currently active page
                    if mouse_pos[0] in range(data["apps"]["areas"][i][1][0],data["apps"]["areas"][i][2][0]) and mouse_pos[1] in range(data["apps"]["areas"][i][1][1], data["apps"]["areas"][i][2][1]):
                        #When an app has been found, start it
                        holo.new_loader()
                        
                        pygame.draw.rect(screen, STATIC_CORE["text_color"], [data["apps"]["areas"][i][1][0], data["apps"]["areas"][i][1][1], SETTINGS["width"] // 10, SETTINGS["width"] // 10])
                        
                        #Update the loader manually
                        for loader in LOADERS:
                            if not (FRAME % math.ceil(FPS / 6)):
                                loader.update()
                            screen.blit(loader.surface,tuple(loader.pos))
                        
                        pygame.display.flip()
                        APP = i
                        exec(APPLAUNCHER)
                        break
        else: #If a swipe has been detected
            if data["cache"]["mouseposcache"] - list(pygame.mouse.get_pos())[0] < 0:
                data["cache"]["swipe"] = 2 if data["page"] > 0 else 0
                data["page"] -= 1 if data["page"] > 0 else 0
            else:
                data["cache"]["swipe"] = -1 if data["page"] + 1 <= len(data["surfaces"]) - 1 else 0
                data["page"] += 1 if data["page"] + 1 <= len(data["surfaces"]) - 1 else 0
