STATIC_CORE: dict = {
"background":pygame.image.fromstring(holo.drawOptimize(Image.open(os.path.join(PATH,os.path.join("assets/images/backgrounds",SETTINGS["background"]+".png"))).resize((SETTINGS["width"],SETTINGS["height"])).convert("RGB")),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert(),
"checked":pygame.image.fromstring(Image.open(os.path.join(PATH,"assets/images/icons/checkbox/checked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//10,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//10,SETTINGS["height"]//10),"RGBA").convert_alpha(),
"unchecked":pygame.image.fromstring(Image.open(os.path.join(PATH,"assets/images/icons/checkbox/unchecked-"+SETTINGS["theme"]+".png")).resize((SETTINGS["height"]//10,SETTINGS["height"]//10)).tobytes(),(SETTINGS["height"]//10,SETTINGS["height"]//10),"RGBA").convert_alpha(),
}
#Static objects which belong to HOLO itself and persist until the end of the session.