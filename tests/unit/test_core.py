from alda.core import Accidental, Note, Part, Pitch, Score


class TestCore:
    def test_default_score(self) -> None:
        score = Score()
        assert score.serialize() == "(tempo! 60)"

    def test_default_part(self) -> None:
        part = Part()
        assert part.serialize() == "piano:"

    def test_notes(self) -> None:
        assert Note(pitch=Pitch.E).serialize() == "e4"
        assert Note(pitch=Pitch.F_SHARP).serialize() == "f+4"
        assert Note(pitch=Pitch.B_FLAT).serialize() == "b-4"

    def test_note_with_octave(self) -> None:
        note = Note(pitch=Pitch.E)
        assert note.serialize(with_octave=True) == "o3 e4"

    def test_note_accident(self) -> None:
        note = Note(pitch=Pitch.E, accidental=Accidental.FLAT)
        assert note.serialize() == "e-4"

    def test_note_duration(self) -> None:
        note = Note(pitch=Pitch.E, duration=2)
        assert note.serialize() == "e2"
