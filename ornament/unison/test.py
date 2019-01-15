import abjad
from abjadext import tonality
from ornament.unison.unison_decorator import UnisonDecorator
from ornament.skeletons import skeleton
from ornament.unison.unison_dictionary import unison_dictionary
# from ornament.passaggi.passaggi import ornament_melody
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.suspension.suspension_decorator import SuspensionDecorator

scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[E2, C5]')

def fix_meter(score):
    for staff in score:
        abjad.mutate(staff[:]).split(durations=[(4,4)], cyclic=True)
        for component in staff:
            if isinstance(component, abjad.Tuplet):
                tuplet = component
                if True == tuplet.trivial():
                    component.hide = True

# def scale_skeleton(skeleton, scale factor):
#     output_score = abjad.Score()
#     for staff in skeleton:
#         for leaf in abjad.iterate(staff).leaves():
#             copies = []

def add_clef_changes(staff):
    for leaf in abjad.iterate(staff).leaves():
        clef = abjad.inspect(leaf).effective(abjad.Clef)
        if abjad.NamedPitch("g") >= leaf.written_pitch and abjad.Clef('treble') == clef:
            abjad.attach(abjad.Clef('bass'), leaf)
        elif abjad.NamedPitch("c'") <= leaf.written_pitch and abjad.Clef('bass') == clef:
            abjad.attach(abjad.Clef('treble'), leaf)

def ornament_score(score):
    for staff in score:
        ornament_melody(score)

# score = abjad.Score()
# top = abjad.Staff("c' c' d' d' e' f' f' f'")
# bottom = abjad.Staff("b b b a g g g f f f f")
# score.extend([top, bottom])
# suspension_decorator = SuspensionDecorator(scale, pitch_range, suspension_dictionary)
# suspension_decorator(skeleton)
# threshold = abjad.Duration(1,2)
# unison_decorator = UnisonDecorator(unison_dictionary)
# unison_decorator(skeleton)
#
# first_bass_leaf = abjad.inspect(skeleton[2][0]).leaf(0)
# abjad.attach(abjad.Clef('bass'), first_bass_leaf)
# first_middle_leaf = abjad.inspect(skeleton[1][0]).leaf(0)
# abjad.attach(abjad.Clef('treble'), first_middle_leaf)
# fix_meter(skeleton)
# add_clef_changes(skeleton[1])
abjad.show(skeleton)
