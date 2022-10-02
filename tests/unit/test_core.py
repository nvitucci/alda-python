from alda import pitch
from alda.core import Note, Part, Score
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
        note = Note(pitch.E, duration=2)
        assert note.serialize() == "e2"
