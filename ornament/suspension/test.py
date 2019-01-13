import abjad
from abjadext import tonality
import itertools
from ornament.suspension.suspension_decorator import SuspensionDecorator


score = abjad.Score()
top = abjad.Staff("a'4 c'' c'' e'' d'' d'' c'' c'' b'4 a'4 a'4 b'4")
middle = abjad.Staff("f'4 a' a' g' f' f' e' e' d'4 f'4 f'4 g'")
bottom = abjad.Staff("d' f' f' c' bf bf a a g d' d' e'")
score.extend([top, middle, bottom])

decorator = SuspensionDecorator(score)
decorator.identify_suspension_leaves_in_score()


# abjad.show(score)
