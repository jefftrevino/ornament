# dictionary of ornaments for use with Passaggio class

passaggi_dictionary = {
# the ornament is represented as diatonic steps relative to the witness
# i.e., 0 is the witness, 1 upper neighbor, -1 lower neighbor
# multiple by -1 to invert ornament
    '1': {
        'bombus': ([1] * 4, [0,0,0,0]),
        'circulo': ([1] * 4, [0, -1, -2, -1]),
        'tallis suspirans': ([-2, 3, 1, 1, 1], [0,0,-1, -2, -1]),
        },

    '2': {
        'mezzo circulo': ([1] * 5, [0, -1, -2, -1, 0]),
        'groppo': ([1] * 3, [0, -1, 0]),
        'jeffs': ([6, 1, 1], [0, 0, 2])
        },
    '3': {
        'mezzo circulo': ([1] * 4, [0, -1, 0, 1]),
        'groppo': ([1] * 3, [0, 0, 1]),
        },
    '4': {
        'mezzo circulo': ([1] * 5, [0, -1, 0, 1, 2]),
        'tirata': ([1] * 3, [0, 1, 2]),
        },
    '5': {
        'mezzo circulo tirata': ([1] * 8, [0, -1, -2, -1, 0, 1, 2, 3]),
        'tirata suspirans': ([-2, 3, 1, 1, 1], [0, 0, 1, 2, 3]),
        },

}