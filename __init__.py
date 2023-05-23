from re import S
from Parking import Parking;
from SpotType import SpotType;
import time

def main():
    floors = int(input('Please enter the number of floors\n'))
    spots = int(input('Please enter the number of spots at each floor\n'))
    parking = Parking(floors, spots)
    while True:
        license = input('Please enter the license number\n')
        type = int(input('Please enter your vehicle type 1->SMALL 2->MEDIUM 3->LARGE\n'))
        operation = int(input('Enter 0 for entry and 1 for exit\n'))
        spot = None
        if type == SpotType.SMALL.value:
            spot = SpotType.SMALL
        if type == SpotType.MEDIUM.value:
            spot = SpotType.MEDIUM
        if type == SpotType.LARGE.value:
            spot = SpotType.LARGE
        print(spot)
        if operation==0:
            try:
                parking.enter(spot, license, time.time())
            except ValueError:
                print('No parking space is available, please try again later')
        else:
            try:
                parking.exit(license, time.time())
            except ValueError:
                print(f'The vehicle with license {license} is not available, please try again with a different license number')

if __name__ == '__main__':
    main()