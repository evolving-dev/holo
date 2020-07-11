data["assets"] = {
    "overlay": pygame.image.fromstring(Image.open(holo.path(join(APP_PATH["assets"] , "images/overlay-" + SETTINGS["theme"] + ".png"))).resize((SETTINGS["width"],SETTINGS["height"])).tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGBA").convert_alpha(),
}

data["apps"] = {
    "apps": [],
    "appnames": {},
    "appicons": {}
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
            
        data["apps"]["appnames"][i] = text_wrap(data["apps"]["appnames"][i], SETTINGS["width"] // 6, FONTS["p-sans-serif"])
            
        data["apps"]["appicons"][i] = PATHFILE[i].get("icon",holo.path("assets/images/icons/default.png")) #Get the path of the icon. If it's missing, replace the path with the path of the default icon
        
        if not os.path.isfile(data["apps"]["appicons"][i]):
            data["apps"]["appicons"][i] = holo.path("assets/images/icons/default.png") #If the specified icon could not be found, replace it with HOLO's default icon
        
        
        
        
        
        
        
        
data["apps"]["apps"].sort()