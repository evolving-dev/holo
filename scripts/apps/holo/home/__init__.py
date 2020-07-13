data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
}

data["apps"] = {
    "apps": [],
    "appnames": {},
    "appicons": {},
    "icons": {}
}

for i in PATHFILE.keys(): #For every app in the Pathfile
    
    if i != "home": #Ignore the home app
        
        data["apps"]["apps"] += [i] # Add the app to the list of 
        
        if os.path.isfile(holo.path(PATHFILE[i].get("about", ""))): #If the app has an ABOUT file
            
            data["apps"]["appnames"][i] = eval(readfile(holo.path(PATHFILE[i]["about"]))).get("name", i + " (incomplete ABOUTFILE)") if not "name_" + SETTINGS["lang"] in eval(readfile(holo.path(PATHFILE[i]["about"]))) else eval(readfile(holo.path(PATHFILE[i]["about"])))["name_"+SETTINGS["lang"]]
            #Get the language-specific app name. Get the universal app name if the specific name does not exist
        
        else:
            
            data["apps"]["appnames"][i] = i + " (missing files?)"
            #If the app has no ABOUT file report that files might be missing and display the app name as the ID
            
        data["apps"]["appnames"][i] = text_wrap(data["apps"]["appnames"][i], SETTINGS["width"] // 8, FONTS["p-sans-serif"])
            
        data["apps"]["appicons"][i] = holo.path(PATHFILE[i].get("icon",holo.path("assets/images/icons/default.png"))) #Get the path of the icon. If it's missing, replace the path with the path of the default icon
        
        if not os.path.isfile(data["apps"]["appicons"][i]):
            data["apps"]["appicons"][i] = holo.path("assets/images/icons/default.png") #If the specified icon could not be found, replace it with HOLO's default icon
        
        
        data["apps"]["icons"][i] = pygame.image.fromstring(Image.open(data["apps"]["appicons"][i]).resize((SETTINGS["width"] // 8,SETTINGS["width"] // 8)).convert("RGBA").tobytes(),(SETTINGS["width"] // 8,SETTINGS["width"] // 8),"RGBA").convert_alpha()

        

data["apps"]["apps"].sort()




data["surfaces"]:list = []
for data["page"] in range(math.ceil(len(data["apps"]["apps"]) / (int(SETTINGS["height"]*0.9 / (SETTINGS["width"] / 7)) * 6))): #For every page that needs to be created
    data["surfaces"] += [pygame.Surface([SETTINGS["width"], SETTINGS["height"]], pygame.SRCALPHA)]
    for i in range(int(SETTINGS["height"]*0.9 // (SETTINGS["width"] // 7))): #For every row
        for m in range(6): #For every app in a row
            try:
                data["surfaces"][data["page"]].blit(data["apps"]["icons"][data["apps"]["apps"][data["page"]*6*int(SETTINGS["height"]*0.9 // (SETTINGS["width"] // 7)) + i*6 + m]] , (0,0))
            except:
                pass
                
                
data["page"] = 0