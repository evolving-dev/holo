data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
}

data["apps"] = {
    "apps": [],
    "appnames": {},
    "appicons": {}
}

for i in PATHFILE.keys():
    if i != "home":
        apps += [i]
        if os.path.isfile(holo.path(PATHFILE[i]["about"])):
            data["apps"]["appnames"][i] = eval(readfile(holo.path(PATHFILE[i]["about"])))["name"]
        else:
            data["apps"]["appnames"][i] = i + " (missing files)"
        data["apps"]["appicons"][i] = PATHFILE[i].get("icon",holo.path("assets/icons/default.png"))