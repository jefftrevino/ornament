# interval-aware proportional passaggi algorithm
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
        # witnesses: tuple of two abjad.LogicalTie
        # scale: abjadext.tonality.Scale
        # pitch_range abjad.pitch.PitchRange
        self.ornament_dictionary = ornament_dictionary
        self.scale = scale
        self.pitch_range = pitch_range
        self.pitch_list = self.sorted_pitch_list_from_scale_and_pitch_range()

    def __call__(self, witnesses, debug=False):
        self.debug = debug
        return self.passaggio_from_ornament(witnesses)

    def sorted_pitch_list_from_scale_and_pitch_range(self):
        named_pitch_set = self.scale.create_named_pitch_set_in_pitch_range(self.pitch_range)
        return sorted(list(named_pitch_set))

    def unpitched_leaves_from_ornament(self, ornament):
        ratio = ornament[0]
        duration = self.present.written_duration
        tuplet = abjad.Tuplet().from_duration_and_ratio(duration, ratio)
        tuplet.trivialize()
        if tuplet.trivial():
            tuplet.hide = True
        return tuplet

    def pitch_leaves_with_ornament(self, passaggio, ornament):
        pitch_list = ornament[1]
        if isinstance(self.present, abjad.LogicalTie):
            witness_index = self.pitch_list.index(self.present[0].written_pitch)
        elif isinstance(self.present, abjad.Note):
            witness_index = self.pitch_list.index(self.present.written_pitch)
        pitch_indexes = [witness_index + x for x in pitch_list]
        pitches = [self.pitch_list[x] for x in pitch_indexes]
        leaves = abjad.select(passaggio).leaves()
        for leaf, pitch in zip(leaves, pitches):
            if not isinstance(leaf, abjad.Rest):
                leaf.written_pitch = pitch

    def choose_ornament_from_dictionary(self, interval_dictionary):
        dict_keys = list(interval_dictionary.keys())
        the_key = random.choice(dict_keys)
        ornament = interval_dictionary[the_key]
        self.ornament = ornament
        return (the_key, ornament)

    def invert_ornament(self, ornament, direction):
        if not direction:
            direction = random.choice([-1, 1])
        return (ornament[0], [note * direction for note in ornament[1]])

    def get_interval_from_witnesses(self, witnesses):
        self.present = witnesses[0]
        self.future = witnesses[1]
        if isinstance(self.present, abjad.LogicalTie):
            from_pitch = self.present[0].written_pitch
            to_pitch = self.future[0].written_pitch
        elif isinstance(self.present, abjad.Note):
            from_pitch = self.present.written_pitch
            to_pitch = self.future.written_pitch
        interval = abjad.NamedInterval.from_pitch_carriers(from_pitch, to_pitch)
        self.interval = interval

    def look_up_ornament(self):
        interval_dictionary = self.ornament_dictionary[self.interval.name[-1:]]
        self.ornament_name, self.ornament = self.choose_ornament_from_dictionary(interval_dictionary)
        self.ornament = self.invert_ornament(
            self.ornament,
            self.interval.direction_number
            )
    def create_ornament_leaves(self, ornament):
        passaggio = self.unpitched_leaves_from_ornament(ornament)
        self.pitch_leaves_with_ornament(passaggio, ornament)
        return passaggio

    def label_ornament(self, passaggio, ornament_name):
        markup = abjad.Markup(ornament_name, direction=abjad.Up)
        first_leaf = abjad.inspect(passaggio).leaf(0)
        abjad.attach(markup, first_leaf)

    def passaggio_from_ornament(self, witnesses):
        self.present = witnesses[0]
        self.future = witnesses[1]
        if not self.ornament:
            self.get_interval_from_witnesses(witnesses)
            self.look_up_ornament()
        passaggio = self.create_ornament_leaves(self.ornament)
        if True == self.debug:
            self.label_ornament(passaggio, self.ornament_name)
        return passaggio
