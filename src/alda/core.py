from enum import Enum, auto
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


class Pitch(Enum):
    C_FLAT = (Letter.C, Accidental.FLAT)
    C = (Letter.C, Accidental.NONE)
    C_SHARP = (Letter.C, Accidental.SHARP)
    D_FLAT = (Letter.D, Accidental.FLAT)
    D = (Letter.D, Accidental.NONE)
    D_SHARP = (Letter.D, Accidental.SHARP)
    E_FLAT = (Letter.E, Accidental.FLAT)
    E = (Letter.E, Accidental.NONE)
    E_SHARP = (Letter.E, Accidental.SHARP)
    F_FLAT = (Letter.F, Accidental.FLAT)
    F = (Letter.F, Accidental.NONE)
    F_SHARP = (Letter.F, Accidental.SHARP)
    G_FLAT = (Letter.G, Accidental.FLAT)
    G = (Letter.G, Accidental.NONE)
    G_SHARP = (Letter.G, Accidental.SHARP)
    A_FLAT = (Letter.A, Accidental.FLAT)
    A = (Letter.A, Accidental.NONE)
    A_SHARP = (Letter.A, Accidental.SHARP)
    B_FLAT = (Letter.B, Accidental.FLAT)
    B = (Letter.B, Accidental.NONE)
    B_SHARP = (Letter.B, Accidental.SHARP)

    def __str__(self) -> str:
        return f"{self.value[0]}{self.value[1]}"


class Score:
    def __init__(self, tempo: int = 60):
        self.tempo: int = tempo
        self.parts: List[Part] = []

    def serialize(self) -> str:
        ser = [f"(tempo! {self.tempo})"]
        ser.extend([p.serialize() for p in self.parts])

        return "\n".join(ser)


class Part:
    def __init__(self, instr: str = "piano"):
        self.instr: str = instr
        self.notes: List[Note] = []

    def serialize(self) -> str:
        ser = [f"{self.instr}:"]
        ser.extend([p.serialize() for p in self.notes])

        return "\n".join(ser)


class Note:
    def __init__(self, pitch: Pitch, duration: int = 4, accidental: Accidental = Accidental.NONE, octave: int = 3):
        self.pitch = pitch
        self.duration = duration
        self.accident = accidental
        self.octave = octave

    def serialize(self, with_octave: bool = False) -> str:
        ser = f"{self.pitch}{self.accident}{self.duration}"

        if with_octave:
            ser = f"o{self.octave} {ser}"

        return ser
