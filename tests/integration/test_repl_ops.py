import re
import time

import pytest

from alda import Client

CODE = "piano: o3 c2 d2 e2"


class TestReplOps:
    @pytest.fixture(autouse=True, scope="class")
    def client(self):
        c = Client()
        yield c
        del c

    @pytest.fixture(autouse=True)
    def reset_score(self, client) -> None:
        client.new_score()

        # Pause to allow the server to respond
        time.sleep(1)
        yield
        # Pause to allow the server to play
        time.sleep(4)

    def test_play(self, client) -> None:
        assert client.play(CODE) == {"status": ["done"]}

    def test_play_malformed(self, client) -> None:
        code = "piano: o3 c2 d2 y"

        assert client.play(code) == {
            "problems": ["<no file>:1:18 Unexpected control character (0) in note/rest/name"],
            "status": ["done", "error"],
        }

    def test_describe(self, client) -> None:
        assert client.describe() == {
            "ops": {
                "clone": {},
                "describe": {},
                "eval": {},
                "eval-and-play": {},
                "export": {},
                "instruments": {},
                "load": {},
                "new-score": {},
                "replay": {},
                "score-ast": {},
                "score-data": {},
                "score-events": {},
                "score-text": {},
                "stop": {},
            },
            "status": ["done"],
            "versions": {"alda": {"version-string": "2.2.3"}},
        }

    def test_export_empty(self, client) -> None:
        assert client.export() == {
            "binary-data": b"MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x80MTrk\x00\x00"
            b"\x00\x0b\x00\xffQ\x03\x07\xa1 \x00\xff/\x00",
            "status": ["done"],
        }

    def test_export(self, client) -> None:
        client.load(CODE)

        assert client.export() == {
            "binary-data": b"MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x80MTrk\x00\x00"
            b"\x002\x00\xffQ\x03\x07\xa1 \x00\xc0\x00\x00\x00\x00\xb0"
            b"\x0bd\x00\n@\x00\x900E\x81f\x800E\x1a\x902E\x81f\x802E\x1a"
            b"\x904E\x81f\x804E\x00\xff/\x00",
            "status": ["done"],
        }

    def test_instruments(self, client) -> None:
        res = client.instruments()

        assert set(res.keys()) == {"instruments", "status"}
        assert res["status"] == ["done"]
        assert len(res["instruments"]) == 129
        assert all(el.startswith("midi-") for el in res["instruments"])
        assert res["instruments"][-1] == "midi-percussion"

    def test_load_empty(self, client) -> None:
        assert client.load("") == {"status": ["done"]}

    def test_load(self, client) -> None:
        assert client.load(CODE) == {"status": ["done"]}

    def test_new_score(self, client) -> None:
        assert client.new_score() == {"status": ["done"]}

    def test_replay_empty(self, client) -> None:
        assert client.replay() == {"status": ["done"]}

    def test_replay_empty_with_start_end(self, client) -> None:
        assert client.replay(start="0:00", end="0:01") == {"status": ["done"]}

    def test_replay(self, client) -> None:
        client.load(CODE)

        assert client.replay() == {"status": ["done"]}

    def test_replay_with_start_end(self, client) -> None:
        client.load(CODE)

        assert client.replay(start="0:00", end="0:01") == {"status": ["done"]}

    def test_score_ast_empty(self, client) -> None:
        assert client.score_ast() == {"ast": '{"type":"RootNode"}', "status": ["done"]}

    def test_score_ast(self, client) -> None:
        client.load(CODE)

        assert client.score_ast() == {
            "ast": '{"children":[{"children":[{"children":[{"children":[{"literal":"piano","source-context":{"column":1,"line":1},"type":"PartNameNode"}],"source-context":{"column":1,"line":1},"type":"PartNamesNode"}],"source-context":{"column":1,"line":1},"type":"PartDeclarationNode"},{"children":[{"literal":3,"source-context":{"column":8,"line":1},"type":"OctaveSetNode"},{"children":[{"children":[{"literal":"c","source-context":{"column":11,"line":1},"type":"NoteLetterNode"}],"source-context":{"column":11,"line":1},"type":"NoteLetterAndAccidentalsNode"},{"children":[{"children":[{"literal":2,"type":"DenominatorNode"}],"source-context":{"column":12,"line":1},"type":"NoteLengthNode"}],"source-context":{"column":12,"line":1},"type":"DurationNode"}],"source-context":{"column":11,"line":1},"type":"NoteNode"},{"children":[{"children":[{"literal":"d","source-context":{"column":14,"line":1},"type":"NoteLetterNode"}],"source-context":{"column":14,"line":1},"type":"NoteLetterAndAccidentalsNode"},{"children":[{"children":[{"literal":2,"type":"DenominatorNode"}],"source-context":{"column":15,"line":1},"type":"NoteLengthNode"}],"source-context":{"column":15,"line":1},"type":"DurationNode"}],"source-context":{"column":14,"line":1},"type":"NoteNode"},{"children":[{"children":[{"literal":"e","source-context":{"column":17,"line":1},"type":"NoteLetterNode"}],"source-context":{"column":17,"line":1},"type":"NoteLetterAndAccidentalsNode"},{"children":[{"children":[{"literal":2,"type":"DenominatorNode"}],"source-context":{"column":18,"line":1},"type":"NoteLengthNode"}],"source-context":{"column":18,"line":1},"type":"DurationNode"}],"source-context":{"column":17,"line":1},"type":"NoteNode"}],"source-context":{"column":8,"line":1},"type":"EventSequenceNode"}],"source-context":{"column":1,"line":1},"type":"PartNode"}],"type":"RootNode"}',
            "status": ["done"],
        }

    def test_score_data_empty(self, client) -> None:
        assert client.score_data() == {
            "data": '{"aliases":{},"current-parts":[],"events":[],"global-attributes":{},"markers":{},"parts":{},"variables":{}}',
            "status": ["done"],
        }

    def test_score_data(self, client) -> None:
        client.load(CODE)

        res = client.score_data()
        res["data"] = re.sub("0x[0-9a-f]{10}", "0x0000000000", res["data"])
        assert res == {
            "data": '{"aliases":{},"current-parts":["0x0000000000"],"events":[{"audible-duration":900,"duration":1000,"midi-note":48,"offset":0,"panning":0.5,"part":"0x0000000000","track-volume":0.7874015748031497,"volume":0.5421},{"audible-duration":900,"duration":1000,"midi-note":50,"offset":1000,"panning":0.5,"part":"0x0000000000","track-volume":0.7874015748031497,"volume":0.5421},{"audible-duration":900,"duration":1000,"midi-note":52,"offset":2000,"panning":0.5,"part":"0x0000000000","track-volume":0.7874015748031497,"volume":0.5421}],"global-attributes":{},"markers":{},"parts":{"0x0000000000":{"current-offset":3000,"duration":{"components":[{"denominator":2,"dots":0}]},"key-signature":{},"last-offset":2000,"name":"piano","octave":3,"panning":0.5,"quantization":0.9,"reference-pitch":440,"stock-instrument":"midi-acoustic-grand-piano","tempo":120,"tempo-role":"master","tempo-values":{},"time-scale":1,"track-volume":0.7874015748031497,"transposition":0,"volume":0.5421}},"variables":{}}',
            "status": ["done"],
        }

    def test_score_events_empty(self, client) -> None:
        assert client.score_events() == {"events": "[]", "status": ["done"]}

    def test_score_events(self, client) -> None:
        client.load(CODE)

        assert client.score_events() == {
            "events": '[{"type":"part-declaration","value":{"names":["piano"]}},{"attribute":"octave","type":"attribute-update","value":3},{"type":"note","value":{"duration":{"components":[{"denominator":2,"dots":0}]},"pitch":{"accidentals":[],"letter":"C"}}},{"type":"note","value":{"duration":{"components":[{"denominator":2,"dots":0}]},"pitch":{"accidentals":[],"letter":"D"}}},{"type":"note","value":{"duration":{"components":[{"denominator":2,"dots":0}]},"pitch":{"accidentals":[],"letter":"E"}}}]',
            "status": ["done"],
        }

    def test_score_text_empty(self, client) -> None:
        assert client.score_text() == {"text": "", "status": ["done"]}

    def test_score_text(self, client) -> None:
        client.load(CODE)

        assert client.score_text() == {"text": "piano: o3 c2 d2 e2\n", "status": ["done"]}

    def test_stop(self, client) -> None:
        assert client.stop() == {"status": ["done"]}
