import abjad
from abjadext import tonality
from ornament.suspension.suspension import Suspension

class SuspensionWitness:

    def __init__(self):
        self.possible_suspensions = {}
        self.test_dict = {'fourthree':[
                        self.top_voice_descends_by_step,
                        self.moves_to_third,
                        self.voices_stay_put_for_second_adjacency,
                                    ],

                        'sevensix': [
                        self.top_voice_descends_by_step,
                        self.is_all_sixths,
                        self.voices_stay_put_for_second_adjacency,
                                    ]
                        }

    def __call__(self, first_adjacency, second_adjacency, index_pair):
        self.first_adjacency = first_adjacency
        self.second_adjacency = second_adjacency
        self.index_pair = index_pair

    def is_all_sixths(self):
        if '6' == \
        self.first_adjacency.from_harmonic_interval.name[-1] == \
        self.first_adjacency.to_harmonic_interval.name[-1] == \
        self.second_adjacency.from_harmonic_interval.name[-1] == \
        self.second_adjacency.to_harmonic_interval.name[-1]:
            return True
        else:
            return False
    def moves_to_third(self):
        if '3' == self.first_adjacency.to_harmonic_interval.name[-1]:
            return True
        else:
            return False

    def voices_stay_put_for_second_adjacency(self):
        if '1' == self.second_adjacency.top_melodic_interval.name[-1] == \
        self.second_adjacency.bottom_melodic_interval.name[-1]:
            return True
        else:
            return False

    def top_voice_descends_by_step(self):
        analyzer = tonality.analyze([
            self.first_adjacency.present_moment.start_leaves[self.index_pair[0]],
            self.first_adjacency.future_moment.start_leaves[self.index_pair[0]],
            ])
        return analyzer.are_stepwise_descending_notes()

    def register_suspension_leaves(self):
        top = (self.first_adjacency.present_moment.start_leaves[self.index_pair[0]],
        self.first_adjacency.future_moment.start_leaves[self.index_pair[0]],
        self.second_adjacency.future_moment.start_leaves[self.index_pair[0]],
        )
        bottom = (self.first_adjacency.present_moment.start_leaves[self.index_pair[1]],
        self.first_adjacency.future_moment.start_leaves[self.index_pair[1]],
        self.second_adjacency.future_moment.start_leaves[self.index_pair[1]],
        )
        self.suspension_leaves = {}
        self.suspension_leaves['top'] = abjad.select(top[:])
        self.suspension_leaves['bottom'] = abjad.select(bottom[:])

    def add_markup_to_suspension_leaves(self, color):
        for x, leaf in enumerate(self.suspension_leaves):
            abjad.override(leaf).note_head.color = color
            markup = abjad.Markup(str(x+1), direction = abjad.Up)
            abjad.attach(markup, leaf)

    def add_possible_suspension(self, suspension):
        index_pair = self.index_pair
        start_offset = suspension.offsets[0]
        if start_offset not in self.possible_suspensions:
            self.possible_suspensions[start_offset] = {}
        offset_dict = self.possible_suspensions[start_offset]
        if index_pair in offset_dict:
            offset_dict[index_pair].append(suspension)
        else:
            offset_dict[index_pair] = [suspension]

    def is_suspension_candidate(self):
        for key in self.test_dict.keys():
            if not (False in [test_function() for test_function in self.test_dict[key]]):
                self.register_suspension_leaves()
                self.add_possible_suspension(Suspension(self.suspension_leaves, self.index_pair))
                return True
        return False

    def color_suspension_candidate(self):
        if self.is_seven_six_suspension_candidate():
            color = 'red'
            self.add_markup_to_suspension_leaves(color)
        elif self.is_four_three_suspension_candidate():
            color = 'green'
            self.add_markup_to_suspension_leaves(color)
