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