# string ==> Immuatable ==> ' ' or " " single line string 
#'''  ''' or """ """ ==> Multi line string 
s = "python"
s = s.capitalize()
print(s)

#without using built in methods
def Reverse_str(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(Reverse_str("abc"))      # "cba"
print(Reverse_str("python"))   # "nohtyp"

def Reverse_str1(s):
    rev = ""
    stop = -1 * (len(s)+1)
    for i in range(-1,stop,-1):
        rev = rev + s[i]
    return rev 
print(Reverse_str1("abc"))      # "cba"
print(Reverse_str1("python"))   # "nohtyp"

def is_palindrome(s):
    reversed_s = ""
    
    for char in s:
        reversed_s = char + reversed_s
    
    if s == reversed_s:
        return True
    else:
        return False

print(is_palindrome("abc"))    # False
print(is_palindrome("madam"))  # True

def Frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1 
        else:
            d[ch] += 1 
    return d

print(Frequency_count("abcabc"))


def Anagrams(str1,str2):
    return Frequency_count(str1) == Frequency_count(str2)
print(Anagrams("paces","space"))
print(Anagrams("abcabc","abc"))

from collections import Counter
print(Counter("aabbcc"))