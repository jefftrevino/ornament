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
            self.identify_suspension_leaves_in_voice_pairs(first_adjacency, second_adjacency)

    def identify_suspension_leaves_in_voice_pair(self, first_adjacency, second_adjacency):
        first_adjacency = AdjacencyWitness(first, second)
        second_adjacency = AdjacencyWitness(second, third)


        for first, second, third in zip(vertical_moments, vertical_moments[1:], vertical_moments[2:]):
            first_adjacency = AdjacencyWitness(first, second)
            second_adjacency = AdjacencyWitness(second, third)
            suspension_witness = SuspensionWitness(first_adjacency, second_adjacency)
            if suspension_witness.is_seven_six_suspension_candidate():
                suspension_witness.color_suspension_candidate()
            if suspension_witness.is_four_three_suspension_candidate():
                suspension_witness.color_suspension_candidate()


    # def engrave_suspensions(self):
    #     for voice_pair in itertools.combinations(score[:], 2):
