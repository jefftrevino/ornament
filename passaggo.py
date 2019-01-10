# pitches from intervals
# Jeff Trevino, 2019
# minimal strategy making a passaggo based on:
# a witness pitch
# an ornament dictionary
# a diatonic context

import abjad
from abjadext import tonality
import random

scale = tonality.Scale(('c', 'major'))
pitch_range = abjad.pitch.PitchRange('[G3, C6]')

def sorted_pitch_list_from_scale_and_pitch_range(scale, pitch_range):
    named_pitch_set = scale.create_named_pitch_set_in_pitch_range(pitch_range)
    named_pitch_list = sorted(list(named_pitch_set))
    return named_pitch_list

named_pitch_list = sorted_pitch_list_from_scale_and_pitch_range(scale, pitch_range)

ornament_dict = {
# the ornament is represented as diatonic steps relative to the witness
# i.e., 0 is the witness, 1 upper neighbor, -1 lower neighbor
    'ascending mezza tirata': [0, 1, 2, 3, 4],
    'descending mezza tirata': [0, -1, -2, -3, -2],

}

def unpitched_leaves_from_ornament(witness, ornament):
    num_notes = len(ornament)
    note_duration = witness.written_duration / num_notes
    durations = [note_duration] * num_notes
    maker = abjad.LeafMaker()
    leaves = maker(0, durations)
    return leaves

def pitch_leaves_with_ornament(witness, passaggo, ornament, pitch_list):
    # to pitch, which scale degree witnesses the ornament?
    witness_index = pitch_list.index(witness.written_pitch)
    # derive scale degrees from the ornament
    pitch_indexes = [witness_index + x for x in ornament]
    pitches = [pitch_list[x] for x in pitch_indexes]
    # then paint on pitches from the ornament
    leaves = abjad.select(passaggo).leaves()
    for leaf, pitch in zip(leaves, pitches):
        leaf.written_pitch = pitch

def choose_ornament_from_dict(the_dict):
    # returns a passago based on a starting pitch and dictionary of ornaments
    dict_keys = list(ornament_dict.keys())
    the_key = random.choice(dict_keys)
    ornament = ornament_dict[the_key]
    return ornament

def passaggo_from_witness(witness, pitch_list):
    # make a random choice from the dictionary
    ornament = choose_ornament_from_dict(ornament_dict)
    # use the chosen diminution to make new leaves from the starting pitch
    passaggo = unpitched_leaves_from_ornament(witness, ornament)
    pitch_leaves_with_ornament(witness, passaggo, ornament, pitch_list)
    return passaggo

# ornament each note of a melody with a passaggo:
staff = abjad.Staff("c''4. b'8 a'4 g' f'4. g'8 a'4 c'' b'4. a'8 g'4 f' e'1")
out = abjad.Staff()
for note in staff:
    passaggo = passaggo_from_witness(note, named_pitch_list)
    out.append(passaggo)
abjad.show(out)
