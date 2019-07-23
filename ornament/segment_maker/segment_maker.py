# segment maker
# Jeff Trevino; Summer, 2019
# adds suspensions,
# fuses non-suspension halves,
# ornaments unisons,
# adds passaggi

import random
from collections import defaultdict

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

    def __call__(self, skeleton, dict_tuple, n_attacks=None):
        '''
        inputs:
        skeleton: (abjad.Score) three-voice quarter-note texture
        dict_tuple: tuple containing (1) suspension dict (2) passagi dict (3) unison dict
        n_attacks: filter unison and passaggi dictionaries to include ornaments of only up to n attacks
        Note that the passaggi dictionary must have at least two ornaments per  interval;
        otherwise, imitation will be stuck in an infinite while loop
        '''
        self.skeleton = skeleton
        self.suspension_dictionary, self.passaggi_dictionary, self.unison_dictionary = dict_tuple
        if n_attacks:
            self.n_attacks = n_attacks
            self.filter_ornaments_by_attack_count()
        self.decorate_skeleton()
        self.fix_meter_at_measure_boundaries(abjad.Duration(1,2))
        self.rosatize()

    def fix_meter_at_measure_boundaries(self, chop_duration):
        for staff in self.skeleton:
            abjad.mutate(staff[:]).split(durations=[chop_duration], cyclic=True)

    def filter_ornaments_by_attack_count(self):
        self.filter_passaggi_by_attack_count()
        # self.filter_unisons_by_attack_count()

    def filter_passaggi_by_attack_count(self):
        output = {}
        for interval_key, ornament_dict in self.passaggi_dictionary.items():
            output[interval_key] = {name: o_tuple for name, o_tuple in ornament_dict.items() if len(o_tuple[0]) <= self.n_attacks}
        self.passaggi_dictionary = output

    def filter_unisons_by_attack_count(self):
        output = {}
        for duration, ornament_list in self.unison_dictionary.items():
            output[duration] = [ornament for ornament in ornament_list if len(ornament) <= self.n_attacks]
        self.unison_dictionary = output

    def decorate_skeleton(self):
        suspension_decorator = SuspensionDecorator(self.scale, self.pitch_range, self.suspension_dictionary)
        suspension_decorator(self.skeleton)
        dict_dict = {'unison': self.unison_dictionary, 'passaggi': self.passaggi_dictionary}
        ornament_decorator = OrnamentDecorator(self.scale, self.pitch_range, dict_dict)
        ornament_decorator(self.skeleton) # add debug=False to debug
        print('got here')
        unison_decorator = UnisonDecorator(self.unison_dictionary)
        unison_decorator(self.skeleton)

    def rosatize(self):
        # transposing up an octave and add dynamic for Rosa Guitar Trio
        for staff in self.skeleton:
            first_leaf = abjad.inspect(staff).leaf(0)
            abjad.attach(abjad.Dynamic('pp'), first_leaf)
            for note in abjad.iterate(staff).components(prototype=abjad.Note):
                note.written_pitch += 12
