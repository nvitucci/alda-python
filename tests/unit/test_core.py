import pytest

from alda import core, pitch
from alda.core import Duration, Note, Part, Score, Chord
from alda.pitch import Accidental, Letter, Pitch


class TestCore:
    def test_default_score(self) -> None:
        score = Score()
        assert score.serialize() == "(tempo! 60)"

    def test_default_part(self) -> None:
        part = Part()
        assert part.serialize() == "piano:"

    def test_notes(self) -> None:
        assert Note(pitch.E).serialize() == "e4"
        assert Note(pitch.F_SHARP).serialize() == "f+4"
        assert Note(pitch.B_FLAT).serialize() == "b-4"

    def test_note_with_octave(self) -> None:
        note = Note(pitch.E)
        assert note.serialize(with_octave=True) == "o3 e4"

    def test_note_from_components(self) -> None:
        note = Note(Pitch(Letter.B, Accidental.FLAT))
        assert note.serialize() == "b-4"

    def test_note_duration(self) -> None:
        note = Note(pitch.E, duration=Duration(2))
        assert note.serialize() == "e2"

    def test_chord(self) -> None:
        note = Note(pitch.C)

        assert Chord.build_chord(note, core.DOM_7) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G), Note(pitch.B_FLAT)]
        )

    def test_chord_inversion(self) -> None:
        note = Note(pitch.C)

        assert Chord.build_chord(note, core.DOM_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G), Note(pitch.B_FLAT)]
        )
        assert Chord.build_chord(note, core.DOM_7, pitch.E) == Chord(
            [Note(pitch.E), Note(pitch.G), Note(pitch.B_FLAT), Note(pitch.C, octave=4)]
        )
        assert Chord.build_chord(note, core.DOM_7, pitch.G) == Chord(
            [Note(pitch.G), Note(pitch.B_FLAT), Note(pitch.C, octave=4), Note(pitch.E, octave=4)]
        )
        assert Chord.build_chord(note, core.DOM_7, pitch.B_FLAT) == Chord(
            [Note(pitch.B_FLAT), Note(pitch.C, octave=4), Note(pitch.E, octave=4), Note(pitch.G, octave=4)]
        )

        with pytest.raises(ValueError):
            Chord.build_chord(note, core.DOM_7, pitch.A)

    def test_all_c_chords(self):
        note = Note(pitch.C)

        assert Chord.build_chord(note, core.DOM_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G), Note(pitch.B_FLAT)]
        )

        assert Chord.build_chord(note, core.MAJ_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G), Note(pitch.B)]
        )

        assert Chord.build_chord(note, core.MIN_MAJ_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E_FLAT), Note(pitch.G), Note(pitch.B)]
        )

        assert Chord.build_chord(note, core.MIN_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E_FLAT), Note(pitch.G), Note(pitch.B_FLAT)]
        )

        assert Chord.build_chord(note, core.AUG_MAJ_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G_SHARP), Note(pitch.B)]
        )

        assert Chord.build_chord(note, core.AUG_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G_SHARP), Note(pitch.B_FLAT)]
        )

        assert Chord.build_chord(note, core.MIN_7_DIM_5, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E_FLAT), Note(pitch.G_FLAT), Note(pitch.B_FLAT)]
        )

        assert Chord.build_chord(note, core.DIM_7, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E_FLAT), Note(pitch.G_FLAT), Note(Pitch(Letter.B, [Accidental.FLAT] * 2))]
        )

        assert Chord.build_chord(note, core.DOM_7_DIM_5, pitch.C) == Chord(
            [Note(pitch.C), Note(pitch.E), Note(pitch.G_FLAT), Note(pitch.B_FLAT)]
        )
