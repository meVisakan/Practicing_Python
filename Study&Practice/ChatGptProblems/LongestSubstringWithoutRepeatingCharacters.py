# Given a string s, find the length of the longest substring without repeating characters and print it.


def length_of_longest_substring(s):
    char_set = set()
    left = 0
    start = 0
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > result:
            result = right - left + 1
            start = left

    longest_subs = s[start: start + result]

    print(f"Length of longest substring is {result}")
    print(f"The longest substring is {longest_subs}")


# Input
s = str(input("Enter a string: "))
length_of_longest_substring(s)
