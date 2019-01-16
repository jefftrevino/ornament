# passaggi test code
# Jeff Trevino; Winter, 2019
# adds suspensions,
# fuses non-suspension halves,
# ornaments unisons,
# adds passaggi

import random
import abjad
from ornament.passaggi.passaggio import Passaggio
from abjadext import tonality
from ornament.passaggi.passaggi_dictionary import passaggi_dictionary
from ornament.unison.unison_dictionary import unison_dictionary
from ornament.skeletons import skeleton
from ornament.unison.unison_decorator import UnisonDecorator
from ornament.suspension.suspension_decorator import SuspensionDecorator
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.passaggi.ornament_decorator import OrnamentDecorator

random.seed(2)
scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[E2, B5]')

def fix_meter(score, chop_duration):
    for staff in score:
        abjad.mutate(staff[:]).split(durations=[chop_duration], cyclic=True)

suspension_decorator = SuspensionDecorator(scale, pitch_range, suspension_dictionary)
suspension_decorator(skeleton)
dict_dict = {'unison': unison_dictionary, 'passaggi': passaggi_dictionary}
ornament_decorator = OrnamentDecorator(scale, pitch_range, dict_dict)
ornament_decorator(skeleton, debug=False)
fix_meter(skeleton, abjad.Duration(1,4))
first_bass_leaf = abjad.inspect(skeleton[2]).leaf(0)
abjad.attach(abjad.Clef('bass'), first_bass_leaf)
abjad.show(skeleton)
