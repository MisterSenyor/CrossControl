from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from data.devices import DeviceDB
from server.server import SERVER_PORT
from network.sync import sync_with_server


class DeviceMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.db = DeviceDB()

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.layout.add_widget(Label(text="Devices", size_hint=(1, 0.1)))

        self.sync_btn = Button(text="🔄 Sync Devices", size_hint=(1, 0.15))
        self.sync_btn.bind(on_press=self.sync)
        self.layout.add_widget(self.sync_btn)

        self.device_list = BoxLayout(orientation="vertical", spacing=5)
        self.layout.add_widget(self.device_list)

        self.add_widget(self.layout)

    def sync(self, _):
        result = sync_with_server(
            server_ipv6="fe80::34d7:b2c6:1d56:c68d",
            port=SERVER_PORT,
            my_device_name="Controller"
        )

        self.db.update_from_sync(result["devices"])
        self.refresh_device_list()

    def refresh_device_list(self):
        self.device_list.clear_widgets()

        for name, ipv6 in self.db.list_devices():
            btn = Button(text=f"{name} ({ipv6})")
            btn.bind(on_press=lambda _, n=name: self.open_device(n))
            self.device_list.add_widget(btn)

    def open_device(self, device_name):
        device_screen = self.manager.get_screen("device_screen")
        device_screen.set_device(device_name)
        self.manager.current = "device_screen"