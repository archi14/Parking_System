from Floor import Floor;

class Parking:

    def __init__(self, number_of_floors, spots):
        self.number_of_floors = number_of_floors
        self.floors = []
        self.booked = {}
        for floor in range(self.number_of_floors):
            self.floors.append(Floor(spots, floor))
    
    def enter(self, type, license, time):
        for floor in range(self.number_of_floors):
            try:
                spot = self.floors[floor].book_spot(type, license, time)
                self.booked[license] = spot
                print(f'Vehicle {license} has been parked at {floor} at {time}')
                return True
            except ValueError:
                continue
        
        raise ValueError
        
    def exit(self, license, time):

        if license in self.booked.keys():
            spot = self.booked[license]
            floor = spot.floor
            spot.remove_vehicle(license, spot.floor, time)
            self.floors[floor].unbook_spot(spot.type)
            return True
        
        raise ValueError