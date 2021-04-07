def readfile(name):
    with open(name,"rb") as f:
        return(f.read().decode("utf-8"))

exec(readfile("scripts/init/modules.py")) #Import necessary modules

PATH = os.path.dirname(os.path.abspath(__file__)) #Get startup path

exec(readfile("scripts/core/holo_io.py")) #Initialize core I/O functions like holo_io.file.read

del readfile

resolution = [256, 256]

done = False

error_loop = 0

run_setup = 0




pygame.init()
ICON = pygame.image.load(join(PATH,'assets/images/icons/icon.png'))

pygame.display.set_icon(ICON)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.display.set_caption("Startup - HOLO" if os.path.isdir(join(PATH,"storage")) else "Setup - HOLO")

exec(holo_io.file.read(join(PATH, "scripts/init/fonts_setup.py")))
STARTUP_LANG_FILE = eval(holo_io.file.read(join(PATH,"assets/text/startup_en-US"))) if not os.path.isfile(join(PATH,"storage/system/settings")) else eval(holo_io.file.read(join(PATH,"assets/text/startup_"+eval(holo_io.file.read(join(PATH,"storage/system/settings")))["lang"])))
STARTUP_TEXTS:dict = {}
for i in list(STARTUP_LANG_FILE.keys()):
    STARTUP_TEXTS[i] = FONTS["small"].render(STARTUP_LANG_FILE[i],True,[255]*3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if error_loop == 0:
        for n,m in enumerate(list(STARTUP_TEXTS.keys())):
            screen.blit(STARTUP_TEXTS[m],((resolution[0]-STARTUP_TEXTS[m].get_width())//2,(n+1)*resolution[1]//8))
        if os.path.isdir(join(PATH,"storage")):
            run_setup = 0
            pygame.display.flip()
            done = True
        else:
            run_setup = 1
            pygame.display.flip()
            done = True
            import tkinter as tk
            root = tk.Tk()
            root.title("HOLO Setup")
            root.update_idletasks()
            root.attributes('-fullscreen', True)
            root.state('iconic')
            START_RESOLUTION = root.winfo_geometry().split("+")[0].split("x") # Get current resolution for settings
            root.destroy()
            del tk
            del root

    else:
        screen.blit(ERRORMSG,((resolution[0] - ERRORMSG.get_width())//2,(resolution[1] - ERRORMSG.get_height())//2))
    if done:
        pygame.quit()
        break
    pygame.display.flip()

del error_loop

if run_setup:
    exec(holo_io.file.read("scripts/init/setup.py"))
else:
    exec(holo_io.file.read("scripts/init/startup.py"))
