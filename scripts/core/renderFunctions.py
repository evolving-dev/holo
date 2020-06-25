class holo:
    def text(text,font="p-sans-serif",color=[255,255,255]):
        if FONTS.get(font) == None:
            return False
        return FONTS[font].render(text,True,color)
    def static(item,itemID):
        if STATIC.get(itemID) == None:
            STATIC[itemID] = item #Make item static if an item of the given ID doesn't exist.
            return True
        return False
    def drawOptimize(img):
        with BytesIO() as f:
            img.save(f, format='JPEG')
            f.seek(0)
            return Image.open(f).tobytes()
    class checkbox:
        def __init__(self,pos):
            self.isChecked = False
            self.surface = STATIC_CORE["unchecked"]
            self.width = self.surface.get_width()
            self.height = self.surface.get_height()
            self.pos = pos
        def updateSurface(self):
            self.surface = STATIC_CORE["checked" if self.isChecked else "unchecked"]
        def onClick(self):
            self.isChecked = not self.isChecked
            self.updateSurface()
        def detectClick(self,clickPos):
            if clickPos[0] in range(self.pos[0],self.pos[0]+self.width):
                self.onClick()
    class alert:
        def __init__(self,message):
            self.visible = True
            self.surface = STATIC_CORE["alert"].copy()
            self.width = self.surface.get_width()
            self.height = self.surface.get_height()
            self.message = text_wrap(message, int(self.width*0.95), FONTS["p-sans-serif"])
            ###Text rendering###
            self.texts = []
            for i in self.message.split("\n"):
                self.texts += [FONTS["p-sans-serif"].render(i,True,[0,0,0] if SETTINGS["theme"] == "light" else [255,255,255])]
            ###
            self.button_width = STATIC_CORE["ok_button"].get_width()
            self.button_height = STATIC_CORE["ok_button"].get_height()
            self.surface.blit(STATIC_CORE["ok_button"],(self.width // 2 - self.button_width // 2, int(self.height*0.95 - self.button_height))) #Blit OK Button to surface
            
            for i in range(len(self.texts)):
                self.surface.blit(self.texts[i],(self.width // 2 - self.texts[i].get_width() // 2, self.height * 0.05 + i * 1.05 * self.texts[i].get_height())) #Blit texts to surface
            
            self.xy = (SETTINGS["width"] // 2 - self.width // 2, SETTINGS["height"] // 2 - self.height // 2) #Position for the alert to be displayed
        def detectClick(self, clickPos):
            if clickPos[0] in range(self.xy[0] + self.width // 2 - self.button_width // 2, self.xy[0] + self.width // 2 - self.button_width // 2 + self.button_width) and clickPos[1] in range(self.xy[1] + int(self.height*0.95 - self.button_height), self.xy[1] + int(self.height*0.95 - self.button_height) + self.button_height):
                self.visible = False
    def new_alert(message="Sample Text"):
        global ALERTS
        ALERTS += [holo.alert(message)]
            