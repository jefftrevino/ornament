# segment maker
# Jeff Trevino; Summer, 2019
# adds suspensions,
# fuses non-suspension halves,
# ornaments unisons,
# adds passaggi

import random
import abjad

from ornament.suspension.suspension_decorator import SuspensionDecorator
from ornament.passaggi.ornament_decorator import OrnamentDecorator
from ornament.unison.unison_decorator import UnisonDecorator
from ornament.suspension.suspension_dictionary import suspension_dictionary
from ornament.passaggi.passaggi_dictionary import passaggi_dictionary
from ornament.unison.unison_dictionary import unison_dictionary

class SegmentMaker:
    def __init__(self, scale, pitch_range):
        self.scale = scale
        self.pitch_range = pitch_range

    def __call__(self, skeleton, dict_tuple):
        '''
        inputs:
        skeleton: (abjad.Score) three-voice quarter-note texture
        dict_tuple: tuple containing (1) suspension dict (2) passagi dict (3) unison dict
        '''
        self.skeleton = skeleton
        self.suspension_dictionary, self.passaggi_dictionary, self.unison_dictionary = dict_tuple
        self.decorate_skeleton()
        self.fix_meter_at_measure_boundaries(abjad.Duration(1,2))
        self.rosatize()

    def fix_meter_at_measure_boundaries(self, chop_duration):
        for staff in self.skeleton:
            abjad.mutate(staff[:]).split(durations=[chop_duration], cyclic=True)

    def decorate_skeleton(self):
        suspension_decorator = SuspensionDecorator(self.scale, self.pitch_range, self.suspension_dictionary)
        suspension_decorator(self.skeleton)
        dict_dict = {'unison': self.unison_dictionary, 'passaggi': self.passaggi_dictionary}
        ornament_decorator = OrnamentDecorator(self.scale, self.pitch_range, dict_dict)
        ornament_decorator(self.skeleton) # add debug=False to debug
        unison_decorator = UnisonDecorator(self.unison_dictionary)
        unison_decorator(self.skeleton)

    def rosatize(self):
        # transposing up an octave and add dynamic for Rosa Guitar Trio
        for staff in self.skeleton:
            first_leaf = abjad.inspect(staff).leaf(0)
            abjad.attach(abjad.Dynamic('pp'), first_leaf)
            for note in abjad.iterate(staff).components(prototype=abjad.Note):
                note.written_pitch += 12
