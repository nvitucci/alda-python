from alda import pitch


class TestPitch:
    def test_predefined_pitches(self) -> None:
        assert str(pitch.C) == "c"
        assert str(pitch.C_SHARP) == "c+"
        assert str(pitch.D_FLAT) == "d-"
        assert str(pitch.D) == "d"
        assert str(pitch.D_SHARP) == "d+"
        assert str(pitch.E_FLAT) == "e-"
        assert str(pitch.E) == "e"
        assert str(pitch.F) == "f"
        assert str(pitch.F_SHARP) == "f+"
        assert str(pitch.G_FLAT) == "g-"
        assert str(pitch.G) == "g"
        assert str(pitch.G_SHARP) == "g+"
        assert str(pitch.A_FLAT) == "a-"
        assert str(pitch.A) == "a"
        assert str(pitch.A_SHARP) == "a+"
        assert str(pitch.B_FLAT) == "b-"
        assert str(pitch.B) == "b"
