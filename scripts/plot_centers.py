from typing import List
import json
import numpy as np
import matplotlib.pyplot as plt

from find_centers import JSON_FILENAME


def plot_centers(data: dict) -> None:
    modules: List[str] = data.keys()

    for module in modules:
        # Extract center coordinates
        center_x = np.array([entry['centerX'] for entry in data[module].values()])
        center_y = np.array([entry['centerY'] for entry in data[module].values()])
        v = np.sqrt((center_x ** 2 + center_y ** 2) / 2) # RMS
        # Plot points
        plt.scatter(center_x / v, center_y / v, label=module)

    # Add labels and title
    plt.xlabel('Center X')
    plt.ylabel('Center Y')
    plt.title(f'Center Coordinates from {JSON_FILENAME}')
    plt.legend()

    # Show plot
    plt.show()


if __name__ == "__main__":
    # Load JSON data from the file
    with open(JSON_FILENAME, 'r', encoding='utf8') as filereader:
        CENTERS: dict = json.load(filereader)
    plot_centers(CENTERS)