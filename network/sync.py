import socket
import json

from network.main_protocol import HEADER_SIZES, TERMINATOR


def pad(text, size):
    return text.encode("utf-8").ljust(size, b"\x00")


def sync_with_server(
    server_ipv6,
    port,
    my_device_name
):
    message = (
        pad(my_device_name, HEADER_SIZES["src"]) +
        pad("SERVER", HEADER_SIZES["dst"]) +
        pad("SYNC_REQ", HEADER_SIZES["proto"]) +
        TERMINATOR
    )

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
        sock.connect((server_ipv6, port))
        sock.sendall(message)

        data = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            if TERMINATOR in data:
                break

    response, _ = data.split(TERMINATOR, 1)
    payload = response[HEADER_SIZES["src"] + HEADER_SIZES["dst"] + HEADER_SIZES["proto"]:]
    return json.loads(payload.decode("utf-8"))