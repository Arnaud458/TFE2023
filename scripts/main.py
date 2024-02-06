import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density # adds projection='scatter_density'
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from utils import save_signal, compute_differential, load_signal
import datashader as ds
from datashader.mpl_ext import dsshow
import pandas as pd
from capture_signal import SAMPLE_RATE

SPREADING_FACTOR = 7
RS = 125_000 / (2**SPREADING_FACTOR)

def using_hist2d(ax, x, y, bins=(1000, 1000)):
        
    ax.hist2d(x, y, bins, cmap=plt.cm.jet)



def using_datashader(ax, x, y):

    df = pd.DataFrame(dict(x=x, y=y))
    dsartist = dsshow(
        df,
        ds.Point("x", "y"),
        ds.count(),
        vmin=0,
        vmax=100,
        norm="linear",
        aspect="auto",
        ax=ax,
    )

    plt.colorbar(dsartist)

if __name__ == "__main__":
    
    DATA = load_signal('preambles/sf8.complex', dtype=np.complex64)
    #DATA = load_signal('sample_data/pretest_64_misc', dtype=np.complex64)
    print(len(DATA))
    #n = int(SAMPLE_RATE / RS)
    n = 4096
    delta_f = -62500
    differential_data = np.zeros_like(DATA)
    for i in range(n, len(DATA)):
        differential_data[i] = DATA[i] * np.conj(DATA[i - n]) * np.exp(-1j * 2 * np.pi * delta_f * n)


    differential_i = np.real(differential_data)
    differential_q = np.imag(differential_data)

    density, x_edges, y_edges = np.histogram2d(differential_i, differential_q, bins=50, density=True)
    print("sort density",-np.sort(-density.flatten())[:50])
    max_density_index = np.argmax(density)
    max_density_x_index, max_density_y_index = np.unravel_index(max_density_index, density.shape)
    max_density_x = (x_edges[max_density_x_index] + x_edges[max_density_x_index + 1]) / 2
    max_density_y = (y_edges[max_density_y_index] + y_edges[max_density_y_index + 1]) / 2
    max_density = np.max(density)
    threshold = 0.1

    highest_density_points_mask = density >= threshold * density[max_density_x_index, max_density_y_index]
    #with np.printoptions(threshold=np.inf):
        #print(highest_density_points_mask)
    
    marked_points = np.argwhere(density >= threshold * density[max_density_x_index, max_density_y_index])
    markedx = []
    markedy = []
    for point in marked_points :
        x = (x_edges[point[0]] + x_edges[point[0] + 1]) / 2
        y = (y_edges[point[1]] + y_edges[point[1] + 1]) / 2
        markedx.append(x)
        markedy.append(y)

    print(marked_points)
    #highest_density_points = np.column_stack((differential_i[highest_density_points_mask], differential_q[highest_density_points_mask]))

    print("--------------------------")
    print("Highest Density Point:", (max_density_x, max_density_y))
    print("Number of Points in Highest Density Region:", np.sum(highest_density_points_mask))
    print("density",max_density)
    print("index", max_density_index)

    plt.figure(figsize=(8, 6))
    plt.scatter(differential_i, differential_q, s=5, c='blue', alpha=0.5)
    plt.scatter(max_density_x, max_density_y, s=50, c='red', marker='o', label='Highest Density Point')
    plt.scatter(markedx, markedy, s=5, c='orange', marker='o', label='Highest Density Points')
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential Constellation Trace Figure')
    plt.legend()
    plt.grid(True)
    plt.show()


  

    """fig, ax = plt.subplots()
    #fig = plt.figure(figsize=(8, 6))
    #ax = fig.add_subplot(1, 1, 1, projection='scatter_density')

    using_datashader(ax, differential_i, differential_q)
    #using_hist2d(ax, differential_i, differential_q)
    #plt.scatter(differential_i, differential_q, s=1, c='red', alpha=0.5)
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential I/Q Samples')
    #plt.grid(True)
    plt.show()"""