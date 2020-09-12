class holo:
    
    def path(path):
        if PATH not in path:
            return join(PATH,path)
        return path
        
        
    
    class loader:#Loader object
        
        def __init__(self):
            self.frame = 0
            self.finished = False
            self.surface = STATIC_CORE["loading"][0].copy()
            
            self.pos = [(SETTINGS["width"]//2) - self.surface.get_width() // 2, (SETTINGS["height"] // 2) - self.surface.get_height() // 2] #Automatically align the laoder to the middle
        
        def update(self):
            self.frame = 0 if self.frame >= len(STATIC_CORE["loading"]) - 1 else self.frame+1 #Loop animation if end is reached, if not, add 1 to the frame count
            self.surface = STATIC_CORE["loading"][self.frame].copy()
    
    def new_loader():
        global LOADERS
        LOADERS += [holo.loader()]
    
    
    def responsive_scale(image,new_scale): #Function to scale an image without stretching
        im = image
        old_width, old_height = im.size
        
        # Center the image
        paste_coords = [(new_scale[0] - old_width) // 2,(new_scale[1] - old_height) // 2]
        
        newImage = Image.new("RGBA", tuple(new_scale),(255,255,255,255))
        newImage.paste(im, (paste_coords[0], paste_coords[1], paste_coords[0] + old_width, paste_coords[1] + old_height))
        
        return newImage
    def text(text,font="p-sans-serif",color=[255,255,255]):
        if FONTS.get(font) == None:
            return False
        return FONTS[font].render(text,True,color)
    def static(item,itemID):
        if STATIC.get(itemID) == None:
            STATIC[itemID] = item #Make item static if an item of the given ID doesn't exist.
            return True
        return False
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
            if clickPos[0] in range(self.pos[0],self.pos[0]+self.width) and clickPos[1] in range(self.pos[1],self.pos[1]+self.height):
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
                return True
            return False
    
    def new_alert(message="Sample Text"):
        
        global ALERTS
        ALERTS += [holo.alert(message)]
            
    class keyboard:
        
        def __init__(self):
            
            self.text = ""
            self.uppercase = False
            self.visible = False
            self.surface = {"lower" : STATIC_CORE["keyboard_lower"], "upper" : STATIC_CORE["keyboard_upper"]} #Load keyboard
            self.keymap = KEYMAP
        
        def reset(self):
            
            self.text = ""
            self.visible = False
            self.uppercase = False
            
        def update(self, mousePos):
            
            for i in list(KEYMAP["upper" if self.uppercase else "lower"].keys()):
                if mousePos[0] in range(KEYMAP["upper" if self.uppercase else "lower"][i][0][0], KEYMAP["upper" if self.uppercase else "lower"][i][1][0]):
                    if mousePos[1] in range(KEYMAP["upper" if self.uppercase else "lower"][i][0][1], KEYMAP["upper" if self.uppercase else "lower"][i][1][1]):
                        self.text += "\n" if i == "|" else "" if (i == "<<" or i == "^") else i #TODO: SPACE zur Keymap hinzufügen
                        if i == "<<":
                            self.text = self.text[:-1]
                        if i == "^":
                            self.uppercase = not self.uppercase
                        break
                    
        def get_surface(self):
            
            return self.surface["upper"] if self.uppercase else self.surface["lower"]
        
        def show(self):
            
            self.visible = True
            
        def hide(self):
            
            self.visible = False
            
        def clear(self):
            
            self.text = ""
    
    
    
    class list_selector:
        
        def __init__(self, pos, items, width=SETTINGS["width"] // 4, display_text=0):
            
            self.pos = pos
            self.width = width
            self.selected = 0
            self.items = items
            
            if display_text == 0:
                self.display_text = items
            else:
                self.display_text = display_text
            
            self.text_renders = []
            for i in self.display_text:
                self.text_renders += [FONTS["p-sans-serif"].render(text_cutoff(i, int(self.width - (STATIC_CORE["arrow_left"].get_width() * 2) - int(self.width * 0.05)), FONTS["p-sans-serif"]), True, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0])]
            
            
            self.text_render = self.text_renders[self.selected]
            
            self.empty_surface = pygame.Surface([int(self.width), int(SETTINGS["height"] // 15)], pygame.SRCALPHA).convert_alpha()
            
            self.empty_surface.fill([50,50,50,128] if SETTINGS["theme"] == "dark" else [200,200,200,128])
            
            self.empty_surface.blit(STATIC_CORE["arrow_right"], [width - STATIC_CORE["arrow_right"].get_width(), self.empty_surface.get_height() // 2 - STATIC_CORE["arrow_right"].get_height() // 2])
            self.empty_surface.blit(STATIC_CORE["arrow_left"], [0, self.empty_surface.get_height() // 2 - STATIC_CORE["arrow_right"].get_height() // 2])
            
            self.surface = self.empty_surface.copy()
            self.surface.blit(self.text_render, [STATIC_CORE["arrow_left"].get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])
            
            
        
        def detect_click(self, pos):
            
            if pos[0] in range(self.pos[0], self.pos[0] + self.width) and pos[1] in range(self.pos[1], self.pos[1] + self.empty_surface.get_height()):
                if pos[0] - self.pos[0] in range(0, STATIC_CORE["arrow_left"].get_width()):
                    pygame.draw.rect(self.surface, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [0, 0, STATIC_CORE["arrow_left"].get_width(), self.surface.get_height()])
                    screen.blit(self.surface, self.pos)
                    pygame.display.flip()
                    self.selected -= 1 if self.selected > 0 else 0
                    self.text_render = self.text_renders[self.selected]
                    self.surface = self.empty_surface.copy()
                    self.surface.blit(self.text_render, [STATIC_CORE["arrow_left"].get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])
                if pos[0] - self.pos[0] in range(self.width - STATIC_CORE["arrow_right"].get_width(), self.width):
                    pygame.draw.rect(self.surface, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0], [self.width - STATIC_CORE["arrow_right"].get_width(), 0, self.width , self.surface.get_height()])
                    screen.blit(self.surface, self.pos)
                    pygame.display.flip()
                    self.selected += 1 if len(self.items) - 1 > self.selected else 0
                    self.text_render = self.text_renders[self.selected]
                    self.surface = self.empty_surface.copy()
                    self.surface.blit(self.text_render, [STATIC_CORE["arrow_left"].get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])

            
            
            
                return True
            
            return False
    
        def update(self):
            self.text_render = self.text_renders[self.selected]
            self.surface = self.empty_surface.copy()
            self.surface.blit(self.text_render, [STATIC_CORE["arrow_left"].get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])
