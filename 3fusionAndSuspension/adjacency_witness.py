import abjad

class AdjacencyWitness:
    def __init__(self, present_moment, future_moment):
        self.present_moment = present_moment
        self.future_moment = future_moment
        self.from_harmonic_interval = self.calculate_and_octave_reduce_interval(
            self.present_moment.start_leaves[0],
            self.present_moment.start_leaves[1]
        )
        self.to_harmonic_interval = self.calculate_and_octave_reduce_interval(
            self.future_moment.start_leaves[0],
            self.future_moment.start_leaves[1]
        )
        self.top_melodic_interval = self.calculate_and_octave_reduce_interval(
            self.present_moment.start_leaves[0],
            self.future_moment.start_leaves[0]
        )
        self.bottom_melodic_interval = self.calculate_and_octave_reduce_interval(
            self.present_moment.start_leaves[1],
            self.future_moment.start_leaves[1]
        )

    def calculate_and_octave_reduce_interval(self, interval1, interval2):
        interval = abjad.NamedInterval().from_pitch_carriers(
            interval1,
            interval2
            )
        if interval.semitones > 12:
            interval -= abjad.NamedInterval('P8')
        return interval


    def __repr__(self):
        return "AdjacencyWitness(\n\t" + \
            "from: " + str(self.from_harmonic_interval.name[1:]) + "\n\t" + \
            "to: " + str(self.to_harmonic_interval.name[1:]) + "\n\t" + \
            "top: " + str(self.top_melodic_interval) + "\n\t" + \
            "bottom: " + str(self.bottom_melodic_interval) + "\n\t" + \
            ")"
