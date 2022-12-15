# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
months_quantity = 0

while principal > 0:
    months_quantity += 1
    principal = principal * (1+rate/12)
    if months_quantity <= 12:
        actual_payment = payment + extra_payment
    else:
        actual_payment = payment
    principal = principal - actual_payment
    total_paid = total_paid + actual_payment

print(f'Total paid {total_paid} over {months_quantity} months')
