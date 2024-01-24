def IterativeVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for c in word: # iterating through a string in python
        if c in vowels:
            total = total+1
    return total

print(IterativeVowels("Brook Hill"))

def RecursiveVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(word) == 0:
        return 0
    if word[0] in vowels:
        return 1 + RecursiveVowels(word[1:])
    else:
        return RecursiveVowels(word[1:])
    

print(RecursiveVowels("Brook Hilla"))