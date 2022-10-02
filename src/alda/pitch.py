from enum import Enum
from typing import List, Union


class Letter(Enum):
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    A = "a"
    B = "b"

    def __str__(self) -> str:
        return str(self.value)


class Accidental(Enum):
    NONE = ""
    SHARP = "+"
    FLAT = "-"
    NATURAL = "_"

    def __str__(self) -> str:
        return str(self.value)


class Pitch:
    def __init__(self, letter: Letter, accidentals: Union[List[Accidental], Accidental, None] = None):
        self.letter: Letter = letter

        if isinstance(accidentals, list):
            self.accidentals: List[Accidental]
        if isinstance(accidentals, Accidental):
            self.accidentals = [accidentals]
        else:
            self.accidentals = []

    def __str__(self) -> str:
        return str(self.letter) + "".join([str(acc) for acc in self.accidentals])


C = Pitch(Letter.C)
C_SHARP = Pitch(Letter.C, Accidental.SHARP)
D_FLAT = Pitch(Letter.D, Accidental.FLAT)
D = Pitch(Letter.D)
D_SHARP = Pitch(Letter.D, Accidental.SHARP)
E_FLAT = Pitch(Letter.E, Accidental.FLAT)
E = Pitch(Letter.E)
F = Pitch(Letter.F)
F_SHARP = Pitch(Letter.F, Accidental.SHARP)
G_FLAT = Pitch(Letter.G, Accidental.FLAT)
G = Pitch(Letter.G)
G_SHARP = Pitch(Letter.G, Accidental.SHARP)
A_FLAT = Pitch(Letter.A, Accidental.FLAT)
A = Pitch(Letter.A)
A_SHARP = Pitch(Letter.A, Accidental.SHARP)
B_FLAT = Pitch(Letter.B, Accidental.FLAT)
B = Pitch(Letter.B)
