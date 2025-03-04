#Prac 2_3
weight = int(input("Enter your weight im kilograms: "))
height = int(input("Enter your height in centimeters (cm): ")) / 100

BMI = weight / (height ** 2)

print(f"BMI = {BMI:.3f}")
