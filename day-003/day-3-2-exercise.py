# Don't change the code below
height = float(input("enter your height in m : "))
weight = float(input("enter your height in kg : "))
# Don't change the code above

# Write your code here

bmi =round(weight/height**2)
#print(bmi)
if bmi < 18.5 :
    status="Underweight"
elif bmi < 25:
    status="Normal Weight"
elif bmi < 30 :
    status="Overweight"
elif bmi < 35 :
    status="Obese"
else:
    status="Clinically Obese"
print (f"Your BMI is {bmi} and you are {status}")
