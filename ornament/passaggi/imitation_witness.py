# imitation witness
# Jeff Trevino, 2019
# traverses a score three adjacencies wide to store possible imitations

import abjad
from ornament.passaggi.imitation import Imitation
from ornament.adjacency.adjacency import Adjacency

class ImitationWitness:
    def __init__(self, scale, pitch_range):
        self.scale = scale
        self.pitch_range = pitch_range
        self.possible_imitations = []

    def __call__(self, score, debug=False):
        self.score = score
        moments = list(abjad.iterate(score).vertical_moments())
        for tetramoment in zip(moments, moments[1:], moments[2:], moments[3:]):
            print(tetramoment)
            if self.begins_in_valid_metrical_position(tetramoment[0]) \
            and self.all_contain_three_start_notes(tetramoment):
                adjacencies = self.make_adjacencies(tetramoment)
                self.witness_imitations_in_score(adjacencies)

        if debug:
            for i in self.possible_imitations:
                self.color_imitation(i)

    def all_contain_three_start_notes(self, tetramoment):
        if False in [3 == len(moment.start_notes) for moment in tetramoment]:
            return False
        else:
            return True

    def begins_in_valid_metrical_position(self, first_moment):
        if 0 == first_moment.offset % abjad.Duration(1,4):
            return True
        return False


    def witness_imitations_in_score(self, adjacencies):
        self.witness_triple_imitations(adjacencies)
        self.witness_double_imitations(adjacencies)

    def witness_triple_imitations(self, adjacencies):
        if self.is_triple_imitation(adjacencies):
            imitation = Imitation(self.scale, self.pitch_range, adjacencies)
            self.possible_imitations.append(imitation)

    def witness_double_imitations(self, adjacencies):
        result = self.is_double_imitation(adjacencies)
        if result:
            source_adjacencies = [adjacencies[index] for index in result]
            imitation = Imitation(self.scale, self.pitch_range, source_adjacencies)
            self.possible_imitations.append(imitation)

    def make_adjacencies(self, tetramoment):
        adjacencies = [
            Adjacency(tetramoment[0], tetramoment[1], 0),
            Adjacency(tetramoment[1], tetramoment[2], 1),
            Adjacency(tetramoment[2], tetramoment[3], 2)
        ]
        return adjacencies

    def is_triple_imitation(self, adjacencies):
        if adjacencies[0].melodic_interval == \
        adjacencies[1].melodic_interval == \
        adjacencies[2].melodic_interval:
            return True
        return False

    def is_double_imitation(self, adjacencies):
        if adjacencies[0].melodic_interval == adjacencies[1].melodic_interval:
            return (0,1)
        elif adjacencies[1].melodic_interval == adjacencies[2].melodic_interval:
            return (1,2)
        else:
            return ()

    def color_imitation(self, imitation):
        adjacencies = imitation.adjacencies
        for a in adjacencies:
            abjad.override(a.from_note).note_head.color = 'red'
            abjad.override(a.to_note).note_head.color = 'red'
