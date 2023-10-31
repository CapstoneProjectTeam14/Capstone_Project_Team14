
import matplotlib.pyplot as plt
import numpy as np

# Create a list of time stamps
time_stamps = np.array([39.597, 40.697, 41.797, 42.897, 43.997, 45.098, 46.198, 47.298, 48.398, 49.498, 50.599, 51.699, 52.799, 53.899, 54.999, 56.099])

# Create a list of response/request ratios
response_request_ratios = np.array([9.942311, 30.677177, 30.972801, 36.862152, 33.896966, 44.262548, 43.691956, 39.343351, 37.212963, 46.104606, 45.880650, 49.743280, 34.472931, 43.317719, 35.980158, 48.649903])

# Plot the data
plt.plot(time_stamps, response_request_ratios)

# Set the title and labels
plt.title("Response/Request Ratios over Time")
plt.xlabel("Time (PST)")
plt.ylabel("Response/Request Ratio (per ms)")

# Show the plot
plt.show()
