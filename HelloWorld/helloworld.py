import json

with open("HelloWorld/text.json", "r") as message:
    data = json.load(message)

# Access and print the 'message' key
print(data["message"])

