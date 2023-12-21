from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt
from utils import load_signal , compute_differential


def display_quadrature(*signals: List[Tuple[np.ndarray, str]]) -> None:
    plt.figure(figsize=(8, 6))
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.title('I/Q Samples')
    plt.grid(True)
    for signal, signal_label in signals:
        i = np.real(signal)
        q = np.imag(signal)
        plt.scatter(i, q, s=5, alpha=0.5, label=signal_label)
    plt.legend()
    plt.show()


def display(data) -> None:
    i = np.real(data)
    q = np.imag(data)

    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(i)), i, s=5, c='orange', alpha=0.5)
    plt.scatter(range(len(i)), q, s=5, c='blue', alpha=0.5)
    plt.xlabel('Sample index')
    plt.ylabel('Quadrature')
    plt.title('I/Q Samples')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    display(load_signal('sample_data/test_64_misc', np.complex64))
    #display_quadrature((load_signal('sample_data/test_64_1MHz', dtype=np.complex64)),'data')
