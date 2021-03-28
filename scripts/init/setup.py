os.chdir(PATH)

with open(join(PATH,"INITFILE"),"r") as f:
    INITFILE = f.readlines()
    f.close()

os.mkdir("USERS")
os.chdir(join(PATH,"USERS"))

SETTINGS = {
    "width":int(INITFILE[0]),
    "height":int(INITFILE[1]),
    "lang":"en-US",
    'background':'standard.png',
    'theme':'dark',
    'timeout':120,
    'keyboard':'qwerty',
    'timeformat': '%H:%M:%S',
    'dateformat':'%d.%m.%Y',
    'init_sound': 0,
    'keyboard_mode': "both",
    'connectivity_enabled': 1,
    }

with open("settings","w") as f:
    f.write(str(SETTINGS))
    f.close()

#Create WIDGETFILE

with open("WIDGETS", "w") as f:
    f.write("""{
    'clock': {
    'enabled': 1,
    'init': 'scripts/apps/holo/clock/__initwidget__.py',
    'update': 'scripts/apps/holo/clock/__widget__.py',
    'event': 'scripts/apps/holo/clock/__widgetevt__.py',
    'x': 0,
    'y': 0
    }
    }""")
    f.close()

os.chdir(PATH)
os.remove("INITFILE")
#CREATING USER DIRECTORY AND WRITING SETTINGS FILE TO IT

exec(holo_io.file.read(join(PATH,"scripts/init/startup.py")),globals())