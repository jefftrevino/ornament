import abjad

# skeleton_old = abjad.Score()
# top = abjad.Staff(
#     "d''4 d'' a' a' c'' c'' b' b' \
#      c'' c'' a' a' c'' c'' d'' d'' \
#      e'' e'' c'' c'' c'' c'' e'' e'' \
#      e'' e'' c'' c'' c'' c'' g' g' \
#      c'' c'' a' a' c'' c'' a' a' \
#      g' g' e' e' c' c' e' e' \
#      d' d' d' d' d' d' d' d' \
#      d' d' f' f' a' a' f' f' \
#      a' a' f' f' a' a' f' f' \
#      e' e' c'' c'' b' b' b' b' cs'' cs'' cs'' cs''\
# ")
# abjad.attach(abjad.TimeSignature((4,4)), top[0])
#
# middle = abjad.Staff(" \
#     f'4 f' f' f' e' e' d' d' \
#     e' e' e' e' e' e' g' g'\
#     g' g' g' g' g' g' g' g'\
#     g' g' g' g' e' e' e' e'\
#     f' f' f' f' f' f' f' f'\
#     e' e' \clef bass g g g g g g \
#     g g g g b b b b \
#     a a a a d d a a \
#     d d a a d d a a \
#     \clef treble c' c' e' e' e' e' g' g' e' e' e' e' \
#     \
# ")
#
# bottom = abjad.Staff(" \
# \clef bass a4 a d' d' g g g g \
# a a c' c' a a b b \
# c' c' e' e' e e c c \
# c c e e g g c' c' \
# a a c' c' a a c' c' \
# c' c' c c e e c c \
# b, b, b, b, g, g, g g  \
# f f d d f f d d \
# f f d d f f d d \
# a a a a g g e e a, a, a a \
# ")
skeleton = abjad.Score()
top = abjad.Staff("\
    b'4 b' b' e' \
    g' e' g' e'\
    b' b' b' e' \
    g' e' g' e'\
    d' d' c' a c' a c' d' \
    e' c' e' c'\
    e' c' e' c'\
    d' d' d' d'\
    d' d' d' d'\
    d' a fs' d'\
    fs' d' fs' d'\
    d' a fs' d'\
    fs' d' fs' d'\
    c' a' e' c'\
    a c' a c'\
    b e' g' e'\
    e' e' e' e'\
    b e' g' e'\
    e' e' e' e'\
    e' e' c' g'\
    c'' g' g' e'\
    e' e' c' g'\
    c'' g' g' e'\
    d' g' g' g'\
    d' g' g' b'\
    d' g' g' g'\
    d' g' g' b'\
    a'1")

middle = abjad.Staff("\
    g e g b\
    b b b b \
    g e g b\
    b b b b \
    fs a e e\
    e e e g\
    g g g g \
    g g g g \
    g b g b\
    g b g b\
    a fs a a\
    a a a a\
    a fs a a\
    a a a a\
    e e c e\
    e e e a\
    g b b b\
    g b g b\
    g b b b\
    g b g b\
    c' g g c'\
    e' e' c' c'\
    c' g g c'\
    e' e' c' c'\
    b b d' b\
    b b d' d'\
    b b d' b\
    b b d' d'\
    d1")

bottom = abjad.Staff("\
    e, g, e, g,\
    e, g, e, g,\
    e, g, e, g,\
    e, g, e, g,\
    b, fs, a, c\
    a, c a, b,\
    c e c e\
    c e c e\
    b, g, b, g,\
    b, g, b, g,\
    fs, d d fs\
    d fs d fs\
    fs, d d fs\
    d fs d fs\
    a, c a, a,\
    c a, c e\
    e g, e, g,\
    b, g, b, g,\
    e g, e, g,\
    b, g, b, g,\
    g, c e e\
    g c' e g\
    g, c e e\
    g c' e g\
    g d b, d\
    g d b, g,\
    g d b, d\
    g d b, g,\
    fs,1")

skeleton.extend([top, middle, bottom])


if __name__ == '__main__':
    abjad.show(skeleton)
    abjad.play(skeleton)
