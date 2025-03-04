# Given two strings s and t, return true if t is an
# anagram of s, and false otherwise.

def anagram_check(s, t):

    ls = list(s)
    print("ls", ls)

    lt = list(t)
    print("lt", lt)

    if len(ls) == len(lt):
        pass
    else:
        return False

    ls.sort()
    lt.sort()
    if ls == lt:
        return True
    else:
        return False


# Input
s = str(input("Enter s string: "))
t = str(input("Enter t string: "))
if anagram_check(s, t):
    print("Anagrams")
else:
    print("Not anagrams")
