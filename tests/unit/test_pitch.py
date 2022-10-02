from alda import interval, pitch
from alda.pitch import Accidental, Letter, Interval, Pitch


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

    def test_interval(self):
        assert pitch.C.get_interval(Interval(7, -1)) == pitch.B_FLAT
        assert pitch.C.get_interval(Interval(7, -2)) == Pitch(Letter.B, [Accidental.FLAT, Accidental.FLAT])

        assert pitch.C_SHARP.get_interval(Interval(7, -1)) == pitch.B
        assert pitch.C_SHARP.get_interval(Interval(7, -2)) == Pitch(Letter.B, Accidental.FLAT)
        
    def test_all_c_intervals(self):
        c = pitch.C
        
        assert str(c.get_interval(interval.P1)) == "c"
        assert str(c.get_interval(interval.m2)) == "d-"
        assert str(c.get_interval(interval.M2)) == "d"
        assert str(c.get_interval(interval.m3)) == "e-"
        assert str(c.get_interval(interval.M3)) == "e"
        assert str(c.get_interval(interval.P4)) == "f"
        assert str(c.get_interval(interval.P5)) == "g"
        assert str(c.get_interval(interval.m6)) == "a-"
        assert str(c.get_interval(interval.M6)) == "a"
        assert str(c.get_interval(interval.m7)) == "b-"
        assert str(c.get_interval(interval.M7)) == "b"
        assert str(c.get_interval(interval.P8)) == "c"

        assert str(c.get_interval(interval.d2)) == "d--"
        assert str(c.get_interval(interval.A1)) == "c+"
        assert str(c.get_interval(interval.d3)) == "e--"
        assert str(c.get_interval(interval.A2)) == "d+"
        assert str(c.get_interval(interval.d4)) == "f-"
        assert str(c.get_interval(interval.A3)) == "e+"
        assert str(c.get_interval(interval.d5)) == "g-"
        assert str(c.get_interval(interval.A4)) == "f+"
        assert str(c.get_interval(interval.d6)) == "a--"
        assert str(c.get_interval(interval.A5)) == "g+"
        assert str(c.get_interval(interval.d7)) == "b--"
        assert str(c.get_interval(interval.A6)) == "a+"
        assert str(c.get_interval(interval.d8)) == "c-"
        assert str(c.get_interval(interval.A7)) == "b+"
        
    def test_all_c_sharp_intervals(self):
        c_sharp = pitch.C_SHARP
        
        assert str(c_sharp.get_interval(interval.P1)) == "c+"
        assert str(c_sharp.get_interval(interval.m2)) == "d"
        assert str(c_sharp.get_interval(interval.M2)) == "d+"
        assert str(c_sharp.get_interval(interval.m3)) == "e"
        assert str(c_sharp.get_interval(interval.M3)) == "e+"
        assert str(c_sharp.get_interval(interval.P4)) == "f+"
        assert str(c_sharp.get_interval(interval.P5)) == "g+"
        assert str(c_sharp.get_interval(interval.m6)) == "a"
        assert str(c_sharp.get_interval(interval.M6)) == "a+"
        assert str(c_sharp.get_interval(interval.m7)) == "b"
        assert str(c_sharp.get_interval(interval.M7)) == "b+"
        assert str(c_sharp.get_interval(interval.P8)) == "c+"

        assert str(c_sharp.get_interval(interval.d2)) == "d-"
        assert str(c_sharp.get_interval(interval.A1)) == "c++"
        assert str(c_sharp.get_interval(interval.d3)) == "e-"
        assert str(c_sharp.get_interval(interval.A2)) == "d++"
        assert str(c_sharp.get_interval(interval.d4)) == "f"
        assert str(c_sharp.get_interval(interval.A3)) == "e++"
        assert str(c_sharp.get_interval(interval.d5)) == "g"
        assert str(c_sharp.get_interval(interval.A4)) == "f++"
        assert str(c_sharp.get_interval(interval.d6)) == "a-"
        assert str(c_sharp.get_interval(interval.A5)) == "g++"
        assert str(c_sharp.get_interval(interval.d7)) == "b-"
        assert str(c_sharp.get_interval(interval.A6)) == "a++"
        assert str(c_sharp.get_interval(interval.d8)) == "c"
        assert str(c_sharp.get_interval(interval.A7)) == "b++"

    def test_all_d_flat_intervals(self):
        d_flat = pitch.D_FLAT

        assert str(d_flat.get_interval(interval.P1)) == "d-"
        assert str(d_flat.get_interval(interval.m2)) == "e--"
        assert str(d_flat.get_interval(interval.M2)) == "e-"
        assert str(d_flat.get_interval(interval.m3)) == "f--"
        assert str(d_flat.get_interval(interval.M3)) == "f-"
        assert str(d_flat.get_interval(interval.P4)) == "g-"
        assert str(d_flat.get_interval(interval.P5)) == "a-"
        assert str(d_flat.get_interval(interval.m6)) == "b--"
        assert str(d_flat.get_interval(interval.M6)) == "b-"
        assert str(d_flat.get_interval(interval.m7)) == "c--"
        assert str(d_flat.get_interval(interval.M7)) == "c-"
        assert str(d_flat.get_interval(interval.P8)) == "d-"

        assert str(d_flat.get_interval(interval.d2)) == "e---"
        assert str(d_flat.get_interval(interval.A1)) == "d"
        assert str(d_flat.get_interval(interval.d3)) == "f---"
        assert str(d_flat.get_interval(interval.A2)) == "e"
        assert str(d_flat.get_interval(interval.d4)) == "g--"
        assert str(d_flat.get_interval(interval.A3)) == "f"
        assert str(d_flat.get_interval(interval.d5)) == "a--"
        assert str(d_flat.get_interval(interval.A4)) == "g"
        assert str(d_flat.get_interval(interval.d6)) == "b---"
        assert str(d_flat.get_interval(interval.A5)) == "a"
        assert str(d_flat.get_interval(interval.d7)) == "c---"
        assert str(d_flat.get_interval(interval.A6)) == "b"
        assert str(d_flat.get_interval(interval.d8)) == "d--"
        assert str(d_flat.get_interval(interval.A7)) == "c"
