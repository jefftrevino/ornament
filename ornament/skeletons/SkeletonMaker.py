from itertools import permutations
from random import shuffle
import abjad

class SkeletonMaker:
    # todo: calculate sequences of permutations for n sets of three pitches separately,
    # then interleave the sequences to get the skeleton
    def __init__(self, pitch_set):
        self.permutations = self.make_permutations(pitch_set)
        self.permutation_sequence = self.permutations
        self.staves = [abjad.Staff(), abjad.Staff(), abjad.Staff()]

    def make_permutations(self, pitch_set):
        return list(permutations(pitch_set.items))

    def __call__(self, duration, repetitions):
        self.duration = duration
        for cycle in range(repetitions):
            shuffle(self.permutation_sequence)
            self.add_permutation_sequence_to_staves(self.permutation_sequence)
        return abjad.Score(self.staves)

    def add_permutation_sequence_to_staves(self, permutation_sequence):
        for chord in permutation_sequence:
            for staff_number, pitch in enumerate(chord):
                note = abjad.Note(pitch, self.duration)
                self.staves[staff_number].append(note)



if __name__ == "__main__":

    pset = abjad.PitchSet(
    ["g'", "a'", "b'"],
    item_class=abjad.NamedPitch,
    )

    m = SkeletonMaker(pset)
    score = m(abjad.Duration(1,4), 10)
    abjad.show(score)
    abjad.play(score)
