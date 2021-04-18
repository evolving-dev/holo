class holo_screen:

    objects = {}

    class text:

        def __init__(self, font, text, color, pos, aa=True, visible=True):
            self.uuid = uuid.uuid4().hex

            while self.uuid in holo_screen.objects: #Generate new UUID if the one generated already exists
                self.uuid = uuid.uuid4().hex

            holo_screen.objects[self.uuid] = holo_prefabs.text(font, text, color, pos, aa, visible)

        def hide(self):

            holo_screen.objects[self.uuid].visible = False
            return self

        def show(self):

            holo_screen.objects[self.uuid].visible = True
            return self

        def is_visible(self):

            return holo_screen.objects[self.uuid].visible

        def set_color(self, color):

            holo_screen.objects[self.uuid].color = color
            holo_screen.objects[self.uuid].rerender = True
            return self

        def get_color(self):

            return holo_screen.objects[self.uuid].color

        def set_text(self, text):

            holo_screen.objects[self.uuid].text = text
            holo_screen.objects[self.uuid].rerender = True
            return self

        def move(self, pos):

            holo_screen.objects[self.uuid].pos = pos
            return self

        def get_pos(self):

            return holo_screen.objects[self.uuid].pos

        def get_width(self):

            return holo_screen.objects[self.uuid].width

        def get_height(self):

            return holo_screen.objects[self.uuid].height

        def rerender(self):

            holo_screen.objects[self.uuid].rerender = True
            holo_screen.objects[self.uuid].update()
            return self

        def center_horizontal(self, width=SETTINGS["width"], offset=0):

            holo_screen.objects[self.uuid].pos[0] = (width // 2) - (holo_screen.objects[self.uuid].width // 2) + offset
            return self

        def center_vertical(self, height=SETTINGS["height"], offset=0):

            holo_screen.objects[self.uuid].pos[1] = (height // 2) - (holo_screen.objects[self.uuid].height // 2) + offset
            return self

    class image:

        def __init__(self, image, pos, visible=True, alpha=True):
            self.uuid = uuid.uuid4().hex

            while self.uuid in holo_screen.objects: #Generate new UUID if the one generated already exists
                self.uuid = uuid.uuid4().hex

            holo_screen.objects[self.uuid] = holo_prefabs.image(image, pos, alpha, visible)

        def hide(self):

            holo_screen.objects[self.uuid].visible = False
            return self

        def show(self):

            holo_screen.objects[self.uuid].visible = True
            return self

        def is_visible(self):

            return holo_screen.objects[self.uuid].visible

        def move(self, pos):

            holo_screen.objects[self.uuid].pos = pos
            return self

        def get_pos(self):

            return holo_screen.objects[self.uuid].pos

        def get_width(self):

            return holo_screen.objects[self.uuid].width

        def get_height(self):

            return holo_screen.objects[self.uuid].height

        def center_horizontal(self, width=SETTINGS["width"], offset=0):

            holo_screen.objects[self.uuid].pos[0] = (width // 2) - (holo_screen.objects[self.uuid].width // 2) + offset
            return self

        def center_vertical(self, height=SETTINGS["height"], offset=0):

            holo_screen.objects[self.uuid].pos[1] = (height // 2) - (holo_screen.objects[self.uuid].height // 2) + offset
            return self


    class checkbox:

        def __init__(self, pos, checked=False, visible=True):
            self.uuid = uuid.uuid4().hex

            while self.uuid in holo_screen.objects: #Generate new UUID if the one generated already exists
                self.uuid = uuid.uuid4().hex

            holo_screen.objects[self.uuid] = holo_prefabs.checkbox(pos, checked, visible)

        def hide(self):

            holo_screen.objects[self.uuid].visible = False
            return self

        def show(self):

            holo_screen.objects[self.uuid].visible = True
            return self

        def is_visible(self):

            return holo_screen.objects[self.uuid].visible

        def move(self, pos):

            holo_screen.objects[self.uuid].pos = pos
            return self

        def get_pos(self):

            return holo_screen.objects[self.uuid].pos

        def get_width(self):

            return holo_screen.objects[self.uuid].width

        def get_height(self):

            return holo_screen.objects[self.uuid].height

        def center_horizontal(self, width=SETTINGS["width"], offset=0):

            holo_screen.objects[self.uuid].pos[0] = (width // 2) - (holo_screen.objects[self.uuid].width // 2) + offset
            return self

        def center_vertical(self, height=SETTINGS["height"], offset=0):

            holo_screen.objects[self.uuid].pos[1] = (height // 2) - (holo_screen.objects[self.uuid].height // 2) + offset
            return self

        def get_checked(self):

            return holo_screen.objects[self.uuid].checked

        def set_checked(self, checked):

            holo_screen.objects[self.uuid].checked = checked
            return self



    def draw():
        for i in list(holo_screen.objects.keys()):
            holo_screen.objects[i].update()

    def handle_events(event):
        if event.type == pygame.MOUSEBUTTONUP:
            for i in list(holo_screen.objects.keys()):
                if "detect_click" in dir(holo_screen.objects[i]):
                    holo_screen.objects[i].detect_click(list(pygame.mouse.get_pos()))
