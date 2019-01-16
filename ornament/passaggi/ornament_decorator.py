# ornament (passaggi, unison, and imitation) decorator
# Jeff Trevino, 2019
# fuses quarters into halves, unless suspensions,
# then traverses for imitations
# then traverses for passaggi

import abjad
from ornament.passaggi.imitation_witness import ImitationWitness

class OrnamentDecorator:
    def __init__(self, scale, pitch_range, dict_dict):
        self.scale = scale
        self.pitch_range = pitch_range
        self.dict_dict = dict_dict

    def __call__(self, score, debug=False):
        first_leaf = abjad.inspect(score[0]).leaf(0)
        self.resolution = abjad.Duration(first_leaf.written_duration)
        self.score = score
        self.debug = debug
        self.fuse_moments()
        self.add_imitations()

    def is_suspension_indicator(self, indicator):
        if 'suspension' == indicator.string:
            return True
        return False

    def contains_suspension(self, leaves):
        for leaf in leaves:
            indicators = abjad.inspect(leaf).indicators()
            for indicator in indicators:
                if isinstance(indicator, abjad.LilyPondComment):
                    if self.is_suspension_indicator(indicator):
                        return True
            return False

    def collect_indicators(self, selection):
        indicators = []
        for leaf in selection[1:]:
            indicators = abjad.inspect(leaf).indicators()
            if indicators:
                indicators.extend(indicators)
        return indicators

    def attach_indicators_to_leaf(self, indicators, leaf):
        for i in indicators:
            abjad.attach(i, leaf)

    def fuse_selection(self, selection):
        indicators = self.collect_indicators(selection)
        fused = abjad.mutate(selection).fuse()
        if indicators:
            self.attach_indicators_to_leaf(indicators, fused[0])

    def are_both_quarters(self, one, two):
        if abjad.Duration(1,4) == one.written_duration == two.written_duration:
            return True
        print("not both quarters")
        print(one, two)
        return False

    def contains_only_quarters(self, note_pair):
        if abjad.Duration(1,4) == note_pair[0].written_duration == note_pair[1].written_duration:
            return True
        return False

    def all_quarters(self, moment, moment_two):
        for staff_index in range(len(self.score)):
            if not self.contains_only_quarters((moment.start_notes[staff_index], moment_two.start_notes[staff_index])):
                return False
        return True

    def get_adjacency_pairs(self, moment_one, moment_two):
        pairs = []
        for staff_index in range(len(self.score)):
            print(moment_one)
            print(moment_two)
            print(moment_one.start_notes)
            print(moment_two.start_notes)
            pair = (moment_one.start_notes[staff_index], moment_two.start_notes[staff_index])
            pairs.append(pair)
        return pairs

    def fuse_moments(self):
        for staff in self.score:
            for pair in abjad.iterate(staff).leaf_pairs():
                if self.resolution == pair[0].written_duration == pair[1].written_duration \
                and pair[0].written_pitch == pair[1].written_pitch \
                and 0 == abjad.inspect(pair[0]).vertical_moment().offset % (2 * self.resolution) \
                and not self.contains_suspension(pair):
                    abjad.mutate(pair).fuse()

    def add_imitations(self):
        self.witness_imitations()
        if not self.debug:
            self.decorate_imitations()

    def witness_imitations(self):
        imitation_witness = ImitationWitness(self.scale, self.pitch_range)
        self.possible_imitations = imitation_witness(self.score, debug = self.debug)

    def decorate_imitations(self):
        passaggi_dict = self.dict_dict['passaggi']
        for imitation in self.possible_imitations:
            if imitation.adjacencies[0].from_note in imitation.pitch_list:
                imitation(passaggi_dict)
