import json
from typing import Tuple, List
import os
import numpy as np
import matplotlib.pyplot as plt
from utils import compute_differential, load_signal, DIFFERENTIAL_INTERVAL
from utils_display import display_density
from rn2483 import SPREADING_FACTOR

RS = 125_000 / (2**SPREADING_FACTOR)
JSON_FILENAME = "centers.json"
DENSITY_THRESHOLD = 0.8

MODULE = "set36"
SAMPLES_FOLDER = f'preambles/{MODULE}/'
#SAMPLES_FOLDER = 'sample_data/test/'


def display_preamble(density, x_edges, y_edges, differential_i, differential_q, markedx, markedy):
    """Display the signal in the complex plan, following the search of highest density points.
        The area is divised in zones. The highest density zone is displayed in red, 
        the zones that have density over the threshold are displayed in orange.

        The points of the signal are displayed in blue (not depending of the zones)
    """

    max_density_x_index, max_density_y_index = np.unravel_index(np.argmax(density), density.shape)
    max_density_x = (x_edges[max_density_x_index] + x_edges[max_density_x_index + 1]) / 2
    max_density_y = (y_edges[max_density_y_index] + y_edges[max_density_y_index + 1]) / 2
    # print("Highest Density Point:", (max_density_x, max_density_y))

    plt.figure(figsize=(8, 6))
    plt.scatter(differential_i, differential_q, s=5, c='blue', alpha=0.5)
    plt.scatter(max_density_x, max_density_y, s=25, c='red', marker='o', label='Highest Density Point')
    plt.scatter(markedx, markedy, s=5, c='orange', marker='o', label='Highest Density Points')
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential Constellation Trace Figure ')
    plt.legend()
    plt.grid(True)
    plt.show()


def find_preamble_center(data: np.array) -> Tuple[int, int]:
    # DCTF method
    differential_data = compute_differential(data, DIFFERENTIAL_INTERVAL)
    differential_i = np.real(differential_data)
    differential_q = np.imag(differential_data)

    density, x_edges, y_edges = np.histogram2d(differential_i, differential_q, bins=300, density=True)
    highest_density_points_mask = density >= DENSITY_THRESHOLD * np.max(density)
    highest_density_points = np.argwhere(highest_density_points_mask)
    markedx = [(x_edges[p[0]] + x_edges[p[0] + 1]) / 2 for p in highest_density_points]
    markedy = [(y_edges[p[1]] + y_edges[p[1] + 1]) / 2 for p in highest_density_points]

    # Uncomment the display the graph of the highest density points in the complex plan
    # display_preamble(density, x_edges, y_edges, differential_i, differential_q, markedx, markedy)

    return np.mean(markedx), np.mean(markedy)


def find_preamble_centers(filepaths: List[str], module_data: dict) -> None:
    for filepath in filepaths:
        data = load_signal(filepath, dtype=np.complex64)
        # Uncomment to display density graph of the preamble
        # display_density(data, filepath)
        center_x, center_y = find_preamble_center(data)
        filename = filepath.split('/')[-1]
        module_data[filename] = {
            "centerX": center_x,
            "centerY": center_y
        }


if __name__ == "__main__":

    with open(JSON_FILENAME, 'r', encoding='utf8') as file_reader:
        centers_data = json.load(file_reader)

    files = os.listdir(SAMPLES_FOLDER)

    if centers_data.get(MODULE) is None:
        centers_data[MODULE] = {}

    find_preamble_centers(
        [SAMPLES_FOLDER + filename for filename in files],
        centers_data[MODULE]
    )

    with open(JSON_FILENAME, 'w', encoding='utf8') as file_writer:
        json.dump(centers_data, file_writer)
