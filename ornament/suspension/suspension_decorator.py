import abjad
from ornament.suspension.suspension_witness import SuspensionWitness
from ornament.adjacency.adjacency_witness import AdjacencyWitness
from ornament.suspension.suspension_dictionary import suspension_dictionary
import itertools

class SuspensionDecorator:
    def __init__(self, input_score):
        self.input_score = input_score

    def make_empty_output_score(self):
        self.output_score = abjad.Score([abjad.Staff() for staff in self.input_score])

    def identify_suspension_leaves_in_score(self):
        vertical_moments = list(abjad.iterate(self.input_score).vertical_moments())
        for moment in vertical_moments:
            print(moment.start_leaves)
        for first, second, third in zip(vertical_moments, vertical_moments[1:], vertical_moments[2:]):
            self.identify_suspension_leaves_in_voice_pairs((first, second, third))

    def identify_suspension_leaves_in_voice_pairs(self, moments):
        for index_pair in itertools.combinations(range(len(self.input_score)), 2):
            print(index_pair)
            first_adjacency = AdjacencyWitness(moments[0], moments[1], index_pair)
            second_adjacency = AdjacencyWitness(moments[1], moments[2], index_pair)
            print(first_adjacency)
            print(second_adjacency)
            suspension_witness = SuspensionWitness(first_adjacency, second_adjacency, index_pair)
            print(suspension_witness.is_suspension_candidate())
            if suspension_witness.is_suspension_candidate():
                suspension_witness.color_suspension_candidate()
