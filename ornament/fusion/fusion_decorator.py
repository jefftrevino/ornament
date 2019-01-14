# fusion decorator
# Jeff Trevino, 2019
# This class uses a fusion witness to find possible fusions
# And then it fuses them

import abjad
from ornament.fusion.fusion_witness import FusionWitness

class FusionDecorator:
    def __init__(self, fusion_dictionary):
        self.fusion_dictionary = fusion_dictionary

    def __call__(self, score):
        self.witness_score(score)
        self.decorate_score()

    def witness_score(self, score):
        witness = FusionWitness()
        self.possible_fusions = witness(score)

    def decorate_score(self):
        for key in self.possible_fusions:
            fusion_list = self.possible_fusions[key]
            for fusion in fusion_list:
                fusion(self.fusion_dictionary, debug=False)
