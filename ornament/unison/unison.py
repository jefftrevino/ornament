# unison
# Jeffrey Trevino, 2019
# model of consecutive same-pitched leaves to maybe fuse

import abjad
import random

random.seed(1)

class Unison:
    def __init__(self, consecutive_leaves):
        self.proportion = None
        self.selection = abjad.select(consecutive_leaves)
        self.duration = sum([l.written_duration for l in self.selection])
        self.pitch = self.selection[0].written_pitch
        self.start_offset = self.get_leaf_offset(self.selection[0])
        self.stop_offset = self.get_offset_after_note_duration(self.selection[-1])
        self.timespan = abjad.Timespan(self.start_offset, self.stop_offset)

    def __call__(self, unison_dictionary, debug=False):
        if debug:
            self.color_leaves()
        else:
            if not self.proportion:
                self.choose_proportion(unison_dictionary)
            leaves = self.build_fused_leaves(self.proportion)
            abjad.mutate(self.selection).replace(leaves)

    def choose_proportion(self, unison_dictionary):
        proportions_list = unison_dictionary[self.duration]
        self.proportion = random.choice(proportions_list)


    def color_leaves(self):
            abjad.override(self.selection[0]).note_head.color = 'red'
            abjad.override(self.selection[-1]).note_head.color = 'red'


    def pitch_leaves(self, leaves):
        for leaf in leaves:
            leaf.written_pitch = self.pitch

    def build_fused_leaves(self, proportion):
        leaves = abjad.Tuplet().from_duration_and_ratio(self.duration, proportion)
        leaves.trivialize()
        if leaves.trivial():
            leaves.hide = True
        self.pitch_leaves(leaves)
        return leaves

    def __repr__(self):
        return "Unison(Pitch:" + str(self.pitch) + ", " + \
        "Duration:" + str(self.duration) + ", " + \
        "Start:" + str(self.start_offset) + ", " + \
        "Stop:" + str(self.stop_offset) + ", " + \
        "Prop:" + str(self.proportion) + \
         ")"

    def get_offset_after_note_duration(self, note):
        return self.get_leaf_offset(note) + note.written_duration

    def get_leaf_offset(self, leaf):
        return abjad.inspect(leaf).vertical_moment().offset

    def is_happening_at_offset(self, offset):
        moment = abjad.Timespan(offset, offset)
        return moment.happens_during_timespan(self.timespan)

    def timespan_overlap(self, timespan):
        return self.timespan.get_overlap_with_timespan(timespan)
