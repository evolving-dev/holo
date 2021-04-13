while not CLOSE:
    if TIMEOUT > 0: #If screen timeout not reached
        if holo_gui.background.is_visible():
            screen.blit(holo_assets.system.background,(0,0))
        else:
            screen.fill([0,0,0])

        try:
            exec(APP_CODE) #Run the updatefile of the current app
        except Exception as e: #CRASH PROTECTION
            APP_CRASHED = True
            holo_prefabs.alert.new(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
            APP = "home"
            exec(APPLAUNCHER)

        #KEYBOARD UPDATE ROUTINE

        if KEYBOARD.visible:
            screen.blit(KEYBOARD.get_surface(),(0, SETTINGS["height"] // 2))

        #ALERT UPDATE ROUTINE
        for index,alert in enumerate(ALERTS):
            if not alert.visible:
                del ALERTS[index]
        for alert in ALERTS:
            screen.blit(alert.surface,(SETTINGS["width"] // 2 - alert.width // 2, SETTINGS["height"] // 2 - alert.height // 2))
        ###

        #LOADER UPDATE ROUTINE
        for index,loader in enumerate(LOADERS):
            if loader.finished:
                del LOADERS[index]
        for loader in LOADERS:
            if not (FRAME % math.ceil(FPS / 6)):
                loader.update()
            screen.blit(loader.surface,tuple(loader.pos))


        if not BLOCK_PROCESS_HANDLER and not PRIORITY_MODE_ACTIVE:
            try:
                exec(PROCESS_HANDLER)
            except Exception as e:
                BLOCK_PROCESS_HANDLER = 1
                print("[HOLO:MAIN_LOOP/ERROR]: The background process handler crashed. Stacktrace below:\n" + str(e))
                holo_prefabs.alert.new(SYSTEM_TEXTS["background_process_error"])
            except:pass

        clock.tick(FPS)
        pygame.display.flip()
        FRAME += 1
        if FRAME%FPS == 0:
            SECOND += 1
            FRAME = 0
            if TIMEOUT:
                TIMEOUT -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLOSE = True
            else:
                TIMEOUT = SETTINGS["timeout"]
            if event.type == pygame.MOUSEBUTTONUP:
                if len(ALERTS) >= 1:
                    ALERT_CLICKED = ALERTS[-1:][0].detect_click(list(pygame.mouse.get_pos())) #Only detect most recent alert
                else:
                    ALERT_CLICKED = False
                if KEYBOARD.visible and list(pygame.mouse.get_pos())[1] >= SETTINGS["height"] // 2:
                    KEYBOARD.update(list(pygame.mouse.get_pos()))

            if not event.type == pygame.MOUSEMOTION and not ALERT_CLICKED: #Mousemotion is ignored for touchscreen displays. Apps need to detect mouse motion themselves

                try:
                    exec(APP_EVENTHANDLER) #Pass the event onto the currently active app
                except Exception as e:
                    if APP != "home":
                        APP_CRASHED = True
                        holo_prefabs.alert.new(APP + SYSTEM_TEXTS["crash"] + "\n" + str(e)) #Show an alert of the exception thrown
                        APP = "home"
                        exec(APPLAUNCHER) #Start the home app

                    else: #If the HOME app crashes, exit
                        print("ERROR: HOLO crashed due to an unexpected error. Please report the following error message on HOLO's GitHub page: HOLO HOME: ",e)
                        pygame.quit()
                        sys.exit()






    else: #If screen timeout reached
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    CLOSE = True
                    TIMEOUT = SETTINGS["timeout"] #End timeout loop either through closing or clicking/tapping
                if event.type == pygame.MOUSEBUTTONUP:
                    TIMEOUT = SETTINGS["timeout"]
            if TIMEOUT > 0:
                break
            else:
                clock.tick(1)
                screen.fill([0,0,0])
                pygame.display.flip()


pygame.quit()
