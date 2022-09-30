from enum import Enum
from typing import List


class Pitch(Enum):
    C: str = "c"
    D: str = "d"
    E: str = "e"
    F: str = "f"
    G: str = "g"
    A: str = "a"
    B: str = "b"

    def __str__(self):
        return self.value


class Accident(Enum):
    NONE = ""
    SHARP = "+"
    FLAT = "-"

    def __str__(self):
        return self.value


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
    def __init__(self, pitch: Pitch, duration: int = 4, accident: Accident = Accident.NONE, octave: int = 3):
        self.pitch = pitch
        self.duration = duration
        self.accident = accident
        self.octave = octave

    def serialize(self, with_octave: bool = False) -> str:
        ser = f"{self.pitch}{self.accident}{self.duration}"

        if with_octave:
            ser = f"o{self.octave} {ser}"

        return ser
