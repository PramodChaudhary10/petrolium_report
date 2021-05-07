import requests
import json

URL = "http://127.0.0.1:8000/databasedata/"

adata = requests.get(
    'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json').json()

r = requests.post(url=URL, data=adata)
data = r.json()
print(data)
