class holo_launcher:

    def open_app(name, crash=False):
        global APP
        global APP_CRASHED
        APP_CRASHED = crash
        APP = name
        exec(APPLAUNCHER)

    def to_home(crash=False):
        global APP
        global APP_CRASHED
        global SETTINGS
        APP_CRASHED = crash
        if APP != SETTINGS["default_home"]:
            APP = SETTINGS["default_home"]
        else:
            APP = "home"
        exec(APPLAUNCHER)
