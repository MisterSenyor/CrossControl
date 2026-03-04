class DeviceRegistry:
    def __init__(self):
        self.devices = {}

    def register(self, name, ipv6):
        self.devices[name] = ipv6

    def all_devices(self):
        return [
            {"name": name, "ipv6": ipv6}
            for name, ipv6 in self.devices.items()
        ]