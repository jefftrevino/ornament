import itertools
import random
import abjad
from ornament.suspension.suspension_witness import SuspensionWitness
from ornament.adjacency.adjacency_witness import AdjacencyWitness
from ornament.suspension.suspension_dictionary import suspension_dictionary

class SuspensionDecorator:
    def __init__(self, input_score):
        self.input_score = input_score

    def make_empty_output_score(self):
        self.output_score = abjad.Score([abjad.Staff() for staff in self.input_score])

    def witness_suspensions(self):
        self.suspension_witness = SuspensionWitness()
        self.vertical_moments = list(abjad.iterate(self.input_score).vertical_moments())
        for first, second, third in zip(self.vertical_moments, self.vertical_moments[1:], self.vertical_moments[2:]):
                self.identify_suspension_leaves_in_voice_pairs((first, second, third))
        self.possible_suspensions = self.suspension_witness.possible_suspensions
        print(self.possible_suspensions)

    def identify_suspension_leaves_in_voice_pairs(self, moments):
        for index_pair in itertools.combinations(range(len(self.input_score)), 2):
            first_adjacency = AdjacencyWitness(moments[0], moments[1], index_pair)
            second_adjacency = AdjacencyWitness(moments[1], moments[2], index_pair)
            self.suspension_witness(first_adjacency, second_adjacency, index_pair)
            # debug coloring
            if self.suspension_witness.is_suspension_candidate():
                self.suspension_witness.color_suspension_candidate()
