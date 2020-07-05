STATIC_CORE: dict = {
"background":pygame.image.fromstring(Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"]+".png"))).resize((SETTINGS["width"],SETTINGS["height"])).convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert(),
"checked":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
"unchecked":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
"alert":pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/messagebox/alert-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5*4,SETTINGS["height"]//5*3)).tobytes(),(SETTINGS["height"]//5*4,SETTINGS["height"]//5*3),"RGBA").convert_alpha(), #MAINTAIN 4:3 ASPECT RATIO
"ok_button":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/buttons/OK/okbutton-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//5,SETTINGS["height"]//10),"RGBA").convert_alpha(), #MAINTAIN 2:1 ASPECT RATIO
"loading":[],
"surface_1_1":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5,SETTINGS["height"]//5)).tobytes(),(SETTINGS["height"]//5,SETTINGS["height"]//5),"RGBA").convert_alpha(),
"surface_4_1":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_4_1_"+SETTINGS["theme"]+".png")).resize(((SETTINGS["height"]//5)*4,SETTINGS["height"]//5)).tobytes(),((SETTINGS["height"]//5)*4,SETTINGS["height"]//5),"RGBA").convert_alpha(),
"keyboard_lower":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
"keyboard_upper":pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 2], pygame.SRCALPHA).convert_alpha(),
}
#Static objects which belong to HOLO itself and persist until the end of the session.

#LOADER OBJECT
im = Image.open(join(PATH,"assets/animations/loading/loading.gif"))
try:
    while True:
        STATIC_CORE["loading"] += [pygame.image.fromstring(im.convert('RGBA').resize((SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746))).tobytes(),(SETTINGS["height"]//5,int(SETTINGS["height"]//5//2.746)),"RGBA").convert_alpha()]
        im.seek(im.tell()+1)
except EOFError:
    del im
LOADERWIDTH = STATIC_CORE["loading"][0].get_width()
TEXTCACHE = FONTS["p-sans-serif"].render(SYSTEM_TEXTS["loading"], True, [0,0,0] if SETTINGS["theme"] == "light" else [255,255,255])
for i in range(len(STATIC_CORE["loading"])):
    INITCACHE = STATIC_CORE["surface_4_1"].copy()
    INITCACHE.blit(STATIC_CORE["loading"][i],(int(0.05*INITCACHE.get_width()),int(INITCACHE.get_height()//2)-STATIC_CORE["loading"][i].get_height() // 2))
    INITCACHE.blit(TEXTCACHE,(((int(INITCACHE.get_width()) - int(LOADERWIDTH*1.1)) // 2 - TEXTCACHE.get_width() // 2) + int(LOADERWIDTH*1.1) , int(INITCACHE.get_height()//2)-TEXTCACHE.get_height() // 2))
    STATIC_CORE["loading"][i] = INITCACHE.copy()
del INITCACHE
del TEXTCACHE
del LOADERWIDTH
###
#KEYBOARD
KEYTEMPLATE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png")).resize((SETTINGS["width"]//15,SETTINGS["height"]//10)).tobytes(),(SETTINGS["width"]//15,SETTINGS["height"]//10),"RGBA").convert_alpha()
KEYBOARD_LAYOUT = eval(readfile(join(PATH,"assets/text/keyboard_layouts.json")))[SETTINGS["keyboard"]]
SPACEBAR = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_8_1_"+SETTINGS["theme"]+".png")).resize(((SETTINGS["height"]//10)*8 if (SETTINGS["height"]//10)*8 < SETTINGS["width"] else SETTINGS["width"] // 1.5,SETTINGS["height"]//10)).tobytes(),((SETTINGS["height"]//10)*8 if (SETTINGS["height"]//10)*8 < SETTINGS["width"] else SETTINGS["width"] // 1.5,SETTINGS["height"]//10),"RGBA").convert_alpha()
SHIFT = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/shift-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//20,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//20,SETTINGS["height"]//20),"RGBA").convert_alpha()
BACKSPACE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/backspace-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//10,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//10,SETTINGS["height"]//20),"RGBA").convert_alpha()
ENTER = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/enter-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//20,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//20,SETTINGS["height"]//20),"RGBA").convert_alpha()
BACKSPACE_SURFACE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_2_1_"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//5,SETTINGS["height"]//10),"RGBA").convert_alpha()

#BLIT KEYS ONTO SURFACES


KEYSURFACE = SHIFT.copy()
SHIFT = KEYTEMPLATE.copy()
SHIFT.blit(KEYSURFACE,(KEYTEMPLATE.get_width() // 2 - KEYSURFACE.get_width() // 2, KEYTEMPLATE.get_height() // 2 - KEYSURFACE.get_height() // 2))
KEYSURFACE = ENTER.copy()
ENTER = KEYTEMPLATE.copy()
ENTER.blit(KEYSURFACE,(KEYTEMPLATE.get_width() // 2 - KEYSURFACE.get_width() // 2, KEYTEMPLATE.get_height() // 2 - KEYSURFACE.get_height() // 2))
KEYSURFACE = BACKSPACE.copy()
BACKSPACE = BACKSPACE_SURFACE.copy()
BACKSPACE.blit(KEYSURFACE,(BACKSPACE_SURFACE.get_width() // 2 - KEYSURFACE.get_width() // 2, BACKSPACE_SURFACE.get_height() // 2 - KEYSURFACE.get_height() // 2))

for ROW_INDEX,ROW_ITEM in enumerate(KEYBOARD_LAYOUT):
    ROW = pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 10], pygame.SRCALPHA).convert_alpha()
    for i,char in enumerate(ROW_ITEM):
        key = KEYTEMPLATE.copy()
        letter = FONTS["p-sans-serif"].render(char,True,[0,0,0] if SETTINGS["theme"] == "light" else [255,255,255])
        key.blit(letter,[key.get_width() // 2 - letter.get_width() // 2, key.get_height() // 2 - letter.get_height() // 2]) #Project text onto key
        ROW.blit(key, (i * key.get_width() + ((2 if i not in [2,3,1] else 3)*i),0)) # Project key onto row
    STATIC_CORE["keyboard_lower"].blit(ROW,((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2 ,ROW_INDEX * key.get_height())) #Project row onto keyboard
STATIC_CORE["keyboard_lower"].blit(SPACEBAR, [SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) ,4 * key.get_height()]) #Add the spacebar
#STATIC_CORE["keyboard_lower"].blit(SHIFT, (0,(SETTINGS["height"] // 10) * 3 ))
#STATIC_CORE["keyboard_lower"].blit(ENTER, (SETTINGS["width"] - ENTER.get_width(),(SETTINGS["height"] // 10) * 4 ))
#STATIC_CORE["keyboard_lower"].blit(BACKSPACE, (SETTINGS["width"] - BACKSPACE.get_width(),(SETTINGS["height"] // 10)))

del BACKSPACE_SURFACE
del SPACEBAR
del ROW_ITEM
del ROW_INDEX
del i
del KEYTEMPLATE
del char
del key
del letter
del ROW

