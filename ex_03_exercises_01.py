xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
fh = float(xh)
fr = float(xr)
#print(fh, fr)
if fh > 40:
	print("Overtime")
else:
	print("Regular")

fp = fh * fr
print("Pay: ", fp)
