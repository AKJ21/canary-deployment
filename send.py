import requests
import json

url = "http://a059f531bbea949a8a8cdcf4eafc0281-2074342327.ap-south-1.elb.amazonaws.com/v1/models/imagenet-vit:predict" ## change

with open("input.json") as f:
	payload = json.load(f)
headers = {
  'Host': 'imagenet-vit-predictor.default.emlo.tsai', ## change
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)