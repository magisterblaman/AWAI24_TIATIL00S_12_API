import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

data = response.json()

print(data["setup"])
guess = input()
if guess == data["punchline"]:
    print("Correct")
else:
    print(data["punchline"])


