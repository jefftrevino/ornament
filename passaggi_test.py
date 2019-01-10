# passaggi test code
# Jeff Trevino; Winter, 2019
# ornaments each melody note with a passaggio

import random
import abjad
from passaggi import Passaggio
from abjadext import tonality
from ornaments import ornament_dict

scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[G3, C6]')

def choose_ornament_from_dict(the_dict):
    # returns a passaggio based on a starting pitch and dictionary of ornaments
    dict_keys = list(ornament_dict.keys())
    the_key = random.choice(dict_keys)
    ornament = ornament_dict[the_key]
    return ornament

def ornament_melody(melody):
    # ornament each note of a melody with a passaggio:
    out = abjad.Staff()
    for note in staff:
        ornament = choose_ornament_from_dict(ornament_dict)
        passaggio = Passaggio(note, scale, pitch_range)
        replacement_leaves = passaggio(ornament)
        out.append(replacement_leaves)
    return out

staff = abjad.Staff("c''4. b'8 a'4 g' f'4. g'8 a'4 c'' b'4. a'8 g'4 f' e'1")
output = ornament_melody(staff)
abjad.show(output)
