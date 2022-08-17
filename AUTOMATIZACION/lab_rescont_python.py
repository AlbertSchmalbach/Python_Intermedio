import json
import requests
requests.packages.urllib3.disable_warnings()
#api_url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"
api_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces"
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }
basicauth = ("developer", "C1sco12345")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
#print(response_json)
print(json.dumps(response_json, indent=4))