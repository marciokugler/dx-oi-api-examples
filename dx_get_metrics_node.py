import requests
import json

token = 'Bearer '



with open('query_metric_payload.json', 'r') as f:
  query_json_parse = json.load(f)
  query_json = json.dumps(query_json_parse)
print (query_json)

input()
#def query_tas_all(token, impersonate, tas_dump)
url = "https://apmgw.dxi-na1.saas.broadcom.com/metadata/queryMetric"
headers = {
      'content-type': "application/json",
      'authorization': token,
      }

response = requests.request("POST", url, data=query_json, headers=headers)

  # TODO SPLIT edges and vertex

print (json.dumps(response.json(), indent=4))
# Closing file
f.close()

