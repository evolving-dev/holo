class holo:

    def path(path):
        if PATH not in path:
            return join(PATH,path)
        return path



    def new_loader():
        global LOADERS
        LOADERS += [holo_prefabs.loader()]


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


    def new_alert(message="Sample Text"):

        global ALERTS
        ALERTS += [holo_prefabs.alert(message)]


    def add_to_autostart(path):
        AUTOSTART += {"app": APP, "path":holo_io.path.to_absolute(str(path))}
        holo.new_alert(SYSTEM_TEXTS["settings"]["general"]["alert_autostart"] + " " + APP)
