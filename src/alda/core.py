from typing import List, Tuple

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

    def __eq__(self, other):
        return self.length == other.length

    def __str__(self):
        return str(self.length)


class Note:
    def __init__(self, pitch: Pitch, duration: Duration = Duration(4), octave: int = 3):
        self.pitch = pitch
        self.duration = duration
        self.octave = octave

    def __eq__(self, other):
        return self.pitch == other.pitch and self.duration == other.duration and self.octave == other.octave

    def serialize(self, with_octave: bool = False) -> str:
        ser = f"{self.pitch}{self.duration}"

        if with_octave:
            ser = f"o{self.octave} {ser}"

        return ser


DOM_7 = (interval.M3, interval.P5, interval.m7)
MAJ_7 = (interval.M3, interval.P5, interval.M7)
MIN_MAJ_7 = (interval.m3, interval.P5, interval.M7)
MIN_7 = (interval.m3, interval.P5, interval.m7)
AUG_MAJ_7 = (interval.M3, interval.A5, interval.M7)
AUG_7 = (interval.M3, interval.A5, interval.m7)
MIN_7_DIM_5 = (interval.m3, interval.d5, interval.m7)
DIM_7 = (interval.m3, interval.d5, interval.d7)
DOM_7_DIM_5 = (interval.M3, interval.d5, interval.m7)


class Chord:
    def __init__(self, notes: List[Note]):
        self.notes = notes

    def __eq__(self, other):
        return self.notes == other.notes

    def __repr__(self):
        return self.serialize()

    @staticmethod
    def build_chord(base_note: Note, name: Tuple[Interval], inversion_base: Pitch = None):
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

        return Chord(notes)

    def serialize(self):
        return "/".join([note.serialize(with_octave=True) for note in self.notes])
