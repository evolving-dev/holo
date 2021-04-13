class holo_color:

    class system:

        text_color = [255, 255, 255] if SETTINGS["theme"] == "dark" else [0,0,0]
        theme_color = [255, 255, 255] if SETTINGS["theme"] == "light" else [0,0,0]

    class transform:

        def invert(color):
            for i in range(len(color)):
                color[i] = 255 - color[i]
            return color
