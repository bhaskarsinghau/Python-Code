weight_in_kg = float(input("Enter the weight in kg: "))
height_in_meter = float(input("Enter the height in meters: "))

#Formula of BMI
bmi = weight_in_kg / ( height_in_meter * height_in_meter )
print("BMI is: ", bmi, end = " ")

if bmi < 18.5:
    print(".... Underweight")
elif bmi < 25:
    print(".... Normal")
elif bmi < 30:
    print(".... Overweight")   
else:
    print(".... Obses")

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com