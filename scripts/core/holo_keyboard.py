class holo_keyboard:

    class Keyboard:

        def __init__(self):

            self.text = ""
            self.uppercase = False
            self.visible = False
            self.surface = {"lower" : holo_assets.keyboard.lower, "upper" : holo_assets.keyboard.upper} #Load keyboard
            self.keymap = KEYMAP

        def reset(self):

            self.text = ""
            self.visible = False
            self.uppercase = False

        def update(self, mousePos):

            for i in list(KEYMAP["upper" if self.uppercase else "lower"].keys()):
                if mousePos[0] in range(KEYMAP["upper" if self.uppercase else "lower"][i][0][0], KEYMAP["upper" if self.uppercase else "lower"][i][1][0]):
                    if mousePos[1] in range(KEYMAP["upper" if self.uppercase else "lower"][i][0][1], KEYMAP["upper" if self.uppercase else "lower"][i][1][1]):
                        self.text += "\n" if i == "|" else "" if (i == "<<" or i == "^") else i
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
