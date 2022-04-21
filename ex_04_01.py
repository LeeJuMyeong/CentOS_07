def computepay(Hours, Rate):
	if Hours > 40:
		reg = Hours * Rate
		otp = (Hours - 40) * (Rate * 0.5)
		pay = reg + otp
	else:
		pay = Hours * Rate
	return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay: ", xp)

