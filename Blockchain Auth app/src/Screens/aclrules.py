import requests
import json

headers_list = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Basic b25vczpyb2Nrcw==",
    "Content-Type": "application/json"
}

body_content = {
    "srcIp": "10.0.0.1/24",
    "srcMac": "00:00:00:00:00:01",
    "dstMac": "00:00:00:00:00:04",
}

url = "http://172.17.0.7:8181/onos/v1/acl/rules"

response = requests.post(url, headers=headers_list, data=json.dumps(body_content))
print(response.json())
