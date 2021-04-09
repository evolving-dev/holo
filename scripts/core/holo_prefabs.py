class holo_prefabs:

    class loader:#Loader object

        def __init__(self):
            self.frame = 0
            self.finished = False
            self.surface = holo_assets.system.loading[0]

            self.pos = [(SETTINGS["width"]//2) - self.surface.get_width() // 2, (SETTINGS["height"] // 2) - self.surface.get_height() // 2] #Automatically align the laoder to the middle

        def update(self):
            self.frame = 0 if self.frame >= len(holo_assets.system.loading) - 1 else self.frame+1 #Loop animation if end is reached, if not, add 1 to the frame count
            self.surface = holo_assets.system.loading[self.frame]

        def new():
            global LOADERS
            LOADERS += [holo_prefabs.loader()]

    class checkbox:

        def __init__(self,pos):
            self.isChecked = False
            self.surface = holo_assets.prefabs.checkbox.unchecked
            self.width = self.surface.get_width()
            self.height = self.surface.get_height()
            self.pos = pos
        def update_surface(self):
            self.surface = holo_assets.prefabs.checkbox.checked if self.isChecked else holo_assets.prefabs.checkbox.unchecked
        def on_click(self):
            self.isChecked = not self.isChecked
            self.update_surface()
        def detect_click(self,clickPos):
            if clickPos[0] in range(self.pos[0],self.pos[0]+self.width) and clickPos[1] in range(self.pos[1],self.pos[1]+self.height):
                self.on_click()
                return True
            return False

    class alert:

        def __init__(self,message):
            self.visible = True
            self.surface = holo_assets.prefabs.alert.alert.copy()
            self.width = self.surface.get_width()
            self.height = self.surface.get_height()
            self.message = text_wrap(message, int(self.width*0.95), FONTS["p-sans-serif"])
            ###Text rendering###
            self.texts = []
            for i in self.message.split("\n"):
                self.texts += [FONTS["p-sans-serif"].render(i,True,holo_color.system.text_color)]
            ###
            self.button_width = holo_assets.prefabs.alert.ok_button.get_width()
            self.button_height = holo_assets.prefabs.alert.ok_button.get_height()
            self.surface.blit(holo_assets.prefabs.alert.ok_button,(self.width // 2 - self.button_width // 2, int(self.height*0.95 - self.button_height))) #Blit OK Button to surface

            for i in range(len(self.texts)):
                self.surface.blit(self.texts[i],(self.width // 2 - self.texts[i].get_width() // 2, self.height * 0.05 + i * 1.05 * self.texts[i].get_height())) #Blit texts to surface

            self.xy = (SETTINGS["width"] // 2 - self.width // 2, SETTINGS["height"] // 2 - self.height // 2) #Position for the alert to be displayed

        def detect_click(self, clickPos):
            if clickPos[0] in range(self.xy[0] + self.width // 2 - self.button_width // 2, self.xy[0] + self.width // 2 - self.button_width // 2 + self.button_width) and clickPos[1] in range(self.xy[1] + int(self.height*0.95 - self.button_height), self.xy[1] + int(self.height*0.95 - self.button_height) + self.button_height):
                self.visible = False
                return True
            return False

        def new(text="Sample text"):
            global ALERTS
            ALERTS += [holo_prefabs.alert(text)]

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
                self.text_renders += [FONTS["p-sans-serif"].render(text_cutoff(i, int(self.width - (holo_assets.prefabs.dropdown.arrow_left.get_width() * 2) - int(self.width * 0.05)), FONTS["p-sans-serif"]), True, holo_color.system.text_color)]


            self.text_render = self.text_renders[self.selected]

            self.empty_surface = pygame.Surface([int(self.width), int(SETTINGS["height"] // 15)], pygame.SRCALPHA).convert_alpha()

            self.empty_surface.fill([50,50,50,128] if SETTINGS["theme"] == "dark" else [200,200,200,128])

            self.empty_surface.blit(holo_assets.prefabs.dropdown.arrow_right, [width - holo_assets.prefabs.dropdown.arrow_right.get_width(), self.empty_surface.get_height() // 2 - holo_assets.prefabs.dropdown.arrow_right.get_height() // 2])
            self.empty_surface.blit(holo_assets.prefabs.dropdown.arrow_left, [0, self.empty_surface.get_height() // 2 - holo_assets.prefabs.dropdown.arrow_right.get_height() // 2])

            self.surface = self.empty_surface.copy()
            self.surface.blit(self.text_render, [holo_assets.prefabs.dropdown.arrow_left.get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])



        def detect_click(self, pos):

            if pos[0] in range(self.pos[0], self.pos[0] + self.width) and pos[1] in range(self.pos[1], self.pos[1] + self.empty_surface.get_height()):
                if pos[0] - self.pos[0] in range(0, holo_assets.prefabs.dropdown.arrow_left.get_width()):
                    pygame.draw.rect(self.surface, holo_color.system.text_color, [0, 0, holo_assets.prefabs.dropdown.arrow_left.get_width(), self.surface.get_height()])
                    screen.blit(self.surface, self.pos)
                    pygame.display.flip()
                    self.selected -= 1 if self.selected > 0 else 0
                    self.text_render = self.text_renders[self.selected]
                    self.surface = self.empty_surface.copy()
                    self.surface.blit(self.text_render, [holo_assets.prefabs.dropdown.arrow_left.get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])
                if pos[0] - self.pos[0] in range(self.width - holo_assets.prefabs.dropdown.arrow_right.get_width(), self.width):
                    pygame.draw.rect(self.surface, holo_color.system.text_color, [self.width - holo_assets.prefabs.dropdown.arrow_right.get_width(), 0, self.width , self.surface.get_height()])
                    screen.blit(self.surface, self.pos)
                    pygame.display.flip()
                    self.selected += 1 if len(self.items) - 1 > self.selected else 0
                    self.text_render = self.text_renders[self.selected]
                    self.surface = self.empty_surface.copy()
                    self.surface.blit(self.text_render, [holo_assets.prefabs.dropdown.arrow_left.get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])




                return True

            return False

        def update(self):
            self.text_render = self.text_renders[self.selected]
            self.surface = self.empty_surface.copy()
            self.surface.blit(self.text_render, [holo_assets.prefabs.dropdown.arrow_left.get_width(), self.empty_surface.get_height() // 2 -self.text_render.get_height() // 2])
