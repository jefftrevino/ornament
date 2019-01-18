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
    e'' e'' e'' a' c'' a' c'' a' e'' e'' e'' a' c'' a' c'' a'\
    g' g' f' d' f' d' f' g'\
    a' f' a' f' a' f' a' f' g' g' g' g' g' g' g' g' \
    g' d' b' g' b' g' b' g' g' d' b' g' b' g' b' g' \
    f' d'' a' f' d' f' d' f' \
    e' a' c'' a' a' a' a' a' e' a' c'' a' a' a' a' a'\
    a' a' f' c'' f'' c'' c'' a' a' a' f' c'' f'' c'' c'' a'\
    g' c'' c'' c'' g' c'' c'' e''\
    d''1")



middle = abjad.Staff("\
    c' a c' e' e' e' e' e' c' a c' e' e' e' e' e'\
    b d' a a a a a c' \
    c' c' c' c' c' c' c' c' c' e' c' e' c' e' c' e'\
    d' b d' d' d' d' d' d' d' b d' d' d' d' d' d'\
    a a f a a a a d'\
    c' e' e' e' c' e' c' e' c' e' e' e' c' e' c' e'\
    f' c' c' f' a' a' f' f' f' c' c' f' a' a' f' f'\
    e' e' g' e' e' e' g' g'\
    g'1")

bottom = abjad.Staff("\
    a, c a, c a, c a, c a, c a, c a, c a, c\
    e b, d f d f d e\
    f a f a f a f a e c e c e c e c\
    b, g g b g b g b b, g g b g b g b\
    d f d d f d f a\
    a c a, c e c e c a c a, c e c e c\
    c f a a c' f' a c' c f a a c' f' a c'\
    c' g e g c' g' e c \
    b,1")

skeleton.extend([top, middle, bottom])


if __name__ == '__main__':
    abjad.show(skeleton)
    abjad.play(skeleton)
