class holo_assets:

    class prefabs:

        class checkbox:
            checked = holo_gui.load_image("assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))
            unchecked = holo_gui.load_image("assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))

        class alert:
            alert = holo_gui.load_image("assets/images/system/messagebox/alert-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5*4,SETTINGS["height"]//5*3))
            ok_button = holo_gui.load_image("assets/images/icons/buttons/OK/okbutton-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5,SETTINGS["height"]//10))

        class surfaces:
            s_1_1 = holo_gui.load_image("assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5,SETTINGS["height"]//5))
            s_4_1 = holo_gui.load_image("assets/images/icons/surface_4_1_"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5*4,SETTINGS["height"]//5))
            s_2_1 = holo_gui.load_image("assets/images/icons/surface_2_1_"+SETTINGS["theme"]+".png", (SETTINGS["width"]//5,SETTINGS["width"]//10))

        class dropdown:
            dropdown_button = holo_gui.load_image("assets/images/system/dropdown/dropdown-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20))
            arrow_left = holo_gui.load_image("assets/images/system/dropdown/left_arrow-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20))
            arrow_right = holo_gui.load_image("assets/images/system/dropdown/right_arrow-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20))


    class keyboard:

        lower = pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha()
        upper = pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha()

    class arrows:

        up = holo_gui.load_image("assets/images/icons/buttons/arrows/up-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))
        down = holo_gui.load_image("assets/images/icons/buttons/arrows/down-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))
        left = holo_gui.load_image("assets/images/icons/buttons/arrows/left-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))
        right = holo_gui.load_image("assets/images/icons/buttons/arrows/right-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))

    class buttons:

        home = holo_gui.load_image("assets/images/icons/buttons/home/home-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12))
        back = holo_gui.load_image("assets/images/icons/buttons/back/back-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//10,SETTINGS["height"]//10))

    class overlays:

        main = holo_gui.load_image("assets/images/system/overlays/overlay-"+SETTINGS["theme"]+".png", (SETTINGS["width"],SETTINGS["height"]))
        light = holo_gui.load_image("assets/images/system/overlays/overlay-light.png", (SETTINGS["width"],SETTINGS["height"]))
        dark = holo_gui.load_image("assets/images/system/overlays/overlay-dark.png", (SETTINGS["width"],SETTINGS["height"]))

    class system:

        background = Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"])))
        loading = []
