# unison dictionary
# Jeff Trevino, 2019
# this dictionary gives fusions possible ways to fuse

import abjad

unison_dictionary = {
    abjad.Duration(14,4): [[1] * 7],
    abjad.Duration(10,4): [[1] * 5],
    abjad.Duration(9,4): [[2, 4, 3, 1, 1, 1, 3, 1, 1, 1]],
    abjad.Duration(8,4): [[1, 1, 1, 1]],
    abjad.Duration(7,4): [[5, 1, 3, 1, 2, 2]],
    abjad.Duration(6,4): [[1, 1, 1]],
    abjad.Duration(5,4): [[1] * 10],
    abjad.Duration(4,4): [[1, 2, 1], [1, 1], [6, 1, 1, 2, 4, 2]],
    abjad.Duration(3,4): [[2, 3, 1]],
    abjad.Duration(5,8): [[1, 1, 3, 1, 4]],
    abjad.Duration(1,2): [[1, 1], [1]],

}
