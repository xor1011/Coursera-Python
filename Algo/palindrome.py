from bdb import Breakpoint


def isPalindrome(str):
    str='racecar'
    c=len(str)-1
    for x in range(c):
        if (str[x]!=str[c]):
            return False
        c-=1
    return True
#print("Palindrome")

if (isPalindrome('racecar') is True):
    print("Palindrome")
else:
    print("Not a palindrome")