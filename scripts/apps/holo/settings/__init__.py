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

data["constants"] = {
    "menu_items":["general", "display", "network", "troubleshooting"]
}
data["constants"]["menu_headers"] = {}
data["constants"]["menu_desc"] = {}
for i in data["constants"]["menu_items"]:
    data["constants"]["menu_headers"][i] = text_cutoff(SYSTEM_TEXTS["settings"]["type"][i][:], width=int(SETTINGS["width"] * 0.75), font=FONTS["p-sans-serif"])
    data["constants"]["menu_desc"][i] = text_cutoff(SYSTEM_TEXTS["settings"]["type"][i+"_desc"][:], width=int(SETTINGS["width"] * 0.75), font=FONTS["p-sans-serif-small"])
    
    data["constants"]["menu_headers"][i] = FONTS["h4"].render(data["constants"]["menu_headers"][i], True, STATIC_CORE["text_color"])
    data["constants"]["menu_desc"][i] = FONTS["p-sans-serif-small"].render(data["constants"]["menu_desc"][i], True, STATIC_CORE["text_color"])
    
data["general"]:dict = {
    "language": FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["general"]["language"], True, STATIC_CORE["text_color"])
}