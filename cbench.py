import matplotlib.pyplot as plt
import re

# Initialize empty lists to store the data
timestamps = []
switches = []
response_requests = []

# Regular expression pattern to extract the response/requests data
pattern = r'response/requests:\s+(\d+/\d+)\s+'

# Read the data from the cbench.txt file
with open('cbench.txt', 'r') as file:
    for line in file:
        # Extract the timestamp
        if re.match(r'\d+:\d+:\d+\.\d+', line):
            timestamps.append(line.split()[0])
        # Extract the number of switches and response/requests data
        elif "switches: response/requests:" in line:
            data = re.findall(pattern, line)
            switches.append(int(line.split()[2]))
            response_requests.append([tuple(map(int, x.split('/'))) for x in data])

# Create the x-axis data
x = list(range(len(timestamps)))

# Determine the maximum number of switches
max_switches = max(switches)

# Create subplots for response and requests
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
for i in range(max_switches):
    response_data = [item[i][0] if i < len(item) else 0 for item in response_requests]
    plt.plot(x, response_data, label=f'Switch {i+1}')

plt.title('Response Metrics')
plt.xlabel('Timestamp')
plt.ylabel('Responses')
plt.legend()

plt.subplot(2, 1, 2)
for i in range(max_switches):
    request_data = [item[i][1] if i < len(item) else 0 for item in response_requests]
    plt.plot(x, request_data, label=f'Switch {i+1}')

plt.title('Request Metrics')
plt.xlabel('Timestamp')
plt.ylabel('Requests')
plt.legend()

plt.tight_layout()
plt.show()
