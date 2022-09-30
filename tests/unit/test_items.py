from alda.items import Accident
from alda.items import Note
from alda.items import Part
from alda.items import Pitch
from alda.items import Score


class TestScore:
    def test_default_score(self):
        score = Score()
        assert score.serialize() == "(tempo! 60)"

    def test_default_part(self):
        part = Part()
        assert part.serialize() == "piano:"

    def test_note(self):
        note = Note(pitch=Pitch.E)
        assert note.serialize() == "e4"

    def test_note_with_octave(self):
        note = Note(pitch=Pitch.E)
        assert note.serialize(with_octave=True) == "o3 e4"

    def test_note_accident(self):
        note = Note(pitch=Pitch.E, accident=Accident.FLAT)
        assert note.serialize() == "e-4"

    def test_note_duration(self):
        note = Note(pitch=Pitch.E, duration=2)
        assert note.serialize() == "e2"
