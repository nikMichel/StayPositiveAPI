import requests
import json

url = "http://127.0.0.1:80/postive" # for docker if exposed to 80
data = {"input": "It would be <blank> to work for Persado"}
json_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=json_data, headers=headers)
#print(r, r.text)
#print(type(r.text))
json_output = json.loads(r.text)
json_output_fmt = json.dumps(json_output, indent=2)
print(json_data)
print(json_output_fmt)