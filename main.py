# Programmers: Oreoluwa Adebusoye & Andrew Leimbach
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/02/2024
# Lab Assignment: 03
# Problem Statement: Winter is coming! One winter sport is the ski jump, where the score is determined by the distance traveled after skiing down a ramp and into the air.
#                    What type of speed does a ski jumper need to achieve on the ramp to make a good distance on their jump?
# Purpose: Given the type of ski jump (normal vs. large) and the jumper’s speed at the end of the ramp, this program predicts how far they will jump
# Data In: Hill type, Speed
# Data Out: Distance, Points earned
# Credits: Used calculations provided in class

# Include built-in math module
import math

# Prompt user to input hill type
hill_type = input("Enter hill type (Normal or Large): ")

# Set parameters based on hill type
if hill_type.lower() == "normal":
    height = 46
    points_per_meter = 2
    par = 90
elif hill_type.lower()== "large":
    height = 70
    points_per_meter = 1.8
    par = 120
else:
    print("Invalid hill type. Please enter a valid value (Normal or Large).")
    exit()

# Prompt user to input jumper’s speed
speed = float(input("\nEnter jumper's speed in m/s: "))

# Calculate time in the air
time_in_air = math.sqrt((2 * height) / 9.8)

# Calculate distance traveled
distance = speed * time_in_air

# Calculate the points earned
points_earned = 60 + (distance - par) * points_per_meter

# Output distance
print(f"\nDistance: {distance:.2f} meters\n")

# Step 10: Output points earned
print(f"Points earned: {points_earned:.2f}\n")

# Output messages based on points earned
if points_earned >= 61:
    print("Great job for doing better than par!")
elif points_earned < 10:
    print("What happened??")
else:
    print("Sorry you didn’t go very far.")
