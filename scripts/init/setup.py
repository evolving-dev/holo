os.chdir(PATH)

os.mkdir("storage")
os.chdir(join(PATH,"storage"))
os.mkdir("apps")
os.mkdir("apps_private")
os.mkdir("main")
os.mkdir("system")
os.chdir(join(PATH,"storage/system"))

SETTINGS = {
    'width':int(START_RESOLUTION[0]),
    'height':int(START_RESOLUTION[1]),
    'lang':'en-US',
    'background':'standard.png',
    'theme':'dark',
    'timeout':120,
    'keyboard':'qwerty',
    'timeformat': '%H:%M:%S',
    'dateformat':'%d.%m.%Y',
    'init_sound': 0,
    'keyboard_mode': 'both',
    'connectivity_enabled': 1,
    'default_home': 'home'
    }

with open("settings","w") as f:
    f.write(str(SETTINGS))
    f.close()

#Create WIDGETFILE

with open("widgets", "w") as f:
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

with open("path", "w") as f:
    f.write("""{
    'home' : {
    'assets' : 'assets/apps/holo/home' ,
    'scripts' : 'scripts/apps/holo/home',
    'about' : 'scripts/apps/holo/home/ABOUT',
    'priority':0
    },
    'widgets' : {
    'assets' : 'assets/apps/holo/widgets',
    'scripts' : 'scripts/apps/holo/widgets',
    'about' : 'scripts/apps/holo/widgets/ABOUT',
    'icon' : 'assets/apps/holo/widgets/icon-' + SETTINGS["theme"] + '.png',
    'priority':0
    },
    'settings' : {
    'assets' : 'assets/apps/holo/settings',
    'scripts' : 'scripts/apps/holo/settings',
    'about' : 'scripts/apps/holo/settings/ABOUT',
    'icon' : 'assets/apps/holo/settings/icon-' + SETTINGS["theme"] + '.png',
    'priority':1
    },
    'clock' : {
    'widget' : 'assets/apps/holo/clock/__widget__.py',
    'priority':0
    },
    'installer' : {
    'assets' : 'assets/apps/holo/installer',
    'scripts' : 'scripts/apps/holo/installer',
    'about' : 'scripts/apps/holo/installer/ABOUT',
    'icon' : 'assets/apps/holo/installer/icon-' + SETTINGS["theme"] + '.png',
    'priority':1
    },
    }""")
    f.close()

with open("widgets", "w") as f:
    f.write("""{
    'clock': {
    'name': 'Clock',
    'name_de-DE': 'Uhr',
    'name_en-US': 'Clock',
    'enabled': 1,
    'init': 'scripts/apps/holo/clock/__initwidget__.py',
    'update': 'scripts/apps/holo/clock/__widget__.py',
    'event': 'scripts/apps/holo/clock/__widgetevt__.py',
    'x': 0,
    'y': 0
    }
    }""")
    f.close()

with open("autostart", "w") as f:
    f.write("{}")
    f.close()

os.chdir(PATH)

exec(holo_io.file.read(join(PATH,"scripts/init/startup.py")),globals())
