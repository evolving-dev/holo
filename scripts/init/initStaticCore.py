STATIC_CORE: dict = {
"checked": holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"unchecked": holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"alert":holo_gui.load_image(holo_io.path.to_absolute("assets/images/system/messagebox/alert-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//5*4,SETTINGS["height"]//5*3)), #MAINTAIN 4:3 ASPECT RATIO
"ok_button":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/OK/okbutton-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//5,SETTINGS["height"]//10)), #MAINTAIN 2:1 ASPECT RATIO
"loading":[],
"surface_1_1":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//5,SETTINGS["height"]//5)),
"surface_4_1":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/surface_4_1_"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//5*4,SETTINGS["height"]//5)),
"keyboard_lower":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
"keyboard_upper":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
"widget_small":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/surface_2_1_"+SETTINGS["theme"]+".png"), (SETTINGS["width"]//5,SETTINGS["width"]//10)),
"dropdown_button": holo_gui.load_image(holo_io.path.to_absolute("assets/images/system/dropdown/dropdown-"+SETTINGS["theme"]+".png"), (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"arrow_left": holo_gui.load_image(holo_io.path.to_absolute("assets/images/system/dropdown/left_arrow-"+SETTINGS["theme"]+".png"), (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"arrow_right": holo_gui.load_image(holo_io.path.to_absolute("assets/images/system/dropdown/right_arrow-"+SETTINGS["theme"]+".png"), (SETTINGS["width"]//20,SETTINGS["width"]//20)),
"overlay": holo_gui.load_image(holo_io.path.to_absolute("assets/images/system/overlays/overlay-"+SETTINGS["theme"]+".png"), (SETTINGS["width"],SETTINGS["height"])),
"home": holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/home/home-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
"back": holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/back/back-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//10,SETTINGS["height"]//10)),
"text_color": [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0],
"arrows": {
        "up":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/arrows/up-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "down":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/arrows/down-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "left":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/arrows/left-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
        "right":holo_gui.load_image(holo_io.path.to_absolute("assets/images/icons/buttons/arrows/right-"+SETTINGS["theme"]+".png"), (SETTINGS["height"]//12,SETTINGS["height"]//12)),
    },
}
KEYMAP:dict = {"upper":{},"lower":{}}
#Static objects which belong to HOLO itself and persist until the end of the session.

###
#Background

STATIC_CORE["background"] = Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"])))

BACKGROUND_SIZE_CACHE = STATIC_CORE["background"].size

TRANSFORM_CACHE = [
    [SETTINGS["width"], round(BACKGROUND_SIZE_CACHE[1] * (SETTINGS["width"] / BACKGROUND_SIZE_CACHE[0]))],
    [round(BACKGROUND_SIZE_CACHE[0] * (SETTINGS["height"] / BACKGROUND_SIZE_CACHE[1])), SETTINGS["height"]] #Try to resize the image to as small of a size as possible, while staying over the screen resolution and maintaining aspect ratio
                   ]

if TRANSFORM_CACHE[0][1] >= SETTINGS["height"]:
    STATIC_CORE["background"] = STATIC_CORE["background"].resize(tuple(TRANSFORM_CACHE[0]))

elif TRANSFORM_CACHE[1][0] >= SETTINGS["width"]:
    STATIC_CORE["background"] = STATIC_CORE["background"].resize(tuple(TRANSFORM_CACHE[1]))


STATIC_CORE["background"] = holo.responsive_scale(STATIC_CORE["background"],[SETTINGS["width"], SETTINGS["height"]]) #Crop to center of image

STATIC_CORE["background"] = pygame.image.fromstring(STATIC_CORE["background"].convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert()



#CLEANUP
del BACKGROUND_SIZE_CACHE
del TRANSFORM_CACHE


#LOADER OBJECT
im = Image.open(join(PATH,"assets/animations/loading/loading.gif"))

try:

    while True:

        #Convert every frame into a separate image
        STATIC_CORE["loading"] += [pygame.image.fromstring(im.convert('RGBA').resize((SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746))).tobytes(),(SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746)),"RGBA").convert_alpha()]
        im.seek(im.tell()+1)

except EOFError:
    del im #Cleanup if all of the frames have been converted

LOADERWIDTH = STATIC_CORE["loading"][0].get_width()
TEXTCACHE = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["loading"], True, [0,0,0] if SETTINGS["theme"] == "light" else [255,255,255])

for i in range(len(STATIC_CORE["loading"])):

    INITCACHE = STATIC_CORE["surface_4_1"].copy()

    #Blit Loading text and animation frame onto surface
    INITCACHE.blit(STATIC_CORE["loading"][i],(int(0.05*INITCACHE.get_width()),int(INITCACHE.get_height()//2)-STATIC_CORE["loading"][i].get_height() // 2))
    INITCACHE.blit(TEXTCACHE,(((int(INITCACHE.get_width()) - int(LOADERWIDTH*1.1)) // 2 - TEXTCACHE.get_width() // 2) + int(LOADERWIDTH*1.1) , int(INITCACHE.get_height()//2)-TEXTCACHE.get_height() // 2))

    STATIC_CORE["loading"][i] = INITCACHE.copy()#Move cached frame into STATIC_CORE variable

#CLEANUP LOADER
del INITCACHE
del TEXTCACHE
del LOADERWIDTH


exec(readfile(holo_io.path.to_absolute("scripts/init/initKeyboard.py")))

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
