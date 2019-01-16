import abjad
import random

class Suspension:
    def __init__(self, selections, index_pair):
        self.selections = selections
        self.offsets = [abjad.inspect(note).vertical_moment().offset for note in selections['top']]
        self.index_pair = index_pair

    def __call__(self, scale, pitch_range, suspension_dictionary):
        self.scale = scale
        self.pitch_range = pitch_range
        self.pitch_list = self.sorted_pitch_list_from_scale_and_pitch_range()
        ornament_name, ornament = self.look_up_ornament(suspension_dictionary)
        leaves = self.unpitched_leaves_from_ornament(ornament)
        leaves = self.pitch_leaves_with_ornament(leaves, ornament)
        self.label_leaves(leaves, 'suspension')
        abjad.mutate(self.selections['top']).replace(leaves)
        self.label_leaves(self.selections['bottom'], 'no ornament')

    def label_leaves(self, leaves, label):
        for leaf in leaves:
            label = abjad.LilyPondComment(label)
            abjad.attach(label, leaf)

    def sorted_pitch_list_from_scale_and_pitch_range(self):
        named_pitch_set = self.scale.create_named_pitch_set_in_pitch_range(self.pitch_range)
        return sorted(list(named_pitch_set))

    def look_up_ornament(self, suspension_dictionary):
        dict_keys = list(suspension_dictionary.keys())
        the_key = random.choice(dict_keys)
        ornament = suspension_dictionary[the_key]
        return (the_key, ornament)

    def unpitched_leaves_from_ornament(self, ornament):
        ratio = ornament[0]
        duration = sum([x.written_duration for x in self.selections['top']])
        tuplet = abjad.Tuplet().from_duration_and_ratio(duration, ratio)
        tuplet.trivialize()
        if tuplet.trivial():
            tuplet.hide = True
        return tuplet

    def pitch_leaves_with_ornament(self, passaggio, ornament):
        pitch_list = ornament[1]
        witness_index = self.pitch_list.index(self.selections['top'][0].written_pitch)
        pitch_indexes = [witness_index + x for x in pitch_list]
        pitches = [self.pitch_list[x] for x in pitch_indexes]
        leaves = abjad.select(passaggio).leaves()
        for leaf, pitch in zip(leaves, pitches):
            if not isinstance(leaf, abjad.Rest):
                leaf.written_pitch = pitch
        self.label_leaves(leaves, 'suspension')
        return leaves

    def __repr__(self):
        return "Suspension() starting at " + str(self.offsets[0])
