# passaggi test code
# Jeff Trevino; Winter, 2019
# ornaments each melody note with a passaggio

import random
import abjad
from passaggi import Passaggio
from abjadext import tonality
from ornaments import ornament_dictionary

scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[E3, C6]')

score = abjad.Score()

def ornament_melody(melody):
    # ornament each note of a melody with a passaggio:
    out = abjad.Staff()
    ties = list(abjad.iterate(staff).logical_ties(pitched=True))
    for x, tie in enumerate(ties):
        if x < len(ties) - 1:
            print(tie)
            present_witness = tie
            future_witness = ties[x + 1]
            passaggio = Passaggio(ornament_dictionary, scale, pitch_range)
            replacement_leaves = passaggio((present_witness, future_witness))
        else:
            replacement_leaves = abjad.mutate(ties[-1]).copy()
        out.append(replacement_leaves)
    return out

# staff = abjad.Staff("c'4 d' c' e' c' f' c' b c' a c' g c' c' c'")
staff = abjad.Staff("c'4 c' c' c'")
copy = abjad.mutate(staff).copy()
for leaf in copy:
    abjad.mutate(leaf).transpose(-12)
abjad.attach(abjad.Clef('bass'), copy[0])
output = ornament_melody(staff)
score.append(output)
score.append(copy)
abjad.show(score)
