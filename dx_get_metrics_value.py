import requests
import json
import time

token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjkyMjMzNzIwMzY4NTQ3NzUsImludCI6dHJ1ZSwidGlkIjo1MTgsImp0aSI6ImIxMDc5Y2I3LWZjNmMtNGFhOC1iZTI4LTkyZjUwZWMyYWYxOCJ9.Jvo53Apcr7pZRJFqmlXAIZC1pLHzdb2GfFZDDmMeOjr4x7hDca6bSy9KgrSm1DobDfHzjH_WBu97K0rtrA3VZw'

epoch_time = int(time.time())
print (epoch_time)
input ()

with open('query_metric_values_payload.json', 'r') as f:
  query_json_parse = json.load(f)
  query_json = json.dumps(query_json_parse)
print (query_json)

input()
#def query_tas_all(token, impersonate, tas_dump)
url = "https://apmgw.dxi-na1.saas.broadcom.com/nass/metricValue/fetch"
headers = {
      'content-type': "application/json",
      'authorization': token,
      }

response = requests.request("POST", url, data=query_json, headers=headers)

  # TODO SPLIT edges and vertex

print (json.dumps(response.json(), indent=4))
# Closing file
f.close()

