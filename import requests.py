import requests
import json

url = "http://localhost:8000/predict"
data = {
    "data": [
        [9290.89660239, 9202.41545055, 9369.62808116, 9326.59962378,
         9335.75240233, 9226.48582088, 8794.35864452]
    ]
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
