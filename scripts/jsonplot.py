import json
import matplotlib.pyplot as plt

# Load JSON data from the file
with open('centers.json', 'r') as file:
    data = json.load(file)

# Extract center coordinates
center_x = [entry['centerX'] for entry in data.values()]
center_y = [entry['centerY'] for entry in data.values()]

# Plot points
plt.scatter(center_x, center_y)

# Add labels and title
plt.xlabel('Center X')
plt.ylabel('Center Y')
plt.title('Center Coordinates from centers.json')

# Show plot
plt.show()