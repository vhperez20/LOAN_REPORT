# Author: Victor Hugo Perez
# Date:    5/25/2025
# Purpose: CS119-PJ9: Loan Payment Report
n = 1
print('Welcome to the Loan Payment Report of "Victor Hugo Perez"!')
print(n, "============================================================"); n += 1

# Constants
loan_amount = 1000.00
annual_interest_rate = 0.18  # 18%
monthly_interest_rate = annual_interest_rate / 12  # 0.015
monthly_payment = 50.00
min_balance_to_stop = 0.10

# Initialization
balance = loan_amount
totalInterest = 0
month = 1

#print("LOAN PAYMENT REPORT")
#print("==========================================================================")
print(f"{'Month':<6}{'Payment':>10}{'Interest':>12}{'Principal':>15}{'Balance':>15}")
print("--------------------------------------------------------------------------")

# Loop through months until loan is paid
while balance > min_balance_to_stop:
    interest = balance * monthly_interest_rate
    totalInterest += interest
    principal = monthly_payment - interest

    # If final payment would overpay
    if principal > balance:
        principal = balance
        monthly_payment = interest + principal  # Adjust final payment

    balance -= principal

    # Print current month's details
    print(f"{month:<6}{'$'+format(monthly_payment, ',.2f'):>10}"
          f"{'$'+format(interest, ',.2f'):>12}"
          f"{'$'+format(principal, ',.2f'):>15}"
          f"{'$'+format(balance, ',.2f'):>15}")
    
    month += 1

print("==========================================================================")
#print(f"Loan is paid off in {month - 1} months.")
print(f"Total Amount of Interest Paid: {totalInterest:.2f}")

print(n, "============================================================"); n += 1
print("Thank you for using the Loan Payment Report of Victor Perez!")
print(n, "============================================================"); n += 1
