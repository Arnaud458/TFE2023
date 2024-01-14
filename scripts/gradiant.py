import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density # adds projection='scatter_density'
from matplotlib.colors import LinearSegmentedColormap
from utils import cut_signal, save_signal, compute_differential, load_signal


if __name__ == "__main__":
    
    DATA = load_signal('sample_data/test_64_misc', dtype=np.complex64)
    print(len(DATA))

    n = 5000
    delta_f = -62500
    differential_data = np.zeros_like(DATA)
    for i in range(n, len(DATA)):
        differential_data[i] = DATA[i] * np.conj(DATA[i - n]) * np.exp(-1j * 2 * np.pi * delta_f * n)


    differential_i = np.real(differential_data)
    differential_q = np.imag(differential_data)

    white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
        (0, '#ff0000'),
        (1e-20, '#440053'),
        (0.2, '#404388'),
        (0.4, '#2a788e'),
        (0.6, '#21a784'),
        (0.8, '#78d151'),
        (1, '#fde624'),
    ], N=256)

    def using_mpl_scatter_density(fig, x, y):
        ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
        density = ax.scatter_density(x, y, cmap=white_viridis)
        fig.colorbar(density, label='Number of points per pixel')



    fig = plt.figure(figsize=(8, 6))
    using_mpl_scatter_density(fig, differential_i, differential_q)
    #plt.scatter(differential_i, differential_q, s=1, c='red', alpha=0.5)
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential I/Q Samples')
    plt.grid(True)
    plt.show()