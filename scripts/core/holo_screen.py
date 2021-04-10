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

        def show(self):

            holo_screen.objects[self.uuid].visible = True

        def is_visible(self):

            return holo_screen.objects[self.uuid].visible

        def set_color(self, color):

            holo_screen.objects[self.uuid].color = color
            holo_screen.objects[self.uuid].rerender = True

        def get_color(self):

            return holo_screen.objects[self.uuid].color

        def set_text(self, text):

            holo_screen.objects[self.uuid].text = text
            holo_screen.objects[self.uuid].rerender = True

        def move(self, pos):

            holo_screen.objects[self.uuid].pos = pos

        def get_pos(self):

            return holo_screen.objects[self.uuid].pos

        def get_width(self):

            return holo_screen.objects[self.uuid].width

        def get_height(self):

            return holo_screen.objects[self.uuid].height

        def rerender(self):

            holo_screen.objects[self.uuid].rerender = True
            holo_screen.objects[self.uuid].update()

    def draw():
        for i in list(holo_screen.objects.keys()):
            holo_screen.objects[i].update()
