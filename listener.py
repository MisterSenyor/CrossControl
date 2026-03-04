import socket
from network.main_protocol import *

class IPv6Listener:
    def __init__(self, host="::", port=9999, buffer_size=4096):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

    def start(self):
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.listen(5)

            print(f"[LISTENER] Listening on [{self.host}]:{self.port}")

            while True:
                conn, addr = server.accept()
                print(f"[CONNECT] From {addr}")

                with conn:
                    self.handle_connection(conn)

    def handle_connection(self, conn):
        data = b""

        while True:
            chunk = conn.recv(self.buffer_size)
            if not chunk:
                break

            data += chunk

            if TERMINATOR in data:
                break

        if TERMINATOR not in data:
            print("[ERROR] Message terminated unexpectedly")
            return

        message, _ = data.split(TERMINATOR, 1)

        if len(message) < HEADER_SIZE_TOTAL:
            print("[ERROR] Message too short")
            return

        header = message[:HEADER_SIZE_TOTAL]
        payload = message[HEADER_SIZE_TOTAL:]

        src, dst, proto = parse_header(header)

        print("[MESSAGE RECEIVED]")
        print(f"  SRC  : {src}")
        print(f"  DST  : {dst}")
        print(f"  PROTO: {proto}")
        print(f"  DATA : {payload!r}")

        self.dispatch(src, dst, proto, payload)

    def dispatch(self, src, dst, proto, payload):
        """
        Hook this into your app logic later.
        """
        print(f"[DISPATCH] {proto} from {src} to {dst}")
   
    
def main():
    listener = IPv6Listener()
    print("=== STARTING CONNECTION")
    listener.start()

if __name__ == "__main__":
    main()