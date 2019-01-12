# interval-aware passaggi algorithm
# Jeff Trevino, 2019
# minimal strategy making a passaggio based on:
# a witness pitch
# an ornament dictionary
# a diatonic context

import abjad
import random

class Passaggio:
    """Model of a passaggio based on a starting pitch, diatonic context, and ornament"""
    def __init__(self, ornament_dictionary, scale, pitch_range):
        # witnesses: tuple of two abjad.Note
        # scale: abjadext.tonality.Scale
        # pitch_range abjad.pitch.PitchRange
        self.ornament_dictionary = ornament_dictionary
        self.scale = scale
        self.pitch_range = pitch_range
        self.pitch_list = self.sorted_pitch_list_from_scale_and_pitch_range()

    def __call__(self, witnesses):
        return self.passaggio_from_ornament(witnesses)

    def sorted_pitch_list_from_scale_and_pitch_range(self):
        named_pitch_set = self.scale.create_named_pitch_set_in_pitch_range(self.pitch_range)
        return sorted(list(named_pitch_set))

    def unpitched_leaves_from_ornament(self, ornament):
        num_notes = len(ornament)
        note_duration = self.present.written_duration / num_notes
        durations = [note_duration] * num_notes
        maker = abjad.LeafMaker()
        leaves = maker(0, durations)
        return leaves

    def pitch_leaves_with_ornament(self, passaggio, ornament):
        witness_index = self.pitch_list.index(self.present.written_pitch)
        pitch_indexes = [witness_index + x for x in ornament]
        pitches = [self.pitch_list[x] for x in pitch_indexes]
        leaves = abjad.select(passaggio).leaves()
        for leaf, pitch in zip(leaves, pitches):
            leaf.written_pitch = pitch

    def choose_ornament_from_dictionary(self, interval_dictionary):
        dict_keys = list(interval_dictionary.keys())
        the_key = random.choice(dict_keys)
        ornament = interval_dictionary[the_key]
        return (the_key, ornament)

    def invert_ornament(self, ornament, direction):
        if not direction:
            direction = random.choice([-1, 1])
        return [note * direction for note in ornament]

    def get_interval_from_witnesses(self, witnesses):
        self.present = witnesses[0]
        self.future = witnesses[1]
        interval = abjad.NamedInterval.from_pitch_carriers(
            self.present.written_pitch,
            self.future.written_pitch
            )
        return interval

    def look_up_ornament(self, interval):
        interval_dictionary = self.ornament_dictionary[interval.name[-1:]]
        ornament_name, ornament = self.choose_ornament_from_dictionary(interval_dictionary)
        ornament = self.invert_ornament(
            ornament,
            interval.direction_number
            )
        return ornament_name, ornament

    def create_ornament_leaves(self, ornament):
        passaggio = self.unpitched_leaves_from_ornament(ornament)
        self.pitch_leaves_with_ornament(passaggio, ornament)
        return passaggio

    def label_ornament(self, passaggio, ornament_name):
        markup = abjad.Markup(ornament_name, direction=abjad.Up)
        first_leaf = abjad.inspect(passaggio).leaf(0)
        abjad.attach(markup, first_leaf)

    def passaggio_from_ornament(self, witnesses):
        interval = self.get_interval_from_witnesses(witnesses)
        ornament_name, ornament = self.look_up_ornament(interval)
        passaggio = self.create_ornament_leaves(ornament)
        self.label_ornament(passaggio, ornament_name)
        return passaggio
