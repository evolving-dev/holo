exec(holo_io.file.read("scripts/core/holo_assets.py"))

KEYMAP:dict = {"upper":{},"lower":{}}
#Static objects which belong to HOLO itself and persist until the end of the session.

###
#Background

holo_assets.system.background = Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"])))

BACKGROUND_SIZE_CACHE = holo_assets.system.background.size

TRANSFORM_CACHE = [
    [SETTINGS["width"], round(BACKGROUND_SIZE_CACHE[1] * (SETTINGS["width"] / BACKGROUND_SIZE_CACHE[0]))],
    [round(BACKGROUND_SIZE_CACHE[0] * (SETTINGS["height"] / BACKGROUND_SIZE_CACHE[1])), SETTINGS["height"]] #Try to resize the image to as small of a size as possible, while staying over the screen resolution and maintaining aspect ratio
                   ]

if TRANSFORM_CACHE[0][1] >= SETTINGS["height"]:
    holo_assets.system.background = holo_assets.system.background.resize(tuple(TRANSFORM_CACHE[0]))

elif TRANSFORM_CACHE[1][0] >= SETTINGS["width"]:
    holo_assets.system.background = holo_assets.system.background.resize(tuple(TRANSFORM_CACHE[1]))


holo_assets.system.background = holo_gui.responsive_scale(holo_assets.system.background,[SETTINGS["width"], SETTINGS["height"]]) #Crop to center of image

holo_assets.system.background = pygame.image.fromstring(holo_assets.system.background.convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert()



#CLEANUP
del BACKGROUND_SIZE_CACHE
del TRANSFORM_CACHE


#LOADER OBJECT
im = Image.open(join(PATH,"assets/animations/loading/loading.gif"))

try:

    while True:

        #Convert every frame into a separate image
        holo_assets.system.loading += [pygame.image.fromstring(im.convert('RGBA').resize((SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746))).tobytes(),(SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746)),"RGBA").convert_alpha()]
        im.seek(im.tell()+1)

except EOFError:
    del im #Cleanup if all of the frames have been converted

LOADERWIDTH = holo_assets.system.loading[0].get_width()
TEXTCACHE = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["loading"], True, holo_color.system.text_color)

for i in range(len(holo_assets.system.loading)):

    INITCACHE = holo_assets.prefabs.surfaces.s_4_1.copy()

    #Blit Loading text and animation frame onto surface
    INITCACHE.blit(holo_assets.system.loading[i],(int(0.05*INITCACHE.get_width()),int(INITCACHE.get_height()//2)-holo_assets.system.loading[i].get_height() // 2))
    INITCACHE.blit(TEXTCACHE,(((int(INITCACHE.get_width()) - int(LOADERWIDTH*1.1)) // 2 - TEXTCACHE.get_width() // 2) + int(LOADERWIDTH*1.1) , int(INITCACHE.get_height()//2)-TEXTCACHE.get_height() // 2))

    holo_assets.system.loading[i] = INITCACHE.copy()#Move cached frame into system assets

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
