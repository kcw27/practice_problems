def is_palindrome(word):
	"""
	Checks if a string is a palindrome. Not case-sensitive.
	Strings of lengths 0 and 1 count as palindromes.
	"""
	if len(word) <= 1: # base case
		return True
	if word[0].lower() == word[-1].lower(): # compares the first and last letter
		return is_palindrome(word[1:-1]) # if they're the same letter, then proceed with comparisons
	return False

def is_palindrome_v2(word): # refactored after reading chapter 8
	return word.lower() == word[::-1].lower() # -1 step size goes through the word backwards


print(is_palindrome("flower")) # returns False
print(is_palindrome("racecar"))
print(is_palindrome("Rats live on no evil star"))
print(is_palindrome("a"))
print(is_palindrome(""))

print(is_palindrome_v2("flower")) # returns False
print(is_palindrome_v2("Rats live on no evil star"))
