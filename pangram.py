import string
def pangram(str,alphabet):
	for char in alphabet:
		if char not in str.lower():
			return False
	return True
alphabet=string.ascii_lowercase
str=input('enter the string to check pangram: ')
if (pangram(str,alphabet)==True):
	print("string is pangram")
else:
	print("string is not pangram")		
		