num = 0
total = 0.0

while True:
	sval = input("Enter a number: ")
	if sval == 'done':
		break
	try:
		fval = float(sval)
	except:
		print("Ivalid input")
		continue
	num = num + 1
	total = total + fval
	print(fval)

print("ALL DONE")
print(total, num, total / num)
