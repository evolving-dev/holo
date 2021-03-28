def readfile(name):
    with open(name,"rb") as f:
        return(f.read().decode("utf-8"))

exec(readfile("scripts/init/modules.py")) #Import necessary modules

PATH = os.path.dirname(os.path.abspath(__file__)) #Get startup path

exec(readfile("scripts/core/holo_io.py")) #Define core I/O functions like holo_io.file.read

del readfile

resolution = [256, 256]

class game:
    class options:
        dimensions = [256,256]
        gameTitle = "Startup - HOLO" if os.path.isdir(join(PATH,"USERS")) else "Setup - HOLO"
        cursorVisible = True
    class state:
        done = False
    class storage:
        state = 1


ii=0

class execute:
    def onDrawFunction():
        screen.fill((40,60,100))
        if game.storage.state == 1:
            global ii
            for n,m in enumerate(list(STARTUP_TEXTS.keys())):
                screen.blit(STARTUP_TEXTS[m],((resolution[0]-STARTUP_TEXTS[m].get_width())//2,(n+1)*resolution[1]//8))
            if os.path.isdir(join(PATH,"USERS")):
                ii = 0
                pygame.display.flip()
                game.state.done = True
            elif os.path.isfile(join(PATH,"INITFILE")):
                ii = 1
                pygame.display.flip()
                game.state.done = True
            else:
                global ERRORMSG
                ERRORMSG = FONTS["big"].render("ERROR: Missing INITFILE",True,[255,0,0])
                game.storage.state = 2
        else:
            screen.blit(ERRORMSG,((resolution[0] - ERRORMSG.get_width())//2,(resolution[1] - ERRORMSG.get_height())//2))

pygame.init()
ICON = pygame.image.load(join(PATH,'assets/images/icons/icon.png'))

pygame.display.set_icon(ICON)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.display.set_caption("Startup - HOLO" if os.path.isdir(join(PATH,"USERS")) else "Setup - HOLO")
pygame.key.set_repeat(100, 10)

PLATFORM = "HOLO"

exec(holo_io.file.read(join(PATH, "scripts/init/fonts_setup.py")))
STARTUP_LANG_FILE = eval(holo_io.file.read(join(PATH,"assets/text/startup_en-US"))) if not os.path.isdir(join(PATH,"USERS")) else eval(holo_io.file.read(join(PATH,"assets/text/startup_"+eval(holo_io.file.read(join(PATH,"USERS/settings")))["lang"])))
STARTUP_TEXTS:dict = {}
for i in list(STARTUP_LANG_FILE.keys()):
    STARTUP_TEXTS[i] = FONTS["small"].render(STARTUP_LANG_FILE[i],True,[255]*3)

while not game.state.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state.done = True
    execute.onDrawFunction()
    if game.state.done:
        pygame.quit()
        break
    pygame.mouse.set_visible(game.options.cursorVisible)
    pygame.display.flip()

    clock.tick(1)



if ii:
    exec(holo_io.file.read(join(PATH,"scripts/init/setup.py")),globals())
else:
    exec(holo_io.file.read(join(PATH,"scripts/init/startup.py")),globals())
