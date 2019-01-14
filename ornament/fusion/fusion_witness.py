# This class assesses an entire polyphonic texture
# and identifies consecutive identical pitches to possibly fuse together

import abjad
from ornament.fusion.fusion import Fusion

class FusionWitness:
    def __init__(self):
        self.possible_fusions = {}

    def __call__(self, score):
        self.catalog_fusion_candidates(score)
        return self.possible_fusions

    def have_same_pitch(leaf1, leaf2):
        if leaf1.written_pitch == leaf2.written_pitch:
            return True
        return False

    def catalog_fusion(self, fusion):
        if fusion.start_offset in self.possible_fusions:
            self.possible_fusions[fusion.start_offset].append(fusion)
        else:
            self.possible_fusions[fusion.start_offset] = [fusion]

    def process_run(self, index, run):
        selection = abjad.select(run)
        fusion = Fusion(index, selection)
        self.catalog_fusion(fusion)


    def find_fusions_in_staff(self, index, staff):
        run = []
        run_pitch = None
        for leaf in staff:
            if not run:
                run = [leaf]
                run_pitch = leaf.written_pitch
            elif leaf.written_pitch == run_pitch:
                run.append(leaf)
            else:
                if 1 < len(run):
                    self.process_run(index, run)
                run = [leaf]
                run_pitch = leaf.written_pitch
        if 1 < len(run):
            self.process_run(index, run)

    def catalog_fusion_candidates(self, score):
        for index, staff in enumerate(score):
            self.find_fusions_in_staff(index, staff)
