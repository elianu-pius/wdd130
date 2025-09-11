# tire_volume.py
import math
from datetime import date

width = int(input("Enter the width of the tire in mm (example 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (example 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (example 15): "))
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters")
today = date.today()

with open("volumes.txt", "a") as file:
    file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
