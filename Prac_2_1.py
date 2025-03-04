#Prac 2_1
watts = int(input("Enter the appliance power in WATTS (W):"))
hours = int(input("Enter the duration of the appliance is used in hours:"))

comsumption = (watts * hours) / 1000
print("Energy consumption", comsumption, "kWh")