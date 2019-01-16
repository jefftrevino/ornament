import abjad

class Adjacency:
    def __init__(self, present_moment, future_moment, staff_index):
        # staff_index specifies which index in
        self.present_moment = present_moment
        self.future_moment = future_moment
        self.from_note = self.present_moment.start_leaves[staff_index]
        self.to_note = self.future_moment.start_leaves[staff_index]
        self.melodic_interval = self.calculate_and_octave_reduce_interval(
            self.from_note,
            self.to_note
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
        return "Adjacency(\n\t" + \
            "interval: " + str(self.melodic_interval) + "\n\t" + ","\
            "from:" + str(self.from_note) + "\n\t" + ","\
            "to:" + str(self.to_note) + "\n\t" + "," \
            ")"
