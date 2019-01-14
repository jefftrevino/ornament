# fusion candidate
# Jeffrey Trevino, 2019
# model of consecutive same-pitched leaves to maybe fuse

import abjad
import random

random.seed(0)

class Fusion:
    def __init__(self, staff_index, consecutive_leaves):
        self.staff_index = staff_index
        self.selection = abjad.select(consecutive_leaves)
        self.duration = sum([l.written_duration for l in self.selection])
        self.pitch = self.selection[0].written_pitch
        self.start_offset = self.get_leaf_offset(self.selection[0])
        self.stop_offset = self.get_offset_after_note_duration(self.selection[-1])
        self.timespan = abjad.Timespan(self.start_offset, self.stop_offset)

    def __call__(self, fusion_dictionary):
        proportions_list = fusion_dictionary[self.duration]
        leaves = self.build_fused_leaves()
        abjad.mutate(self.selection).replace(leaves)

    def pitch_leaves(leaves):
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
        return "Fusion(Pitch:" + str(self.pitch) + ", " + \
        "Duration:" + str(self.duration) + ", " + \
        "Start:" + str(self.start_offset) + ", " + \
        "Stop:" + str(self.stop_offset) + \
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
