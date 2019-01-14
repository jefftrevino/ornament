import itertools
import random
import abjad
import time
from ornament.passaggi.passaggi import Passaggio
from ornament.suspension.suspension_witness import SuspensionWitness
from ornament.adjacency.adjacency import Adjacency

random.seed(4)

class SuspensionDecorator:
    def __init__(self, scale, pitch_range, suspension_dictionary):
        self.scale = scale
        self.pitch_range = pitch_range
        self.suspension_dictionary = suspension_dictionary

    def __call__(self, input_score):
        self.input_score = input_score
        self.decorate_score()

    def witness_suspensions(self):
        self.suspension_witness = SuspensionWitness()
        self.vertical_moments = list(abjad.iterate(self.input_score).vertical_moments())
        for first, second, third in zip(self.vertical_moments, self.vertical_moments[1:], self.vertical_moments[2:]):
                self.identify_suspension_leaves_in_voice_pairs((first, second, third))
        self.possible_suspensions = self.suspension_witness.possible_suspensions

    def identify_suspension_leaves_in_voice_pairs(self, moments):
        for index_pair in itertools.combinations(range(len(self.input_score)), 2):
            first_adjacency = Adjacency(moments[0], moments[1], index_pair)
            second_adjacency = Adjacency(moments[1], moments[2], index_pair)
            self.suspension_witness(first_adjacency, second_adjacency, index_pair)
            self.suspension_witness.is_suspension_candidate()
            #     self.suspension_witness.color_suspension_candidate()

    def choose_suspension_from_list(self, the_list):
        if 1 == len(the_list):
            return the_list[0]
        else:
            return random.choice(the_list)

    def choose_suspensions(self):
        # build a list of suspensions to suspend
        self.chosen_suspensions = []
        for offset_key in self.possible_suspensions.keys():
            suspensions_by_staff_dict = self.possible_suspensions[offset_key]
            dict_keys = list(suspensions_by_staff_dict.keys())
            staff_index = random.choice(dict_keys)
            suspension = suspensions_by_staff_dict[staff_index][0]
            self.chosen_suspensions.append(suspension)

    def get_note_by_offset(offset, staff):
        for note in staff:
            if abjad.inspect(note).vertical_moment().offset == offset:
                return note
        else:
            return None

    def build_suspended_staff(self, staff_index, staff):
        output_staff = abjad.mutate(staff).copy()
        if staff_index in self.decorating_dictionary:
            suspensions = self.decorating_dictionary[staff_index]
        else:
            return output_staff
        for suspension in suspensions:
            start_offset = suspension.offsets[0]
            suspension_leaves = suspension(self.scale, self.pitch_range, self.suspension_dictionary)

    def decorate_score(self):
        self.witness_suspensions()
        self.choose_suspensions()
        for s in self.chosen_suspensions:
            s(self.scale, self.pitch_range, self.suspension_dictionary)
