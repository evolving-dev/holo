SYSTEM_ASSETS: dict = {
"checked": holo_gui.load_image("assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"unchecked": holo_gui.load_image("assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"alert":holo_gui.load_image("assets/images/system/messagebox/alert-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5*4,SETTINGS["height"]//5*3)), #MAINTAIN 4:3 ASPECT RATIO
"ok_button":holo_gui.load_image("assets/images/icons/buttons/OK/okbutton-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5,SETTINGS["height"]//10)), #MAINTAIN 2:1 ASPECT RATIO
"loading":[],
"surface_1_1":holo_gui.load_image("assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5,SETTINGS["height"]//5)),
"surface_4_1":holo_gui.load_image("assets/images/icons/surface_4_1_"+SETTINGS["theme"]+".png", (SETTINGS["height"]//5*4,SETTINGS["height"]//5)),
"keyboard_lower":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
"keyboard_upper":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
"widget_small":holo_gui.load_image("assets/images/icons/surface_2_1_"+SETTINGS["theme"]+".png", (SETTINGS["width"]//5,SETTINGS["width"]//10)),
"dropdown_button": holo_gui.load_image("assets/images/system/dropdown/dropdown-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"arrow_left": holo_gui.load_image("assets/images/system/dropdown/left_arrow-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"arrow_right": holo_gui.load_image("assets/images/system/dropdown/right_arrow-"+SETTINGS["theme"]+".png", (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"overlay": holo_gui.load_image("assets/images/system/overlays/overlay-"+SETTINGS["theme"]+".png", (SETTINGS["width"],SETTINGS["height"])),
"home": holo_gui.load_image("assets/images/icons/buttons/home/home-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"back": holo_gui.load_image("assets/images/icons/buttons/back/back-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//10,SETTINGS["height"]//10)),
"text_color": [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0],
"arrows": {
        "up":holo_gui.load_image("assets/images/icons/buttons/arrows/up-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "down":holo_gui.load_image("assets/images/icons/buttons/arrows/down-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "left":holo_gui.load_image("assets/images/icons/buttons/arrows/left-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "right":holo_gui.load_image("assets/images/icons/buttons/arrows/right-"+SETTINGS["theme"]+".png", (SETTINGS["height"]//12,SETTINGS["height"]//12)),
    },
}
KEYMAP:dict = {"upper":{},"lower":{}}
#Static objects which belong to HOLO itself and persist until the end of the session.

###
#Background

SYSTEM_ASSETS["background"] = Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"])))

BACKGROUND_SIZE_CACHE = SYSTEM_ASSETS["background"].size

TRANSFORM_CACHE = [
    [SETTINGS["width"], round(BACKGROUND_SIZE_CACHE[1] * (SETTINGS["width"] / BACKGROUND_SIZE_CACHE[0]))],
    [round(BACKGROUND_SIZE_CACHE[0] * (SETTINGS["height"] / BACKGROUND_SIZE_CACHE[1])), SETTINGS["height"]] #Try to resize the image to as small of a size as possible, while staying over the screen resolution and maintaining aspect ratio
                   ]

if TRANSFORM_CACHE[0][1] >= SETTINGS["height"]:
    SYSTEM_ASSETS["background"] = SYSTEM_ASSETS["background"].resize(tuple(TRANSFORM_CACHE[0]))

elif TRANSFORM_CACHE[1][0] >= SETTINGS["width"]:
    SYSTEM_ASSETS["background"] = SYSTEM_ASSETS["background"].resize(tuple(TRANSFORM_CACHE[1]))


SYSTEM_ASSETS["background"] = holo.responsive_scale(SYSTEM_ASSETS["background"],[SETTINGS["width"], SETTINGS["height"]]) #Crop to center of image

SYSTEM_ASSETS["background"] = pygame.image.fromstring(SYSTEM_ASSETS["background"].convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert()



#CLEANUP
del BACKGROUND_SIZE_CACHE
del TRANSFORM_CACHE


#LOADER OBJECT
im = Image.open(join(PATH,"assets/animations/loading/loading.gif"))

try:

    while True:

        #Convert every frame into a separate image
        SYSTEM_ASSETS["loading"] += [pygame.image.fromstring(im.convert('RGBA').resize((SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746))).tobytes(),(SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746)),"RGBA").convert_alpha()]
        im.seek(im.tell()+1)

except EOFError:
    del im #Cleanup if all of the frames have been converted

LOADERWIDTH = SYSTEM_ASSETS["loading"][0].get_width()
TEXTCACHE = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["loading"], True, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0])

for i in range(len(SYSTEM_ASSETS["loading"])):

    INITCACHE = SYSTEM_ASSETS["surface_4_1"].copy()

    #Blit Loading text and animation frame onto surface
    INITCACHE.blit(SYSTEM_ASSETS["loading"][i],(int(0.05*INITCACHE.get_width()),int(INITCACHE.get_height()//2)-SYSTEM_ASSETS["loading"][i].get_height() // 2))
    INITCACHE.blit(TEXTCACHE,(((int(INITCACHE.get_width()) - int(LOADERWIDTH*1.1)) // 2 - TEXTCACHE.get_width() // 2) + int(LOADERWIDTH*1.1) , int(INITCACHE.get_height()//2)-TEXTCACHE.get_height() // 2))

    SYSTEM_ASSETS["loading"][i] = INITCACHE.copy()#Move cached frame into SYSTEM_ASSETS variable

#CLEANUP LOADER
del INITCACHE
del TEXTCACHE
del LOADERWIDTH


exec(holo_io.file.read("scripts/init/init_keyboard.py"))

#KEYBOARD CLEANUP
del SPACEBAR
del ROW_ITEM
del ROW_INDEX
del i
del KEYTEMPLATE
del char
del key
del letter
del ROW
del ENTER
del BACKSPACE
del BACKSPACE_DRAWN
del SHIFT

################################END ONSCREEN KEYBOARD###################################
