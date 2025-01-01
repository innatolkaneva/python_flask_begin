import requests

url = 'http://127.0.0.1:5000/seach'

params = {
    'cell_tower_id': [1, 2, 4],
    'phone_prefix': ['025', '345', '143'],
    'protocols': ['011', '311', '123'],
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.headers)

if response.ok:
    print(response.text)