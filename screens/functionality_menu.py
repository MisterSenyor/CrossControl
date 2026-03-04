from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel

from widgets.header import DeviceHeader
from functionalities.mouse import MouseDeviceTab


class DeviceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.header = DeviceHeader(on_back=self.go_back)
        # self.tabs = TabbedPanel(do_default_tab=False, tab_pos="left_top")
        self.tabs = TabbedPanel(do_default_tab=False)

        self.root_layout.add_widget(self.header)
        self.root_layout.add_widget(self.tabs)

        self.add_widget(self.root_layout)

    def set_device(self, name, ip):
        self.device = (name, ip)
        self.header.set_title(name)

        self.tabs.clear_widgets()
        self.tabs.clear_tabs()

        self.tabs.add_widget(MouseDeviceTab(self.device, "Test"))

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "device_menu"