# Write a Python function that uses regex to extract all valid email addresses from a given string

import re


def valid_mails(str1):
    mail_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    mails = re.findall(mail_pattern, str1)
    return mails


# Input
str1 = str(input("Enter a string with email id: "))
print(valid_mails(str1))
