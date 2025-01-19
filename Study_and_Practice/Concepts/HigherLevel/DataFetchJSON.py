# Fetch the emails of all the users where interest3 is present against their respective interests

import json

file_path = "/Users/mvisakan/PycharmProjects/PracticingPython/Data/users.json"

with open(file_path, "r") as file:
    data = json.load(file)

emails_with_interest3 = [user["email"] for user in data["users"] if "interest3" in user["interest"]]
print(emails_with_interest3)
