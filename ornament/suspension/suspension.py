import abjad

class Suspension:
    def __init__(self, selection):
        self.selection = selection
        self.offsets = [abjad.inspect(note).vertical_moment().offset for note in selection]

    def __repr__(self):
        return "Suspension() starting at " + str(self.offsets[0])
