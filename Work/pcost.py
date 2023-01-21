# pcost.py
#
# Exercise 1.27

total = 0
with open('Data/portfolio.csv') as file_obj:
	headers = next(file_obj)
	for line in file_obj:
		items = line.split(',')
		number = int(items[1])
		price = float(items[2])
		total += number * price
		
print("Total cost", total)
