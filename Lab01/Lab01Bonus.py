#
# Gregory Jones
# January 15, 2026
# This program calculates the number of hours and minutes it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.
miles = float(input("How many miles are you traveling? "))

# Get the speed in MPH.
speed = float(input("What is your speed in MPH? "))

# Calculate the travel time.
travel_time = miles / speed

# Calculate the minutes of travel time.
remainder = miles % speed

# Display the hours and minutes of travel time (minutes formatted to 2 decimal places).
print(f"It will take you {travel_time:.0f} hours and {remainder:.2f} minutes to get there.")
