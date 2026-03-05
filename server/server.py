import socket
import json

from server.registry import DeviceRegistry
from network.main_protocol import *

SERVER_PORT = 1000

class CoordinationServer:
    def __init__(self, host="::", port=SERVER_PORT):
        self.host = host
        self.port = port
        self.registry = DeviceRegistry()

    def start(self):
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.listen(10)

            print(f"[SERVER] Listening on [{self.host}]:{self.port}")

            while True:
                conn, addr = server.accept()
                print(f"=== NEW CONNECTION {addr}")
                with conn:
                    self.handle_connection(conn, addr)

    def handle_connection(self, conn, addr):
        data = b""

        while True:
            chunk = conn.recv(4096)
            if not chunk:
                return
            data += chunk
            if TERMINATOR in data:
                break

        message, _ = data.split(TERMINATOR, 1)

        header = message[:HEADER_SIZE_TOTAL]
        payload = message[HEADER_SIZE_TOTAL:]

        src, _, proto = parse_header(header)

        ipv6_addr = addr[0]
        self.registry.register(src, ipv6_addr)

        if proto == "SYNC_REQ":
            self.send_sync_response(conn)

    def send_sync_response(self, conn):
        payload = json.dumps({
            "devices": self.registry.all_devices()
        }).encode("utf-8")

        response = (
            self.pad("SERVER", HEADER_SIZES["src"]) +
            self.pad("CLIENT", HEADER_SIZES["dst"]) +
            self.pad("SYNC_RESP", HEADER_SIZES["proto"]) +
            payload +
            TERMINATOR
        )

        conn.sendall(response)

    @staticmethod
    def pad(text, size):
        return text.encode("utf-8").ljust(size, b"\x00")


def main():
    server = CoordinationServer()
    server.registry.register("PC1", "1235")
    server.registry.register("PC2", "1235")
    server.registry.register("PC3", "1235")
    server.registry.register("PC4", "1235")
    server.start()

if __name__ == "__main__":
    main()