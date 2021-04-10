#STEP 1: Initialization
FPS = 15
data["quit"] = False
data["screen"] = "menu"

#STEP 2: Loading assets
data["assets"] = {
    "general": holo_gui.load_image(join(APP_PATH["assets"] , "images/icons/general-" + SETTINGS["theme"] + ".png"), (SETTINGS["height"] // 5,SETTINGS["height"] // 5)),
    "display": holo_gui.load_image(join(APP_PATH["assets"] , "images/icons/display-" + SETTINGS["theme"] + ".png"), (SETTINGS["height"] // 5,SETTINGS["height"] // 5)),
    "network": holo_gui.load_image(join(APP_PATH["assets"] , "images/icons/network-" + SETTINGS["theme"] + ".png"), (SETTINGS["height"] // 5,SETTINGS["height"] // 5)),
    "troubleshooting": holo_gui.load_image(join(APP_PATH["assets"] , "images/icons/troubleshooting-" + SETTINGS["theme"] + ".png"), (SETTINGS["height"] // 5,SETTINGS["height"] // 5)),
    "home": holo_assets.buttons.home,
    "bar_background": pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 10]),
    "textbox": pygame.Surface([SETTINGS["width"] // 5 * 4, SETTINGS["height"] // 10]),
    "button_change": pygame.Surface([SETTINGS["width"] // 8,int(FONTS["p-sans-serif"].render("CHANGE", False, [0,0,0]).get_height() * 1.5)]),
    "button_remove": pygame.Surface([SETTINGS["width"] // 8,int(FONTS["p-sans-serif"].render("REMOVE", False, [0,0,0]).get_height() * 1.5)]),
}
#STEP 2.1: Processing assets
data["assets"]["bar_background"].fill(holo_color.system.theme_color)
data["assets"]["bar_background"].set_alpha(70)

data["assets"]["textbox"].fill(holo_color.system.theme_color)
data["assets"]["textbox"].set_alpha(150)


data["assets"]["button_change"].fill(holo_color.system.theme_color)


data["cache"] = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["general"]["change"], True, holo_color.system.text_color)
data["assets"]["button_change"].blit(data["cache"],[(SETTINGS["width"] // 16 - data["cache"].get_width() // 2), data["assets"]["button_change"].get_height() // 2 - data["cache"].get_height() // 2])


data["assets"]["button_remove"].fill(holo_color.system.theme_color)


data["cache"] = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["general"]["remove"], True, holo_color.system.text_color)
data["assets"]["button_remove"].blit(data["cache"],[(SETTINGS["width"] // 16 - data["cache"].get_width() // 2), data["assets"]["button_remove"].get_height() // 2 - data["cache"].get_height() // 2])

data["assets"]["button_change"].set_alpha(200)
data["assets"]["button_remove"].set_alpha(200)

del data["cache"]

#STEP 3: Initializing constants
data["constants"] = {
    "menu_items":["general", "display", "network", "troubleshooting", "date_format", "time_format", "autostart"],
    "keyboard_layouts": eval(holo_io.file.read(join(PATH,"assets/text/keyboard_layouts.json")))["list"]
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
    data["constants"]["menu_headers"][i] = FONTS["h4"].render(data["constants"]["menu_headers"][i], True, holo_color.system.text_color)
    data["constants"]["menu_desc"][i] = FONTS["p-sans-serif-small"].render(data["constants"]["menu_desc"][i], True, holo_color.system.text_color)

#STEP 4: Initialize sub-menus
data["general"]:dict = {
    "language": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["language"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "languageSelector": holo_prefabs.list_selector(pos=[SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.15)], width=SETTINGS["width"] // 2, items=list(SYSTEM_TEXTS["settings"]["general"]["languages"].keys()), display_text=list(SYSTEM_TEXTS["settings"]["general"]["languages"].values())),
    "keyboard_layout": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["keyboard-layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "layoutSelector": holo_prefabs.list_selector(pos=[SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.25)], width=SETTINGS["width"] // 2, items=data["constants"]["keyboard_layouts"], display_text=[i.upper() for i in data["constants"]["keyboard_layouts"]]),
    "date_format": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["date_layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "time_format": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["time_layout"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "autostart": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["autostart"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "use_sound": FONTS["p-sans-serif"].render(text_cutoff(SYSTEM_TEXTS["settings"]["general"]["use_sound"], width=SETTINGS["width"] // 3, font=FONTS["p-sans-serif"]), True, holo_color.system.text_color),
    "sound_checkbox": holo_prefabs.checkbox([SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.65)])
}

data["autostart"] = {
    "description": text_wrap(SYSTEM_TEXTS["settings"]["autostart"]["description"], width=int(SETTINGS["width"]*0.95), font=FONTS["p-sans-serif"])
}

data["cache"] = data["autostart"]["description"].split("\n")

data["autostart"]["description"] = pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 2], pygame.SRCALPHA)

for n,i in enumerate(data["cache"]):
    data["autostart"]["description"].blit(FONTS["p-sans-serif"].render(i, True, holo_color.system.text_color), [(SETTINGS["width"] - FONTS["p-sans-serif"].render(i, True, holo_color.system.text_color).get_width()) // 2, int(FONTS["p-sans-serif"].render(i, True, holo_color.system.text_color).get_height() * 1.2) * n])
data["autostart"]["processes"]:dict = {}
for i,n in enumerate(AUTOSTART.keys()):
    data["autostart"]["processes"][n] = AUTOSTART[n].copy()
    data["autostart"]["processes"][n]["main"] = pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 8], pygame.SRCALPHA)
    data["autostart"]["processes"][n]["main"].blit(
        FONTS["p-sans-serif"].render(text_cutoff(n, int(SETTINGS["width"]*0.7), FONTS["p-sans-serif"]), True, holo_color.system.text_color),
        [SETTINGS["width"] // 15 ,SETTINGS["height"] // 100]
    )
    data["autostart"]["processes"][n]["main"].blit(
        FONTS["p-sans-serif-small"].render(text_cutoff(AUTOSTART[n]["path"], int(SETTINGS["width"]*0.7), FONTS["p-sans-serif-small"]), True, holo_color.system.text_color),
        [SETTINGS["width"] // 15 ,SETTINGS["height"] // 15]
    )
    data["autostart"]["processes"][n]["checkbox"] = holo_prefabs.checkbox([int(SETTINGS["width"] * 0.85), int((SETTINGS["height"] // 3) * 1.05)])

data["autostart"]["process_list"] = list(data["autostart"]["processes"].keys())

if (len(data["autostart"]["process_list"]) != 0):
    data["autostart"]["active"] = data["autostart"]["process_list"][0]

data["autostart"]["list"] = list(AUTOSTART.keys())

data["autostart"]["empty"] = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["autostart"]["empty"], True, holo_color.system.text_color)



data["time_date"]:dict = {

}

for i in SYSTEM_TEXTS["settings"]["time_date"]:
    data["time_date"][i] = []
    for m in SYSTEM_TEXTS["settings"]["time_date"][i]:
        data["time_date"][i] += [FONTS["p-sans-serif"].render(m, True, holo_color.system.text_color)]

data["time_surface"] = pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 2], pygame.SRCALPHA)
data["date_surface"] = pygame.Surface([SETTINGS["width"], SETTINGS["height"] // 2], pygame.SRCALPHA)

for i, m in enumerate(data["time_date"]["reference_time"]):
    data["time_surface"].blit(m, [0, int(SETTINGS["height"] * 0.225) + i*data["time_date"]["reference_time"][0].get_height()])

for i, m in enumerate(data["time_date"]["reference_date"]):
    data["date_surface"].blit(m, [0, int(SETTINGS["height"] * 0.225) + i*data["time_date"]["reference_time"][0].get_height()])

del data["time_date"]



data["display"]:dict = {
    "theme_text": FONTS["p-sans-serif"].render(SYSTEM_TEXTS["settings"]["display"]["theme"], True, holo_color.system.text_color),
    "theme_selector": holo_prefabs.list_selector(pos=[SETTINGS["width"] // 2, int(SETTINGS["height"] * 0.15)], width=SETTINGS["width"] // 2, items=list(SYSTEM_TEXTS["settings"]["display"]["themes"].keys()), display_text=list(SYSTEM_TEXTS["settings"]["display"]["themes"].values())),
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

#GENERAL->SOUNDS
if SETTINGS['init_sound']:
    data["general"]["sound_checkbox"].on_click()

#DISPLAY->THEME
data["display"]["theme_selector"].selected = 0 if SETTINGS["theme"] == "light" else 1
data["display"]["theme_selector"].update()

del data["cache"]
