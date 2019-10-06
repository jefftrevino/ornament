# passaggi test code
# Jeff Trevino; Winter, 2019
# adds suspensions,
# fuses non-suspension halves,
# ornaments unisons,
# adds passaggi

import random
import abjad

from abjadext import tonality
from ornament.skeletons.preprocess_skeleton import preprocessed_skeletons
from ornament.skeletons.SkeletonMaker import SkeletonMaker
from ornament.suspension.suspension_decorator import SuspensionDecorator
from ornament.passaggi.ornament_decorator import OrnamentDecorator
from ornament.unison.unison_decorator import UnisonDecorator
from ornament.segment_maker.segment_maker import SegmentMaker
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.passaggi.passaggi_dictionary import passaggi_dictionary
from ornament.unison.unison_dictionary import unison_dictionary

random.seed(3) # 2, 3,  is not bad

pset = abjad.PitchSet(
["g'", "a'", "b'"],
item_class=abjad.NamedPitch,
)

# choose a skeleton
# skeleton = preprocessed_skeletons[1]
skeleton_maker = SkeletonMaker(pset)
skeleton = skeleton_maker(abjad.Duration(1,4), 10)
scale = tonality.Scale(('a', 'minor'))
pitch_range = abjad.pitch.PitchRange('[E2, B5]')
dict_tuple = (suspension_dictionary, passaggi_dictionary, unison_dictionary)

maker = SegmentMaker(scale, pitch_range)
maker(skeleton, dict_tuple, n_attacks=3) # calling the maker instance configures and decorates

lilypond_file = abjad.LilyPondFile.new(music=maker.skeleton)

lilypond_file.header_block.title = abjad.Markup(r'Past Machine 1')
lilypond_file.header_block.composer = abjad.Markup('J. R. Trevino, 2019')

abjad.show(lilypond_file)
abjad.play(lilypond_file)
