data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
}

data["apps"] = {
    "applist": [],
    "appicons": {}
}

for i in PATHFILE.keys():
    if i != "home":
        data["apps"]["applist"] += i
        data["apps"]["appicons"][i] = PATHFILE[i].get("icon",holo.path("assets/icons/default.png"))