ht: float = float(input("Enter your Heigth in mts: "))
wt: float = float(input("Enter your Weigth in kgs: "))

bmi: int = int(wt / (ht ** 2))
print(f"Your BMI is : {bmi}")
