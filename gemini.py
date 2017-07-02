geminiMap = {
    # entries are byte number (left to right) and bit number (right to left)
    # i.e. entry (byte, bit) means chordBytes[byte] |= 1 << bit
    # Note bit 7 of chordBytes[0] should be 1 in all cases.
    'Fn1': (0,6), '#1': (0, 5), '#2': (0, 4), '#3': (0, 3), '#4': (0, 2), '#5': (0, 1), '#6': (0, 0),
    'S1': (1, 6),
    'S2': (1, 5),
    'T': (1, 4),
    'K': (1, 3),
    'P': (1, 2),
    'W': (1, 1),
    'H': (1, 0),

    'R': (2, 6),
    'A': (2, 5),
    'O': (2, 4),
    '*1': (2, 3),
    '*2': (2, 1),

    '*3': (3, 5),
    '*4': (3, 4),
    'E': (3, 3),
    'U': (3, 2),
    '-F': (3, 1),
    '-R': (3, 0),

    '-P': (4, 6),
    '-B': (4, 5),
    '-L': (4, 4),
    '-G': (4, 3),
    '-T': (4, 2),
    '-S': (4, 1),
    '-D': (4, 0),

    '#7': (0,6), '#8': (5, 5), '#9': (5, 4), '#A': (5, 3), '#B': (5, 2), '#C': (5, 1), '-Z': (5, 0)
}