import requests

response = requests.post('http://52.33.207.242:80', datas, headers={'Content-Type': 'application/octet-stream'})

print(response)