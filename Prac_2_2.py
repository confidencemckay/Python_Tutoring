#Prac 2_2
import math
length = int(input("Enter the length (cm):"))
width = int(input("Enter the width (cm):"))

area = (length * width)
perimeter = 2 * (length + width)
diagonal = ((length ** 2) + (width ** 2)) ** 0.5

print(f"Area of the rectangle is {area:.2f} square cm")
print(f"Perimeter of the rectangle is {perimeter:.1f} cm")
print(f"Diagonal of the rectangle is {diagonal:.3f} cm")

print("**Rectangle dimensions:**")
print(f"Length = {length:.1f} cm /tWidth = {width:.1f} cm")