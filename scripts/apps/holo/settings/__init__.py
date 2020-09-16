#STEP 1: Initialization
FPS = 15
data["quit"] = False
data["screen"] = "menu"

#STEP 2: Loading assets
data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
    "general": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/general-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "display": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/display-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "network": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/network-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "troubleshooting": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/icons/troubleshooting-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["height"] // 5,SETTINGS["height"] // 5)).tobytes(),(SETTINGS["height"] // 5,SETTINGS["height"] // 5),"RGBA").convert_alpha(),
    "home":STATIC_CORE["home"],
    "bar_background": pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 10]),
    "button_change": pygame.Surface([SETTINGS["width"] // 8,int(FONTS["p-sans-serif"].render("CHANGE", False, [0,0,0]).get_height() * 1.5)]),
}
#STEP 2.1: Processing assets
data["assets"]["bar_background"].fill([0,0,0] if SETTINGS["theme"] == "dark" else [255,255,255])
data["assets"]["bar_background"].set_alpha(70)


data["assets"]["button_change"].fill([0,0,0] if SETTINGS["theme"] == "dark" else [255,255,255])
data["assets"]["button_change"].set_alpha(200)

data["cache"] = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["general"]["change"], True, STATIC_CORE["text_color"])
data["assets"]["button_change"].blit(data["cache"],[(SETTINGS["width"] // 16 - data["cache"].get_width() // 2), data["assets"]["button_change"].get_height() // 2 - data["cache"].get_height() // 2])


del data["cache"]

#STEP 3: Initializing constants
data["constants"] = {
    "menu_items":["general", "display", "network", "troubleshooting", "date_format", "time_format"],
    "keyboard_layouts": eval(readfile(join(PATH,"assets/text/keyboard_layouts.json")))["list"]
}
#STEP 3.1: Initialize dictionaries for the menu items
data["constants"]["menu_headers"] = {}
data["constants"]["menu_desc"] = {}

#STEP 3.2: Render menu headers and description
for i in data["constants"]["menu_items"]:
    #STEP 3.2.1: Shorten the text to fit on the screen
    data["constants"]["menu_headers"][i] = text_cutoff(SYSTEM_TEXTS["settings"]["type"][i][:], width=int(SETTINGS["width"] * 0.75), font=FONTS["p-sans-serif"])
    data["constants"]["menu_desc"][i] = text_cutoff(SYSTEM_TEXTS["settings"]["type"][i+"_desc"][:], width=int(SETTINGS["width"] * 0.75), font=FONTS["p-sans-serif-small"])
    
    #STEP 3.2.2: Render the text
    data["constants"]["menu_headers"][i] = FONTS["h4"].render(data["constants"]["menu_headers"][i], True, STATIC_CORE["text_color"])
    data["constants"]["menu_desc"][i] = FONTS["p-sans-serif-small"].render(data["constants"]["menu_desc"][i], True, STATIC_CORE["text_color"])
    
#STEP 4: Initialize sub-menus
data["general"]:dict = {
    "language": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["language"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, STATIC_CORE["text_color"]),
    "languageSelector": holo.list_selector(pos=[SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.15)], width=SETTINGS["width"] // 2, items=list(SYSTEM_TEXTS["settings"]["general"]["languages"].keys()), display_text=list(SYSTEM_TEXTS["settings"]["general"]["languages"].values())),
    "keyboard_layout": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["keyboard-layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, STATIC_CORE["text_color"]),
    "layoutSelector": holo.list_selector(pos=[SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.25)], width=SETTINGS["width"] // 2, items=data["constants"]["keyboard_layouts"], display_text=[i.upper() for i in data["constants"]["keyboard_layouts"]]),
    "date_format": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["date_layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, STATIC_CORE["text_color"]),
    "time_format": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["time_layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, STATIC_CORE["text_color"]),
}



#STEP 5: Display the current settings in the initialized components

#GENERAL->LANGUAGE
try:
    data["general"]["languageSelector"].selected = data["general"]["languageSelector"].items.index(SETTINGS["lang"])
except ValueError:
    data["general"]["languageSelector"].selected = 0
data["general"]["languageSelector"].update()
    
#GENERAL->KEYBOARD LAYOUT
try:
    data["general"]["layoutSelector"].selected = data["general"]["layoutSelector"].items.index(SETTINGS["keyboard"])
except ValueError:
    data["general"]["layoutSelector"].selected = 0
data["general"]["layoutSelector"].update()