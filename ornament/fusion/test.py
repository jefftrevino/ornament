import abjad
from ornament.fusion.fusion_decorator import FusionDecorator
from ornament.skeletons import skeleton
from ornament.fusion.fusion_dictionary import fusion_dictionary

# score = abjad.Score()
# top = abjad.Staff("c' c' d' d' e' f' f' f'")
# bottom = abjad.Staff("b b b a g g g f f f f")
# score.extend([top, bottom])
decorator = FusionDecorator(fusion_dictionary)
decorator(skeleton)
first_bass_leaf = abjad.inspect(skeleton[2][0]).leaf(0)
abjad.attach(abjad.Clef('bass'), first_bass_leaf)
abjad.play(skeleton)
