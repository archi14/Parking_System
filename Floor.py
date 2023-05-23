from ParkingSpot import ParkingSpot;
from SpotType import SpotType;

class Floor:

    def __init__(self, total_spots, floor_number):
        self.floor_number = floor_number
        self.total_spots = total_spots
        self.each_spot_count = self.total_spots//3
        self.spots = {}
        self.spots[SpotType.SMALL] =  []
        self.spots[SpotType.MEDIUM] = []
        self.spots[SpotType.LARGE] = []
        
        for i in range(self.each_spot_count):
            parkingSpot = ParkingSpot(SpotType.SMALL)
            self.spots[SpotType.SMALL].append(parkingSpot)

        for i in range(self.each_spot_count):
            parkingSpot = ParkingSpot(SpotType.MEDIUM)
            self.spots[SpotType.MEDIUM].append(parkingSpot)

        for i in range(self.each_spot_count):
            parkingSpot = ParkingSpot(SpotType.LARGE)
            self.spots[SpotType.LARGE].append(parkingSpot)

    
    def book_spot(self, type, license, time):

        if len(self.spots[type])>0:
            print(f'remaining elements in spot are {self.spots[type]}')
            spot = self.spots[type].pop()
            spot.add_vehicle(license, self.floor_number, time)
            return spot
        
        raise ValueError

    def unbook_spot(self, type):
        parkingSpot = ParkingSpot(type)
        self.spots[type].append(parkingSpot)
        return True

    


        

