if not "PROCESSES" in globals():
    PROCESSES:dict = {}
    PROCESS_LAST_RUN = ""

#Start processes
for a,b in enumerate(AUTOSTART):
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
