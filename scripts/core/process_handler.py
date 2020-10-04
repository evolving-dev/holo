if not "PROCESSES" in globals():
    PROCESSES:dict = {}

#Start processes
for a,b in enumerate(AUTOSTART.keys()):
    if AUTOSTART[b]["enabled"]:
        #Load unloaded processes into memory
        if not b in PROCESSES:
            PROCESSES[b]:dict = {}
            try:
                PROCESSES[b]["path"] = AUTOSTART[b]["path"]
                PROCESSES[b]["code"] = readfile(holo.path(PROCESSES[b]["path"]))
                PROCESSES[b]["var"]:dict = {}
            except:
                #Disable process
                del PROCESSES[b]
                AUTOSTART[b]["enabled"] = 0
                
