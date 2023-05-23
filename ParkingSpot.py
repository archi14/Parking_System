
from tarfile import SUPPORTED_TYPES


class ParkingSpot:
    def __init__(self, type):
        self.type = type
        self.is_booked = False
        self.license = None
        self.time = None
        self.floor = None

    def add_vehicle(self, license, floor, time):
        self.license = license
        self.floor = floor
        self.time = time
        self.is_booked = True

    def remove_vehicle(self, license, floor, time):
        if self.is_booked:
            self.is_booked = False
            self.license = None
            self.time = None
            self.floor = None
            return True
            
        raise ValueError

