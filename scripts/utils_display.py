from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datashader as ds
from datashader.mpl_ext import dsshow
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

def fft(data) -> None:
    fft_result = np.fft.fft(data)

    # Calculate the frequencies corresponding to FFT result
    sampling_rate = 2000000 
    freqs = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

    # Plot the frequency-domain data
    """plt.specgram(data, Fs=2000000)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram')
    plt.colorbar(label='Magnitude (dB)')"""
    plt.plot(freqs, np.abs(fft_result))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Domain Plot')
    plt.show()

def display(data) -> None:
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


def using_hist2d(ax, x, y, bins=(300, 300)):
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
    #display(load_signal('preambles/RN1/sample_1', np.complex64))
    #display_quadrature((load_signal('sample_data/test_64_1MHz', dtype=np.complex64)),'data')
    fft(load_signal('preambles/RN1/sample_1', np.complex64))