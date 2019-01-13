import abjad
from abjadext import tonality
import itertools
from adjacency_witness import AdjacencyWitness
from suspension_witness import SuspensionWitness

score = abjad.Score()
top = abjad.Staff("a'4 c'' c'' e'' d'' d'' c'' c'' b'4 a'4 a'4 b'4")
bottom = abjad.Staff("f'4 a' a' g' f' f' e' e' d'4 f'4 f'4 g'")
score.extend([top, bottom])

vertical_moments = list(abjad.iterate(score).vertical_moments())

for first, second, third in zip(vertical_moments, vertical_moments[1:], vertical_moments[2:]):
    first_adjacency = AdjacencyWitness(first, second)
    second_adjacency = AdjacencyWitness(second, third)
    suspension_witness = SuspensionWitness(first_adjacency, second_adjacency)
    if suspension_witness.is_seven_six_suspension_candidate():
        suspension_witness.color_suspension_candidate()
    if suspension_witness.is_four_three_suspension_candidate():
        suspension_witness.color_suspension_candidate()


abjad.show(score)
