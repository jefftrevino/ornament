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

random.seed(5)
scale = tonality.Scale(('a', 'minor'))
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

fix_meter_at_measure_boundaries(skeleton, abjad.Duration(1,2))
# add_clef_changes(skeleton[2])
# first_bass_leaf = abjad.inspect(skeleton[2]).leaf(0)
# abjad.attach(abjad.Clef('bass'), first_bass_leaf)

def rosatize(score):
    # transposing up an octave for Rosa Guitar Trio
    for staff in score:
        first_leaf = abjad.inspect(staff).leaf(0)
        abjad.attach(abjad.Dynamic('pp'), first_leaf)
        for note in abjad.iterate(staff).components(prototype=abjad.Note):
            note.written_pitch += 12

rosatize(score)
lilypond_file = abjad.LilyPondFile.new(music=skeleton)

lilypond_file.header_block.title = abjad.Markup(r'Past Machine 1')
lilypond_file.header_block.composer = abjad.Markup('J. R. Trevino, 2019')

abjad.show(lilypond_file)
abjad.play(lilypond_file)