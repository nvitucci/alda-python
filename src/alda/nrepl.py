import nrepl


class NREPLClient:
    client = None

    def __init__(self, host, port):
        conn_string = f"nrepl://{host}:{port}"
        self.client = nrepl.connect(conn_string)

    def write(self, message):
        return self.client.write(message)

    def read(self):
        return self.client.read()

    def close(self):
        return self.client.close()
