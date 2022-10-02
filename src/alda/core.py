from typing import List

from .pitch import Pitch


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
    def __init__(self, pitch: Pitch, duration: int = 4, octave: int = 3):
        self.pitch = pitch
        self.duration = duration
        self.octave = octave

    def serialize(self, with_octave: bool = False) -> str:
        ser = f"{self.pitch}{self.duration}"

        if with_octave:
            ser = f"o{self.octave} {ser}"

        return ser
