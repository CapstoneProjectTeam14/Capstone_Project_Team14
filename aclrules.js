import axios from "axios";

let headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Authorization": "Basic b25vczpyb2Nrcw==",
 "Content-Type": "application/json" 
}

let bodyContent = JSON.stringify({
  "srcIp": "10.0.0.1/24",
  "srcMac": "00:00:00:00:00:01",
  "dstMac": "00:00:00:00:00:04"
});

let reqOptions = {
  url: "http://172.17.0.7:8181/onos/v1/acl/rules",
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);
