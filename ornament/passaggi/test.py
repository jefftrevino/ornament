# passaggi test code
# Jeff Trevino; Winter, 2019
# adds suspensions,
# fuses non-suspension halves,
# ornaments unisons,
# adds passaggi

import random
import abjad

from abjadext import tonality
from ornament.preprocess_skeleton import preprocessed_skeleton
from ornament.suspension.suspension_decorator import SuspensionDecorator
from ornament.passaggi.ornament_decorator import OrnamentDecorator
from ornament.unison.unison_decorator import UnisonDecorator
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.passaggi.passaggi_dictionary import passaggi_dictionary
from ornament.unison.unison_dictionary import unison_dictionary


skeleton = preprocessed_skeleton

random.seed(3)
scale = tonality.Scale(('g', 'major'))
pitch_range = abjad.pitch.PitchRange('[E2, B5]')

def fix_meter_at_measure_boundaries(score, chop_duration):
    for staff in score:
        abjad.mutate(staff[:]).split(durations=[chop_duration], cyclic=True)

def add_clef_changes(staff):
    effective = abjad.Clef('treble')
    for note in abjad.iterate(staff).components(prototype=abjad.Note):
        if abjad.Clef('treble') == effective and 'g' >= note.written_pitch:
            abjad.attach(abjad.Clef('bass'), note)
        elif abjad.Clef('bass') == effective and "c'" <= note.written_pitch:
            abjad.attach(abjad.Clef('treble'), note)



suspension_decorator = SuspensionDecorator(scale, pitch_range, suspension_dictionary)
suspension_decorator(skeleton)
dict_dict = {'unison': unison_dictionary, 'passaggi': passaggi_dictionary}
ornament_decorator = OrnamentDecorator(scale, pitch_range, dict_dict)
ornament_decorator(skeleton, debug=False)
unison_decorator = UnisonDecorator(unison_dictionary)
unison_decorator(skeleton)

fix_meter_at_measure_boundaries(skeleton, abjad.Duration(4,4))
add_clef_changes(skeleton[1])
first_bass_leaf = abjad.inspect(skeleton[2]).leaf(0)
abjad.attach(abjad.Clef('bass'), first_bass_leaf)

abjad.show(skeleton)
abjad.play(skeleton)
