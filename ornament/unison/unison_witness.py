# unison witness
# Jeff Trevino, 2019
# This class assesses an entire polyphonic texture
# and identifies consecutive identical pitches to possibly fuse together

import abjad
from ornament.unison.unison import Unison

class UnisonWitness:
    def __init__(self):
        self.possible_unisons = {}

    def __call__(self, score):
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


    def find_unisons_in_staff(self, staff):
        run = []
        run_pitch = None
        for leaf in abjad.iterate(staff).leaves():
            if not run:
                run = [leaf]
                run_pitch = leaf.written_pitch
            elif leaf.written_pitch == run_pitch:
                run.append(leaf)
            else:
                if 1 < len(run):
                    self.process_run(run)
                run = [leaf]
                run_pitch = leaf.written_pitch
        if 1 < len(run):
            self.process_run(run)

    def catalog_unison_candidates(self, score):
        for staff in score:
            self.find_unisons_in_staff(staff)
