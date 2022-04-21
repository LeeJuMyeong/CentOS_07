
str = 'X-DSPM-Confidence: 0.8475'
print(str)

ipos = str.find(':')
#print(ipos)

piece = str[ipos+2:]
#print(piece)

value = float(piece)
print(value)
#print(value + 42)
