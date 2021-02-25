class ObjectHandler:
    def __init__(self):
        self.objects:dict = {}

    def update(self):
        for object in self.objects.values():
            #TODO: Animation cycles and event handling on objects

            if object.visible:#draw all visible objects
                screen.blit(object.surface, [object.x, object.y])

    def new(self, id, x, y, data = dict()):
        pass

    def show(self, id):
        if id in self.objects.keys():
            self.objects["id"].visible = True
            return True
        return False

    def hide(self, id):
        if id in self.objects.keys():
            self.objects["id"].visible = False
            return True
        return False

    
