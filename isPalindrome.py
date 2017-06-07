
def isPalindrome(s: str, kSense: bool):
	if (kSense == False):
		s = s.lower()
	for i in range(0, len(s)):
		if (s[i] != s[((i + 1) * -1)]):
			return (False)
	return (True)

print(isPalindrome("racecar", True))
