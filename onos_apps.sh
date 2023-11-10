#!/bin/bash

# Set the ONOS controller REST API endpoint
ONOS_HOST="http://localhost:8181"
APP_NAME_1="org.onosproject.fwd"
APP_NAME_2="org.onosproject.openflow"

# Username and password (if authentication is enabled)
USERNAME="onos"
PASSWORD="rocks"

# Activate the app
curl -X POST -u $USERNAME:$PASSWORD -H "Content-Type: application/json" \
  -d '{"id":"'${APP_NAME_1}'","activate":true}' \
  $ONOS_HOST/onos/v1/applications

curl -X POST -u $USERNAME:$PASSWORD -H "Content-Type: application/json" \
  -d '{"id":"'${APP_NAME_2}'","activate":true}' \
  $ONOS_HOST/onos/v1/applications

# Check for a successful response (HTTP status code 200)
if [ $? -eq 0 ]; then
  echo "App activation request successful"
else
  echo "App activation request failed"
fi
