import requests

parameters = {
    "amount":10,
    "type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
print(response)

data = response.json()
# print(data)
question_data = data['results']