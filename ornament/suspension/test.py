import abjad
from abjadext import tonality
import itertools
from ornament.suspension.suspension_decorator import SuspensionDecorator
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.skeletons import skeleton


def fix_meter(score):
    for staff in score:
        abjad.mutate(staff[:]).split(durations=[(4,4)], cyclic=True)



scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[E3, C6]')

# score = abjad.Score()
# top = abjad.Staff("a'4 c'' c'' e'' d'' d'' c'' c'' b'4 a'4 a'4 b'4 c'1")
# middle = abjad.Staff("f'4 a' a' g' f' f' e' e' d'4 f'4 e'4 e' c'1")
# bottom = abjad.Staff("d' f' f' c' bf bf c' c' g a g g c'1")
# score.extend([top, middle, bottom])

decorator = SuspensionDecorator(scale, pitch_range, suspension_dictionary)
decorator(skeleton)
fix_meter(skeleton)
abjad.f(skeleton)
