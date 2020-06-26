STATIC_CORE: dict = {
"background":pygame.image.fromstring(Image.open(join(PATH,join("assets/images/backgrounds",SETTINGS["background"]+".png"))).resize((SETTINGS["width"],SETTINGS["height"])).convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert(),
"checked":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
"unchecked":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//12,SETTINGS["height"]//12)).tobytes(),(SETTINGS["height"]//12,SETTINGS["height"]//12),"RGBA").convert_alpha(),
"alert":pygame.image.fromstring(Image.open(join(PATH,"assets/images/system/messagebox/alert-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5*4,SETTINGS["height"]//5*3)).tobytes(),(SETTINGS["height"]//5*4,SETTINGS["height"]//5*3),"RGBA").convert_alpha(), #MAINTAIN 4:3 ASPECT RATIO
"ok_button":pygame.image.fromstring(Image.open(join(PATH,"assets/images/icons/buttons/OK/okbutton-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//5,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//5,SETTINGS["height"]//10),"RGBA").convert_alpha(), #MAINTAIN 2:1 ASPECT RATIO
"loading":[],
}
#Static objects which belong to HOLO itself and persist until the end of the session.

im = Image.open(join(PATH,"assets/animations/loading/loading.gif"))
try:
    while True:
        STATIC_CORE["loading"] += [pygame.image.fromstring(im.convert('RGBA').resize((SETTINGS["height"]//10,int(SETTINGS["height"]//10//2.746))).tobytes(),(SETTINGS["height"]//10,int(SETTINGS["height"]//10//2.746)),"RGBA").convert_alpha()]
        #new_frame.save('foo%02d.png' % im.tell(), 'PNG')
        im.seek(im.tell()+1)
except EOFError:
    del im