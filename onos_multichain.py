import json
import threading
import requests
import time
from Savoir import Savoir

# Multichain RPC parameters
rpcuser = 'multichainrpc'
rpcpasswd = '7FezTue2c2fpkBtZq1L1PxqGGSLnv2xxYBMcFjaBPPmj'
rpchost = '0.0.0.0/0'
rpcport = '7434'
chainname = 'liju'

# Multichain stream names for ONOS data
onos_flows_stream = 'onos_flows'
onos_hosts_stream = 'onos_hosts'
onos_topology_stream = 'onos_topology'

# ONOS REST API endpoints
onos_flows_api = 'http://localhost:8181/onos/v1/flows'
onos_hosts_api = 'http://localhost:8181/onos/v1/hosts'
onos_topology_api = 'http://localhost:8181/onos/v1/topology'

# ONOS authentication credentials
onos_username = 'onos'
onos_password = 'rocks'

# Initialize Savoir for Multichain interaction
multichain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

# Function to retrieve ONOS data and publish it to Multichain
def retrieve_and_publish_onos_data():
   try
    {
    # Retrieve ONOS flows data
    flows_response = requests.get(onos_flows_api)
    flows_data = flows_response.json()
    
    # Retrieve ONOS hosts data
    hosts_response = requests.get(onos_hosts_api)
    hosts_data = hosts_response.json()
    
    # Retrieve ONOS topology data
    topology_response = requests.get(onos_topology_api)
    topology_data = topology_response.json()
    
    # Publish ONOS data to Multichain streams
    multichain_api.publish(onos_flows_stream, 'key1', {'json': flows_data})
    multichain_api.publish(onos_hosts_stream, 'key1', {'json': hosts_data})
    multichain_api.publish(onos_topology_stream, 'key1', {'json': topology_data})
    
    print('ONOS data published to Multichain streams.')

    }
    
        # print('Error retrieving or publishing ONOS data:', str(e))

# Function to subscribe to Multichain streams and update ONOS data
def subscribe_and_update_onos_data():
    try:
        while True:
            # Implement logic to subscribe to Multichain streams and update ONOS data
            # You can use multichain_api.liststreamkeyitems method to retrieve data from Multichain
            # Update ONOS data based on received Multichain data
            pass
            time.sleep(5)  # Adjust the interval as needed

    except Exception as e:
        print('Error subscribing to Multichain streams:', str(e))

if __name__ == "__main__":
    try:
        # Start a thread to retrieve and publish ONOS data to Multichain
        # You can run this in a separate thread or process for continuous data updates

        # Subscribe to Multichain streams and update ONOS data
        subscribe_and_update_onos_data()

    except KeyboardInterrupt:
        print('Script terminated by user.')


