FPS = 15

data["assets"] = {
    "default-icon": pygame.image.fromstring(Image.open(holo_io.path.to_absolute("assets/images/icons/default.png")).resize((SETTINGS["width"] // 10,SETTINGS["width"] // 10)).convert("RGBA").tobytes(),(SETTINGS["width"] // 10,SETTINGS["width"] // 10),"RGBA").convert_alpha(),
    "warning":pygame.image.fromstring(Image.open(holo_io.path.to_absolute("assets/images/system/warning.png")).resize((SETTINGS["width"] // 20,SETTINGS["width"] // 20)).tobytes(),(SETTINGS["width"] // 20,SETTINGS["width"] // 20),"RGBA").convert_alpha()
} #Load in image assets

data["apps"] = {
    "apps": [],
    "appnames": {},
    "appicons": {},
    "icons": {},
    "areas": {}
}

data["layout"] = {
    "margin_vertical" : SETTINGS["height"] // 30,
    "margin_horizontal" : SETTINGS["width"] // 30,
    "rows" : int(SETTINGS["height"]*0.9 // (SETTINGS["width"] // 7))
}

data["cache"] = {
    "name":"",
    "swipecache":0,
}

for i in PATHFILE.keys(): #For every app in the Pathfile
    
    if i != "home" and "scripts" in PATHFILE[i]: #Ignore the home app
        
        data["apps"]["apps"] += [i] # Add the app to the list of apps
        
        if os.path.isfile(holo_io.path.to_absolute(PATHFILE[i].get("about", ""))): #If the app has an ABOUT file
            
            try:
                
                data["apps"]["appnames"][i] = eval(holo_io.file.read(holo_io.path.to_absolute(PATHFILE[i]["about"]))).get("name", i + " (incomplete ABOUTFILE)") if not "name_" + SETTINGS["lang"] in eval(holo_io.file.read(holo_io.path.to_absolute(PATHFILE[i]["about"]))) else eval(holo_io.file.read(holo_io.path.to_absolute(PATHFILE[i]["about"])))["name_"+SETTINGS["lang"]]
                #Get the language-specific app name. Get the universal app name if the specific name does not exist
                
            except:
                
                data["apps"]["appnames"][i] = i + " (corrupted file(s))"
                #If the ABOUTFILE could not be read, report that files might be corrupted
                
        else:
            
            data["apps"]["appnames"][i] = i + " (missing file(s))"
            #If the app has no ABOUT file report that files might be missing and display the app name as the ID
            
        data["apps"]["appnames"][i] = text_wrap(data["apps"]["appnames"][i], SETTINGS["width"] // 9, FONTS["p-sans-serif"])
            
        data["apps"]["appicons"][i] = holo_io.path.to_absolute(PATHFILE[i].get("icon",holo_io.path.to_absolute("assets/images/icons/default.png"))) #Get the path of the icon. If it's missing, replace the path with the path of the default icon
        
        if not os.path.isfile(data["apps"]["appicons"][i]):
            data["apps"]["appicons"][i] = holo_io.path.to_absolute("assets/images/icons/default.png") #If the specified icon could not be found, replace it with HOLO's default icon
        
        if data["apps"]["appicons"][i] == holo_io.path.to_absolute("assets/images/icons/default.png"):
            
            data["apps"]["icons"][i] = data["assets"]["default-icon"].copy() #If the current icon is the default icon, load the cached version to conserve CPU-time and memory
            
        else:
            
            data["apps"]["icons"][i] = pygame.image.fromstring(Image.open(data["apps"]["appicons"][i]).resize((SETTINGS["width"] // 10,SETTINGS["width"] // 10)).convert("RGBA").tobytes(),(SETTINGS["width"] // 10,SETTINGS["width"] // 10),"RGBA").convert_alpha() #Load and convert the icon

        

data["apps"]["apps"].sort()

data["surfaces"]:list = []

for data["page"] in range(math.ceil(len(data["apps"]["apps"]) / (int(SETTINGS["height"]*0.9 / (SETTINGS["width"] / 7)) * 6))): #For every page that needs to be created
    
    data["surfaces"] += [pygame.Surface([SETTINGS["width"], SETTINGS["height"]], pygame.SRCALPHA)] #Create page
    
    for row in range(data["layout"]["rows"]): #For every row
        
        for m in range(6): #For every app in a row
            
            try:
                data["cache"]["displayname"] = data["apps"]["appnames"][data["apps"]["apps"][6*data["layout"]["rows"]*data["page"] + m + row*6]] #Cache the app's display name
                
                if "file(s)" in data["cache"]["displayname"] or "ABOUTFILE" in data["cache"]["displayname"]: #If the app files are incomplete
                    data["apps"]["icons"][data["apps"]["apps"][data["page"]*6*data["layout"]["rows"] + row*6 + m]].blit(data["assets"]["warning"],(0,0)) #Render a warning sign on top of the app's logo
                    
                data["surfaces"][data["page"]].blit(data["apps"]["icons"][data["apps"]["apps"][data["page"]*6*data["layout"]["rows"] + row*6 + m]] , (data["layout"]["margin_horizontal"] + m*(SETTINGS["width"] // 6) ,data["layout"]["margin_vertical"] + row*(SETTINGS["width"] // 6)))
                
                data["textsurfacecache"] = FONTS["p-sans-serif"].render(data["cache"]["displayname"].split("\n")[0] + "..." if "\n" in data["cache"]["displayname"] else data["cache"]["displayname"] , True, STATIC_CORE["text_color"])
                
                data["surfaces"][data["page"]].blit(data["textsurfacecache"], ((data["layout"]["margin_horizontal"] + m*(SETTINGS["width"] // 6) + ((SETTINGS["width"] // 18) - data["textsurfacecache"].get_width() // 2) ,data["layout"]["margin_vertical"] + row*(SETTINGS["width"] // 6) + SETTINGS["width"] // 9)))
                
                data["apps"]["areas"][data["apps"]["apps"][6*data["layout"]["rows"]*data["page"] + m + row*6]] = [data["page"], [data["layout"]["margin_horizontal"] + m*(SETTINGS["width"] // 6) ,data["layout"]["margin_vertical"] + row*(SETTINGS["width"] // 6)] , [data["layout"]["margin_horizontal"] + m*(SETTINGS["width"] // 6) + SETTINGS["width"] // 6 ,data["layout"]["margin_vertical"] + row*(SETTINGS["width"] // 6) + SETTINGS["width"] // 6]]
                
            except:pass #Ignore the spaces with no app assigned
                
                
data["page"] = 0



#CLEANUP
del row
del m
del i
del data["textsurfacecache"]
del data["apps"]["icons"]
del data["apps"]["appicons"]
del data["cache"]

data["cache"] = {"swipecache":0, "mouseposcache":list(pygame.mouse.get_pos())[0],"swipe":0, "swipeframe":0}