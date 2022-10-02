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
    def __init__(self, letter: Letter, accidentals: Union[Accidental, List[Accidental]]):
        self.letter: Letter = letter
        self.accidentals: List[Accidental] = accidentals if isinstance(accidentals, list) else [accidentals]

    def __str__(self) -> str:
        return str(self.letter) + "".join([str(acc) for acc in self.accidentals])


C = Pitch(Letter.C, Accidental.NONE)
C_SHARP = Pitch(Letter.C, Accidental.SHARP)
D_FLAT = Pitch(Letter.D, Accidental.FLAT)
D = Pitch(Letter.D, Accidental.NONE)
D_SHARP = Pitch(Letter.D, Accidental.SHARP)
E_FLAT = Pitch(Letter.E, Accidental.FLAT)
E = Pitch(Letter.E, Accidental.NONE)
F = Pitch(Letter.F, Accidental.NONE)
F_SHARP = Pitch(Letter.F, Accidental.SHARP)
G_FLAT = Pitch(Letter.G, Accidental.FLAT)
G = Pitch(Letter.G, Accidental.NONE)
G_SHARP = Pitch(Letter.G, Accidental.SHARP)
A_FLAT = Pitch(Letter.A, Accidental.FLAT)
A = Pitch(Letter.A, Accidental.NONE)
A_SHARP = Pitch(Letter.A, Accidental.SHARP)
B_FLAT = Pitch(Letter.B, Accidental.FLAT)
B = Pitch(Letter.B, Accidental.NONE)
