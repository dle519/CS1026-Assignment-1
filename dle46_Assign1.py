##
# This program simulates flipping a coin into a grid for a carnival game
from random import random

# Variable list
distance = float(input("Please enter the distance between the lines: "))  # Distance between the lines (in mm)
reward = int(input("Please enter the reward if the customer wins: "))  # How much the customer will win
radius = 14.0  # radius of the circle
customerPocket = ownerPocket = 0
# Constants
TOONIE = 2
ATTEMPTS = 1000

# Randomizing the location of the coin
for coinToss in range(ATTEMPTS):
    r = random()
    xCentre = -radius + (distance + radius) * r  # will randomize the centre of the circle from -14 to 90
    r = random()
    yCentre = -radius + (distance + radius) * r

    if (radius < xCentre < distance - radius) and (radius < yCentre < distance - radius):  # If the coin does not touch the square grid
        customerPocket += reward
    else:  # If the coin touches the square grid
        ownerPocket += TOONIE

# Owner making a profit or losing money
if customerPocket == 0:
    print("For 1000 toonie tosses, the owner will win all $2000!")
elif (ownerPocket / customerPocket) > 1:
    print("For 1000 toonie tosses, the owner may gain of ${}".format(ownerPocket))  # How much the owner will gain if he has a profit
elif 0 < (ownerPocket / customerPocket) < 1:
    print("For 1000 toonie tosses, the owner may lose ${}".format(abs(customerPocket)))  # How much the owner will lose to the customer if there is no profit

