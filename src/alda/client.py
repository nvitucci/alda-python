import nrepl


class Client:
    client = None

    def __init__(self, host: str = "localhost", port: int = 12345):
        """
        Creates an instance of the Python client that connects to
        a running Alda REPL server.

        :param host: the Alda REPL server address
        :type host: str
        :param port: the Alda REPL server port
        :type port: int
        """
        # TODO: add logging
        conn_string = f"nrepl://{host}:{port}"
        self.client = nrepl.connect(conn_string)

    def play(self, code: str) -> dict:
        """
        Parses the provided input in the context of the current score,
        updates the score with the parse results, and plays any new
        events that were added to the score.
        This is the operation that occurs in an Alda REPL session each
        time you enter a line of Alda code and press Enter.

        :param code: a string of Alda code
        :type code: str
        :return:
            - status
            - problems - if there were any
        :rtype: dict
        """
        self.client.write({"op": "eval-and-play", "code": code})
        return self.client.read()

    def export(self) -> dict:
        """
        Exports the current score to MIDI and returns the binary data
        to be saved as a MIDI file.

        :return:
            - status
            - problems - if there were any
            - binary-data - exported MIDI binary data for the current score
        :rtype: dict
        """
        raise NotImplementedError

    def instruments(self) -> dict:
        """
        Returns the list of instruments available to use in an Alda score.

        :return:
            - status
            - problems - if there were any
            - instruments - the list of available instruments
        :rtype: dict
        """
        raise NotImplementedError

    def load(self, code: str) -> dict:
        """
        Parses the provided input as a new score and loads the score into the REPL server.

        :param code: a string of Alda code
        :type code: str
        :return:
            - status
            - problems - if there were any
        :rtype: dict
        """
        raise NotImplementedError

    def new_score(self) -> dict:
        """
        Resets the REPL server state and initializes a new score.

        :return:
            - status
            - problems - if there were any
        :rtype: dict
        """
        raise NotImplementedError

    def replay(self, start: str = None, end: str = None) -> dict:
        """
        Parses the provided input as a new score and loads the score
        into the REPL server.
        Note: in the server API, the parameters are called "from" and
        "to" respectively.

        :param start: a string that is either a minute-second marking
        (e.g. 0:30) or a marker name (e.g. verse), representing where
        in the score to start playing
        :type start: str
        :param end: a string that is either a minute-second marking
        (e.g. 1:00) or a marker name (e.g. chorus), representing where
        in the score to stop playing
        :type end: str
        :return:
            - status
            - problems - if there were any
        :rtype: dict
        """
        raise NotImplementedError

    def score_ast(self) -> dict:
        """
        Returns the parsed AST of the current score.
        (This is the output that you get when you run "alda parse -o ast ..."
        at the command line.)

        :return:
            - status
            - problems - if there were any
            - ast - the parsed AST of the current score, as a JSON string
        :rtype: dict
        """
        raise NotImplementedError

    def score_data(self) -> dict:
        """
        Returns a data representation of the current score.
        (This is the output that you get when you run "alda parse -o data ..."
        at the command line.)

        :return:
            - status
            - problems - if there were any
            - data - a data representation of the current score
        :rtype: dict
        """
        raise NotImplementedError

    def score_events(self) -> dict:
        """
        Returns the parsed events output of the score.
        (This is the output that you get when you run "alda parse -o events ..."
        at the command line.)

        :return:
            - status
            - problems - if there were any
            - events - the parsed events output of the current score
        :rtype: dict
        """
        raise NotImplementedError

    def score_text(self) -> dict:
        """
        Returns the text (Alda code) of the current score.

        :return:
            - status
            - problems - if there were any
            - text - the Alda code of the current score
        :rtype: dict
        """
        raise NotImplementedError

    def stop(self) -> dict:
        """
        Stops playback.

        :return:
            - status
            - problems - if there were any
        :rtype: dict
        """
        raise NotImplementedError
