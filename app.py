from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.device_menu import DeviceMenuScreen
from screens.functionality_menu import DeviceScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(DeviceMenuScreen(name="device_menu"))
        sm.add_widget(DeviceScreen(name="device_screen"))

        return sm


if __name__ == "__main__":
    MyApp().run()