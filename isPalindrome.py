
def isPalindrome(s: str, kSense: bool):
	if (kSense == False):
		s = s.lower()
	for i in range(0, len(s) // 2):
		if (s[i] != s[((i + 1) * -1)]):
			return (False)
	return (True)

userin = input("enter a word: ")
if (isPalindrome(userin, False) == False):
	print("%s is not a palindrome" % (userin))
else:
	print("%s is a palanindrome" % (userin))
