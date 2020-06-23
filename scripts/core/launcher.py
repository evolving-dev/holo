if APP == "startup":
    APP = "home"
    exec(APPLAUNCHER)
else:
    exec(readfile(join(PATH,join(PATHFILE[APP]['scripts'],'__init__.py')))) #Run the init file for the opened app.