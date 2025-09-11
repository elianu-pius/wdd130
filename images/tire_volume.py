import math
from datetime import datetime

print()
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

print()
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter))


print()
volume_rounded = round(volume, 2)
print(f"The approximate volume is {volume_rounded} liters")

print()
current_date = datetime.now()
date = f"{current_date:%Y-%m-%d}" 

print()
with open("volumes.txt", "at") as volume_file:
    
print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}", file=volume_file)
   
