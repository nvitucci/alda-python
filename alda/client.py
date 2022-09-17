import nrepl


class Client:
    client = None

    def __init__(self, host: str = "localhost", port: int = 12345):
        # TODO: add logging
        conn_string = f"nrepl://{host}:{port}"
        self.client = nrepl.connect(conn_string)

    def eval_play(self, code: str):
        self.client.write({"op": "eval-and-play", "code": code})
        return self.client.read()
