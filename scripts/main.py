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
    
    DATA = load_signal('preambules/notp2.complex', dtype=np.complex64)
    #DATA = load_signal('sample_data/pretest_64_misc', dtype=np.complex64)
    print(len(DATA))
    #n = int(SAMPLE_RATE / RS)
    n = 2048
    print("real value= 2048")
    print("n= ",n)
    delta_f = -62500
    differential_data = np.zeros_like(DATA)
    for i in range(n, len(DATA)):
        differential_data[i] = DATA[i] * np.conj(DATA[i - n]) * np.exp(-1j * 2 * np.pi * delta_f * n)


    differential_i = np.real(differential_data)
    differential_q = np.imag(differential_data)

    

  

    fig, ax = plt.subplots()
    #fig = plt.figure(figsize=(8, 6))
    #ax = fig.add_subplot(1, 1, 1, projection='scatter_density')

    using_datashader(ax, differential_i, differential_q)
    #using_hist2d(ax, differential_i, differential_q)
    #plt.scatter(differential_i, differential_q, s=1, c='red', alpha=0.5)
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential I/Q Samples')
    #plt.grid(True)
    plt.show()