import abjad
from suspension_witness import SuspensionWitness

class SuspensionDecorator:
    def __init__(self, score):
        for voice_pair in zip(score, score[1:]):
            
