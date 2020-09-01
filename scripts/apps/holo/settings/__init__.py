FPS = 15
data["quit"] = False

data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
    "general": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/general-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "display": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/display-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "network": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/network-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "troubleshooting": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/troubleshooting-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "home":STATIC_CORE["home"],
    "bottomBar": pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 10]),
}

data["assets"]["bottomBar"].fill([0,0,0] if SETTINGS["theme"] == "dark" else [255,255,255])
data["assets"]["bottomBar"].set_alpha(70)

data["screen"] = "menu"