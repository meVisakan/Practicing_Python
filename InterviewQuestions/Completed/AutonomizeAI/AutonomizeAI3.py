# Q - String with the longest substring without a repeating character


def longest_subs(s):
    if len(s) > 1:
        char_set = set()
        left = 0
        start = 0
        length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            if right - left + 1 > length:
                length = right - left + 1
                start = left

        longest_sub = s[start: start + length]
        print(longest_sub)
    else:
        print("Invalid String!")


# Input
s = "abdcceabd"
longest_subs(s)
