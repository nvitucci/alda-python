from __future__ import annotations

from typing import List, Optional, Tuple

from . import interval
from .interval import Interval
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


class Duration:
    def __init__(self, length: int):
        self.length = length

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Duration):
            return self.length == other.length

        return False

    def __str__(self) -> str:
        return str(self.length)


class Note:
    def __init__(self, pitch: Pitch, duration: Duration = Duration(4), octave: int = 3):
        self.pitch = pitch
        self.duration = duration
        self.octave = octave

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Note):
            return self.pitch == other.pitch and self.duration == other.duration and self.octave == other.octave

        return False

    def serialize(self, with_octave: bool = False) -> str:
        ser = f"{self.pitch}{self.duration}"

        if with_octave:
            ser = f"o{self.octave} {ser}"

        return ser


MAJ = (interval.M3, interval.P5)
MIN = (interval.m3, interval.P5)
AUG = (interval.M3, interval.A5)
DIM = (interval.m3, interval.d5)

SUS_2 = (interval.M2, interval.P5)
SUS_4 = (interval.P4, interval.P5)

ADD_6 = (interval.M3, interval.P5, interval.M6)
MIN_ADD_6 = (interval.m3, interval.P5, interval.M6)
ADD_9 = (interval.M3, interval.P5, interval.M9)
MIN_ADD_9 = (interval.m3, interval.P5, interval.M9)

DOM_7 = (interval.M3, interval.P5, interval.m7)
MAJ_7 = (interval.M3, interval.P5, interval.M7)
MIN_7 = (interval.m3, interval.P5, interval.m7)
MIN_MAJ_7 = (interval.m3, interval.P5, interval.M7)
AUG_7 = (interval.M3, interval.A5, interval.m7)
AUG_MAJ_7 = (interval.M3, interval.A5, interval.M7)
DIM_7 = (interval.m3, interval.d5, interval.d7)
DOM_7_DIM_5 = (interval.M3, interval.d5, interval.m7)
HALF_DIM_7 = MIN_7_DIM_5 = (interval.m3, interval.d5, interval.m7)

DOM_9 = (interval.M3, interval.P5, interval.m7, interval.M9)
DOM_MIN_9 = (interval.M3, interval.P5, interval.m7, interval.m9)
MAJ_9 = (interval.M3, interval.P5, interval.M7, interval.M9)
MIN_9 = (interval.m3, interval.P5, interval.m7, interval.M9)
MIN_MAJ_9 = (interval.m3, interval.P5, interval.M7, interval.M9)
AUG_9 = (interval.M3, interval.A5, interval.m7, interval.M9)
AUG_MAJ_9 = (interval.M3, interval.A5, interval.M7, interval.M9)
DIM_9 = (interval.m3, interval.d5, interval.d7, interval.M9)
DIM_MIN_9 = (interval.m3, interval.d5, interval.d7, interval.m9)
HALF_DIM_9 = (interval.m3, interval.d5, interval.m7, interval.M9)
HALF_DIM_MIN_9 = (interval.m3, interval.d5, interval.m7, interval.m9)


class Chord:
    def __init__(self, notes: List[Note]):
        self.notes = notes

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Chord):
            return self.notes == other.notes

        return False

    def __repr__(self) -> str:
        return self.serialize()

    @classmethod
    def from_name(cls, base_note: Note, name: Tuple[Interval, ...], inversion_base: Optional[Pitch] = None) -> Chord:
        pitches = [base_note.pitch] + [base_note.pitch.get_interval(part) for part in name]
        if inversion_base is not None:
            try:
                inv_index = pitches.index(inversion_base)
            except ValueError:
                raise ValueError(f"'{inversion_base}' does not belong to the chord")

            pitches = pitches[inv_index:] + pitches[:inv_index]

        octave = base_note.octave
        # If inversion is used, the new base note gets the same octave as the original
        notes = [Note(pitches[0], base_note.duration, octave)]
        for pitch in range(1, len(pitches)):
            if pitches[pitch].letter < pitches[pitch - 1].letter:
                octave += 1

            notes.append(Note(pitches[pitch], base_note.duration, octave))

        return cls(notes)

    def serialize(self) -> str:
        return "/".join([note.serialize(with_octave=True) for note in self.notes])
