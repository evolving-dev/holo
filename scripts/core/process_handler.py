if not "PROCESSES" in globals():
    PROCESSES:dict = {}
    PROCESS_LAST_RUN = ""

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
            except Exception as e:
                #Disable process
                del PROCESSES[b]
                AUTOSTART[b]["enabled"] = 0
                holo.new_alert(SYSTEM_TEXTS["process_crash"].replace("__PROCESS__", b) + str(e))

        try:
            process = PROCESSES[b]["var"]
            exec(PROCESSES[b]["code"])
            PROCESSES[b]["var"] = process
            del process
        except Exception as e:
            del PROCESSES[b]
            AUTOSTART[b]["enabled"] = 0
            holo.new_alert(SYSTEM_TEXTS["process_crash"].replace("__PROCESS__", b) + str(e))
