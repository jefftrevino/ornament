import abjad

skeleton = abjad.Score()
top = abjad.Staff(
    "d''8 d'' a' a' c'' c'' b' b' \
     c'' c'' a' a' c'' c'' d'' d'' \
     e'' e'' c'' c'' c'' c'' e'' e'' \
     e'' e'' c'' c'' c'' c'' g' g' \
     c'' c'' a' a' c'' c'' a' a' \
     g' g' e' e' c' c' e' e' \
     d' d' d' d' d' d' d' d' \
     d' d' f' f' a' a' f' f' \
     a' a' f' f' a' a' f' f' \
     e' e' c'' c'' b' b' b' b' cs'' cs'' cs'' cs''\
")
abjad.attach(abjad.TimeSignature((4,4)), top[0])

middle = abjad.Staff(" \
    f'8 f' f' f' e' e' d' d' \
    e' e' e' e' e' e' g' g'\
    g' g' g' g' g' g' g' g'\
    g' g' g' g' e' e' e' e'\
    f' f' f' f' f' f' f' f'\
    e' e' \clef bass g g g g g g \
    g g g g b b b b \
    a a a a d d a a \
    d d a a d d a a \
    \clef treble c' c' e' e' e' e' g' g' e' e' e' e' \
    \
")

bottom = abjad.Staff(" \
\clef bass a8 a d' d' g g g g \
a a c' c' a a b b \
c' c' e' e' e e c c \
c c e e g g c' c' \
a a c' c' a a c' c' \
c' c' c c e e c c \
b, b, b, b, g, g, g g  \
f f d d f f d d \
f f d d f f d d \
a a a a g g e e a, a, a a \
")
skeleton.extend([top, middle, bottom])
