# Create a json file with users 1 to 8, user should have name, dob, number, userid, email, interest, address dictionary
# with locality, city, state, country

import json

# Define user data
users = []
for i in range(1, 9):
    user = {
        "name": f"User{i}",
        "dob": f"199{i}-01-01",
        "number": f"123456789{i}",
        "userid": f"user_{i}",
        "email": f"user{i}@example.com",
        "interest": ["interest1", "interest2"],
        "address": {
            "locality": f"Locality{i}",
            "city": f"City{i}",
            "state": f"State{i}",
            "country": "Country"
        }
    }
    users.append(user)

# Save to a JSON file
file_path = "/Users/mvisakan/PycharmProjects/PracticingPython/Data/users.json"
with open(file_path, "w") as file:
    json.dump({"users": users}, file, indent=4)
