'''
You can input your own data to have a look at your BMI.
And you will know whether you are considered underweight, normal or obese.
'''
weight = float(input("input your weight(kg):"))
height = float(input("input your height(m):"))
BMI = round(weight/height**2,2)
if BMI > 30:
    print(f"Your BMI is {BMI}. You are obese.")
elif BMI < 18.5:
    print(f"Your BMI is {BMI}.You are underweight.")
else:
    print(f"Your BMI is {BMI}.You are normal. ")