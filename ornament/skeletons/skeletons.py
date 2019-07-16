import abjad

skeletons = []

skeleton_one = abjad.Score()
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

skeleton_one.extend([top, middle, bottom])
skeletons.append(skeleton_one)

skeleton_two = abjad.Score()

top = abjad.Staff("\
e' e' d' d' \
e' e' f' f' \
e' e' d' d' \
g' g' e' e' \
a' a' d' f' \
e' e' g' g' \
d' d' d' d' \
e' e' f' f' \
g' g' e' e' \
d' d' d' d' \
e' e' d' d' \
e' e' f' f' \
e' e' d' d' \
g' g' e' e' \
a' a' d' f' \
e' e' g' g' \
d' d' d' d' \
e' e' f' f' \
g' g' e' e' \
d' d' d' d' \
e' c' f' d' \
b e' e' d' \
e' c' f' d' \
b e' e' d' \
g' g' f' f' \
e' e' a' a' \
d' a' d'' a' \
b' b' b' b' \
c''")

middle = abjad.Staff("\
g g g g \
g g c' c' \
g g g g \
c' c' c' c' \
d' d' b b \
c' c' c' c' \
a a g g \
g g c' c' \
c' c' c' c' \
a a b b \
g g g g \
g g c' c' \
g g g g \
c' c' c' c' \
d' d' b b \
c' c' c' c' \
a a g g \
g g c' c' \
c' c' c' c' \
a a b b \
g g a a \
a b c' g \
g g a a \
a b c' g \
e' c' c' c' \
c' c' c' c' \
a d' a' d' \
g' g' e' e' e'")

bottom = abjad.Staff("\
c c b, b, \
c c a, a, \
c c b, b, \
e, e a a \
f f g g \
a a e e \
f f b, b, \
c c a, a, \
e, e a a \
f f g g \
c c b, b, \
c c a, a, \
c c b, b, \
e, e a a \
f f g g \
a a e e \
f f b, b, \
c c a, a, \
e, e a a \
f f g g \
c e d f \
g g, a, b, \
c e d f \
g g, a, b, \
c e a a \
a a f f \
f f f f \
e e g g \
a")

skeleton_two.extend([top, middle, bottom])
skeletons.append(skeleton_two)

if __name__ == '__main__':
    for s in skeletons:
        abjad.attach(abjad.Clef('bass'), s[2][0])
        abjad.show(s)
