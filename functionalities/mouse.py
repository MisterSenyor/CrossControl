import socket
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.button import Button
from listener import HEADER_SIZES, TERMINATOR

def pad_field(text, size):
    raw = text.encode("utf-8")
    return raw.ljust(size, b"\x00")


class MouseDeviceTab(TabbedPanelItem):
    def __init__(self, device, title, **kwargs):
        super().__init__(text=title, **kwargs)
        self.device = device
        btn = Button(text="Send Command")
        btn.bind(on_press=self.send_command)
        self.add_widget(btn)
        
    def send_command(self, _):
        print("=== SENDING COMMAND")
        src = "1"
        dst = "2"
        proto = "SHARE"
        payload = b"10"
        ipv6_addr = "fe80::34d7:b2c6:1d56:c68d"
        port = 9999
        message = (
            pad_field(src, HEADER_SIZES["src"]) +
            pad_field(dst, HEADER_SIZES["dst"]) +
            pad_field(proto, HEADER_SIZES["proto"]) +
            payload +
            TERMINATOR
        )

        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
            sock.connect((ipv6_addr, port))
            sock.sendall(message) 