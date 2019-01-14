import abjad
from ornament.fusion.fusion_witness import FusionWitness

score = abjad.Score()
top = abjad.Staff("c' c' d' d' e' f' f' f'")
bottom = abjad.Staff("b b b a g g g f f f f")
score.extend([top, bottom])
witness = FusionWitness()
witness(score)
abjad.show(score)
