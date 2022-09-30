from alda.core import Accident
from alda.core import Note
from alda.core import Part
from alda.core import Pitch
from alda.core import Score


class TestCore:
    def test_default_score(self) -> None:
        score = Score()
        assert score.serialize() == "(tempo! 60)"

    def test_default_part(self) -> None:
        part = Part()
        assert part.serialize() == "piano:"

    def test_note(self) -> None:
        note = Note(pitch=Pitch.E)
        assert note.serialize() == "e4"

    def test_note_with_octave(self) -> None:
        note = Note(pitch=Pitch.E)
        assert note.serialize(with_octave=True) == "o3 e4"

    def test_note_accident(self) -> None:
        note = Note(pitch=Pitch.E, accident=Accident.FLAT)
        assert note.serialize() == "e-4"

    def test_note_duration(self) -> None:
        note = Note(pitch=Pitch.E, duration=2)
        assert note.serialize() == "e2"
