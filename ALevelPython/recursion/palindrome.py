# check if a string is a palindrome
# a palindrome is a word which is read the same both from left to right and from right to left.Don't ignore case
# this time but it should be problem specified
# ana, anna, anavolimilovana palindromes
# Banana, Ana - not palindromes

def isPalindrome(s):
    # s = s.lower() if you ignore case, uncomment
    if len(s) <= 1:
        return True
    return (s[0] == s[-1]) and isPalindrome(s[1:-1]) 

print(isPalindrome("ana"))
print(isPalindrome("Banana"))
print(isPalindrome("Ana"))