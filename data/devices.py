class Device:
    def __init__(self, name, device_id):
        self.name = name
        self.device_id = device_id


DEVICES = [
    Device("Living Room Sensor", "dev_001"),
    Device("Garage Controller", "dev_002"),
    Device("Office Monitor", "dev_003"),
]