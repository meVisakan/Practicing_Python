# Given a string of size n, write functions to perform following operations on string. 1.
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n). 2.
# Right (Or clockwise) rotate the given string by d elements (where d <= n).
# Input : s = "qwertyu" d = 2 Output : Left rotation : "ertyuqw" Right rotation : "yuqwert"


s = "qwertyu"
r = 2

left = s[r:] + s[:r]
right = s[-r:] + s[:-r]

print(left)
print(right)


