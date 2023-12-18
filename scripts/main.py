import numpy as np
import matplotlib.pyplot as plt
from utils import cut_signal, save_signal, compute_differential, load_signal


if __name__ == "__main__":
    
    DATA = load_signal('sample_data/test_128', dtype=np.complex128)

    n = 15000
    delta_f = -62500
    differential_data = np.zeros_like(DATA)  # Create an array to store differential data
    for i in range(n, len(DATA)):
        differential_data[i] = DATA[i] * np.conj(DATA[i - n]) * np.exp(-1j * 2 * np.pi * delta_f * n)


    differential_i = np.real(differential_data)
    differential_q = np.imag(differential_data)

    plt.figure(figsize=(8, 6))
    plt.scatter(differential_i, differential_q, s=1, c='red', alpha=0.5)
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential I/Q Samples')
    plt.grid(True)
    plt.show()