# Author: Victor Hugo Perez
# Date:    6/10/2025
# Purpose: CS119-PJ9V2: Loan Payment Report
# Changes: This version has user input, file output, plotting, and loop fix

n = 1
print('Welcome to the Loan Payment Report of "Victor Hugo Perez"!')
print(n, "============================================================"); n += 1

import matplotlib.pyplot as plt

def getInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# User Input
loan_amount = getInput("Enter amount of loan: ")
annual_interest_rate = getInput("Enter interest rate: ")
monthly_interest_rate = annual_interest_rate / 12 
monthly_payment = getInput("Enter payment amount: ")
min_balance_to_stop = 0.10

# Check that monthly payment is enough to cover at least the first month's interest
first_interest = loan_amount * monthly_interest_rate
if monthly_payment <= first_interest:
    print(f"Error: Your monthly payment (${monthly_payment:.2f}) is too low to cover the interest (${first_interest:.2f}).")
    print("Please enter a higher payment amount.")
    exit()

# Initialization
balance = loan_amount
totalInterest = 0
month = 1
months = []
balances = []

# File setup
with open("loan_report.txt", "w") as file:
    file.write("Month  Payment   Interest   Principal   Balance\n")
    file.write("--------------------------------------------------\n")

    print(f"{'Month':<6}{'Payment':>10}{'Interest':>12}{'Principal':>15}{'Balance':>15}")
    print("--------------------------------------------------------------------------")

    # Loop through months until loan is paid
    while balance > min_balance_to_stop:
        interest = balance * monthly_interest_rate
        totalInterest += interest
        principal = monthly_payment - interest

        # Adjust for final payment without modifying monthly_payment
        if principal > balance:
            principal = balance
            actual_payment = interest + principal
        else:
            actual_payment = monthly_payment

        balance -= principal

        # Save month data for plotting
        months.append(month)
        balances.append(balance)

        # Print current month's details
        print(f"{month:<6}{'$'+format(actual_payment, ',.2f'):>10}"
              f"{'$'+format(interest, ',.2f'):>12}"
              f"{'$'+format(principal, ',.2f'):>15}"
              f"{'$'+format(balance, ',.2f'):>15}")

        # Write to file
        file.write(f"{month:<6}{'$'+format(actual_payment, ',.2f'):>10}"
                   f"{'$'+format(interest, ',.2f'):>12}"
                   f"{'$'+format(principal, ',.2f'):>15}"
                   f"{'$'+format(balance, ',.2f'):>15}\n")

        month += 1

print("==========================================================================")
print(f"Total Amount of Interest Paid: ${totalInterest:.2f}")
print(n, "============================================================"); n += 1
print("Thank you for using the Loan Payment Report of Victor Perez!")
print(n, "============================================================"); n += 1

# Plot the loan balance over time
plt.plot(months, balances, marker='o')
plt.title("Loan Balance Over Time")
plt.xlabel("Month")
plt.ylabel("Balance ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
