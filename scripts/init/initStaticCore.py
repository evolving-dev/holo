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
KEYMAP:dict = {"upper":{},"lower":{}}

#Static objects which belong to HOLO itself and persist until the end of the session.

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


###
#KEYBOARD

#Load the Keytemplate and the special keys
KEYTEMPLATE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_1_1_"+SETTINGS["theme"]+".png")).resize((int(SETTINGS["width"]//15),int(SETTINGS["height"]//10))).tobytes(),(SETTINGS["width"]//15,SETTINGS["height"]//10),"RGBA").convert_alpha()
SPACEBAR = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_8_1_"+SETTINGS["theme"]+".png")).resize(((SETTINGS["height"]//10)*8 if (SETTINGS["height"]//10)*8 < SETTINGS["width"] else int(SETTINGS["width"] // 1.5),SETTINGS["height"]//10)).tobytes(),((SETTINGS["height"]//10)*8 if (SETTINGS["height"]//10)*8 < SETTINGS["width"] else int(SETTINGS["width"] // 1.5),SETTINGS["height"]//10),"RGBA").convert_alpha()
SHIFT = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/shift-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//20,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//20,SETTINGS["height"]//20),"RGBA").convert_alpha()
BACKSPACE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/backspace-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//10,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//10,SETTINGS["height"]//20),"RGBA").convert_alpha()
ENTER = pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/keyboard/enter-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//20,SETTINGS["height"]//20)).tobytes(),(SETTINGS["height"]//20,SETTINGS["height"]//20),"RGBA").convert_alpha()
BACKSPACE_SURFACE = pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/surface_2_1_"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//5,SETTINGS["height"]//10),"RGBA").convert_alpha()


#BLIT SPECIAL KEYS ONTO SURFACES
KEYSURFACE = SHIFT.copy()
SHIFT = KEYTEMPLATE.copy()
SHIFT.blit(KEYSURFACE,(KEYTEMPLATE.get_width() // 2 - KEYSURFACE.get_width() // 2, KEYTEMPLATE.get_height() // 2 - KEYSURFACE.get_height() // 2))
KEYSURFACE = ENTER.copy()
ENTER = KEYTEMPLATE.copy()
ENTER.blit(KEYSURFACE,(KEYTEMPLATE.get_width() // 2 - KEYSURFACE.get_width() // 2, KEYTEMPLATE.get_height() // 2 - KEYSURFACE.get_height() // 2))
KEYSURFACE = BACKSPACE.copy()
BACKSPACE = BACKSPACE_SURFACE.copy()
BACKSPACE.blit(KEYSURFACE,(BACKSPACE_SURFACE.get_width() // 2 - KEYSURFACE.get_width() // 2, BACKSPACE_SURFACE.get_height() // 2 - KEYSURFACE.get_height() // 2))

#Cleanup to conserve memory
del BACKSPACE_SURFACE
del KEYSURFACE

#################LOWERCASE KEYBOARD###################

KEYBOARD_LAYOUT = eval(readfile(join(PATH,"assets/text/keyboard_layouts.json")))[SETTINGS["keyboard"]] #Load the lowercase keyboard layout

BACKSPACE_DRAWN = False #Variable to compensate for the double width of the backspace character

for ROW_INDEX,ROW_ITEM in enumerate(KEYBOARD_LAYOUT):
    
    ROW = pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 10], pygame.SRCALPHA).convert_alpha() #Create new row
    
    for i,char in enumerate(ROW_ITEM):
        
        #SPECIAL CHARACTERS
        if char == "^": #SHIFT
            ROW.blit(SHIFT, (i * SHIFT.get_width() + 2*i ,0))
            KEYMAP["lower"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            continue
        
        if char == "|": #ENTER
            ROW.blit(ENTER, (i * ENTER.get_width() + 2*i ,0))
            KEYMAP["lower"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            continue
        
        if char == "<":#Backspace
            
            if not BACKSPACE_DRAWN:
                
                ROW.blit(BACKSPACE, (i * ENTER.get_width() + 2*i ,0)) #Width of normal key is used as a workaround
                
                BACKSPACE_DRAWN = True #Compensate for the doubled width of the backspace key
                
                KEYMAP["lower"]["<<"] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * ENTER.get_width()) // 2) + (i * ENTER.get_width() + 2*i),  (ROW_INDEX * BACKSPACE.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * ENTER.get_width()) // 2) + (i * ENTER.get_width() + 2*i) + BACKSPACE.get_width(), BACKSPACE.get_height() +  (ROW_INDEX * BACKSPACE.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            
            continue
        
        key = KEYTEMPLATE.copy() #Load the surface on which the key will be blit
        
        KEYMAP["lower"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
        
        letter = FONTS["p-sans-serif"].render(char,True,[0,0,0] if SETTINGS["theme"] == "light" else [255,255,255]) #Render letter to blit onto the key
        
        key.blit(letter,[key.get_width() // 2 - letter.get_width() // 2, key.get_height() // 2 - letter.get_height() // 2]) #Blit text onto key
        ROW.blit(key, (i * key.get_width() + 2*i ,0)) # Blit key onto row
        
    STATIC_CORE["keyboard_lower"].blit(ROW,((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2 ,ROW_INDEX * key.get_height())) #Blit row onto keyboard

STATIC_CORE["keyboard_lower"].blit(SPACEBAR, [SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) ,4 * key.get_height()]) #Add the spacebar

KEYMAP["lower"][" "] = [[SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) ,4 * key.get_height() + SETTINGS["height"] // 2], [SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) + SPACEBAR.get_width(),4 * key.get_height() + SPACEBAR.get_height() + SETTINGS["height"] // 2]] # Add the spacebar to the keymap

#################UPPERCASE KEYBOARD###################


KEYBOARD_LAYOUT = eval(readfile(join(PATH,"assets/text/keyboard_layouts.json")))[SETTINGS["keyboard"]+"_upper"] #load the uppercase keyboard layout

BACKSPACE_DRAWN = False #Variable to compensate for the double width of the backspace character

for ROW_INDEX,ROW_ITEM in enumerate(KEYBOARD_LAYOUT):
    
    ROW = pygame.Surface([SETTINGS["width"],SETTINGS["height"] // 10], pygame.SRCALPHA).convert_alpha() #Create new row
    
    for i,char in enumerate(ROW_ITEM):
        
        #SPECIAL CHARACTERS
        
        if char == "^":
            KEYMAP["upper"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            ROW.blit(SHIFT, (i * SHIFT.get_width() + 2*i ,0))
            continue
        
        if char == "|":
            KEYMAP["upper"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            ROW.blit(ENTER, (i * ENTER.get_width() + 2*i ,0))
            continue
        
        if char == "<":
            
            if not BACKSPACE_DRAWN:
                
                ROW.blit(BACKSPACE, (i * ENTER.get_width() + 2*i ,0)) #Width of normal key is used as a workaround
                
                BACKSPACE_DRAWN = True #Compensate for the doubled width of the backspace key
                
                KEYMAP["upper"]["<<"] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * ENTER.get_width()) // 2) + (i * ENTER.get_width() + 2*i),  (ROW_INDEX * BACKSPACE.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * ENTER.get_width()) // 2) + (i * ENTER.get_width() + 2*i) + BACKSPACE.get_width(), BACKSPACE.get_height() +  (ROW_INDEX * BACKSPACE.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
            
            continue
        
        key = KEYTEMPLATE.copy() #Load the surface on which the key will be blit
        
        KEYMAP["upper"][char] = [[((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i),  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2], [((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2) + (i * key.get_width() + 2*i) + key.get_width(), key.get_height() +  (ROW_INDEX * key.get_height()) + SETTINGS["height"] // 2]] #Add key to keymap
        
        letter = FONTS["p-sans-serif"].render(char,True,[0,0,0] if SETTINGS["theme"] == "light" else [255,255,255]) # Render letter to blit onto the key
        
        key.blit(letter,[key.get_width() // 2 - letter.get_width() // 2, key.get_height() // 2 - letter.get_height() // 2]) #Blit text onto key
        ROW.blit(key, (i * key.get_width() + 2*i ,0)) # Blit key onto row
        
    STATIC_CORE["keyboard_upper"].blit(ROW,((SETTINGS["width"] // 2) - (len(ROW_ITEM) * key.get_width()) // 2 ,ROW_INDEX * key.get_height())) #Blit row onto keyboard
    
STATIC_CORE["keyboard_upper"].blit(SPACEBAR, [SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) ,4 * key.get_height()]) #Add the spacebar

KEYMAP["upper"][" "] = [[SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) ,4 * key.get_height() + SETTINGS["height"] // 2], [SETTINGS["width"] // 2 - (SPACEBAR.get_width() // 2) + SPACEBAR.get_width(),4 * key.get_height() + SPACEBAR.get_height() + SETTINGS["height"] // 2]] # Add the spacebar to the keymap

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