import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datashader as ds
from datashader.mpl_ext import dsshow


def display_quadrature(data) -> None:
    plt.figure(figsize=(8, 6))
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.title('Constellation Trace')

    i = np.real(data)
    q = np.imag(data)
    plt.scatter(i, q, s=5, alpha=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()



def display_density(data: np.array, filename: str="") -> None:
    """Display a density graph in the complex plan of an array of complex points

    Parameters
    ----------
    data : np.array
        An array of complex
    filename : str, optional
        Used in the title of the plot
    """
    fig, ax = plt.subplots()
    #fig = plt.figure(figsize=(8, 6))
    #ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
    i = np.real(data)
    q = np.imag(data)
    using_datashader(ax, i, q)
    #using_hist2d(ax, differential_i, differential_q)
    #plt.scatter(differential_i, differential_q, s=1, c='red', alpha=0.5)
    plt.xlabel('Differential In-phase')
    plt.ylabel('Differential Quadrature')
    plt.title('Differential I/Q Samples'+ filename)
    #plt.grid(True)
    plt.show()


def display(data: np.array) -> None:
    """
    Display the real part of the signal in orange and the imaginary part in blue
    """
    i = np.real(data) # in-phase
    q = np.imag(data) # quadrature

    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(i)), i, s=5, c='orange', alpha=0.5, label='in-phase')
    plt.scatter(range(len(i)), q, s=5, c='blue', alpha=0.5, label='quadrature')
    plt.xlabel('Sample index')
    plt.title('I/Q Samples')
    plt.legend()
    plt.grid(True)
    plt.show()


def using_datashader(ax, x, y):
    df = pd.DataFrame(dict(x=x, y=y))
    dsartist = dsshow(
        df,
        ds.Point("x", "y"),
        ds.count(),
        vmin=10,
        vmax=100,
        norm="linear",
        aspect="auto",
        ax=ax,
    )

    plt.colorbar(dsartist)
