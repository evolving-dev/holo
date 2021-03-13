class holo_gui:

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
