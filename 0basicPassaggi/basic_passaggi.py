# basic passaggi algorithm
# Jeff Trevino, 2019
# minimal strategy making a passaggio based on:
# a witness pitch
# an ornament dictionary
# a diatonic context

import abjad

class Passaggio:
    """Model of a passaggio based on a starting pitch, diatonic context, and ornament"""

    def __init__(self, witness, scale, pitch_range):
        self.witness = witness
        self.scale = scale
        self.pitch_range = pitch_range
        self.pitch_list = self.sorted_pitch_list_from_scale_and_pitch_range()

    def __call__(self, ornament):
        return self.passaggio_from_witness(ornament)

    def sorted_pitch_list_from_scale_and_pitch_range(self):
        named_pitch_set = self.scale.create_named_pitch_set_in_pitch_range(self.pitch_range)
        return sorted(list(named_pitch_set))

    def unpitched_leaves_from_ornament(self, ornament):
        num_notes = len(ornament)
        note_duration = self.witness.written_duration / num_notes
        durations = [note_duration] * num_notes
        maker = abjad.LeafMaker()
        leaves = maker(0, durations)
        return leaves

    def pitch_leaves_with_ornament(self, passaggio, ornament):
        # to pitch, which scale degree witnesses the ornament?
        witness_index = self.pitch_list.index(self.witness.written_pitch)
        # derive scale degrees from the ornament
        pitch_indexes = [witness_index + x for x in ornament]
        pitches = [self.pitch_list[x] for x in pitch_indexes]
        # then paint on pitches from the ornament
        leaves = abjad.select(passaggio).leaves()
        for leaf, pitch in zip(leaves, pitches):
            leaf.written_pitch = pitch

    def passaggio_from_witness(self, ornament):
        # make a random choice from the dictionary
        # use the chosen diminution to make new leaves from the starting pitch
        passaggio = self.unpitched_leaves_from_ornament(ornament)
        self.pitch_leaves_with_ornament(passaggio, ornament)
        return passaggio
