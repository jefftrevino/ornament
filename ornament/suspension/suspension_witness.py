import abjad
from abjadext import tonality
from ornament.suspension.suspension import Suspension

class SuspensionWitness:

    def __init__(self):
        self.possible_suspensions = {}

    def __call__(self, first_adjacency, second_adjacency, index_pair):
        self.first_adjacency = first_adjacency
        self.second_adjacency = second_adjacency
        self.staff_index = index_pair[0]

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
            self.first_adjacency.present_moment.start_leaves[self.staff_index],
            self.first_adjacency.future_moment.start_leaves[self.staff_index],
            ])
        return analyzer.are_stepwise_descending_notes()

    def is_seven_six_suspension_candidate(self):
        # top voice ascends by steps
        # all intervals are sixths
        # both voices stay put after descent
        if self.top_voice_descends_by_step() and \
        self.is_all_sixths() and \
        self.voices_stay_put_for_second_adjacency():
            self.suspension_leaves = []
            self.suspension_leaves.append(self.first_adjacency.present_moment.start_leaves[self.staff_index])
            self.suspension_leaves.append(self.first_adjacency.future_moment.start_leaves[self.staff_index])
            self.suspension_leaves.append(self.second_adjacency.future_moment.start_leaves[self.staff_index])
            return True
        else:
            return False

    def is_four_three_suspension_candidate(self):
        # top voice ascends by step to a third
        # both voices stay put in second adjacency
        if self.top_voice_descends_by_step() and \
        self.moves_to_third() and \
        self.voices_stay_put_for_second_adjacency():
            self.suspension_leaves = []
            self.suspension_leaves.append(self.first_adjacency.present_moment.start_leaves[self.staff_index])
            self.suspension_leaves.append(self.first_adjacency.future_moment.start_leaves[self.staff_index])
            self.suspension_leaves.append(self.second_adjacency.future_moment.start_leaves[self.staff_index])
            return True
        else:
            return False
    def add_markup_to_suspension_leaves(self, color):
        for x, leaf in enumerate(self.suspension_leaves):
            abjad.override(leaf).note_head.color = color
            markup = abjad.Markup(str(x+1), direction = abjad.Up)
            abjad.attach(markup, leaf)

    def add_possible_suspension(self, suspension):
        staff_index = self.staff_index
        start_offset = suspension.offsets[0]
        if start_offset not in self.possible_suspensions:
            self.possible_suspensions[start_offset] = {}
        offset_dict = self.possible_suspensions[start_offset]
        if staff_index in offset_dict:
            offset_dict[staff_index].append(suspension)
        else:
            offset_dict[staff_index] = [suspension]


    def is_suspension_candidate(self):
        if self.is_seven_six_suspension_candidate() or \
        self.is_four_three_suspension_candidate():
            self.add_possible_suspension(Suspension(abjad.Selection(self.suspension_leaves), self.staff_index))
            return True
        else:
            return False

    def color_suspension_candidate(self):
        if self.is_seven_six_suspension_candidate():
            color = 'red'
            self.add_markup_to_suspension_leaves(color)
        elif self.is_four_three_suspension_candidate():
            color = 'green'
            self.add_markup_to_suspension_leaves(color)
