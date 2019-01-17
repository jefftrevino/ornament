# imitation
# Jeff Trevino, 2019
# models imitation for use with passaggi decorators
# then traverses for imitations
# then traverses for passaggi

import abjad
from ornament.passaggi.passaggio import Passaggio

class Imitation:
    def __init__(self, scale, pitch_range, adjacencies):
        self.scale = scale
        self.pitch_range = pitch_range
        self.pitch_list = self.sorted_pitch_list_from_scale_and_pitch_range()
        self.adjacencies = adjacencies

    def __call__(self, passaggi_dictionary, last_ornament=None):
        self.last_ornament = last_ornament
        self.dictionary = passaggi_dictionary
        self.length = len(self.adjacencies)
        passaggio = self.set_up_passaggio()
        self.mutate_leaves(passaggio)
        return self.last_ornament

    def sorted_pitch_list_from_scale_and_pitch_range(self):
        named_pitch_set = self.scale.create_named_pitch_set_in_pitch_range(self.pitch_range)
        return sorted(list(named_pitch_set))

    def ornaments_are_equal(self, orn1, orn2):
        if self.last_ornament == None:
            return False
        elif orn1 == orn2 or orn1 == (orn2[0], [pitch * -1 for pitch in orn2[1]]):
            return True

    def set_up_passaggio(self):
        passaggio = Passaggio(self.dictionary, self.scale, self.pitch_range)
        first_a = self.adjacencies[0]
        passaggio.get_interval_from_witnesses((first_a.from_note, first_a.to_note))
        passaggio.look_up_ornament()
        while self.ornaments_are_equal(passaggio.ornament, self.last_ornament):
            "they were equal"
            passaggio.look_up_ornament()
        self.last_ornament = passaggio.ornament
        return passaggio

    def mutate_leaves(self, passaggio):
        for adjacency in self.adjacencies:
            from_note = adjacency.from_note
            to_note = adjacency.to_note
            if self.adjacencies[0].from_note.written_pitch in passaggio.pitch_list:
                leaves = passaggio((from_note, to_note), debug=True)
                abjad.mutate(from_note).replace(leaves)
