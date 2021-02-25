class HoloResponse:

    def __init__(self, success, response=None):

        self.success = success

        if response != None:

            self.response = response
