class DeviceDB:
    def __init__(self):
        self.devices = {}

    def update_from_sync(self, devices):
        for d in devices:
            self.devices[d["name"]] = d["ipv6"]

    def list_devices(self):
        return list(self.devices.items())