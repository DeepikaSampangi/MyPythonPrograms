ht: float = float(input("Enter your Heigth in mts: "))
wt: float = float(input("Enter your Weigth in kgs: "))

bmi: int = int(wt / (ht ** 2))
print(f"Your BMI is : {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weigth")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obese")
elif bmi >= 35:
    print("Clinically Obese")
