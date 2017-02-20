# Julio Ureta, CSC102

#Define a class called Car with the following attributes:
#    Total Odometer Miles
#    Speed in miles per hour
#    Driver Name
#    Sponsor
import random

class Car():
    def __init__(self):
        print("A Car is instantiated.")
        self.total_odometer_miles = 0.0
        self.speed_in_miles_per_hour = random.randint(1, 120)
        self.driver_name = ""
        self.sponsor = ""

# Utility functions
def get_total_odometer_miles(a_car):
    a_car.total_odometer_miles = (a_car.total_odometer_miles + a_car.speed_in_miles_per_hour * 1/60)

def get_speed_in_miles_per_hour(a_car):
    a_car.speed_in_miles_per_hour = random.randint(1,120)

def get_driver_distance(a_car):
    print(a_car.driver_name, "at mile", a_car.total_odometer_miles)

# Winning factor functions
def no_winner(cars):
    
    for car in cars:        
        if car.total_odometer_miles >= 500:
            return False        
    return True

def check_for_winner(cars):
    
    while no_winner(cars):
        for car in cars:

            get_speed_in_miles_per_hour(car)
            get_total_odometer_miles(car)
            get_driver_distance(car)

def get_winner(cars):
    
    winner = None

    for car in cars:
        if car.total_odometer_miles >= 500:
            winner = car
    return winner

# Main function
def main():

    #Initialize all the drivers.
    driver_one = Car()
    driver_one.driver_name = "Phil"
    driver_one.sponsor = "IBM"
    
    driver_two = Car()
    driver_two.driver_name = "Cookie Monster"
    driver_two.sponsor = "Sesame Street"
    
    driver_three = Car()
    driver_three.driver_name = "Tyler"
    driver_three.sponsor = "NASA"
    
    driver_four = Car()
    driver_four.driver_name = "Frankie"
    driver_four.sponsor = "Obisidan"
    
    driver_five = Car()
    driver_five.driver_name = "Victor"
    driver_five.sponsor = "Tonka"
    
    driver_six = Car()
    driver_six.driver_name = "Jose"
    driver_six.sponsor = "Bethesda"
    
    driver_seven = Car()
    driver_seven.driver_name = "Alex"
    driver_seven.sponsor = "Matell"
    
    driver_eight = Car()
    driver_eight.driver_name = "Brock"
    driver_eight.sponsor = "Heineken"
    
    driver_nine = Car()
    driver_nine.driver_name = "Jase"
    driver_nine.sponsor = "Crayola"
    
    driver_ten = Car()
    driver_ten.driver_name = "Cade"
    driver_ten.sponsor = "Roseart"
    
    driver_eleven = Car()
    driver_eleven.driver_name = "Melissa"
    driver_eleven.sponsor = "Telltale Games"
    
    driver_twelve = Car()
    driver_twelve.driver_name = "Cecil"
    driver_twelve.sponsor = "Toys R Us"
    
    driver_thirteen = Car()
    driver_thirteen.driver_name = "Jy"
    driver_thirteen.sponsor = "Australia"
    
    driver_fourteen = Car()
    driver_fourteen.driver_name = "Adam"
    driver_fourteen.sponsor = "Google"
    
    driver_fifteen = Car()
    driver_fifteen.driver_name = "Ian"
    driver_fifteen.sponsor = "Ubisoft"
    
    driver_sixteen = Car()
    driver_sixteen.driver_name = "Matt"
    driver_sixteen.sponsor = "Rockstar"
    
    driver_seventeen = Car()
    driver_seventeen.driver_name = "Aaron"
    driver_seventeen.sponsor = "Company X"
    
    driver_eighteen = Car()
    driver_eighteen.driver_name = "Jack"
    driver_eighteen.sponsor = "Black"
    
    driver_nineteen = Car()
    driver_nineteen.driver_name = "Fred"
    driver_nineteen.sponsor = "Dread"
    
    driver_twenty = Car()
    driver_twenty.driver_name = "Why"
    driver_twenty.sponsor = "Because"

    # Store all of the drivers in a list.
    cars = []
    cars.append(driver_one)
    cars.append(driver_two)
    cars.append(driver_three)
    cars.append(driver_four)
    cars.append(driver_five)
    cars.append(driver_six)
    cars.append(driver_seven)
    cars.append(driver_eight)
    cars.append(driver_nine)
    cars.append(driver_ten)
    cars.append(driver_eleven)
    cars.append(driver_twelve)
    cars.append(driver_thirteen)
    cars.append(driver_fourteen)
    cars.append(driver_fifteen)
    cars.append(driver_sixteen)
    cars.append(driver_seventeen)
    cars.append(driver_eighteen)
    cars.append(driver_nineteen)
    cars.append(driver_twenty)

    check_for_winner(cars)

    winner = get_winner(cars)

    #Display the winner.
    print("The winner is", winner.driver_name, "who was sponsored by", winner.sponsor)

main()
