# mortgage.py
#
# Exercise 1.7 .. 1.9

principal = 500000.0
rate = 0.05
payment = 2684.11

total_paid = 0.0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

months_quantity = 0

while principal > 0:
    months_quantity += 1
    principal = principal * (1 + rate / 12)
    if (months_quantity >= extra_payment_start_month) & (months_quantity <= extra_payment_end_month):
        actual_payment = payment + extra_payment
    else:
        actual_payment = payment
    principal = principal - actual_payment
    total_paid = total_paid + actual_payment

print(f'Total paid {round(total_paid, 2)} over {months_quantity} months')
