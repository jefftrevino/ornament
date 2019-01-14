# fusion dictionary
# Jeff Trevino, 2019
# this dictionary gives fusions possible ways to fuse

import abjad

fusion_dictionary = {
    abjad.Duration(14,4): [[1] * 7],
    abjad.Duration(10,4): [[1] * 5],
    abjad.Duration(8,4): [[1, 1, 1, 1]],
    abjad.Duration(7,4): [[5, 1, 3, 1, 2, 2]],
    abjad.Duration(6,4): [[1, 1, 1]],
    abjad.Duration(4,4): [[1, 2, 1], [1, 1], [6, 1, 1, 2, 4, 2]],
    abjad.Duration(1,2): [[1, 1], [1]],

}
