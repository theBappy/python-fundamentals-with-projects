def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Inter amount of years: "))

    month_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * month_interest_rate / (1 - (1 + month_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this load is: %.2f " % monthly_payment)

main()