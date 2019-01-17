# unison witness
# Jeff Trevino, 2019
# This class assesses an entire polyphonic texture
# and identifies consecutive identical pitches to possibly fuse together

import abjad
from ornament.unison.unison import Unison
from itertools import groupby

class UnisonWitness:
    def __init__(self):
        self.possible_unisons = {}

    def __call__(self, score):
        leaf = abjad.inspect(score[0]).leaf(0)
        self.resolution = leaf.written_duration
        self.catalog_unison_candidates(score)
        return self.possible_unisons


    def have_same_pitch(leaf1, leaf2):
        if leaf1.written_pitch == leaf2.written_pitch:
            return True
        return False

    def catalog_unison(self, unison):
        if unison.start_offset in self.possible_unisons:
            self.possible_unisons[unison.start_offset].append(unison)
        else:
            self.possible_unisons[unison.start_offset] = [unison]

    def process_run(self, run):
        selection = abjad.select(run)
        unison = Unison(selection)
        self.catalog_unison(unison)

    def is_base_duration(self, leaf):
        return self.resolution == leaf.written_duration

    def should_add_to_run(self, note, run_pitch):
        return self.is_base_duration(note) and run_pitch == note.written_pitch

    def group_quarter_runs_in_staff(self, staff):
        quarter_runs = []
        notes = abjad.select(staff).components(prototype=abjad.Note)
        grouped = groupby(notes, lambda x: x.written_duration)
        for group in grouped:
            run_list = list(group[1])
            if self.resolution == group[0] and 1 < len(run_list):
                quarter_runs.append(run_list)
        return quarter_runs

    def group_pitch_runs(self, quarter_runs):
        unison_runs = []
        for quarter_run in quarter_runs:
            grouped = groupby(quarter_run, lambda x: x.written_pitch)
            for group in grouped:
                run = list(group[1])
                if 1 < len(run):
                    unison_runs.append(run)
        return unison_runs

    def find_unisons_in_staff(self, staff):
        quarter_runs = self.group_quarter_runs_in_staff(staff)
        unison_runs = self.group_pitch_runs(quarter_runs)
        for run in unison_runs:
                self.process_run(run)

    def catalog_unison_candidates(self, score):
        for staff in score:
            self.find_unisons_in_staff(staff)
