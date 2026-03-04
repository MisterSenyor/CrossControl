from kivy.uix.tabbedpanel import TabbedPanelItem


class BaseDeviceTab(TabbedPanelItem):
    def __init__(self, device, title, **kwargs):
        super().__init__(text=title, **kwargs)
        self.device = device