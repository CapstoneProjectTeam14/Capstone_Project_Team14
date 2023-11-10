import requests

def onos_auth(ip, port, username, password):
    url = f"http://{ip}:{port}/onos/"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        print("Failed to authenticate.")
        return None

ip = "127.0.0.1" # ONOS IP address
port = "8181" # ONOS REST API port
username = "onos" # ONOS username
password = "rocks" # ONOS password

token = onos_auth(ip, port, username, password)
if token:
    print(f"Access Token: {token}")