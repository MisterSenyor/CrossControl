from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class DeviceHeader(BoxLayout):
    def __init__(self, on_back, **kwargs):
        super().__init__(orientation="horizontal", size_hint=(1, 0.1), **kwargs)

        self.back_button = Button(text="←", size_hint=(0.15, 1))
        self.back_button.bind(on_press=lambda _: on_back())

        self.title = Label(text="", halign="left", valign="middle")

        self.add_widget(self.back_button)
        self.add_widget(self.title)

    def set_title(self, text):
        self.title.text = text