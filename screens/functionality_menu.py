from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel

from widgets.header import DeviceHeader
from functionalities.mouse import BaseDeviceTab


class DeviceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root_layout = BoxLayout(orientation="vertical")

        self.header = DeviceHeader(on_back=self.go_back)
        self.tabs = TabbedPanel(do_default_tab=False)

        self.root_layout.add_widget(self.header)
        self.root_layout.add_widget(self.tabs)

        self.add_widget(self.root_layout)

    def set_device(self, device):
        self.device = device
        self.header.set_title(device.name)

        self.tabs.clear_widgets()

        self.tabs.add_widget(BaseDeviceTab(device, "Test"))

    def go_back(self):
        self.manager.current = "device_menu"