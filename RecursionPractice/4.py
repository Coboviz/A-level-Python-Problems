def palindromeRec(s):
    if len(s) < 2:
        return True
    else:
        if s[0] == s[-1]:
            return palindromeRec(s[1:-1])
        else:
            return False
        
print(palindromeRec("ana"))
print(palindromeRec("AnnA"))
print(palindromeRec("banana"))
print(palindromeRec("anavolimilovana"))
