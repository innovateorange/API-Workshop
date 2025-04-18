import requests

url = "https://v2.jokeapi.dev/joke/Miscellaneous"

response = requests.get(url) #sends a GET request
data = response.json() #converts API's JSON response into a Python dic
# print(data)

if data["type"] == "single":
    #print(" Random Jokes:"r)
    print(data["joke"])
elif data["type"] == "twopart":
    #print(" Random Jokes2:")
    print(data["setup"])
    print(data["delivery"])
else:
    print("unexpected format")

