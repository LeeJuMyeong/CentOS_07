
words = 'Connect Foundation'

# Invalid Code
#if 'F' in words:
#	words.lower()
#	words[7] = '&'
	
#else :
#	print(words)

# Valid Code
if 'F' in words:
	words = words.lower()
	words = words.replace(' ', '&')

print(words)
