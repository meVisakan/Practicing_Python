# Q - List all the emails coming up in the response

# import requests
#
# url = "https://reqres.in/api/users?page=2"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# result = respons
# print(response.text)

import json

file_path = "/Data/response.json"

with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines[0].split())
    # result = json.loads(lines)
    # print(result)
    # for line in lines:
    #     for l in line.split("email"):
    #         print(l.split(":"))

