from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from data.devices import DEVICES


class DeviceMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="Select a Device", size_hint=(1, 0.1)))

        for device in DEVICES:
            btn = Button(text=device.name, size_hint=(1, 0.15))
            btn.bind(on_press=lambda _, d=device: self.open_device(d))
            layout.add_widget(btn)

        self.add_widget(layout)

    def open_device(self, device):
        self.manager.transition.direction = 'left'
        device_screen = self.manager.get_screen("device_screen")
        device_screen.set_device(device)
        self.manager.current = "device_screen"