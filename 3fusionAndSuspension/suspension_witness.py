import abjad

class SuspensionWitness:

    def __init__(self, first_adjacency, second_adjacency):
        self.first_adjacency = first_adjacency
        self.second_adjacency = second_adjacency

    def is_all_sixths(self):
        if '6' == \
        self.first_adjacency.from_harmonic_interval.name[-1] == \
        self.first_adjacency.to_harmonic_interval.name[-1] == \
        self.second_adjacency.from_harmonic_interval.name[-1] == \
        self.second_adjacency.to_harmonic_interval.name[-1]:
            return True
        else:
            return False

    def is_melodically_sound(self):
        # both voices descend by step in the first adjacency
        # both voices stay put in second adjacency
        print(self.first_adjacency)
        print(self.second_adjacency)
        if '-' == self.first_adjacency.top_melodic_interval.name[0] and \
        '2' == self.first_adjacency.top_melodic_interval.name[-1] and \
        '1' == self.second_adjacency.top_melodic_interval.name[-1] == \
        self.second_adjacency.bottom_melodic_interval.name[-1]:
            return True
        else:
            return False


    def is_suspension_candidate(self):
        if self.is_melodically_sound() and self.is_all_sixths():
            self.suspension_leaves = []
            self.suspension_leaves.append(self.first_adjacency.present_moment.start_leaves[0])
            self.suspension_leaves.append(self.first_adjacency.future_moment.start_leaves[0])
            self.suspension_leaves.append(self.second_adjacency.future_moment.start_leaves[0])
            return True
        else:
            return False

    def color_suspension_candidate(self):
        if self.is_suspension_candidate():
            for x, leaf in enumerate(self.suspension_leaves):
                abjad.override(leaf).note_head.color = 'red'
                markup = abjad.Markup(str(x+1), direction = abjad.Up)
                abjad.attach(markup, leaf)
