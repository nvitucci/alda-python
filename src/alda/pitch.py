from enum import Enum, IntEnum
from typing import List, Union

from .interval import Interval


class Letter(IntEnum):
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7

    def __str__(self) -> str:
        return str(self.name).lower()


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
        self.accidentals: List[Accidental]

        if isinstance(accidentals, list):
            self.accidentals = accidentals
        elif isinstance(accidentals, Accidental):
            self.accidentals = [accidentals]
        else:
            self.accidentals = []

    def __str__(self) -> str:
        return str(self.letter) + "".join([str(acc) for acc in self.accidentals])

    def __repr__(self) -> str:
        return str(self.letter) + "".join([str(acc) for acc in self.accidentals])

    def __eq__(self, other):
        return self.letter == other.letter and self.accidentals == other.accidentals

    def get_interval(self, interval: Interval):
        letters = list(Letter)

        start_pos = letters.index(self.letter)
        new_pos = letters[(start_pos + interval.positions - 1) % 7]
        new_accidentals = self.accidentals + Pitch._semitones_to_accidentals(interval.semitones)

        return Pitch(new_pos, Pitch._simplify_accidentals(new_accidentals))

    @staticmethod
    def _semitones_to_accidentals(semitones: int) -> List[Accidental]:
        if semitones > 0:
            return [Accidental.SHARP] * semitones
        elif semitones < 0:
            return [Accidental.FLAT] * (-semitones)
        else:
            return []

    @staticmethod
    def _simplify_accidentals(accidentals: List[Accidental]) -> List[Accidental]:
        sharps = accidentals.count(Accidental.SHARP)
        flats = accidentals.count(Accidental.FLAT)
        return Pitch._semitones_to_accidentals(sharps - flats)


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
