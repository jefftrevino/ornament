# unison decorator
# Jeff Trevino, 2019
# This class uses a unison witness to find successions of the same pitch
# And then fuse and articulate them in various ways

import abjad
from ornament.unison.unison_witness import UnisonWitness

class UnisonDecorator:
    def __init__(self, unison_dictionary):
        self.unison_dictionary = unison_dictionary

    def __call__(self, score):
        self.witness_score(score)
        self.decorate_score()

    def witness_score(self, score):
        witness = UnisonWitness()
        self.possible_unisons = witness(score)

    def choose_different_props(self, first, second):
        first.choose_proportion(self.unison_dictionary)
        second.choose_proportion(self.unison_dictionary)
        while first.proportion == second.proportion:
            second.choose_proportion(self.unison_dictionary)

    def decorate_score(self):
        for key in self.possible_unisons:
            unison_list = self.possible_unisons[key]
            of_concern = [unison for unison in unison_list if abjad.Duration(4,4) <= unison.duration]
            if 2 == len(of_concern) and of_concern[0].duration == of_concern[1].duration:
                self.choose_different_props(of_concern[0], of_concern[1])
            for unison in unison_list:
                if abjad.Duration(1,2) <= unison.duration:
                    unison(self.unison_dictionary, debug=False)
