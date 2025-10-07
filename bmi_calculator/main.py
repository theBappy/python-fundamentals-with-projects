import tabulate #to display tabular data
import csv

def reference_chart():
    list2 = []
    with open("bmi_calculator\\bmi.csv") as file1:
        list1 = csv.reader(file1)
        for line in list1:
            list2.append(line)
        print("Here you can take the reference chart \n")
        print(tabulate.tabulate(list2[1:], headers=list2[0], tablefmt="fancy_grid"))


def calculate_bmi(height, weight):
    try:
        bmi = round(weight / (height**2), 2)
        return bmi
    except ZeroDivisionError:
        return None

def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input. Height should be greater than 0."
    elif bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, your have a normal weight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)"
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)"
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)"

def main():
    reference_chart()
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        result = interpret_bmi(bmi)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numerical values to calculate BMI")

if __name__ == "__main__":
    main()