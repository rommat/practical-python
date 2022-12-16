# mortgage.py
#
# Exercise 1.7 .. 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11

total_paid = 0.0
months_quantity = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months_quantity += 1
    principal *= 1 + rate / 12


    if months_quantity >= extra_payment_start_month and months_quantity <= extra_payment_end_month:
        actual_payment = payment + extra_payment
    else:
        actual_payment = payment

    if principal < actual_payment:
        actual_payment = principal

    principal -= actual_payment
    total_paid += actual_payment

    print(f'{months_quantity: >3} {total_paid: >10.2f} {principal: >10.2f}')

print(f'Total paid {total_paid: >10.2f}')
print(f'Months {months_quantity}')
