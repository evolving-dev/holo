class holo_gui:

    def responsive_scale(image,new_scale): #Function to scale an image without stretching
        im = image
        old_width, old_height = im.size

        # Center the image
        
        paste_coords = [(new_scale[0] - old_width) // 2,(new_scale[1] - old_height) // 2]
        newImage = Image.new("RGBA", tuple(new_scale),(255,255,255,255))
        newImage.paste(im, (paste_coords[0], paste_coords[1], paste_coords[0] + old_width, paste_coords[1] + old_height))

        return newImage

    def load_image(path, size, aa=True, alpha=True):
        if aa:#Antialiasing enabled

            if alpha:#Alpha channel enabled
                return pygame.image.fromstring(Image.open(path).resize(tuple(size)).tobytes(), tuple(size), "RGBA").convert_alpha()
            else:
                return pygame.image.fromstring(Image.open(path).resize(tuple(size)).tobytes(), tuple(size), "RGB").convert()

        else:

            if alpha:#Alpha channel enabled
                return pygame.transform.scale(pygame.image.load(path).convert_alpha(), list(size))
            else:
                return pygame.transform.scale(pygame.image.load(path).convert(), list(size))


    class background:

        def show():
            global DISPLAY_BACKGROUND
            DISPLAY_BACKGROUND = True

        def hide():
            global DISPLAY_BACKGROUND
            DISPLAY_BACKGROUND = False

        def is_visible():
            return DISPLAY_BACKGROUND

        def set_background(image_path): #TODO: CLEAN UP
            holo_assets.system.background = Image.open(image_path)

            BACKGROUND_SIZE_CACHE = holo_assets.system.background.size

            TRANSFORM_CACHE = [
                [SETTINGS["width"], round(BACKGROUND_SIZE_CACHE[1] * (SETTINGS["width"] / BACKGROUND_SIZE_CACHE[0]))],
                [round(BACKGROUND_SIZE_CACHE[0] * (SETTINGS["height"] / BACKGROUND_SIZE_CACHE[1])), SETTINGS["height"]] #Try to resize the image to as small of a size as possible, while staying over the screen resolution and maintaining aspect ratio
                               ]

            if TRANSFORM_CACHE[0][1] >= SETTINGS["height"]:
                holo_assets.system.background = holo_assets.system.background.resize(tuple(TRANSFORM_CACHE[0]))

            elif TRANSFORM_CACHE[1][0] >= SETTINGS["width"]:
                holo_assets.system.background = holo_assets.system.background.resize(tuple(TRANSFORM_CACHE[1]))


            holo_assets.system.background = holo_gui.responsive_scale(holo_assets.system.background,[SETTINGS["width"], SETTINGS["height"]]) #Crop to center of image

            holo_assets.system.background = pygame.image.fromstring(holo_assets.system.background.convert("RGB").tobytes(),(SETTINGS["width"],SETTINGS["height"]),"RGB").convert()
