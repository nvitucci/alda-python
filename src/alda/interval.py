class Interval:
    def __init__(self, positions: int, semitones: int):
        self.positions = positions
        self.semitones = semitones


P1 = Interval(1, 0)
m2 = Interval(2, -1)
M2 = Interval(2, 0)
m3 = Interval(3, -1)
M3 = Interval(3, 0)
P4 = Interval(4, 0)
P5 = Interval(5, 0)
m6 = Interval(6, -1)
M6 = Interval(6, 0)
m7 = Interval(7, -1)
M7 = Interval(7, 0)
P8 = Interval(8, 0)

d2 = Interval(2, -2)
A1 = Interval(1, 1)
d3 = Interval(3, -2)
A2 = Interval(2, 1)
d4 = Interval(4, -1)
A3 = Interval(3, 1)
d5 = Interval(5, -1)
A4 = Interval(4, 1)
d6 = Interval(6, -2)
A5 = Interval(5, 1)
d7 = Interval(7, -2)
A6 = Interval(6, 1)
d8 = Interval(8, -1)
A7 = Interval(7, 1)
